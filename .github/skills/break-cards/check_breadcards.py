#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check BreadCards - 檢測文件是否已拆解為候選卡片
跨平台支援 (Windows/Mac/Linux)

Exit Codes:
  0: 成功檢測到 BreadCards 內容
  1: 文件不存在
  2: 未找到 BreadCards 標記（尚未拆解）
  3: 提取失敗
"""

import sys
import os
from pathlib import Path
import io

# 設置 Windows 上的 UTF-8 輸出
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def check_breadcards(file_path):
    """檢測文件是否包含 BreadCards 並提取內容"""
    
    # 檢查文件是否存在
    file_path = Path(file_path)
    if not file_path.exists():
        print(f"[X] 文件不存在: {file_path}", file=sys.stderr)
        return 1
    
    # 讀取文件內容
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"[X] 讀取文件失敗: {e}", file=sys.stderr)
        return 3
    
    # 檢查是否包含 BreadCards 標記
    if '# BreadCards' not in content:
        print("[X] 未找到 # BreadCards 標記")
        print("此檔案尚未執行 break-cards 處理")
        return 2
    
    # 提取 # BreadCards 之後的內容
    try:
        breadcards_index = content.find('# BreadCards')
        if breadcards_index == -1:
            print("[X] 無法定位 BreadCards 標記", file=sys.stderr)
            return 3
        
        breadcards_content = content[breadcards_index:]
        
        print("[OK] 成功檢測到 BreadCards 內容")
        print(f"內容長度: {len(breadcards_content)} 字元")
        print("\n" + "="*80 + "\n")
        print(breadcards_content)
        return 0
        
    except Exception as e:
        print(f"[X] 提取失敗: {e}", file=sys.stderr)
        return 3

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方式: python check_breadcards.py <file_path>")
        sys.exit(1)
    
    exit_code = check_breadcards(sys.argv[1])
    sys.exit(exit_code)
