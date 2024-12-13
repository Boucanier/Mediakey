@echo off
REM Check if the script is already running
python scripts/check_running.py
if %errorlevel% equ 1 (
    echo Script is already running
    exit /b
)

REM Start the script in the background
start "Mediakey" .venv/Scripts/pythonw.exe src/mediakey.py --ok
