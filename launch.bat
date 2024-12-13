@echo off
set PROJECT_PATH=%~dp0

REM Move to the project directory
cd /d %PROJECT_PATH%

REM Check if the script is already running
call "%PROJECT_PATH%.venv\Scripts\python.exe" "%PROJECT_PATH%scripts\check_running.py"
if %errorlevel% equ 1 (
    echo Mediakey is already running
    exit /b 1
)

REM Start the script in the background
echo Starting Mediakey
start "Mediakey" "%PROJECT_PATH%.venv\Scripts\pythonw.exe" "%PROJECT_PATH%src\mediakey.py" --ok

exit /b 0
