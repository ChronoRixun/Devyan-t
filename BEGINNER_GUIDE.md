# 🚀 New to AI, Python, Ollama, or Github? Start Here!

*A complete beginner's guide to getting Devyan(t) running on your computer*

---

## 🤔 What is Devyan(t)?

Devyan(t) is an AI-powered coding assistant that can help you create complete software projects. Think of it as having a team of AI programmers that can:

- **Create full applications** (like calculators, games, websites)
- **Write all the code files** you need for a project
- **Generate documentation** and tests
- **Work completely offline** (no internet required after setup)

**The best part?** It runs entirely on your computer - no cloud services, no monthly fees, no data leaving your machine!

---

## 📋 What You'll Need

- **A Windows, Mac, or Linux computer**
- **At least 8GB of RAM** (16GB recommended)
- **About 30 minutes** for the full setup
- **Basic comfort with downloading and installing software**

---

## 🛠️ Step-by-Step Installation

### Step 1: Install Python 🐍

Python is the programming language that runs Devyan(t).

#### **Windows Users:**
1. Go to [python.org/downloads](https://python.org/downloads)
2. Click the big yellow "Download Python" button
3. Run the downloaded file
4. **IMPORTANT:** Check the box "Add Python to PATH" before clicking Install
5. Click "Install Now"

#### **Mac Users:**
1. Go to [python.org/downloads](https://python.org/downloads)
2. Download the macOS installer
3. Run the .pkg file and follow the installer

#### **Linux Users:**
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install python3 python3-pip

# Red Hat/CentOS/Fedora
sudo dnf install python3 python3-pip
```

#### **Verify Python Installation:**
1. Open your terminal/command prompt
2. Type: `python --version` (or `python3 --version` on Mac/Linux)
3. You should see something like "Python 3.11.x"

---

### Step 2: Install Ollama 🦙

Ollama runs the AI models locally on your computer.

#### **Windows:**
1. Go to [ollama.ai](https://ollama.ai)
2. Click "Download for Windows"
3. Run the installer
4. Restart your computer after installation

#### **Mac:**
1. Go to [ollama.ai](https://ollama.ai)
2. Click "Download for macOS"
3. Drag Ollama to your Applications folder
4. Run Ollama from Applications

#### **Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

#### **Verify Ollama Installation:**
1. Open terminal/command prompt
2. Type: `ollama --version`
3. You should see the Ollama version number

---

### Step 3: Download AI Models 🧠

These are the "brains" that power Devyan(t). We'll download some efficient models that work well on most computers.

**Open your terminal/command prompt and run these commands one by one:**

```bash
# Primary model (fastest, most efficient)
ollama pull llama3.2:3b

# Backup models (in case the first doesn't work)
ollama pull phi3.5:3.8b
ollama pull qwen2.5-coder:3b
```

**This will take some time** (10-30 minutes depending on your internet speed). Each model is several GB in size.

#### **Test Your Models:**
```bash
ollama run llama3.2:3b "Hello, can you help me code?"
```
You should get a friendly AI response. Type `/bye` to exit.

---

### Step 4: Get Devyan(t) 📁

#### **Option A: Download ZIP (Easiest)**
1. Go to the [Devyan(t) repository](https://github.com/ChronoRixun/Devyan)
2. Click the green "Code" button
3. Click "Download ZIP"
4. Extract the ZIP file to a folder like `C:\Devyan` or `~/Devyan`

#### **Option B: Use Git (If you have it)**
```bash
git clone https://github.com/ChronoRixun/Devyan.git
cd Devyan
```

---

### Step 5: Install Devyan(t) Dependencies 📦

Navigate to the Devyan(t) folder and install the required Python packages.

#### **Windows:**
1. Open Command Prompt
2. Navigate to your Devyan folder: `cd C:\path\to\Devyan`
3. Run: `python -m pip install -r requirements.txt`

#### **Mac/Linux:**
1. Open Terminal
2. Navigate to your Devyan folder: `cd /path/to/Devyan`
3. Run: `python3 -m pip install -r requirements.txt`

---

### Step 6: Launch Devyan(t) 🚀

#### **Easy Launch (Recommended):**

**Windows:**
- Double-click `launch.bat` in the Devyan folder

**Mac/Linux:**
```bash
python3 launch.py
```

#### **Manual Launch:**
```bash
python devyan_main.py
# or on Mac/Linux:
python3 devyan_main.py
```

---

## 🎉 You're Ready to Go!

If everything worked, you should see the Devyan(t) GUI with:
- A modern dark interface
- Demo projects you can try
- Options to create custom projects

### **Try Your First Project:**
1. Click on "Calculator GUI" in the Beginner section
2. Click "Generate Project"
3. Watch as Devyan(t) creates a complete calculator application!
4. Your files will be saved in the `projects/` folder

---

## 🔧 Troubleshooting

### **"Python is not recognized"**
- **Windows:** Reinstall Python and make sure to check "Add Python to PATH"
- **Mac/Linux:** Try using `python3` instead of `python`

### **"Ollama is not recognized"**
- Make sure Ollama is installed and running
- Try restarting your computer
- Check that Ollama is in your PATH

### **Models download slowly or fail**
- Check your internet connection
- Try downloading one model at a time
- Use a wired connection if possible

### **"Permission denied" errors**
- **Windows:** Run Command Prompt as Administrator
- **Mac/Linux:** You might need to use `sudo` for some commands

### **Devyan(t) won't start**
- Make sure all dependencies installed: `pip install -r requirements.txt`
- Check that at least one Ollama model is downloaded: `ollama list`
- Try running from the correct directory

### **GUI doesn't appear**
- Make sure you're running `devyan_main.py` (not an older version)
- Check that tkinter is installed: `python -c "import tkinter"`
- Try the manual launch method

---

## 🆘 Still Need Help?

### **Quick Diagnostic:**
Run this command to check your setup:
```bash
python launch.py --check
```

### **Common Questions:**

**Q: How much disk space do I need?**
A: About 10-15GB total (Python + Ollama + Models + Devyan(t))

**Q: Will this slow down my computer?**
A: Only when actively generating projects. Models run efficiently on modern computers.

**Q: Can I use this without internet?**
A: Yes! Once everything is installed, Devyan(t) works completely offline.

**Q: What if I want to uninstall everything?**
A: Uninstall Python and Ollama through your system's normal uninstall process, then delete the Devyan folder.

**Q: Is this safe?**
A: Yes! Everything runs locally on your computer. No data is sent to external servers.

### **Get Support:**
- Check the main [README.md](README.md) for technical details
- Look at the [issues page](https://github.com/ChronoRixun/Devyan/issues) on GitHub
- The Devyan(t) community is friendly and helpful!

---

## 🎯 What's Next?

Once you have Devyan(t) running:

1. **Try the demo projects** to see what's possible
2. **Experiment with custom prompts** like "Create a simple game" or "Build a todo list app"
3. **Explore the generated code** to learn how the AI builds applications
4. **Share your creations** with friends and the community!

---

## 🎁 Pro Tips for Beginners

- **Start with demo projects** before trying custom ones
- **Don't worry about understanding all the code** - Devyan(t) creates working applications
- **Generated projects include README files** that explain how to use them
- **Each project is complete** - you can run them immediately
- **Experiment freely** - you can't break anything!

---

**Welcome to the world of AI-assisted programming! 🤖✨**

*You're about to discover how fun and accessible software development can be with AI assistance.*
