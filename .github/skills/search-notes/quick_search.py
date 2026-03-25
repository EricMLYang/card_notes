#!/usr/bin/env python3
"""
quick_search.py — 筆記快速搜尋工具
搜尋 003_Capture、005_PARA/02_Areas、010_CardNotes/02_Cards 的關鍵內容
"""

import os
import re
import sys
import json
import time
import argparse
from pathlib import Path

# 確保 Windows 終端以 UTF-8 輸出
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def find_repo_root():
    """從腳本所在目錄或 cwd 往上找到含 AGENTS.md 的專案根目錄"""
    for start in [Path(__file__).resolve().parent, Path.cwd()]:
        current = start
        for _ in range(6):
            if (current / "AGENTS.md").exists():
                return current
            current = current.parent
    return Path.cwd()


def read_file(path):
    """讀取檔案內容，處理編碼問題"""
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def parse_frontmatter(content):
    """解析 YAML frontmatter（--- 區塊），回傳 dict"""
    fm = {}
    if not content.startswith("---"):
        return fm
    end = content.find("\n---", 3)
    if end == -1:
        return fm
    for line in content[4:end].splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()
    return fm


def extract_section(content, section_name):
    """提取 ## section_name 到下一個 ## 之間的文字"""
    escaped = re.escape(section_name)
    pattern = rf"## {escaped}(.*?)(?=\n##|\Z)"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def extract_tags(content):
    """提取 #標籤 格式的標籤（支援中英文）"""
    return re.findall(r"#([\w\u4e00-\u9fff]+)", content)


def get_card_title(filename):
    """從 '3-001_標題.md' 提取標題部分"""
    stem = Path(filename).stem
    match = re.match(r"^\d+-\d+_(.*)", stem)
    return match.group(1) if match else stem


def compute_score(query_terms, title, highlights, tags, full_text):
    """
    分層加權評分：
      標題命中      +3.0
      [重點]命中    +2.0
      標籤命中      +1.5
      全文命中      min(count × 0.3, 1.0)
    最終除以 query_terms 數量做正規化
    """
    score = 0.0
    title_l = title.lower()
    hl_l = highlights.lower()
    tags_l = " ".join(tags).lower()
    full_l = full_text.lower()

    for term in query_terms:
        t = term.lower()
        if t in title_l:
            score += 3.0
        if t in hl_l:
            score += 2.0
        if t in tags_l:
            score += 1.5
        score += min(full_l.count(t) * 0.3, 1.0)

    if query_terms:
        score /= len(query_terms)
    return round(score, 2)


def make_snippet(text, max_len=150):
    """將文字截斷為單行 snippet"""
    snippet = text.replace("\n", " ").strip()
    if len(snippet) > max_len:
        snippet = snippet[:max_len] + "..."
    return snippet


# ──────────────────────────────────────────
# 搜尋各範圍
# ──────────────────────────────────────────

def search_cards(root, query_terms, category_filter=None):
    """搜尋 010_CardNotes/02_Cards/"""
    cards_root = root / "010_CardNotes" / "02_Cards"
    results = []
    if not cards_root.exists():
        return results, 0

    file_count = 0
    for category_dir in sorted(cards_root.iterdir()):
        if not category_dir.is_dir():
            continue
        cat_name = category_dir.name
        if category_filter and not cat_name.startswith(category_filter):
            continue

        for md_file in sorted(category_dir.glob("*.md")):
            content = read_file(md_file)
            if not content:
                continue
            file_count += 1

            title = get_card_title(md_file.name)
            # 提取第一個 ## 區段的內容作為卡片核心概念
            section_match = re.search(r"## .+?\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
            first_section = section_match.group(1).strip() if section_match else ""
            tags = extract_tags(content)

            score = compute_score(query_terms, title, first_section, tags, content)
            if score < 0.1:
                continue

            results.append({
                "type": "card",
                "path": str(md_file.relative_to(root)).replace("\\", "/"),
                "title": title,
                "filename": md_file.stem,
                "category": cat_name,
                "score": score,
                "snippet": make_snippet(first_section),
                "tags": tags[:5],
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results, file_count


def search_folder(root, folder_rel, doc_type, query_terms):
    """通用搜尋 Areas 或 Capture 資料夾"""
    folder = root / folder_rel
    results = []
    if not folder.exists():
        return results, 0

    file_count = 0
    for md_file in sorted(folder.rglob("*.md")):
        content = read_file(md_file)
        if not content:
            continue
        file_count += 1

        # 從檔名提取標題
        stem = md_file.stem
        title_match = re.match(r"^\d{8}_(.*)", stem)
        title = title_match.group(1) if title_match else stem
        title = re.sub(r"^CoreNote_", "", title)

        fm = parse_frontmatter(content)
        highlights = extract_section(content, "[重點]")
        summary = extract_section(content, "[摘要]")
        tags = extract_tags(content)

        score = compute_score(query_terms, title, highlights + " " + summary, tags, content)
        if score < 0.1:
            continue

        # snippet 優先用 [重點]，否則用正文第一段
        if highlights:
            snippet = make_snippet(highlights)
        else:
            lines = [l for l in content.split("\n") if l.strip() and not l.startswith("#") and "---" not in l]
            snippet = make_snippet(lines[0]) if lines else ""

        entry = {
            "type": doc_type,
            "path": str(md_file.relative_to(root)).replace("\\", "/"),
            "title": title,
            "score": score,
            "snippet": snippet,
            "tags": tags[:5],
        }
        if "process_level" in fm:
            entry["process_level"] = fm["process_level"].split("#")[0].strip()
        if "last_review" in fm:
            entry["last_review"] = fm["last_review"]

        results.append(entry)

    results.sort(key=lambda x: x["score"], reverse=True)
    return results, file_count


# ──────────────────────────────────────────
# 輸出格式化
# ──────────────────────────────────────────

def format_text(results, meta):
    lines = [
        f"搜尋：「{meta['query']}」",
        f"找到 {meta['total_found']} 筆結果（掃描 {meta['files_scanned']} 個檔案，耗時 {meta['search_time_ms']} ms）",
        "━" * 50,
    ]

    if not results:
        lines.append("（無結果，請嘗試其他關鍵字）")
        return "\n".join(lines)

    type_labels = {"card": "卡片", "area": "文章", "capture": "Capture"}
    for r in results:
        label = type_labels.get(r["type"], r["type"])
        lines.append(f"\n[{label}] {r['title']}  (分數: {r['score']})")
        if r.get("category"):
            lines.append(f"  分類: {r['category']}")
        if r.get("process_level"):
            lines.append(f"  process_level: {r['process_level']}")
        if r.get("snippet"):
            lines.append(f"  重點: {r['snippet']}")
        if r.get("tags"):
            lines.append(f"  標籤: {' '.join('#' + t for t in r['tags'])}")
        lines.append(f"  路徑: {r['path']}")

    lines.append("\n" + "━" * 50)
    lines.append("提示：--scope cards/areas/capture 篩選範圍，--format json 輸出機器可讀格式")
    return "\n".join(lines)


# ──────────────────────────────────────────
# 主程式
# ──────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="筆記快速搜尋工具")
    parser.add_argument("query", help="搜尋關鍵字（多個關鍵字用空格分隔）")
    parser.add_argument("--scope", choices=["cards", "areas", "capture", "all"], default="all")
    parser.add_argument("--format", choices=["json", "text"], default="text", dest="fmt")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--category", default=None, help="只搜特定卡片分類前綴，例如 03")
    args = parser.parse_args()

    start = time.time()
    root = find_repo_root()
    query_terms = args.query.split()

    all_results = []
    total_files = 0

    if args.scope in ("all", "cards"):
        r, n = search_cards(root, query_terms, args.category)
        all_results.extend(r)
        total_files += n

    if args.scope in ("all", "areas"):
        r, n = search_folder(root, Path("005_PARA/02_Areas"), "area", query_terms)
        all_results.extend(r)
        total_files += n

    if args.scope in ("all", "capture"):
        r, n = search_folder(root, Path("003_Capture"), "capture", query_terms)
        all_results.extend(r)
        total_files += n

    all_results.sort(key=lambda x: x["score"], reverse=True)
    all_results = all_results[: args.limit]

    elapsed_ms = int((time.time() - start) * 1000)
    meta = {
        "query": args.query,
        "total_found": len(all_results),
        "files_scanned": total_files,
        "search_time_ms": elapsed_ms,
        "scope": args.scope,
    }

    if args.fmt == "json":
        payload = {
            "query": args.query,
            "total_found": len(all_results),
            "files_scanned": total_files,
            "search_time_ms": elapsed_ms,
            "scope": args.scope,
            "results": all_results,
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(format_text(all_results, meta))


if __name__ == "__main__":
    main()
