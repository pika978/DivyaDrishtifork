#!/usr/bin/env python3
"""
DivyaDrishti Launcher
Ensures proper module isolation and launches the DivyaDrishti system
"""

import sys
import os
from pathlib import Path

# Ensure we're using only DivyaDrishti modules
current_dir = Path(__file__).parent.absolute()

# Remove parent directory from Python path to avoid conflicts
parent_dir = current_dir.parent
if str(parent_dir) in sys.path:
    sys.path.remove(str(parent_dir))

# Add only the DivyaDrishti directory to the front of the path
sys.path.insert(0, str(current_dir))

# Change working directory to DivyaDrishti
os.chdir(current_dir)

print("🎯 DivyaDrishti Launcher")
print("=" * 50)
print(f"Working Directory: {os.getcwd()}")
print(f"Python Path (first 3): {sys.path[:3]}")
print("=" * 50)

try:
    # Import DivyaDrishti modules
    print("📦 Loading DivyaDrishti modules...")

    import config
    print(f"✓ Config loaded: {config.APP_NAME} v{config.APP_VERSION}")

    import utils
    print("✓ Utils loaded")

    from object_detector import MultiModelDetector
    print("✓ MultiModelDetector loaded")

    from detection_logger import DetectionLogger
    print("✓ DetectionLogger loaded")

    from performance_monitor import PerformanceMonitor
    print("✓ PerformanceMonitor loaded")

    print("\n🚀 Starting DivyaDrishti GUI...")

    # Import and start GUI
    import tkinter as tk
    from gui_app import DivyaDrishtiGUI

    # Create and run the application
    root = tk.Tk()
    app = DivyaDrishtiGUI(root)

    # Handle window closing
    def on_closing():
        if hasattr(app, 'on_closing'):
            app.on_closing()
        else:
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    print("✅ DivyaDrishti GUI started successfully!")
    print("🎮 GUI window should now be visible...")

    # Start the main loop
    root.mainloop()

except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please ensure all DivyaDrishti modules are present.")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error starting DivyaDrishti: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
finally:
    print("\n👋 DivyaDrishti shutdown complete")

if __name__ == "__main__":
    pass
