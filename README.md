# 🎯 DivyaDrishti - AI-Powered Drone Surveillance System

<div align="center">

![DivyaDrishti Logo](https://img.shields.io/badge/DivyaDrishti-AI%20Surveillance-00ff41?style=for-the-badge&logo=drone&logoColor=white)

**Advanced AI-Powered Drone Surveillance System with Custom FootTrail Detection**

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.5.1+-ee4c2c?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org)
[![YOLO](https://img.shields.io/badge/YOLO-v11-00d4ff?style=flat-square&logo=yolo&logoColor=white)](https://ultralytics.com)
[![CUDA](https://img.shields.io/badge/CUDA-12.1-76b900?style=flat-square&logo=nvidia&logoColor=white)](https://developer.nvidia.com/cuda-zone)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

</div>

## 🌟 Overview

**DivyaDrishti** is a cutting-edge AI-powered drone surveillance system specifically designed for outdoor monitoring and foottrail detection. Built with state-of-the-art computer vision technology, it features a **custom-trained YOLO model** for specialized foottrail and outdoor environment detection, wrapped in an intuitive cyberpunk-themed interface.

### 🎯 Key Highlights
- **Custom FootTrail Detection Model**: Specially trained YOLO model for outdoor/hiking scenarios
- **Real-time AI Processing**: GPU-accelerated detection with 25-30 FPS performance
- **Multi-Model Support**: Dynamic switching between YOLOv11 variants
- **Cyberpunk GUI**: Futuristic interface with real-time monitoring capabilities
- **Comprehensive Logging**: Advanced detection tracking and performance monitoring

## 🚀 Features

### 🤖 AI Detection Capabilities
- **🥾 Custom FootTrail Detection**: Specialized model trained for outdoor environments
- **👤 Person & Hiker Detection**: Real-time human detection and tracking
- **🌿 Vegetation & Terrain Analysis**: Grass, rocks, trails, and natural structures
- **📦 Equipment Recognition**: Outdoor gear and camping equipment detection
- **🎯 Multi-Class Detection**: 8+ specialized outdoor environment classes

### ⚡ Advanced Technology
- **🔄 Real-time Processing**: Live video feed analysis with GPU acceleration
- **🤖 AI Segmentation**: Toggle between detection and segmentation modes
- **📊 Performance Monitoring**: Real-time FPS and system metrics
- **💾 Smart Logging**: Simplified notification-based detection logs
- **📸 Auto-capture**: Intelligent screenshot and video recording
- **🗺️ Tactical Mapping**: Interactive drone location visualization

### 🎮 User Experience
- **🌌 Cyberpunk Interface**: Dark theme with neon accents and animations
- **📱 Intuitive Controls**: Easy-to-use detection controls and settings
- **📊 Live Dashboard**: Real-time performance and detection statistics
- **🔧 Dynamic Configuration**: Hot-swappable models and settings
- **📹 Multi-source Input**: Camera, video files, and stream support

## 🛠️ Technology Stack

### 🧠 AI/ML Framework
```
🔥 PyTorch 2.5.1+        # Deep learning framework with CUDA support
🎯 Ultralytics YOLOv11   # State-of-the-art object detection
🖼️ OpenCV 4.11.0+        # Computer vision and image processing
🔢 NumPy & Pandas        # Data processing and numerical computing
⚡ CUDA 12.1             # GPU acceleration for real-time processing
```

### 💻 Core Technologies
```
🐍 Python 3.8+          # Primary programming language
🖥️ Tkinter               # GUI framework with custom styling
🧵 Threading             # Multi-threaded processing
📊 JSON/CSV              # Data logging and export
🌐 HTML/JavaScript       # Tactical map interface
```

### 🎨 Additional Libraries
```
🖼️ Pillow (PIL)          # Image processing and manipulation
📁 Pathlib               # Modern path handling
⏰ DateTime              # Timestamp management
🌐 Webbrowser            # Tactical map integration
```

## 🎯 Custom FootTrail Detection Model

### 🏗️ Model Architecture
- **Base**: YOLOv11 architecture optimized for outdoor environments
- **Training Data**: Custom dataset of hiking trails, outdoor terrains, and natural environments
- **Classes**: 8 specialized outdoor detection classes
- **Performance**: 25-30 FPS on NVIDIA GTX 1650, 54.8MB model size

### 🌿 Detection Classes
```
🌱 grass          # Grass and ground vegetation
🪨 rock           # Rock formations and stones
🥾 rocky-trail    # Rocky hiking trails
🌳 roots          # Tree roots and natural obstacles
🛤️ rough-trail    # Rough or uneven trail surfaces
🏗️ structure      # Man-made structures and facilities
🌲 tree-trunk     # Tree trunks and large vegetation
🌿 vegetation     # General vegetation and plant life
```

### 📊 Model Performance
- **Accuracy**: High precision for outdoor environment detection
- **Speed**: Real-time processing at 25-30 FPS (GPU)
- **Size**: Optimized 54.8MB model for efficient deployment
- **Compatibility**: CUDA-accelerated with CPU fallback support

## 📁 Project Structure

```
DivyaDrishti/
├── 🎯 main.py                      # Application entry point
├── 🎮 gui_app.py                   # Cyberpunk-themed GUI interface
├── 🤖 object_detector.py           # Multi-model YOLO detector
├── 📊 detection_logger.py          # Simplified notification logging
├── ⚡ performance_monitor.py       # Real-time performance tracking
├── 🔧 config.py                    # System configuration
├── 🛠️ utils.py                     # Utility functions and helpers
├── 📋 requirements.txt             # Python dependencies
├── 🎯 divyadrishti_tracker.yaml    # Custom tracking configuration
├── 🗺️ tactical_map.html            # Interactive map interface
├── 🚀 Installation Scripts/
│   ├── install.bat                 # Windows installation
│   ├── install.sh                  # Linux/macOS installation
│   └── install_dependencies.py     # Python dependency installer
├── 📁 logs/                        # Detection and performance logs
├── 📸 screenshots/                 # Captured screenshots
├── 🎬 saved_videos/                # Processed video outputs
├── 📚 Documentation/
│   ├── README.md                   # This file
│   ├── SYSTEM_OVERVIEW.md          # Technical overview
│   └── SYSTEM_COMPLETE.md          # Complete system documentation
└── 🎯 Models/
    └── FootTrail Detection Model/  # Custom trained model
        └── hiking_trail_dataset/
            └── pretrained_model/
                └── foottrail.pt    # Custom FootTrail YOLO model
```

## 🚀 Quick Start Guide

### 📋 Prerequisites
- **Python**: 3.8 or higher
- **GPU**: NVIDIA GPU with CUDA support (recommended)
- **RAM**: 8GB+ (16GB recommended)
- **Storage**: 2GB free space
- **Input**: Webcam or video files for testing

### ⚡ Installation

#### 1️⃣ Clone Repository
```bash
git clone https://github.com/didaco97/DivyaDrishti.git
cd DivyaDrishti
```

#### 2️⃣ Install Dependencies
```bash
# 🪟 Windows (Recommended)
install.bat

# 🐧 Linux/macOS
chmod +x install.sh
./install.sh

# 🐍 Manual Installation
python install_dependencies.py
pip install -r requirements.txt
```

#### 3️⃣ Verify Installation
```bash
python main.py --check
```

#### 4️⃣ Launch Application
```bash
python main.py
```

### 🎮 First Run
1. **Select Input Source**: Choose camera, video file, or stream
2. **Choose Model**: Select FootTrail Detection Model (default)
3. **Start Detection**: Click "🚀 START DETECTION"
4. **Monitor Results**: View real-time detections in the notification panel

## 🔧 Configuration & Customization

### ⚙️ System Configuration
Edit `config.py` to customize:
```python
# Detection Settings
CONFIDENCE_THRESHOLD = 0.5      # Detection confidence
DEFAULT_MODEL_KEY = "foottrail" # Default model selection
ENABLE_GPU = True               # GPU acceleration

# GUI Settings
CYBERPUNK_THEME = {             # Interface styling
    "primary_color": "#00ff41",
    "bg_color": "#0a0a0a"
}

# Performance Settings
MAX_FPS = 30                    # Maximum processing FPS
SKIP_FRAMES = 1                 # Frame processing interval
```

### 🎯 Adding Custom Models
1. Place model file in `Models/` directory
2. Update `AVAILABLE_MODELS` in `config.py`:
```python
"custom_model": {
    "name": "Custom Model Name",
    "path": "path/to/model.pt",
    "classes": ["class1", "class2"],
    "icon": "🎯"
}
```
3. Restart application

## 🎮 User Interface Guide

### 🎛️ Main Controls
- **🚀 START DETECTION**: Begin real-time AI detection
- **⏹️ STOP**: Stop detection process
- **📹 SOURCE**: Select input source (camera/video/stream)
- **🎯 MODEL**: Switch between available YOLO models
- **🤖 AI ANALYSIS**: Toggle segmentation mode
- **📸 SCREENSHOT**: Capture current frame
- **🗺️ TACTICAL MAP**: Open interactive map
- **🔄 RESTART**: Restart application

### 📊 Information Panels
- **🎯 Detection Notifications**: Simple one-line detection alerts
- **📈 Performance Monitor**: Real-time FPS and system metrics
- **🗺️ Drone Location**: GPS coordinates and sector information
- **⚙️ System Status**: Model info and device status

### 🎚️ Settings Panel
- **Confidence Threshold**: Adjust detection sensitivity
- **Auto-save Screenshots**: Toggle automatic capture
- **Performance Monitoring**: Enable/disable metrics tracking

## 🚨 Troubleshooting

### ❌ Common Issues

#### Model Not Found
```
✗ FootTrail model not found
```
**Solution**: Ensure model is at: `FootTrail Detection Model/hiking_trail_dataset/pretrained_model/foottrail.pt`

#### GPU Not Available
```
⚠️ GPU not available, using CPU
```
**Solutions**:
1. Install NVIDIA CUDA Toolkit 12.1+
2. Reinstall PyTorch with CUDA: `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121`
3. Update GPU drivers

#### Dependencies Missing
```
✗ Missing dependencies: torch, ultralytics
```
**Solution**: Run installation script or `pip install -r requirements.txt`

### 🐛 Performance Issues
- **Low FPS**: Enable GPU acceleration or reduce confidence threshold
- **High Memory Usage**: Restart application or close other programs
- **Detection Lag**: Reduce video resolution or increase frame skip

### 🔍 Debug Mode
```bash
python main.py --debug    # Enable debug logging
python main.py --version  # Show version info
python main.py --check    # System diagnostics
```

## 📊 Performance Benchmarks

### 🖥️ Tested Hardware
| Component | Specification |
|-----------|---------------|
| **GPU** | NVIDIA GeForce GTX 1650 |
| **CPU** | Intel i7-10750H |
| **RAM** | 16GB DDR4 |
| **CUDA** | 12.1 |

### ⚡ Performance Metrics
| Metric | GPU Performance | CPU Performance |
|--------|----------------|-----------------|
| **Detection FPS** | 25-30 FPS | 8-12 FPS |
| **Model Loading** | 3-5 seconds | 5-8 seconds |
| **Memory Usage** | 2-4GB | 1-2GB |
| **Inference Time** | 33-40ms | 80-125ms |

## 🤝 Contributing

We welcome contributions to DivyaDrishti! Here's how you can help:

### 🔧 Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Add tests if applicable
5. Commit changes: `git commit -m 'Add amazing feature'`
6. Push to branch: `git push origin feature/amazing-feature`
7. Submit a Pull Request

### 📝 Contribution Guidelines
- Follow Python PEP 8 style guidelines
- Add docstrings to new functions
- Update documentation for new features
- Test on both GPU and CPU environments

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Development Team

**DivyaDrishti** is developed and maintained by:

### 🎯 Lead Developer
**Dhiraj Dahale** - *Project Lead & AI Engineer*
- 🔗 GitHub: [@didaco97](https://github.com/didaco97)
- 📧 Email: dhirajdahale96@gmail.com
- 💼 LinkedIn: [Dhiraj Dahale]([https://linkedin.com/in/dhiraj-dahale](https://www.linkedin.com/in/dhiraj-dahale-028b6229b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app))

### 🤝 Development Team
- **AI/ML Engineering**: Custom model training and optimization
- **Computer Vision**: Real-time detection and tracking systems
- **GUI Development**: Cyberpunk-themed interface design
- **Performance Optimization**: GPU acceleration and system optimization

### 🙏 Acknowledgments
- **Ultralytics Team** for the excellent YOLO framework
- **PyTorch Community** for the robust deep learning platform
- **OpenCV Contributors** for computer vision capabilities
- **Open Source Community** for inspiration and support

## 🆘 Support & Contact

### 📞 Getting Help
1. **Documentation**: Check this README and system docs
2. **Issues**: Create a GitHub issue for bugs or feature requests
3. **Discussions**: Use GitHub Discussions for questions
4. **Email**: Contact the development team directly

### 🔗 Links
- **Repository**: [https://github.com/didaco97/DivyaDrishti](https://github.com/didaco97/DivyaDrishti)
- **Documentation**: [Wiki](https://github.com/didaco97/DivyaDrishti/wiki)
- **Issues**: [Bug Reports](https://github.com/didaco97/DivyaDrishti/issues)
- **Releases**: [Latest Releases](https://github.com/didaco97/DivyaDrishti/releases)

### 📊 System Information
```bash
# Get detailed system info
python main.py --version
python main.py --check
python main.py --debug
```

---

<div align="center">

**🎯 DivyaDrishti v1.0.0** - *AI-Powered Drone Surveillance System*

*Developed with ❤️ by Dhiraj Dahale and Team*

[![GitHub Stars](https://img.shields.io/github/stars/didaco97/DivyaDrishti?style=social)](https://github.com/didaco97/DivyaDrishti/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/didaco97/DivyaDrishti?style=social)](https://github.com/didaco97/DivyaDrishti/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/didaco97/DivyaDrishti)](https://github.com/didaco97/DivyaDrishti/issues)

</div>
