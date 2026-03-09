#!/usr/bin/env python3
"""
Workspace Statistics and Recent Changes Review
統計工作區資料夾並回顧最近變更
"""

import os
import subprocess
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# 核心資料夾列表
CORE_FOLDERS = [
    "000_MyContext",
    "003_Capture",
    "005_PARA",
    "010_CardNotes",
    "015_Write"
]

def count_md_files(folder_path):
    """統計資料夾內的 .md 檔案數量"""
    if not os.path.exists(folder_path):
        return 0
    
    count = 0
    for root, dirs, files in os.walk(folder_path):
        # 排除 .git 等隱藏資料夾
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        count += sum(1 for f in files if f.endswith('.md'))
    return count

def get_folder_stats():
    """取得各資料夾的統計資訊"""
    stats = {}
    total = 0
    
    print("=" * 60)
    print("📊 工作區資料夾統計")
    print("=" * 60)
    print()
    
    for folder in CORE_FOLDERS:
        count = count_md_files(folder)
        stats[folder] = count
        total += count
        
        # 顯示進度條效果
        bar_length = 30
        filled = int(bar_length * count / max(1, total)) if total > 0 else 0
        bar = "█" * filled + "░" * (bar_length - filled)
        
        print(f"{folder:20s} │ {count:4d} 個檔案")
    
    print("-" * 60)
    print(f"{'總計':20s} │ {total:4d} 個檔案")
    print()
    
    return stats

def get_recent_git_changes():
    """取得最近的 git 變更記錄"""
    try:
        # 取得最近 20 次 commit
        result = subprocess.run(
            ["git", "log", "--name-only", "--pretty=format:%H|%ad|%s", 
             "--date=format:%Y-%m-%d %H:%M", "-20"],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            check=False
        )
        
        if result.returncode != 0 or not result.stdout:
            print("⚠️  無法取得 git 記錄")
            return
        
        # 解析 git log
        commits = []
        current_commit = None
        
        for line in result.stdout.split('\n'):
            if '|' in line:
                # 新的 commit
                parts = line.split('|')
                if len(parts) >= 3:
                    current_commit = {
                        'hash': parts[0][:7],
                        'date': parts[1],
                        'message': parts[2],
                        'files': []
                    }
                    commits.append(current_commit)
            elif line.strip() and current_commit:
                # 檔案路徑
                current_commit['files'].append(line.strip())
        
        # 篩選涉及核心資料夾的變更
        relevant_commits = []
        folder_activity = defaultdict(int)
        
        for commit in commits:
            relevant_files = []
            for file in commit['files']:
                for folder in CORE_FOLDERS:
                    if file.startswith(folder):
                        relevant_files.append(file)
                        folder_activity[folder] += 1
                        break
            
            if relevant_files:
                commit['relevant_files'] = relevant_files
                relevant_commits.append(commit)
        
        # 顯示最近變更
        print("=" * 60)
        print("📝 最近變更記錄（最多顯示 10 筆）")
        print("=" * 60)
        print()
        
        for commit in relevant_commits[:10]:
            print(f"🔹 {commit['date']} | {commit['hash']}")
            print(f"   {commit['message']}")
            
            # 顯示變更的檔案（最多 5 個）
            for file in commit['relevant_files'][:5]:
                # 縮短路徑顯示
                if len(file) > 55:
                    file = file[:52] + "..."
                print(f"   • {file}")
            
            if len(commit['relevant_files']) > 5:
                print(f"   ... 還有 {len(commit['relevant_files']) - 5} 個檔案")
            print()
        
        # 顯示活躍度分析
        if folder_activity:
            print("=" * 60)
            print("📈 資料夾活躍度分析（最近 20 次 commit）")
            print("=" * 60)
            print()
            
            # 排序
            sorted_activity = sorted(folder_activity.items(), 
                                   key=lambda x: x[1], reverse=True)
            
            max_activity = max(folder_activity.values())
            
            for folder, count in sorted_activity:
                bar_length = 30
                filled = int(bar_length * count / max_activity)
                bar = "█" * filled + "░" * (bar_length - filled)
                
                print(f"{folder:20s} │ {bar} {count:3d} 次變更")
            print()
        
    except subprocess.CalledProcessError:
        print("⚠️  無法執行 git 命令，請確認：")
        print("   1. 當前目錄是 git repository")
        print("   2. git 已正確安裝")
        print()
    except Exception as e:
        print(f"⚠️  發生錯誤: {e}")
        print()

def main():
    """主程式"""
    print()
    print("🔍 開始分析工作區...")
    print()
    
    # 確認在正確的目錄
    if not os.path.exists("AGENTS.md"):
        print("⚠️  警告：未在專案根目錄執行")
        print("   請在 card_notes 專案根目錄執行此腳本")
        print()
        return
    
    # 統計資料夾
    stats = get_folder_stats()
    
    # 顯示 git 變更
    get_recent_git_changes()
    
    print("=" * 60)
    print("✅ 分析完成")
    print("=" * 60)
    print()

if __name__ == "__main__":
    main()
