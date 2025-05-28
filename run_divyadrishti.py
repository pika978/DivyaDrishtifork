#!/usr/bin/env python3
"""
DivyaDrishti Complete System Launcher
Final production-ready hiking trail detection system with single shot detection and tracking
"""

import sys
import os
import time
from pathlib import Path

def print_banner():
    """Print DivyaDrishti banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║    🥾 DivyaDrishti v1.0.0 - Complete System                 ║
    ║    🎯 Hiking Trail Detection with Single Shot Tracking      ║
    ║    🚀 Production Ready System                                ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_system_requirements():
    """Check if all system requirements are met"""
    print("🔍 Checking System Requirements...")

    # Check Python version
    if sys.version_info < (3.8, 0):
        print("❌ Python 3.8+ required")
        return False
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

    # Check required modules
    required_modules = [
        'torch', 'torchvision', 'ultralytics', 'cv2', 'numpy',
        'PIL', 'tkinter', 'pandas', 'matplotlib'
    ]

    missing_modules = []
    for module in required_modules:
        try:
            if module == 'cv2':
                import cv2
            elif module == 'PIL':
                from PIL import Image
            elif module == 'tkinter':
                import tkinter
            else:
                __import__(module)
            print(f"✓ {module}")
        except ImportError:
            missing_modules.append(module)
            print(f"❌ {module}")

    if missing_modules:
        print(f"\n❌ Missing modules: {', '.join(missing_modules)}")
        print("Run: pip install -r requirements.txt")
        return False

    return True

def check_models():
    """Check if required models are available"""
    print("\n🎯 Checking Models...")

    # Check foottrail model
    foottrail_model_path = Path("../FootTrail Detection Model/hiking_trail_dataset/pretrained_model/foottrail.pt")
    if foottrail_model_path.exists():
        print(f"✓ FootTrail Detection Model: {foottrail_model_path}")
    else:
        print(f"❌ FootTrail Detection Model not found: {foottrail_model_path}")
        return False

    # Check tracker configuration
    tracker_config = Path("divyadrishti_tracker.yaml")
    if tracker_config.exists():
        print(f"✓ Custom Tracker Config: {tracker_config}")
    else:
        print(f"❌ Tracker config not found: {tracker_config}")
        return False

    return True

def check_gpu():
    """Check GPU availability"""
    print("\n🖥️ Checking GPU...")

    try:
        import torch
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            print(f"✓ GPU Available: {gpu_name}")
            print(f"✓ CUDA Version: {torch.version.cuda}")
            return True
        else:
            print("⚠️ No GPU available, will use CPU")
            return True
    except Exception as e:
        print(f"❌ GPU check failed: {e}")
        return False

def show_system_info():
    """Show complete system information"""
    print("\n📊 System Information:")
    print("=" * 50)

    try:
        import config
        print(f"App Name: {config.APP_NAME}")
        print(f"Version: {config.APP_VERSION}")
        print(f"Window Size: {config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        print(f"Confidence Threshold: {config.CONFIDENCE_THRESHOLD}")
        print(f"IoU Threshold: {config.IOU_THRESHOLD}")
        print(f"Tracking Enabled: {config.USE_TRACKING}")
        print(f"Single Shot Detection: {config.ENABLE_SINGLE_SHOT_DETECTION}")
        print(f"Custom Tracker: {config.CUSTOM_TRACKER_CONFIG}")
        print(f"GPU Enabled: {config.ENABLE_GPU}")
        print(f"Max FPS: {config.MAX_FPS}")
    except Exception as e:
        print(f"❌ Could not load config: {e}")

def show_features():
    """Show system features"""
    print("\n🚀 System Features:")
    print("=" * 50)
    features = [
        "🎯 Multi-Model Support (Hiking Trail, YOLOv11n/s/m, YOLOv11s-seg)",
        "📍 Advanced Object Tracking (BoT-SORT with ReID)",
        "🎯 Single Shot Detection (Prevents Duplicate Detections)",
        "🖥️ GPU Acceleration (CUDA Support)",
        "🎨 Cyberpunk-themed GUI with Real-time Controls",
        "📊 Performance Monitoring and Logging",
        "💾 Auto-save Screenshots and Detection Logs",
        "🔧 Real-time Parameter Adjustment",
        "📈 Detection Analytics and Statistics",
        "🎮 Interactive Controls and Model Switching"
    ]

    for feature in features:
        print(f"  {feature}")

def launch_system():
    """Launch the complete DivyaDrishti system"""
    print("\n🚀 Launching DivyaDrishti Complete System...")
    print("=" * 50)

    try:
        # Import and launch the GUI
        from gui_app import DivyaDrishtiGUI

        print("✓ GUI modules loaded")
        print("✓ Starting graphical interface...")

        # Create and run the application
        app = DivyaDrishtiGUI()
        print("✅ DivyaDrishti system launched successfully!")
        print("\n🎮 GUI Controls:")
        print("  🎯 SINGLE-SHOT: Toggle single shot detection")
        print("  📍 TRACKING: Toggle object tracking")
        print("  🎯 SEGMENTATION: Toggle segmentation mode")
        print("  🎚️ CONFIDENCE: Adjust detection threshold")
        print("  📹 SOURCE: Select video input (Camera/File/Stream)")
        print("  🎯 MODEL: Switch between YOLO models")

        app.run()

    except Exception as e:
        print(f"❌ Failed to launch system: {e}")
        import traceback
        traceback.print_exc()
        return False

    return True

def main():
    """Main launcher function"""
    print_banner()

    # System checks
    if not check_system_requirements():
        print("\n❌ System requirements not met!")
        return False

    if not check_models():
        print("\n❌ Required models not found!")
        return False

    if not check_gpu():
        print("\n❌ GPU check failed!")
        return False

    # Show system information
    show_system_info()
    show_features()

    # Launch confirmation
    print("\n" + "=" * 60)
    print("🎯 Ready to launch DivyaDrishti Complete System!")
    print("=" * 60)

    try:
        user_input = input("\nPress Enter to launch or 'q' to quit: ").strip().lower()
        if user_input == 'q':
            print("👋 Goodbye!")
            return True
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        return True

    # Launch the system
    success = launch_system()

    if success:
        print("\n✅ DivyaDrishti system completed successfully!")
    else:
        print("\n❌ DivyaDrishti system encountered errors!")

    return success

if __name__ == "__main__":
    print("🎯 DivyaDrishti Complete System Launcher")
    print("🥾 Advanced Hiking Trail Detection with Single Shot Tracking")
    print()

    success = main()

    if not success:
        print("\n🔧 Troubleshooting:")
        print("  1. Check requirements: pip install -r requirements.txt")
        print("  2. Verify hiking trail model path")
        print("  3. Check GPU drivers and CUDA installation")
        print("  4. Run test_single_shot_tracking.py for diagnostics")

    print("\n🏁 Launcher finished.")
