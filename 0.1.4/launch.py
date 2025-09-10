#!/usr/bin/env python3
"""
Devyan v0.1.4 Launch Script
System checker and dependency installer

This script checks your system for the required dependencies
and launches the Devyan application.
"""

import subprocess
import sys
import os
import importlib.util

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"   Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} - OK")
    return True

def check_package(package_name, import_name=None):
    """Check if a package is installed"""
    if import_name is None:
        import_name = package_name
    
    spec = importlib.util.find_spec(import_name)
    if spec is None:
        return False
    return True

def install_requirements():
    """Install requirements from requirements.txt"""
    if os.path.exists("requirements.txt"):
        print("📦 Installing dependencies...")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
            ])
            print("✅ Dependencies installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies")
            return False
    else:
        print("⚠️ requirements.txt not found")
        return False

def check_ollama():
    """Check if Ollama is running"""
    try:
        import requests
        response = requests.get("http://localhost:11434/api/version", timeout=5)
        if response.status_code == 200:
            print("✅ Ollama server - OK")
            return True
        else:
            print("⚠️ Ollama server responded with error")
            return False
    except Exception:
        print("⚠️ Ollama server not accessible at localhost:11434")
        print("   Note: Devyan will still run but may have limited functionality")
        return False

def check_tkinter():
    """Check if tkinter is available"""
    try:
        import tkinter
        print("✅ Tkinter - OK")
        return True
    except ImportError:
        print("❌ Tkinter not available")
        print("   Install with: sudo apt-get install python3-tk (Linux)")
        print("   Or: brew install python-tk (macOS)")
        return False

def main():
    """Main launch function"""
    print("🚀 Devyan v0.1.4 System Check")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check tkinter
    if not check_tkinter():
        sys.exit(1)
    
    # Check and install dependencies
    print("\n📋 Checking dependencies...")
    
    missing_packages = []
    required_packages = [
        ("crewai", "crewai"),
        ("python-dotenv", "dotenv"),
        ("requests", "requests")
    ]
    
    for package_name, import_name in required_packages:
        if check_package(package_name, import_name):
            print(f"✅ {package_name} - OK")
        else:
            print(f"❌ {package_name} - Missing")
            missing_packages.append(package_name)
    
    if missing_packages:
        print(f"\n📦 Installing missing packages: {', '.join(missing_packages)}")
        if not install_requirements():
            print("\n❌ Failed to install dependencies. Please run:")
            print("   pip install -r requirements.txt")
            sys.exit(1)
    
    # Check Ollama (optional)
    print("\n🔍 Checking optional services...")
    check_ollama()
    
    # Create projects directory if it doesn't exist
    if not os.path.exists("projects"):
        os.makedirs("projects")
        print("✅ Created projects directory")
    
    print("\n" + "=" * 40)
    print("🎉 System check complete!")
    print("🚀 Launching Devyan...")
    print("=" * 40)
    
    # Launch the main application
    try:
        import devyan_main
        devyan_main.main()
    except ImportError as e:
        print(f"❌ Failed to import devyan_main: {e}")
        print("   Make sure devyan_main.py is in the current directory")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error launching Devyan: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
