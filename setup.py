import subprocess
import sys
import os

def install_requirements():
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Successfully installed required packages!")
    except subprocess.CalledProcessError:
        print("Error installing packages. Please try manually: pip install -r requirements.txt")

def setup_system_dependencies():
    if sys.platform.startswith('linux'):
        try:
            # For Fedora
            if os.path.exists('/etc/fedora-release'):
                subprocess.check_call(["sudo", "dnf", "install", "-y", "python3-tk", "python3-pillow"])
            # For Ubuntu/Debian
            elif os.path.exists('/etc/debian_version'):
                subprocess.check_call(["sudo", "apt-get", "install", "-y", "python3-tk", "python3-pil", "python3-pil.imagetk"])
        except subprocess.CalledProcessError:
            print("Error installing system dependencies. Please install them manually.")
    
    # Windows typically comes with required dependencies
    # macOS users should install python-tk via brew

if __name__ == "__main__":
    setup_system_dependencies()
    install_requirements() 