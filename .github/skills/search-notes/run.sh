#!/bin/bash
# 從任何位置執行 quick_search.py
# 使用方式：./run.sh "搜尋關鍵字" [--scope cards|areas|capture|all] [--limit N]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/quick_search.py" "$@"
