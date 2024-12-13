set PROJECT_PATH=%~dp0
@echo off
REM Check if the script is already running
call "%PROJECT_PATH%.venv\Scripts\python.exe" "%PROJECT_PATH%scripts\check_running.py"
if %errorlevel% equ 1 (
    echo Script is already running
    exit /b 1
)

REM Start the script in the background
start "Mediakey" "%PROJECT_PATH%.venv\Scripts\pythonw.exe" "%PROJECT_PATH%src\mediakey.py" --ok

exit /b 0
