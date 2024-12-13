@echo off
REM Stop mediakey.py
call "%~dp0.venv\Scripts\python.exe" scripts/stop_script.py
if %errorlevel% equ 0 (
    echo Script stopped.
) else (
    echo No process found.
)
