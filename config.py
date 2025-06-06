"""
DivyaDrishti Configuration Settings
Independent Hiking Trail Detection System
"""

import os
from pathlib import Path

# Application Info
APP_NAME = "DivyaDrishti"
APP_VERSION = "1.0.0"
WINDOW_TITLE = f"{APP_NAME} - AI Drone Surveillance System v{APP_VERSION}"

# Paths
BASE_DIR = Path(__file__).parent
HIKING_MODEL_PATH = BASE_DIR.parent / "FootTrail Detection Model" / "hiking_trail_dataset" / "pretrained_model" / "foottrail.pt"
SCREENSHOTS_DIR = BASE_DIR / "screenshots"
SAVED_VIDEOS_DIR = BASE_DIR / "saved_videos"
LOGS_DIR = BASE_DIR / "logs"

# Multi-Model Configuration
AVAILABLE_MODELS = {
    "foottrail": {
        "name": "FootTrail Detection Model",
        "description": "Custom foottrail/hiking detection",
        "path": str(HIKING_MODEL_PATH),
        "type": "custom",
        "classes": ["trail", "path", "hiking_trail", "walkway", "footpath", "person", "hiker", "backpack", "tent", "camping_gear"],
        "icon": "🥾",
        "color": "#00ff41"
    },
    "yolov11n": {
        "name": "YOLOv11n",
        "description": "Fast general detection (nano)",
        "path": "yolo11n.pt",
        "type": "coco",
        "classes": ["person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light"],
        "icon": "⚡",
        "color": "#00d4ff"
    },
    "yolov11s": {
        "name": "YOLOv11s",
        "description": "Balanced performance (small)",
        "path": "yolo11s.pt",
        "type": "coco",
        "classes": ["person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light"],
        "icon": "⚖️",
        "color": "#ff8000"
    },
    "yolov11m": {
        "name": "YOLOv11m",
        "description": "High accuracy (medium)",
        "path": "yolo11m.pt",
        "type": "coco",
        "classes": ["person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light"],
        "icon": "🎯",
        "color": "#ff0080"
    },
    "yolov11s_seg": {
        "name": "YOLOv11s-seg",
        "description": "Segmentation mode",
        "path": "yolo11s-seg.pt",
        "type": "segmentation",
        "classes": ["person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light"],
        "icon": "🎨",
        "color": "#8000ff"
    }
}

# Default Model Settings
DEFAULT_MODEL_KEY = "foottrail"
CURRENT_MODEL = DEFAULT_MODEL_KEY
CONFIDENCE_THRESHOLD = 0.5
IOU_THRESHOLD = 0.45
MAX_DETECTIONS = 1000

# Detection Settings
DETECTION_MODE = "detect"  # "detect" or "segment"

# Performance Settings
SKIP_FRAMES = 1  # Process every frame for best quality
MAX_FPS = 30
ENABLE_GPU = True
DEVICE = "auto"  # "auto", "cpu", "cuda", "mps"

# GUI Settings - Cyberpunk Theme
CYBERPUNK_THEME = {
    "bg_color": "#0a0a0a",
    "primary_color": "#00ff41",
    "secondary_color": "#ff0080",
    "accent_color": "#00d4ff",
    "text_color": "#ffffff",
    "button_color": "#1a1a1a",
    "button_hover": "#2a2a2a",
    "border_color": "#333333"
}

# Window Settings
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 1000
RESIZABLE = True

# Drone Video Settings
DEFAULT_DRONE_FEED = 0
DEFAULT_STREAM_URL = "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4"
SUPPORTED_FORMATS = [".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv", ".webm"]

# Logging Settings
LOG_DETECTIONS = True
LOG_LEVEL = "INFO"
MAX_LOG_ENTRIES = 1000

# Screenshot Settings
SCREENSHOT_FORMAT = "jpg"
SCREENSHOT_QUALITY = 95
AUTO_SAVE_SCREENSHOTS = False

# Performance Monitoring
MONITOR_PERFORMANCE = True
PERFORMANCE_LOG_INTERVAL = 5  # seconds

# Advanced Features
ENABLE_SEGMENTATION = True
ENABLE_POSE_ESTIMATION = False
ENABLE_CLASSIFICATION = True

# Hiking Trail Specific Settings
TRAIL_CLASSES = [
    "trail", "path", "hiking_trail", "walkway", "footpath",
    "person", "hiker", "backpack", "tent", "camping_gear"
]

# Detection Zones (for trail-specific detection)
DETECTION_ZONES = {
    "trail_center": {"enabled": True, "weight": 1.0},
    "trail_edges": {"enabled": True, "weight": 0.8},
    "off_trail": {"enabled": False, "weight": 0.3}
}

# Alert Settings
ENABLE_ALERTS = True
ALERT_CONFIDENCE_THRESHOLD = 0.7
ALERT_SOUND = True

# Export Settings
EXPORT_FORMAT = "csv"
INCLUDE_TIMESTAMPS = True
INCLUDE_COORDINATES = True
INCLUDE_CONFIDENCE = True

# Tracking Settings
USE_TRACKING = True
ENABLE_SINGLE_SHOT_DETECTION = True
CUSTOM_TRACKER_CONFIG = "divyadrishti_tracker.yaml"
