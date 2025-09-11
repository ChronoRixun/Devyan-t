# 🚀 Complete Beginners Guide to Devyan(t)

*A comprehensive walkthrough for getting Devyan(t) running on your computer - designed for complete beginners*

---

## 🎯 What is Devyan(t)?

Devyan(t) is an AI-powered coding assistant that creates complete software applications for you. Think of it as having an entire team of AI programmers that can:

- **Create full applications** (calculators, games, websites, utilities)
- **Write all the code files** needed for a complete project
- **Generate documentation** and comprehensive tests
- **Work completely offline** after initial setup (privacy-focused)

**The Revolutionary Difference:** Unlike other AI coding tools that often fail or produce broken code, Devyan(t) **guarantees working applications every time** using its psychology-independent architecture.

---

## 📋 System Requirements

### **Minimum Requirements:**
- **Computer:** Windows 10/11, macOS 10.15+, or modern Linux
- **RAM:** 8GB minimum (16GB strongly recommended)
- **Storage:** 15GB free space for complete setup
- **Internet:** Required for initial download and setup only
- **Time:** About 45-60 minutes for complete setup

### **Critical Version Requirements:**
- **Python 3.10 or newer** - Python 3.8/3.9 will cause complete installation failure
- **CrewAI 0.150.0 exactly** - Newer versions break core functionality
- **Build tools** - Required for compiling dependencies

---

## 🔍 Pre-Installation System Check

Before we start, let's check if you already have some components:

### **Check if Python is Installed:**
1. Open your terminal/command prompt:
   - **Windows:** Press `Win + R`, type `cmd`, press Enter
   - **macOS:** Press `Cmd + Space`, type `terminal`, press Enter  
   - **Linux:** Press `Ctrl + Alt + T`

2. Type: `python --version` (or try `python3 --version`)

3. **If you see "Python 3.10.x" or higher:** ✅ Python is ready
   **If you see "Python 3.8" or "Python 3.9":** ❌ Must upgrade
   **If you get "command not found":** ❌ Need to install Python

### **Check if Ollama is Installed:**
1. In the same terminal, type: `ollama --version`
2. **If you see a version number:** ✅ Ollama is ready
   **If you get "command not found":** ❌ Need to install Ollama

---

## 🛠️ Step 1: Install Python 3.10+ (CRITICAL)

**⚠️ CRITICAL WARNING:** Python 3.8 and 3.9 will cause complete installation failure. You MUST have Python 3.10 or newer.

### **Windows Installation:**

1. **Download Python:**
   - Go to [python.org/downloads](https://python.org/downloads)
   - Click the large yellow "Download Python 3.x.x" button
   - Make sure it shows version 3.10 or higher

2. **Install Python:**
   - Run the downloaded installer
   - **🚨 CRITICAL:** Check "Add Python to PATH" at the bottom
   - **🚨 CRITICAL:** Check "Install for all users" (if available)
   - Click "Install Now"
   - Wait for installation to complete
   - Click "Close"

3. **Verify Installation:**
   - Open a NEW command prompt (important: must be new)
   - Type: `python --version`
   - Should show Python 3.10.x or higher

### **macOS Installation:**

1. **Download Python:**
   - Go to [python.org/downloads](https://python.org/downloads)
   - Click "Download Python 3.x.x" for macOS
   - Ensure version is 3.10 or higher

2. **Install Python:**
   - Open the downloaded .pkg file
   - Follow the installation wizard
   - Enter your password when prompted
   - Complete the installation

3. **Verify Installation:**
   - Open Terminal
   - Type: `python3 --version`
   - Should show Python 3.10.x or higher

### **Linux Installation:**

```bash
# Ubuntu/Debian (most common)
sudo apt update
sudo apt install python3.10 python3.10-pip python3.10-venv

# Fedora/Red Hat
sudo dnf install python3.10 python3.10-pip

# Verify installation
python3.10 --version
```

---

## 🔨 Step 2: Install Build Tools (CRITICAL for Windows)

These tools are required to compile certain Python packages. **Skipping this step will cause installation failures.**

### **Windows: Visual Studio Build Tools**

1. **Download Build Tools:**
   - Go to: https://visualstudio.microsoft.com/visual-cpp-build-tools/
   - Click "Download Build Tools"
   - Run the downloaded installer

2. **Install Correct Components:**
   - In the installer, select "C++ build tools" workload
   - Ensure these are checked:
     - C++ core features
     - CMake tools for C++
     - Windows 10/11 SDK (latest version)
   - Click "Install"
   - **This will take 15-30 minutes and requires several GB**

3. **Restart Your Computer** after installation completes

### **macOS: Xcode Command Line Tools**

```bash
# Install command line tools
xcode-select --install

# Follow the prompts in the dialog that appears
# This may take 10-20 minutes
```

### **Linux: Build Essentials**

```bash
# Ubuntu/Debian
sudo apt install build-essential python3.10-dev

# Fedora/Red Hat  
sudo dnf groupinstall "Development Tools"
sudo dnf install python3.10-devel
```

---

## 🦙 Step 3: Install Ollama (AI Model Runner)

Ollama runs the AI models locally on your computer for privacy and speed.

### **Windows:**
1. Go to [ollama.ai](https://ollama.ai)
2. Click "Download for Windows"
3. Run the installer (OllamaSetup.exe)
4. Follow the installation wizard
5. **Restart your computer** after installation

### **macOS:**
1. Go to [ollama.ai](https://ollama.ai)  
2. Click "Download for macOS"
3. Open the downloaded .zip file
4. Drag Ollama to your Applications folder
5. Launch Ollama from Applications
6. Grant any security permissions requested

### **Linux:**
```bash
# Official installation script
curl -fsSL https://ollama.ai/install.sh | sh

# Start the Ollama service
sudo systemctl start ollama
sudo systemctl enable ollama
```

### **Verify Ollama Installation:**
1. Open a new terminal/command prompt
2. Type: `ollama --version`
3. You should see the Ollama version number
4. If not working, restart your computer and try again

---

## 🧠 Step 4: Download AI Models

These are the "brains" that power Devyan(t). We'll download efficient models that work well on most computers.

**⏱️ Time Warning:** This step takes 20-45 minutes depending on your internet speed. Each model is 3-7GB.

### **Essential Models:**

**Open your terminal/command prompt and run these commands:**

```bash
# Primary architecture model (4GB) - REQUIRED
ollama pull llama3.1:8b

# Primary coding model (3.8GB) - REQUIRED  
ollama pull codellama:7b

# Fast backup models (2-3GB each) - RECOMMENDED
ollama pull phi3.5:3.8b
ollama pull qwen2.5-coder:3b
```

### **Test Your Models:**
```bash
# Test the primary model
ollama run llama3.1:8b "Hello, can you help me with coding?"

# You should get a friendly AI response
# Type /bye to exit the chat
```

**If the test works, your AI models are ready!** ✅

---

## 📁 Step 5: Get Devyan(t)

### **Option A: Download ZIP (Easiest for Beginners)**

1. **Go to the Devyan(t) repository:**
   - Visit: https://github.com/ChronoRixun/Devyan-t
   
2. **Download the code:**
   - Click the green "Code" button
   - Click "Download ZIP"
   - Save to a memorable location (like Desktop or Documents)

3. **Extract the files:**
   - Right-click the downloaded ZIP file
   - Choose "Extract All" (Windows) or double-click (macOS)
   - Extract to a folder like `C:\Devyant` or `~/Devyant`

### **Option B: Using Git (If You Have It)**

```bash
git clone https://github.com/ChronoRixun/Devyan-t.git
cd Devyan-t
```

---

## 📦 Step 6: Install Devyan(t) Dependencies

Now we'll install the Python packages that Devyan(t) needs to run.

### **Navigate to Devyan(t) Folder:**

**Windows:**
1. Open Command Prompt as Administrator (right-click cmd, "Run as administrator")
2. Navigate to your Devyan(t) folder:
   ```cmd
   cd C:\path\to\your\Devyan-t\folder
   # Example: cd C:\Users\YourName\Desktop\Devyan-t
   ```

**macOS/Linux:**
1. Open Terminal
2. Navigate to your Devyan(t) folder:
   ```bash
   cd /path/to/your/Devyan-t/folder
   # Example: cd ~/Desktop/Devyan-t
   ```

### **Install Dependencies:**

**All Platforms:**
```bash
# Navigate to the 0.1.4 directory (production version)
cd 0.1.4

# Install exact dependencies (CRITICAL: exact versions)
pip install crewai==0.150.0 python-dotenv>=1.0.0 requests>=2.28.0

# On some systems, you may need:
pip install --break-system-packages crewai==0.150.0 python-dotenv>=1.0.0 requests>=2.28.0
```

**⚠️ CRITICAL:** If you get dependency errors:
- **Windows:** Run Command Prompt as Administrator
- **macOS/Linux:** Try using `pip3` instead of `pip`  
- **All platforms:** Add `--break-system-packages` flag if needed

### **Verify Installation:**
```bash
# Test if CrewAI installed correctly
python -c "import crewai; print('CrewAI version:', crewai.__version__)"

# Should show: CrewAI version: 0.150.0
```

---

## 🚀 Step 7: Launch Devyan(t)

You're almost there! Let's start Devyan(t).

### **Method 1: Easy Launch (Recommended)**

**Windows:**
```cmd
# From the 0.1.4 directory
python launch.py
```

**macOS/Linux:**
```bash
# From the 0.1.4 directory  
python3 launch.py
```

### **Method 2: Direct Launch**

```bash
# From the 0.1.4 directory
python devyan_main.py
# or on macOS/Linux:
python3 devyan_main.py
```

### **What Should Happen:**
1. Terminal will show startup messages
2. A modern dark GUI window will appear
3. You'll see demo projects and options
4. No error messages in the terminal

**If the GUI appears: 🎉 SUCCESS! You're ready to use Devyan(t)!**

---

## 🎮 Your First Project

Let's create your first AI-generated application:

### **Try a Demo Project:**

1. **In the Devyan(t) GUI, click "Calculator GUI"** (in Beginner section)
2. **Click "Generate Project"**
3. **Watch the magic happen:**
   - Progress updates will show in the interface
   - AI agents will design, code, and test your application
   - Usually takes 1-3 minutes

4. **Find your project:**
   - Generated files will be in the `projects/` folder
   - Look for a folder with timestamp like `calculator_20241112_143022/`

5. **Run your new calculator:**
   ```bash
   cd projects/calculator_[timestamp]
   python main.py
   ```

**You just created a complete calculator application with AI!** 🎊

---

## 🔧 Troubleshooting Guide

### **Installation Issues:**

#### **"Python is not recognized"**
- **Cause:** Python not in system PATH
- **Windows Solution:** 
  1. Reinstall Python, checking "Add Python to PATH"
  2. Or manually add Python to PATH in System Properties
- **macOS/Linux Solution:** Use `python3` instead of `python`

#### **"Could not find a version that satisfies the requirement crewai"**
- **Cause:** Python version too old (3.8/3.9)
- **Solution:** Upgrade to Python 3.10+ (see Step 1)
- **Verify:** `python --version` should show 3.10+

#### **"Microsoft Visual C++ 14.0 is required"**
- **Cause:** Missing Windows build tools
- **Solution:** Complete Step 2 (Visual Studio Build Tools)
- **Critical:** Restart computer after installation

#### **"error: Microsoft Visual C++ 14.0 or greater is required"**
- **Cause:** Incomplete build tools installation
- **Solution:** 
  1. Uninstall any partial VS installations
  2. Reinstall Visual Studio Build Tools completely
  3. Select "C++ build tools" workload
  4. Restart computer

#### **"Permission denied" errors**
- **Windows:** Run Command Prompt as Administrator
- **macOS/Linux:** Use `sudo` for system installations
- **Alternative:** Use virtual environments (see Advanced Setup)

### **Runtime Issues:**

#### **"Ollama connection failed"**
- **Check Ollama is running:** `ollama serve` in separate terminal
- **Check models installed:** `ollama list`
- **Restart Ollama service** if needed

#### **"No module named tkinter"**
- **Most common on Linux:** `sudo apt install python3-tk`
- **macOS:** Reinstall Python from python.org (includes tkinter)
- **Windows:** Tkinter should be included, try reinstalling Python

#### **GUI doesn't appear**
- **Verify you're in 0.1.4 directory:** `pwd` (macOS/Linux) or `cd` (Windows)
- **Check tkinter works:** `python -c "import tkinter; print('OK')"`
- **Try manual launch:** `python devyan_main.py`

#### **"ImportError: cannot import name 'DirectoryReadTool'"**
- **Cause:** Wrong CrewAI version (probably 0.151+)
- **Solution:** `pip install crewai==0.150.0` (exact version required)
- **Verify:** `python -c "import crewai; print(crewai.__version__)"`

### **Model Issues:**

#### **Models download slowly**
- **Use wired internet connection** if possible
- **Download one model at a time** instead of all together
- **Check available disk space** (need 15GB+ free)

#### **"Model not found" errors**
- **List installed models:** `ollama list`
- **Re-download if missing:** `ollama pull model_name`
- **Check spelling** of model names exactly

### **Performance Issues:**

#### **Very slow generation (>10 minutes)**
- **Check system RAM usage** during generation
- **Close other applications** to free RAM
- **Consider using smaller models** on lower-end systems

#### **Out of memory errors**
- **Close other applications**
- **Use smaller models:** `ollama pull gemma2:2b`
- **Increase virtual memory/swap** if possible

---

## 🆘 Getting Help

### **Quick Self-Diagnosis:**

Run this comprehensive system check:
```bash
# From the 0.1.4 directory
python launch.py --check
```

This will test:
- Python version compatibility
- All required dependencies
- Ollama connection and models
- System resources

### **Community Support:**

- 🐛 **Bug Reports:** [GitHub Issues](https://github.com/ChronoRixun/Devyan-t/issues)
- 💬 **Questions:** [GitHub Discussions](https://github.com/ChronoRixun/Devyan-t/discussions)
- 📚 **Documentation:** [Main README](README.md)

### **Frequently Asked Questions:**

**Q: How much disk space do I need?**
A: About 15GB total (Python + Ollama + Models + Devyan(t))

**Q: Will this slow down my computer?**
A: Only when actively generating projects. Models run efficiently.

**Q: Can I use this without internet after setup?**
A: Yes! Devyan(t) works completely offline once installed.

**Q: Is my data private?**
A: Absolutely! Everything runs locally. No data sent to external servers.

**Q: Can I uninstall easily?**
A: Yes. Uninstall Python and Ollama normally, then delete the Devyan(t) folder.

**Q: What if I want to use different AI models?**
A: Devyan(t) supports many Ollama models. Edit the model configuration files.

---

## 🎯 What's Next?

Once you have Devyan(t) working:

### **Beginner Projects:**
1. **Try all demo projects** to see the range of possibilities
2. **Experiment with custom prompts** like:
   - "Create a simple password manager"
   - "Build a random quote generator"
   - "Make a unit converter app"

### **Understanding the Generated Code:**
- **Every project includes a README** explaining how it works
- **Code is well-commented** and beginner-friendly
- **Tests show you how each part works**

### **Customization:**
- **Modify generated projects** to learn programming
- **Combine features** from different projects
- **Share your creations** with the community

---

## 🎁 Pro Tips for Beginners

### **Getting the Best Results:**
- **Be specific in your requests:** "Create a calculator with history" vs "make a calculator"
- **Start simple, then add features:** Build basics first, enhance later
- **Use the demo projects as templates:** Modify existing projects

### **Learning Programming:**
- **Read the generated README files** - they explain everything
- **Look at the architecture.md files** to understand design
- **Run the tests** to see how code should behave
- **Don't worry about understanding everything** - focus on what the app does

### **Troubleshooting Mindset:**
- **Error messages are your friend** - they tell you exactly what's wrong
- **Google error messages** if you don't understand them
- **Ask the community** - we're here to help!

---

## 🎊 Welcome to AI-Assisted Development!

**Congratulations!** You've successfully installed the world's first psychology-independent AI development assistant. You're now equipped with a tool that can create complete, working applications from simple descriptions.

### **What Makes This Special:**
- **Guaranteed Working Code** - No broken projects, ever
- **Complete Applications** - Not just code snippets, but full programs
- **Local Privacy** - Your ideas stay on your computer
- **Beginner Friendly** - No programming experience required

### **Your Journey Starts Now:**
You're about to discover how accessible and fun software development can be with reliable AI assistance. Welcome to the future of programming! 🚀

---

**🔗 Quick Links:**
- **Main Repository:** https://github.com/ChronoRixun/Devyan-t
- **Report Issues:** https://github.com/ChronoRixun/Devyan-t/issues
- **Join Discussions:** https://github.com/ChronoRixun/Devyan-t/discussions

*Happy coding with your new AI development assistant!* ✨
