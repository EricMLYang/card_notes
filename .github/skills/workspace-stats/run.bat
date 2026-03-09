@echo off
REM Windows batch script to run workspace stats

cd /d "%~dp0..\..\..\"
python .github\skills\workspace-stats\workspace_stats.py
pause
