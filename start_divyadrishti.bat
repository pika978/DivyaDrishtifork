@echo off
echo ================================================================
echo 🎯 Starting DivyaDrishti - Hiking Trail Detection System
echo ================================================================
echo.

REM Check if we're in the right directory
if not exist "main.py" (
    echo ❌ Error: main.py not found!
    echo Please run this script from the DivyaDrishti directory.
    pause
    exit /b 1
)

echo 🚀 Launching DivyaDrishti GUI...
echo.

REM Start the application
python main.py

if errorlevel 1 (
    echo.
    echo ❌ Application exited with an error.
    echo Check the error messages above.
    pause
)

echo.
echo 👋 DivyaDrishti has been closed.
pause
