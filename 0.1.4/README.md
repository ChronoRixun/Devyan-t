# Devyan v0.1.4 - Production Release

AI-Powered Development Assistant with Psychology-Independent Architecture

## Features

- **🚀 Direct Execution System**: Psychology-independent content generation
- **🛡️ Output Validation**: Automatic syntax checking and error prevention
- **🎯 Demo Gallery**: 8 pre-built example projects across complexity levels
- **⚡ Custom Project Generation**: Build anything from natural language descriptions
- **🖥️ Professional GUI**: Modern dark-themed interface with real-time feedback
- **📊 Comprehensive Output**: Architecture, code, tests, and documentation for every project

## Quick Start

### Option 1: Automated Setup (Recommended)
```bash
python launch.py
```

### Option 2: Manual Setup
```bash
pip install -r requirements.txt
python devyan_main.py
```

## System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Dependencies**: Listed in `requirements.txt`
- **Optional**: Ollama with Llama3.1:8b model for enhanced functionality

## Architecture

Devyan uses a psychology-independent approach to AI development:

1. **Direct Content Generation**: No agent decision-making loops
2. **Output Sanitization**: Automatic removal of markdown artifacts
3. **Syntax Validation**: Real-time Python syntax checking
4. **Fallback Protection**: Tested fallback code for reliability
5. **Multi-Stage Validation**: Comprehensive quality assurance

## Demo Projects

- 📱 **Calculator GUI** (Beginner)
- 🌤️ **Weather App** (Intermediate) 
- 📝 **Todo List Manager** (Beginner)
- 🎮 **Simple Game** (Intermediate)
- 📊 **Data Visualizer** (Intermediate)
- 🔍 **File Organizer** (Beginner)
- 🌐 **Simple Web Server** (Advanced)
- 🔐 **Password Generator** (Beginner)

## Generated Project Structure

Each generated project includes:
```
project_name/
├── architecture.md    # System design document
├── main.py           # Main application code
├── test_main.py      # Unit tests
└── README.md         # Project documentation
```

## Key Improvements in v0.1.4

- **Enhanced Output Sanitization**: Removes markdown artifacts from LLM outputs
- **Real-time Syntax Validation**: Prevents syntax errors before file creation
- **Improved Error Handling**: Better feedback and recovery mechanisms
- **Professional UI Updates**: Refined interface with validation status indicators

## Troubleshooting

**Common Issues:**

- **Ollama not found**: Install Ollama and the Llama3.1:8b model for best results
- **Tkinter missing**: Install with `sudo apt-get install python3-tk` (Linux)
- **Import errors**: Run `pip install -r requirements.txt`

**Getting Help:**

1. Check the launch script output for specific error messages
2. Ensure all dependencies are installed correctly
3. Verify Python version is 3.8 or higher

## Project Output

Generated projects are saved in the `projects/` directory with timestamped names for easy organization.

## Credits

Built with CrewAI v0.150.0 and enhanced with Claude Sonnet 4's assistance for output validation and system architecture.

## License

MIT License - See LICENSE file for details
