#!/usr/bin/env python3
"""
DivyaDrishti Dependency Installer
Automated installation of required dependencies
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description=""):
    """Run a command and return success status"""
    print(f"🔄 {description}")
    print(f"   Command: {command}")

    try:
        result = subprocess.run(command, shell=True, check=True,
                              capture_output=True, text=True)
        print(f"✓ {description} - Success")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} - Failed")
        print(f"   Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    print(f"🐍 Python version: {version.major}.{version.minor}.{version.micro}")

    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ is required!")
        return False

    print("✓ Python version is compatible")
    return True

def check_pip():
    """Check if pip is available and upgrade it"""
    print("\n📦 Checking pip...")

    try:
        import pip
        print(f"✓ pip is available")
    except ImportError:
        print("❌ pip is not available!")
        return False

    # Upgrade pip
    success = run_command(
        f"{sys.executable} -m pip install --upgrade pip",
        "Upgrading pip"
    )

    return success

def install_pytorch():
    """Install PyTorch with CUDA support"""
    print("\n🔥 Installing PyTorch with CUDA support...")

    # Check if CUDA is available
    try:
        result = subprocess.run("nvidia-smi", shell=True, capture_output=True)
        cuda_available = result.returncode == 0
    except:
        cuda_available = False

    if cuda_available:
        print("✓ NVIDIA GPU detected, installing PyTorch with CUDA")
        command = f"{sys.executable} -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121"
    else:
        print("⚠️ No NVIDIA GPU detected, installing CPU-only PyTorch")
        command = f"{sys.executable} -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu"

    return run_command(command, "Installing PyTorch")

def install_requirements():
    """Install requirements from requirements.txt"""
    print("\n📋 Installing requirements from requirements.txt...")

    requirements_file = Path(__file__).parent / "requirements.txt"

    if not requirements_file.exists():
        print(f"❌ requirements.txt not found at {requirements_file}")
        return False

    command = f"{sys.executable} -m pip install -r {requirements_file}"
    return run_command(command, "Installing requirements")

def verify_installation():
    """Verify that all packages are installed correctly"""
    print("\n🔍 Verifying installation...")

    packages_to_check = [
        ("torch", "PyTorch"),
        ("torchvision", "TorchVision"),
        ("ultralytics", "Ultralytics YOLO"),
        ("cv2", "OpenCV"),
        ("PIL", "Pillow"),
        ("numpy", "NumPy"),
        ("pandas", "Pandas"),
        ("psutil", "psutil"),
        ("yaml", "PyYAML")
    ]

    all_good = True

    for package, name in packages_to_check:
        try:
            if package == "cv2":
                import cv2
                version = cv2.__version__
            elif package == "PIL":
                import PIL
                version = PIL.__version__
            elif package == "yaml":
                import yaml
                version = getattr(yaml, '__version__', 'unknown')
            else:
                module = __import__(package)
                version = getattr(module, '__version__', 'unknown')

            print(f"✓ {name} {version}")
        except ImportError:
            print(f"✗ {name} - Not installed")
            all_good = False

    return all_good

def test_gpu_support():
    """Test GPU support"""
    print("\n🖥️ Testing GPU support...")

    try:
        import torch

        if torch.cuda.is_available():
            device_count = torch.cuda.device_count()
            device_name = torch.cuda.get_device_name(0)
            cuda_version = torch.version.cuda

            print(f"✓ CUDA available: {cuda_version}")
            print(f"✓ GPU devices: {device_count}")
            print(f"✓ Primary GPU: {device_name}")

            # Test tensor operations
            x = torch.randn(3, 3).cuda()
            y = torch.randn(3, 3).cuda()
            z = torch.matmul(x, y)

            print("✓ GPU tensor operations working")
            return True
        else:
            print("⚠️ CUDA not available, will use CPU")
            return True

    except Exception as e:
        print(f"❌ GPU test failed: {e}")
        return False

def main():
    """Main installation process"""
    print("=" * 60)
    print("🎯 DivyaDrishti Dependency Installer")
    print("🥾 Hiking Trail Detection System")
    print("=" * 60)

    # Check Python version
    if not check_python_version():
        return False

    # Check and upgrade pip
    if not check_pip():
        return False

    # Install PyTorch
    if not install_pytorch():
        print("❌ PyTorch installation failed!")
        return False

    # Install other requirements
    if not install_requirements():
        print("❌ Requirements installation failed!")
        return False

    # Verify installation
    if not verify_installation():
        print("❌ Installation verification failed!")
        return False

    # Test GPU support
    test_gpu_support()

    print("\n" + "=" * 60)
    print("✅ Installation completed successfully!")
    print("\nNext steps:")
    print("1. Ensure the hiking trail model is available")
    print("2. Run: python main.py")
    print("=" * 60)

    return True

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n❌ Installation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Installation error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
