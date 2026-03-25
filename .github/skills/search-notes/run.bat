@echo off
REM 從任何位置執行 quick_search.py
REM 使用方式：run.bat "搜尋關鍵字" [--scope cards|areas|capture|all] [--limit N]

set SCRIPT_DIR=%~dp0
python "%SCRIPT_DIR%quick_search.py" %*
