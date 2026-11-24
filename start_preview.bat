@echo off
title Dear 2027, I'm Ready - Preview Hub
cd /d "%~dp0"
echo ========================================================
echo  Launching Dear 2027 Master Suite Local Server...
echo ========================================================
python start_server.py
if %ERRORLEVEL% NEQ 0 (
    echo Python server launch encountered an issue, opening index.html directly...
    start "" "index.html"
)
pause
