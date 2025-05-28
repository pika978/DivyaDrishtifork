"""
DivyaDrishti Multi-Model Object Detector
Support for multiple YOLO models with dynamic switching
"""

import cv2
import torch
import numpy as np
from ultralytics import YOLO
from pathlib import Path
import config
import utils

class MultiModelDetector:
    def __init__(self):
        self.model = None
        self.device = self._get_device()
        self.current_mode = config.DETECTION_MODE
        self.is_loaded = False
        self.class_names = []

        # Multi-model support
        self.current_model_key = config.DEFAULT_MODEL_KEY
        self.available_models = config.AVAILABLE_MODELS
        self.loaded_models = {}  # Cache for loaded models

        # Performance tracking
        self.inference_times = []
        self.frame_count = 0

        # Load the default model
        self.load_model(self.current_model_key)

    def _get_device(self):
        """Determine the best device for inference"""
        if config.DEVICE == "auto":
            if torch.cuda.is_available() and config.ENABLE_GPU:
                return "cuda"
            elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
                return "mps"
            else:
                return "cpu"
        return config.DEVICE

    def load_model(self, model_key=None):
        """Load a YOLO model by key (initial load only)"""
        if model_key is None:
            model_key = self.current_model_key

        # For initial load, use the fresh loading method
        return self._load_model_fresh(model_key)

    def is_model_loaded(self):
        """Check if model is loaded"""
        return self.is_loaded and self.model is not None

    def switch_model(self, model_key):
        """Switch to a different model"""
        if model_key == self.current_model_key:
            print(f"✓ Already using {self.available_models[model_key]['name']}")
            return True

        print(f"🔄 Switching from {self.get_current_model_name()} to {self.available_models[model_key]['name']}...")

        # Clear current model completely
        self.model = None
        self.is_loaded = False
        self.class_names = []

        # Clear GPU cache if using CUDA
        if self.device != "cpu":
            import torch
            torch.cuda.empty_cache()

        # Load the new model fresh (no caching for model switching)
        success = self._load_model_fresh(model_key)

        if success:
            print(f"✓ Successfully switched to {self.available_models[model_key]['name']}")
            print(f"✓ Model type: {self.available_models[model_key]['type']}")
            print(f"✓ Classes loaded: {len(self.class_names)}")
            print(f"✓ First 5 classes: {self.class_names[:5] if len(self.class_names) > 5 else self.class_names}")
        else:
            print(f"✗ Failed to switch to {self.available_models[model_key]['name']}")

        return success

    def _load_model_fresh(self, model_key):
        """Load a model fresh without using cache"""
        if model_key not in self.available_models:
            print(f"✗ Unknown model key: {model_key}")
            return False

        model_info = self.available_models[model_key]
        model_path = model_info["path"]

        try:
            print(f"🔄 Loading {model_info['name']} fresh from: {model_path}")

            # Validate model file before loading
            if not self._validate_model_file(model_path, model_info['name']):
                print(f"🔄 Attempting to re-download {model_info['name']}...")
                if not self._redownload_model(model_path, model_info['name']):
                    print(f"✗ Failed to re-download {model_info['name']}")
                    return False

            # Load new model (force fresh load - don't use any cache)
            self.model = YOLO(model_path)

            # Move model to device
            if self.device != "cpu":
                self.model.to(self.device)

            # Update current model key FIRST
            self.current_model_key = model_key

            # Force model to initialize by running a dummy prediction
            import numpy as np
            dummy_img = np.zeros((640, 640, 3), dtype=np.uint8)
            _ = self.model(dummy_img, verbose=False)

            # Get class names from the model after initialization
            if hasattr(self.model, 'names') and self.model.names:
                self.class_names = list(self.model.names.values())
                print(f"✓ Extracted {len(self.class_names)} classes from model.names")
                print(f"✓ Model classes: {self.class_names}")
            else:
                # Fallback to predefined classes
                self.class_names = model_info["classes"]
                print(f"✓ Using predefined {len(self.class_names)} classes")
                print(f"✓ Predefined classes: {self.class_names}")

            # DON'T cache the model - always load fresh for switching
            # self.loaded_models[model_key] = self.model

            self.is_loaded = True
            print(f"✓ {model_info['name']} loaded successfully on {self.device.upper()}")

            return True

        except Exception as e:
            print(f"✗ Error loading {model_info['name']}: {e}")

            # If it's a corrupted file error, try to fix it
            if "PytorchStreamReader failed" in str(e) or "failed finding central directory" in str(e):
                print(f"🔧 Detected corrupted model file. Attempting to fix...")
                if self._fix_corrupted_model(model_path, model_info['name']):
                    print(f"🔄 Retrying model load after fixing corruption...")
                    # Retry once with a flag to prevent infinite recursion
                    return self._load_model_retry(model_key)

            import traceback
            traceback.print_exc()
            self.is_loaded = False
            return False

    def _validate_model_file(self, model_path, model_name):
        """Validate if model file exists and is not corrupted"""
        import os

        # For custom models (absolute paths), check if file exists
        if os.path.isabs(model_path):
            if not os.path.exists(model_path):
                print(f"✗ Model file not found: {model_path}")
                return False

            # Check if file size is reasonable (not empty)
            file_size = os.path.getsize(model_path)
            if file_size < 1024:  # Less than 1KB is definitely corrupted
                print(f"✗ Model file too small ({file_size} bytes): {model_path}")
                return False

            print(f"✓ Custom model file validated: {model_path} ({file_size:,} bytes)")
            return True

        # For YOLO models (relative paths), check if they exist in current directory
        if os.path.exists(model_path):
            file_size = os.path.getsize(model_path)
            if file_size < 1024:  # Less than 1KB is definitely corrupted
                print(f"✗ Model file too small ({file_size} bytes): {model_path}")
                return False

            # Try to read the file as a zip to check if it's corrupted
            try:
                import torch
                # Just try to load the file structure without loading the model
                with open(model_path, 'rb') as f:
                    # Read first few bytes to check if it's a valid zip/torch file
                    header = f.read(4)
                    if len(header) < 4:
                        print(f"✗ Model file header too short: {model_path}")
                        return False

                print(f"✓ Model file validated: {model_path} ({file_size:,} bytes)")
                return True
            except Exception as e:
                print(f"✗ Model file validation failed: {e}")
                return False

        # File doesn't exist, will be downloaded by YOLO
        print(f"ℹ️ Model file will be downloaded: {model_path}")
        return True

    def _redownload_model(self, model_path, model_name):
        """Re-download a corrupted model file"""
        import os

        # Only handle YOLO models (not custom models)
        if os.path.isabs(model_path):
            print(f"✗ Cannot re-download custom model: {model_path}")
            return False

        try:
            # Delete the corrupted file
            if os.path.exists(model_path):
                print(f"🗑️ Deleting corrupted file: {model_path}")
                os.remove(model_path)

            # Let YOLO download it fresh
            print(f"📥 YOLO will download fresh copy of {model_name}")
            return True

        except Exception as e:
            print(f"✗ Error during re-download: {e}")
            return False

    def _fix_corrupted_model(self, model_path, model_name):
        """Fix a corrupted model file by re-downloading"""
        return self._redownload_model(model_path, model_name)

    def _load_model_retry(self, model_key):
        """Retry loading model after fixing corruption (no recursion)"""
        if model_key not in self.available_models:
            print(f"✗ Unknown model key: {model_key}")
            return False

        model_info = self.available_models[model_key]
        model_path = model_info["path"]

        try:
            print(f"🔄 Retry loading {model_info['name']} from: {model_path}")

            # Load new model (force fresh load - don't use any cache)
            self.model = YOLO(model_path)

            # Move model to device
            if self.device != "cpu":
                self.model.to(self.device)

            # Update current model key FIRST
            self.current_model_key = model_key

            # Force model to initialize by running a dummy prediction
            import numpy as np
            dummy_img = np.zeros((640, 640, 3), dtype=np.uint8)
            _ = self.model(dummy_img, verbose=False)

            # Get class names from the model after initialization
            if hasattr(self.model, 'names') and self.model.names:
                self.class_names = list(self.model.names.values())
                print(f"✓ Extracted {len(self.class_names)} classes from model.names")
                print(f"✓ Model classes: {self.class_names}")
            else:
                # Fallback to predefined classes
                self.class_names = model_info["classes"]
                print(f"✓ Using predefined {len(self.class_names)} classes")
                print(f"✓ Predefined classes: {self.class_names}")

            self.is_loaded = True
            print(f"✓ {model_info['name']} loaded successfully on retry!")

            return True

        except Exception as e:
            print(f"✗ Retry failed for {model_info['name']}: {e}")
            self.is_loaded = False
            return False

    def get_current_model_info(self):
        """Get information about the current model"""
        if self.current_model_key in self.available_models:
            return self.available_models[self.current_model_key]
        return None

    def get_current_model_name(self):
        """Get the name of the current model"""
        info = self.get_current_model_info()
        return info["name"] if info else "Unknown"

    def get_available_models(self):
        """Get list of available models"""
        return self.available_models

    def get_model_list_for_gui(self):
        """Get formatted model list for GUI dropdown"""
        models = []
        for key, info in self.available_models.items():
            display_name = f"{info['icon']} {info['name']} - {info['description']}"
            models.append((key, display_name))
        return models

    def detect(self, frame, confidence_threshold=None, enable_tracking=None):
        """Detect objects in frame using standard YOLO detection"""
        if not self.is_model_loaded():
            return frame, []

        if confidence_threshold is None:
            confidence_threshold = config.CONFIDENCE_THRESHOLD

        try:
            # Standard YOLO detection without tracking
            results = self.model(
                frame,
                conf=confidence_threshold,
                iou=config.IOU_THRESHOLD,
                max_det=config.MAX_DETECTIONS,
                device=self.device,
                verbose=False
            )

            # Process results
            detections = []
            annotated_frame = frame.copy()

            if results and len(results) > 0:
                result = results[0]

                if result.boxes is not None and len(result.boxes) > 0:
                    boxes = result.boxes.xyxy.cpu().numpy()
                    confidences = result.boxes.conf.cpu().numpy()
                    class_ids = result.boxes.cls.cpu().numpy().astype(int)

                    for i, (box, conf, cls_id) in enumerate(zip(boxes, confidences, class_ids)):
                        x1, y1, x2, y2 = box

                        # Get class name
                        class_name = self.class_names[cls_id] if cls_id < len(self.class_names) else f"class_{cls_id}"

                        # Create detection info
                        detection = {
                            'bbox': [int(x1), int(y1), int(x2), int(y2)],
                            'confidence': float(conf),
                            'class_id': int(cls_id),
                            'class_name': class_name,
                            'area': utils.calculate_box_area(x1, y1, x2, y2),
                            'center': utils.calculate_box_center(x1, y1, x2, y2)
                        }

                        detections.append(detection)

                        # Draw bounding box and label
                        annotated_frame = self._draw_detection(annotated_frame, detection)

            self.frame_count += 1
            return annotated_frame, detections

        except Exception as e:
            print(f"✗ Detection error: {e}")
            return frame, []



    def _draw_detection(self, frame, detection):
        """Draw detection on frame with cyberpunk styling"""
        x1, y1, x2, y2 = detection['bbox']
        confidence = detection['confidence']
        class_name = detection['class_name']

        # Grey color scheme as requested
        color = (128, 128, 128)  # Grey for all detections

        # Draw bounding box with cyberpunk style
        thickness = 2
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)

        # Draw corner accents
        corner_length = 20
        corner_thickness = 3

        # Top-left corner
        cv2.line(frame, (x1, y1), (x1 + corner_length, y1), color, corner_thickness)
        cv2.line(frame, (x1, y1), (x1, y1 + corner_length), color, corner_thickness)

        # Top-right corner
        cv2.line(frame, (x2, y1), (x2 - corner_length, y1), color, corner_thickness)
        cv2.line(frame, (x2, y1), (x2, y1 + corner_length), color, corner_thickness)

        # Bottom-left corner
        cv2.line(frame, (x1, y2), (x1 + corner_length, y2), color, corner_thickness)
        cv2.line(frame, (x1, y2), (x1, y2 - corner_length), color, corner_thickness)

        # Bottom-right corner
        cv2.line(frame, (x2, y2), (x2 - corner_length, y2), color, corner_thickness)
        cv2.line(frame, (x2, y2), (x2, y2 - corner_length), color, corner_thickness)

        # Label without track ID
        label = f"{class_name} {confidence:.2%}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.6
        font_thickness = 2

        (label_width, label_height), baseline = cv2.getTextSize(label, font, font_scale, font_thickness)

        # Draw label background
        cv2.rectangle(frame,
                     (x1, y1 - label_height - 10),
                     (x1 + label_width + 10, y1),
                     (0, 0, 0), -1)

        # Draw label border
        cv2.rectangle(frame,
                     (x1, y1 - label_height - 10),
                     (x1 + label_width + 10, y1),
                     color, 1)

        # Draw label text
        cv2.putText(frame, label, (x1 + 5, y1 - 5), font, font_scale, color, font_thickness)

        return frame

    def get_performance_stats(self):
        """Get performance statistics"""
        if len(self.inference_times) == 0:
            return {
                'avg_inference_time': 0,
                'fps': 0,
                'total_frames': self.frame_count
            }

        avg_time = np.mean(self.inference_times[-100:])  # Last 100 frames
        fps = 1.0 / avg_time if avg_time > 0 else 0

        return {
            'avg_inference_time': avg_time * 1000,  # Convert to ms
            'fps': fps,
            'total_frames': self.frame_count
        }

    def reset_stats(self):
        """Reset performance statistics"""
        self.inference_times.clear()
        self.frame_count = 0

    def switch_mode(self, mode):
        """Switch between detection and segmentation modes"""
        if mode not in ["detect", "segment"]:
            return False

        try:
            # For hiking trail model, we'll use the same model but different inference
            self.current_mode = mode
            print(f"✓ Switched to {mode} mode")
            return True
        except Exception as e:
            print(f"✗ Error switching mode: {e}")
            return False
