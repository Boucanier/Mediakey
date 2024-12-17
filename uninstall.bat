@echo off

REM Stopping the script if it is running
call stop.bat

REM Search the Startup folder path
set "STARTUP_FOLDER=%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
set "STARTUP_FILE=%STARTUP_FOLDER%\mediakey_launcher.bat"

REM Check if mediakey_launcher.bat exists in the Startup folder
if exist "%STARTUP_FILE%" (
    echo mediakey_launcher.bat found in Startup folder.

    REM Delete mediakey_launcher.bat from the Startup folder
    del "%STARTUP_FILE%"
    if exist "%STARTUP_FILE%" (
        echo Failed to delete mediakey_launcher.bat from Startup folder.
        exit /b 1
    )
) else (
    echo mediakey_launcher.bat not found in Startup folder.
    exit /b 1
)

echo mediakey_launcher.bat removed from Startup folder.
exit /b 0