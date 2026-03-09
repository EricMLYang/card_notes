#!/usr/bin/env python3
"""
Filename Prefix Guard - 檔名前綴檢查腳本
檢查 003_Capture、015_Write/Draft、015_Write/Publish 的檔名是否符合 YYYYMMDD_[title].md 格式
"""
import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path


TARGET_DIRS = ("003_Capture/", "015_Write/Draft/", "015_Write/Publish/")
NAME_RE = re.compile(r"^(\d{8})_(.+)\.md$")


def run_git(args):
    """執行 git 命令"""
    p = subprocess.run(["git", *args], capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(p.stderr.strip() or "git command failed")
    return p.stdout


def is_valid_name(filename: str) -> bool:
    """檢查檔名是否符合 YYYYMMDD_[title].md 格式"""
    m = NAME_RE.match(filename)
    if not m:
        return False
    date_part = m.group(1)
    try:
        dt.datetime.strptime(date_part, "%Y%m%d")
        return True
    except ValueError:
        return False


def staged_files():
    """取得 git staged 的檔案清單"""
    out = run_git(["diff", "--cached", "--name-only", "--diff-filter=AR"])
    return [line.strip().replace("\\", "/") for line in out.splitlines() if line.strip()]


def all_files():
    """取得目標資料夾下所有 .md 檔案"""
    paths = []
    for d in ("003_Capture", "015_Write/Draft", "015_Write/Publish"):
        root = Path(d)
        if not root.exists():
            continue
        for p in root.rglob("*.md"):
            paths.append(str(p).replace("\\", "/"))
    return paths


def in_target(path: str) -> bool:
    """檢查路徑是否在目標資料夾內"""
    return any(path.startswith(prefix) for prefix in TARGET_DIRS)


def get_git_first_commit_date(filepath: str) -> str | None:
    """取得檔案首次 commit 的日期"""
    try:
        out = run_git([
            "log", "--diff-filter=A", "--follow",
            "--format=%ad", "--date=format:%Y%m%d", "--", filepath
        ])
        lines = [l.strip() for l in out.splitlines() if l.strip()]
        return lines[-1] if lines else None
    except Exception:
        return None


def get_git_last_commit_date(filepath: str) -> str | None:
    """取得檔案最後 commit 的日期"""
    try:
        out = run_git([
            "log", "-1", "--format=%ad", "--date=format:%Y%m%d", "--", filepath
        ])
        return out.strip() or None
    except Exception:
        return None


def get_today() -> str:
    """取得今天日期"""
    return dt.datetime.now().strftime("%Y%m%d")


def suggest_new_name(filepath: str) -> str:
    """建議新檔名"""
    path = Path(filepath)
    name = path.name
    
    # 優先用 git 首次提交日期
    date_prefix = get_git_first_commit_date(filepath)
    if not date_prefix:
        date_prefix = get_git_last_commit_date(filepath)
    if not date_prefix:
        date_prefix = get_today()
    
    new_name = f"{date_prefix}_{name}"
    return str(path.parent / new_name)


def main():
    parser = argparse.ArgumentParser(description="檢查檔名前綴格式")
    parser.add_argument("--all-files", action="store_true", 
                        help="檢查目標資料夾下所有檔案（預設只檢查 staged 檔案）")
    parser.add_argument("--suggest-fix", action="store_true",
                        help="顯示建議的修正檔名")
    args = parser.parse_args()

    files = all_files() if args.all_files else staged_files()
    to_check = [p for p in files if in_target(p)]

    if not to_check:
        print("✅ Filename prefix check passed (no files to check).")
        return 0

    invalid = []
    for path in to_check:
        name = Path(path).name
        if not is_valid_name(name):
            invalid.append(path)

    if invalid:
        print("❌ Filename prefix check failed.", file=sys.stderr)
        print("", file=sys.stderr)
        print("Required format: YYYYMMDD_[title].md", file=sys.stderr)
        print("", file=sys.stderr)
        print("Invalid files:", file=sys.stderr)
        for p in invalid:
            print(f"  - {p}", file=sys.stderr)
            if args.suggest_fix:
                suggested = suggest_new_name(p)
                print(f"    → {suggested}", file=sys.stderr)
        return 1

    print(f"✅ Filename prefix check passed ({len(to_check)} files checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
