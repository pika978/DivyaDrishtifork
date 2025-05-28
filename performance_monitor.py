"""
HickOyolo Performance Monitor
System performance tracking for hiking trail detection
"""

import time
import psutil
import threading
from collections import deque
from datetime import datetime
import config

class PerformanceMonitor:
    def __init__(self):
        self.fps_history = deque(maxlen=100)
        self.inference_times = deque(maxlen=100)
        self.cpu_usage = deque(maxlen=100)
        self.memory_usage = deque(maxlen=100)
        self.gpu_usage = deque(maxlen=100)
        
        self.monitoring = False
        self.monitor_thread = None
        
        # Performance counters
        self.frame_count = 0
        self.start_time = time.time()
        self.last_fps_update = time.time()
        self.fps_counter = 0
        
        # System info
        self.cpu_count = psutil.cpu_count()
        self.memory_total = psutil.virtual_memory().total / (1024**3)  # GB
        
        # GPU monitoring (if available)
        self.gpu_available = self._check_gpu_availability()
    
    def _check_gpu_availability(self):
        """Check if GPU monitoring is available"""
        try:
            import torch
            return torch.cuda.is_available()
        except ImportError:
            return False
    
    def start_monitoring(self):
        """Start performance monitoring"""
        if not self.monitoring:
            self.monitoring = True
            self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
            self.monitor_thread.start()
            print("✓ Performance monitoring started")
    
    def stop_monitoring(self):
        """Stop performance monitoring"""
        self.monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=1)
        print("✓ Performance monitoring stopped")
    
    def _monitor_loop(self):
        """Main monitoring loop"""
        while self.monitoring:
            try:
                # CPU usage
                cpu_percent = psutil.cpu_percent(interval=None)
                self.cpu_usage.append(cpu_percent)
                
                # Memory usage
                memory = psutil.virtual_memory()
                memory_percent = memory.percent
                self.memory_usage.append(memory_percent)
                
                # GPU usage (if available)
                if self.gpu_available:
                    gpu_percent = self._get_gpu_usage()
                    self.gpu_usage.append(gpu_percent)
                
                time.sleep(config.PERFORMANCE_LOG_INTERVAL)
                
            except Exception as e:
                print(f"Performance monitoring error: {e}")
                time.sleep(1)
    
    def _get_gpu_usage(self):
        """Get GPU usage percentage"""
        try:
            import torch
            if torch.cuda.is_available():
                # Get GPU memory usage
                memory_used = torch.cuda.memory_allocated(0)
                memory_total = torch.cuda.max_memory_allocated(0)
                if memory_total > 0:
                    return (memory_used / memory_total) * 100
            return 0
        except Exception:
            return 0
    
    def update_fps(self, inference_time=None):
        """Update FPS counter"""
        current_time = time.time()
        self.frame_count += 1
        self.fps_counter += 1
        
        # Calculate FPS every second
        if current_time - self.last_fps_update >= 1.0:
            fps = self.fps_counter / (current_time - self.last_fps_update)
            self.fps_history.append(fps)
            self.fps_counter = 0
            self.last_fps_update = current_time
        
        # Record inference time
        if inference_time is not None:
            self.inference_times.append(inference_time)
    
    def get_current_fps(self):
        """Get current FPS"""
        return self.fps_history[-1] if self.fps_history else 0
    
    def get_average_fps(self, window=30):
        """Get average FPS over window"""
        if not self.fps_history:
            return 0
        recent_fps = list(self.fps_history)[-window:]
        return sum(recent_fps) / len(recent_fps)
    
    def get_current_stats(self):
        """Get current performance statistics"""
        stats = {
            'fps': self.get_current_fps(),
            'avg_fps': self.get_average_fps(),
            'total_frames': self.frame_count,
            'uptime': time.time() - self.start_time,
            'cpu_usage': self.cpu_usage[-1] if self.cpu_usage else 0,
            'memory_usage': self.memory_usage[-1] if self.memory_usage else 0,
            'gpu_usage': self.gpu_usage[-1] if self.gpu_usage else 0,
            'avg_inference_time': self._get_avg_inference_time()
        }
        return stats
    
    def _get_avg_inference_time(self):
        """Get average inference time in milliseconds"""
        if not self.inference_times:
            return 0
        recent_times = list(self.inference_times)[-30:]  # Last 30 frames
        return (sum(recent_times) / len(recent_times)) * 1000  # Convert to ms
    
    def get_performance_summary(self):
        """Get formatted performance summary"""
        stats = self.get_current_stats()
        uptime_str = self._format_uptime(stats['uptime'])
        
        summary = f"""
🚀 HickOyolo Performance Monitor
═══════════════════════════════════════
⏱️  Uptime: {uptime_str}
📊 Total Frames: {stats['total_frames']:,}
🎯 Current FPS: {stats['fps']:.1f}
📈 Average FPS: {stats['avg_fps']:.1f}
⚡ Inference Time: {stats['avg_inference_time']:.1f}ms

💻 System Resources:
   CPU Usage: {stats['cpu_usage']:.1f}%
   Memory Usage: {stats['memory_usage']:.1f}%
   GPU Usage: {stats['gpu_usage']:.1f}%

🔧 System Info:
   CPU Cores: {self.cpu_count}
   Total Memory: {self.memory_total:.1f}GB
   GPU Available: {'Yes' if self.gpu_available else 'No'}
═══════════════════════════════════════
        """
        return summary.strip()
    
    def _format_uptime(self, seconds):
        """Format uptime in human readable format"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def get_performance_grade(self):
        """Get performance grade based on current stats"""
        stats = self.get_current_stats()
        fps = stats['avg_fps']
        cpu = stats['cpu_usage']
        memory = stats['memory_usage']
        
        # Calculate grade based on performance metrics
        if fps >= 25 and cpu < 70 and memory < 80:
            return "A+", "Excellent", "#00ff41"
        elif fps >= 20 and cpu < 80 and memory < 85:
            return "A", "Very Good", "#00d4ff"
        elif fps >= 15 and cpu < 85 and memory < 90:
            return "B", "Good", "#ffff00"
        elif fps >= 10 and cpu < 90 and memory < 95:
            return "C", "Fair", "#ff8000"
        else:
            return "D", "Poor", "#ff0080"
    
    def reset_stats(self):
        """Reset all performance statistics"""
        self.fps_history.clear()
        self.inference_times.clear()
        self.cpu_usage.clear()
        self.memory_usage.clear()
        self.gpu_usage.clear()
        
        self.frame_count = 0
        self.start_time = time.time()
        self.last_fps_update = time.time()
        self.fps_counter = 0
        
        print("✓ Performance statistics reset")
    
    def export_performance_log(self, filepath=None):
        """Export performance data to file"""
        if filepath is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = config.LOGS_DIR / f"performance_log_{timestamp}.json"
        
        try:
            import json
            
            data = {
                'timestamp': datetime.now().isoformat(),
                'session_info': {
                    'uptime': time.time() - self.start_time,
                    'total_frames': self.frame_count,
                    'system_info': {
                        'cpu_count': self.cpu_count,
                        'memory_total_gb': self.memory_total,
                        'gpu_available': self.gpu_available
                    }
                },
                'performance_data': {
                    'fps_history': list(self.fps_history),
                    'inference_times': list(self.inference_times),
                    'cpu_usage': list(self.cpu_usage),
                    'memory_usage': list(self.memory_usage),
                    'gpu_usage': list(self.gpu_usage)
                },
                'current_stats': self.get_current_stats()
            }
            
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2, default=str)
            
            return True, f"Performance log exported to: {filepath}"
            
        except Exception as e:
            return False, f"Export error: {e}"
