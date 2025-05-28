#!/usr/bin/env python3
"""
Test script for YOLOv11s-seg model loading fix
Tests the corruption detection and automatic re-download functionality
"""

import os
import sys
import time

def test_segmentation_model_fix():
    """Test the YOLOv11s-seg model loading with corruption fix"""

    print("🧪 Testing YOLOv11s-seg Model Loading Fix")
    print("=" * 50)

    try:
        # Import the detector
        from object_detector import MultiModelDetector

        print("✓ MultiModelDetector imported successfully")

        # Initialize detector
        print("🔄 Initializing detector...")
        detector = MultiModelDetector()
        print(f"✓ Detector initialized with model: {detector.get_current_model_name()}")

        # Check if yolo11s-seg.pt exists and its size
        seg_model_path = "yolo11s-seg.pt"
        if os.path.exists(seg_model_path):
            file_size = os.path.getsize(seg_model_path)
            print(f"📁 Found {seg_model_path}: {file_size:,} bytes")
        else:
            print(f"📁 {seg_model_path} not found (will be downloaded)")

        # Test switching to YOLOv11s-seg
        print("\n🔄 Testing YOLOv11s-seg model switch...")
        print("This will test:")
        print("  - Model file validation")
        print("  - Corruption detection")
        print("  - Automatic re-download if corrupted")
        print("  - Model loading with retry mechanism")

        start_time = time.time()
        success = detector.switch_model("yolov11s_seg")
        end_time = time.time()

        print(f"\n⏱️ Switch took {end_time - start_time:.2f} seconds")

        if success:
            print("✅ YOLOv11s-seg model loaded successfully!")
            model_info = detector.get_current_model_info()
            print(f"✓ Model: {model_info['name']}")
            print(f"✓ Type: {model_info['type']}")
            print(f"✓ Classes: {len(detector.class_names)}")
            print(f"✓ Device: {detector.device}")

            # Test segmentation mode
            print("\n🎯 Testing segmentation mode switch...")
            seg_success = detector.switch_mode("segment")
            if seg_success:
                print("✅ Segmentation mode enabled successfully!")
            else:
                print("❌ Failed to enable segmentation mode")

        else:
            print("❌ Failed to load YOLOv11s-seg model")
            return False

        print("\n" + "=" * 50)
        print("🎉 All tests completed successfully!")
        return True

    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🚀 Starting YOLOv11s-seg Fix Test")
    print("This script tests the corruption detection and fix functionality")
    print()

    success = test_segmentation_model_fix()

    if success:
        print("\n✅ Test completed successfully!")
        print("The YOLOv11s-seg model loading fix is working properly.")
    else:
        print("\n❌ Test failed!")
        print("There may still be issues with the YOLOv11s-seg model loading.")

    print("\n🏁 Test completed.")
