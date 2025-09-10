@echo off
title Devyan v0.1.4 - AI Development Assistant
echo.
echo ╔══════════════════════════════════════╗
echo ║         DEVYAN v0.1.4 LAUNCHER      ║
echo ║     AI Development Assistant         ║
echo ║    Enhanced Output Validation        ║
echo ╚══════════════════════════════════════╝
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python not found in PATH
    echo    Please install Python 3.8+ and add to PATH
    echo    Download from: https://python.org/downloads
    pause
    exit /b 1
)

REM Change to script directory
cd /d "%~dp0"

REM Display current directory for debugging
echo 📁 Current directory: %CD%
echo.

REM Check for required files
if not exist "devyan_main.py" (
    echo ❌ Error: devyan_main.py not found
    echo    Make sure you're in the correct directory
    pause
    exit /b 1
)

if not exist "launch.py" (
    echo ❌ Error: launch.py not found
    echo    Make sure you're in the correct directory
    pause
    exit /b 1
)

if not exist "requirements.txt" (
    echo ❌ Error: requirements.txt not found
    echo    Make sure you're in the correct directory
    pause
    exit /b 1
)

REM Run the launcher
echo 🚀 Starting Devyan v0.1.4 with enhanced validation...
echo.
python launch.py

echo.
echo 🏁 Devyan session ended.
pause
