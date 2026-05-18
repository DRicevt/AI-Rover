@echo off
cd /d "%~dp0"

if exist "..\..\.venv\Scripts\python.exe" (
    "..\..\.venv\Scripts\python.exe" run_heatmap.py %*
) else (
    py run_heatmap.py %*
)
