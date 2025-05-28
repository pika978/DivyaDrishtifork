#!/usr/bin/env python3
"""
DivyaDrishti - Hiking Trail Detection System
Independent YOLO-based object detection for hiking trails

Main entry point for the application
"""

import sys
import os
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

import config
import utils
from gui_app import main as gui_main

def check_dependencies():
    """Check if all required dependencies are installed"""
    missing_deps = []

    try:
        import torch
        import torchvision
        print(f"✓ PyTorch {torch.__version__} installed")
    except ImportError:
        missing_deps.append("torch")

    try:
        import ultralytics
        print(f"✓ Ultralytics {ultralytics.__version__} installed")
    except ImportError:
        missing_deps.append("ultralytics")

    try:
        import cv2
        print(f"✓ OpenCV {cv2.__version__} installed")
    except ImportError:
        missing_deps.append("opencv-python")

    try:
        import PIL
        print(f"✓ Pillow {PIL.__version__} installed")
    except ImportError:
        missing_deps.append("pillow")

    try:
        import numpy
        print(f"✓ NumPy {numpy.__version__} installed")
    except ImportError:
        missing_deps.append("numpy")

    try:
        import pandas
        print(f"✓ Pandas {pandas.__version__} installed")
    except ImportError:
        missing_deps.append("pandas")

    return missing_deps

def check_foottrail_model():
    """Check if foottrail model is available"""
    model_path = config.HIKING_MODEL_PATH

    if model_path.exists():
        print(f"✓ FootTrail model found: {model_path}")
        return True
    else:
        print(f"✗ FootTrail model not found: {model_path}")
        print("\nPlease ensure the foottrail model is available at:")
        print(f"  {model_path}")
        print("\nThe model should be located in the 'FootTrail Detection Model' directory.")
        return False

def setup_environment():
    """Setup the application environment"""
    print("=" * 60)
    print(f"🎯 {config.APP_NAME} v{config.APP_VERSION}")
    print("🥾 Hiking Trail Detection System")
    print("=" * 60)

    # Create necessary directories
    utils.create_directories()

    # Check dependencies
    print("\n📦 Checking Dependencies...")
    missing_deps = check_dependencies()

    if missing_deps:
        print(f"\n✗ Missing dependencies: {', '.join(missing_deps)}")
        print("\nTo install missing dependencies, run:")
        print("  pip install -r requirements.txt")
        return False

    # Check foottrail model
    print("\n🎯 Checking FootTrail Detection Model...")
    if not check_foottrail_model():
        return False

    # Check GPU availability
    print("\n🖥️ Checking GPU Support...")
    try:
        import torch
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            print(f"✓ GPU available: {gpu_name}")
            print(f"✓ CUDA version: {torch.version.cuda}")
        else:
            print("⚠️ GPU not available, using CPU")
    except Exception as e:
        print(f"⚠️ GPU check failed: {e}")

    print("\n✓ Environment setup complete!")
    print("=" * 60)
    return True

def print_usage():
    """Print usage information"""
    print(f"""
🎯 {config.APP_NAME} - Hiking Trail Detection System

USAGE:
  python main.py [options]

OPTIONS:
  --help, -h     Show this help message
  --version, -v  Show version information
  --check        Check system requirements only
  --gui          Start GUI application (default)

FEATURES:
  🥾 Hiking trail detection using custom YOLO model
  👤 Person and hiker detection
  📦 Equipment and gear recognition
  🎯 Real-time detection and tracking
  💾 Automatic logging and screenshots
  ⚡ GPU acceleration support
  🎮 Cyberpunk-themed GUI interface

REQUIREMENTS:
  - Python 3.8+
  - PyTorch with CUDA support (recommended)
  - Hiking trail model file
  - Webcam or video file for input

For more information, see README.md
    """)

def main():
    """Main application entry point"""
    # Parse command line arguments
    args = sys.argv[1:]

    if "--help" in args or "-h" in args:
        print_usage()
        return

    if "--version" in args or "-v" in args:
        print(f"{config.APP_NAME} v{config.APP_VERSION}")
        return

    # Setup environment
    if not setup_environment():
        print("\n❌ Environment setup failed!")
        print("Please resolve the issues above and try again.")
        return

    if "--check" in args:
        print("\n✅ System check completed successfully!")
        return

    # Start GUI application
    try:
        print("\n🚀 Starting DivyaDrishti GUI...")
        gui_main()
    except KeyboardInterrupt:
        print("\n\n👋 Application interrupted by user")
    except Exception as e:
        print(f"\n❌ Application error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("\n👋 DivyaDrishti shutdown complete")

if __name__ == "__main__":
    main()
