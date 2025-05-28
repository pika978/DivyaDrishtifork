@echo off
echo ================================================================
echo 🎯 DivyaDrishti - Hiking Trail Detection System
echo 🥾 Automated Installation Script for Windows
echo ================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH!
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo ✓ Python found
python --version

echo.
echo 🔄 Starting installation process...
echo.

REM Run the Python installer
python install_dependencies.py

if errorlevel 1 (
    echo.
    echo ❌ Installation failed!
    echo Please check the error messages above.
    pause
    exit /b 1
)

echo.
echo ================================================================
echo ✅ Installation completed successfully!
echo.
echo Next steps:
echo 1. Ensure the hiking trail model is available
echo 2. Run: python main.py
echo.
echo To start DivyaDrishti:
echo   python main.py
echo.
echo To check system requirements:
echo   python main.py --check
echo ================================================================
echo.
pause
