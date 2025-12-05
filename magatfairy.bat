@echo off
REM magatfairy.bat - Windows double-clickable script
REM Double-click this file to open Command Prompt and start conversion

REM Get the directory where this script is located
cd /d "%~dp0"

REM Run magatfairy with auto command
python magatfairy.py convert auto

REM Keep window open so user can see results
echo.
echo Press any key to close...
pause >nul

