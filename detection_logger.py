"""
DivyaDrishti Detection Logger
Logging system for foottrail detections
"""

import csv
import json
from datetime import datetime
import config

class DetectionLogger:
    def __init__(self):
        self.log_file = config.LOGS_DIR / "foottrail_detections.csv"
        self.json_log_file = config.LOGS_DIR / "foottrail_detections.json"
        self.detections = []
        self.session_stats = {
            'session_start': datetime.now(),
            'total_detections': 0,
            'unique_objects': set(),
            'trail_detections': 0,
            'person_detections': 0,
            'other_detections': 0
        }

        # Ensure log directory exists
        config.LOGS_DIR.mkdir(parents=True, exist_ok=True)

        # Initialize CSV file with headers
        self._initialize_csv()

    def _initialize_csv(self):
        """Initialize CSV file with headers"""
        if not self.log_file.exists():
            with open(self.log_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    'timestamp', 'session_id', 'frame_number', 'object_class',
                    'confidence', 'bbox_x1', 'bbox_y1', 'bbox_x2', 'bbox_y2',
                    'center_x', 'center_y', 'area', 'detection_mode'
                ])

    def log_detection(self, detection, frame_number=0, session_id="default"):
        """Log a single detection"""
        if not config.LOG_DETECTIONS:
            return

        timestamp = datetime.now()

        # Create log entry
        log_entry = {
            'timestamp': timestamp.isoformat(),
            'session_id': session_id,
            'frame_number': frame_number,
            'object_class': detection['class_name'],
            'confidence': detection['confidence'],
            'bbox': detection['bbox'],
            'center': detection['center'],
            'area': detection['area'],
            'detection_mode': config.DETECTION_MODE
        }

        # Add to memory
        self.detections.append(log_entry)

        # Update session stats
        self._update_session_stats(detection)

        # Write to CSV
        self._write_to_csv(log_entry)

        # Keep only recent detections in memory
        if len(self.detections) > config.MAX_LOG_ENTRIES:
            self.detections = self.detections[-config.MAX_LOG_ENTRIES:]

    def _update_session_stats(self, detection):
        """Update session statistics"""
        self.session_stats['total_detections'] += 1
        self.session_stats['unique_objects'].add(detection['class_name'])

        class_name = detection['class_name'].lower()
        if 'trail' in class_name or 'path' in class_name:
            self.session_stats['trail_detections'] += 1
        elif 'person' in class_name or 'hiker' in class_name:
            self.session_stats['person_detections'] += 1
        else:
            self.session_stats['other_detections'] += 1

    def _write_to_csv(self, log_entry):
        """Write log entry to CSV file"""
        try:
            with open(self.log_file, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    log_entry['timestamp'],
                    log_entry['session_id'],
                    log_entry['frame_number'],
                    log_entry['object_class'],
                    log_entry['confidence'],
                    log_entry['bbox'][0],  # x1
                    log_entry['bbox'][1],  # y1
                    log_entry['bbox'][2],  # x2
                    log_entry['bbox'][3],  # y2
                    log_entry['center'][0],  # center_x
                    log_entry['center'][1],  # center_y
                    log_entry['area'],
                    log_entry['detection_mode']
                ])
        except Exception as e:
            print(f"✗ Error writing to CSV log: {e}")

    def get_recent_detections(self, limit=50):
        """Get recent detections"""
        return self.detections[-limit:] if self.detections else []

    def get_session_stats(self):
        """Get current session statistics"""
        stats = self.session_stats.copy()
        stats['unique_objects'] = list(stats['unique_objects'])
        stats['session_duration'] = str(datetime.now() - stats['session_start'])
        return stats

    def get_detection_summary(self):
        """Get detection summary for display - simplified notifications only"""
        if not self.detections:
            return "🔍 Monitoring for detections..."

        # Get recent detections (last 10)
        recent_detections = self.detections[-10:] if len(self.detections) > 10 else self.detections

        # Create simple notification lines
        notifications = []
        for detection in recent_detections:
            timestamp = detection['timestamp'].split('T')[1].split('.')[0]  # Get time only
            class_name = detection['object_class']
            notifications.append(f"🎯 {timestamp} - {class_name} detected")

        # Join notifications with newlines
        summary = "\n".join(notifications)
        return summary

    def export_logs(self, export_path=None, format='csv'):
        """Export logs to file"""
        if not self.detections:
            return False, "No detections to export"

        if export_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            if format == 'csv':
                export_path = config.LOGS_DIR / f"foottrail_detections_export_{timestamp}.csv"
            else:
                export_path = config.LOGS_DIR / f"foottrail_detections_export_{timestamp}.json"

        try:
            if format == 'csv':
                return self._export_csv(export_path)
            else:
                return self._export_json(export_path)
        except Exception as e:
            return False, f"Export error: {e}"

    def _export_csv(self, export_path):
        """Export logs to CSV format"""
        with open(export_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Write header
            writer.writerow([
                'timestamp', 'session_id', 'frame_number', 'object_class',
                'confidence', 'bbox_x1', 'bbox_y1', 'bbox_x2', 'bbox_y2',
                'center_x', 'center_y', 'area', 'detection_mode'
            ])

            # Write data
            for detection in self.detections:
                writer.writerow([
                    detection['timestamp'],
                    detection['session_id'],
                    detection['frame_number'],
                    detection['object_class'],
                    detection['confidence'],
                    detection['bbox'][0],
                    detection['bbox'][1],
                    detection['bbox'][2],
                    detection['bbox'][3],
                    detection['center'][0],
                    detection['center'][1],
                    detection['area'],
                    detection['detection_mode']
                ])

        return True, f"CSV exported to: {export_path}"

    def _export_json(self, export_path):
        """Export logs to JSON format"""
        export_data = {
            'session_info': self.get_session_stats(),
            'detections': self.detections
        }

        with open(export_path, 'w', encoding='utf-8') as file:
            json.dump(export_data, file, indent=2, default=str)

        return True, f"JSON exported to: {export_path}"

    def clear_logs(self):
        """Clear current session logs"""
        self.detections.clear()
        self.session_stats = {
            'session_start': datetime.now(),
            'total_detections': 0,
            'unique_objects': set(),
            'trail_detections': 0,
            'person_detections': 0,
            'other_detections': 0
        }
        print("✓ Detection logs cleared")
