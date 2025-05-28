#!/bin/bash

echo "================================================================"
echo "🎯 DivyaDrishti - Hiking Trail Detection System"
echo "🥾 Automated Installation Script for Linux/macOS"
echo "================================================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "❌ Python is not installed!"
        echo "Please install Python 3.8+ from your package manager or https://python.org"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "✓ Python found"
$PYTHON_CMD --version

echo
echo "🔄 Starting installation process..."
echo

# Run the Python installer
$PYTHON_CMD install_dependencies.py

if [ $? -ne 0 ]; then
    echo
    echo "❌ Installation failed!"
    echo "Please check the error messages above."
    exit 1
fi

echo
echo "================================================================"
echo "✅ Installation completed successfully!"
echo
echo "Next steps:"
echo "1. Ensure the hiking trail model is available"
echo "2. Run: $PYTHON_CMD main.py"
echo
echo "To start DivyaDrishti:"
echo "  $PYTHON_CMD main.py"
echo
echo "To check system requirements:"
echo "  $PYTHON_CMD main.py --check"
echo "================================================================"
echo
