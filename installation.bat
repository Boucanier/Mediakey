@echo off

REM Checking if nircmd is installed
where nircmd >nul 2>nul
if %errorlevel% == 0 (
    echo nircmd is installed
) else (
    echo nircmd is not installed
    exit /b 1
)

REM Install python environment
echo Installing python environment
python -m venv .venv
if %errorlevel% neq 0 (
    echo Failed to install python environment
    exit /b 1
)

REM Installing python packages
echo Installing python packages
call ".venv\Scripts\pip.exe" install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install python packages
    exit /b 1
)

REM Stopping the script if it is running
call stop.bat

REM Get the current project path
set "PROJECT_PATH=%~dp0"

REM Path to new launcher file
set "LAUNCH_FILE=%~dp0mediakey_launcher.bat"

REM Path to temporary launcher file
set "TEMP_LAUNCH_FILE=%~dp0mediakey_launcher.tmp"

REM Check if launch.bat exists
set "ORIGINAL_LAUNCH_FILE=%~dp0launch.bat"
if not exist %ORIGINAL_LAUNCH_FILE% (
    echo %ORIGINAL_LAUNCH_FILE% not found
    exit /b 1
)

REM Create a new launcher file
echo Creating new launcher file: %LAUNCH_FILE%

REM Add line defining PROJECT_PATH to the new launcher file
echo @echo off> %LAUNCH_FILE%
echo set PROJECT_PATH=%PROJECT_PATH%>> %LAUNCH_FILE%

REM Add all lines from the original launch.bat to the new launcher file
type %ORIGINAL_LAUNCH_FILE% >> %TEMP_LAUNCH_FILE%

REM Remove all lines starting with "set PROJECT_PATH=" from the new launcher file
findstr /v /r "^set PROJECT_PATH=" %ORIGINAL_LAUNCH_FILE% | findstr /v /r "^@echo off" > %TEMP_LAUNCH_FILE%
type %TEMP_LAUNCH_FILE% >> %LAUNCH_FILE%
del %TEMP_LAUNCH_FILE%

REM Define the Startup folder path
set "STARTUP_FOLDER=%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

REM Copy new launcher file to the Startup folder
echo Moving mediakey_launcher.bat to %STARTUP_FOLDER%
move "%LAUNCH_FILE%" "%STARTUP_FOLDER%"

REM Check if the copy was successful
set "STARTUP_FILE=%STARTUP_FOLDER%\mediakey_launcher.bat"
if exist "%STARTUP_FILE%" (
    echo mediakey_launcher.bat added to Startup folder successfully.
) else (
    echo Failed to add mediakey_launcher.bat to Startup folder.
    exit /b 1
)

REM Launch the new launcher file
echo Running %STARTUP_FILE%
call "%STARTUP_FILE%"

exit /b 0
