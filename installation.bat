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

REM Path to launch.bat
set "LAUNCH_FILE=%~dp0launch.bat"

REM Check if launch.bat exists
if not exist %LAUNCH_FILE% (
    echo %LAUNCH_FILE% not found
    exit /b 1
)

REM Create a temporary file
set "TEMP_FILE=%~dp0launch.tmp"

REM Add line defining PROJECT_PATH to the temporary file
echo set PROJECT_PATH=%PROJECT_PATH%> %TEMP_FILE%

REM Remove all lines starting with "set PROJECT_PATH=" from launch.bat
findstr /v /r "^set PROJECT_PATH=" %LAUNCH_FILE% > "%LAUNCH_FILE%.tmp"
move /y "%LAUNCH_FILE%.tmp" %LAUNCH_FILE% > nul

REM Add all lines from launch.bat to the temporary file
type %LAUNCH_FILE% >> %TEMP_FILE%

REM Replace launch.bat with the temporary file
move /y %TEMP_FILE% %LAUNCH_FILE% > nul

REM Define the Startup folder path
set "STARTUP_FOLDER=%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

REM Copy launch.bat to the Startup folder
echo Copying launch.bat to %STARTUP_FOLDER%
copy /y %LAUNCH_FILE% "%STARTUP_FOLDER%" > nul

REM Check if the copy was successful
set "STARTUP_FILE=%STARTUP_FOLDER%\launch.bat"
if exist "%STARTUP_FILE%" (
    echo launch.bat added to Startup folder successfully.
) else (
    echo Failed to add launch.bat to Startup folder.
    exit /b 1
)

REM Rename the file in the Startup folder
set "NEW_NAME=%STARTUP_FOLDER%\mediakey_launcher.bat"
REM Remove old file if it exists
if exist "%NEW_NAME%" (
    echo Removing old file %NEW_NAME%
    del /f /q "%NEW_NAME%"
)
rename "%STARTUP_FILE%" "mediakey_launcher.bat"

REM Verify if the renaming was successful
if exist "%NEW_NAME%" (
    echo File renamed to mediakey_launcher.bat successfully.
) else (
    echo Failed to rename the file in the Startup folder.
    exit /b 1
)

REM Launch the script
echo Running %NEW_NAME%
call "%NEW_NAME%"

exit /b 0
