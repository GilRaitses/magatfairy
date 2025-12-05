#!/usr/bin/env python3
"""
Installation script for mat2h5
Installs required Python packages for MATLAB to H5 conversion.
"""

import subprocess
import sys
from pathlib import Path

def check_python_version():
    """Check if Python version is 3.8+"""
    if sys.version_info < (3, 8):
        print("ERROR: Python 3.8 or higher is required.")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

def check_git():
    """Check if git is installed"""
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ Git installed: {result.stdout.strip()}")
            return True
    except FileNotFoundError:
        pass
    print("⚠ Git not found (optional, needed for cloning MAGAT codebase)")
    return False

def install_requirements():
    """Install Python packages from requirements.txt"""
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    if not requirements_file.exists():
        print(f"ERROR: requirements.txt not found at {requirements_file}")
        sys.exit(1)
    
    print("\nInstalling Python packages...")
    print("-" * 60)
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "--upgrade", "pip"
        ])
        
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
        ])
        
        print("-" * 60)
        print("✓ All packages installed successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"\nERROR: Failed to install packages. Exit code: {e.returncode}")
        print("\nYou may need to install MATLAB Engine for Python separately:")
        print("  https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html")
        return False

def main():
    print("=" * 60)
    print("mat2h5 Installation")
    print("=" * 60)
    print()
    
    # Check Python version
    check_python_version()
    
    # Check git (optional)
    git_available = check_git()
    
    # Install requirements
    success = install_requirements()
    
    print()
    print("=" * 60)
    if success:
        print("Installation complete!")
        print()
        print("Next steps:")
        print("  1. Ensure MATLAB is installed and MATLAB Engine for Python is set up")
        print("  2. Run: python mat2h5.py")
    else:
        print("Installation encountered errors. Please check the output above.")
    print("=" * 60)

if __name__ == "__main__":
    main()

