# Gemini Chat 🌟

A command-line tool to interact with Google's Gemini API directly from your terminal. This tool provides a colorful, neatly formatted chat interface that works on both Windows CMD and Linux Bash. 🚀

## Features ✨

- Simple chat interface with Google's Gemini API. 💬
- Colorful output for better readability (using colorama). 🌈
- Cross-platform: Works on Windows and Linux. 🖥️🐧
- Graceful handling of interrupts (Ctrl+C) and errors. 🛡️
- Easy setup as a standalone CLI command (`gemini_chat`). ⚙️

## Prerequisites ✅

Before setting up, ensure you have:

- **Python 3.6+**: Installed and added to your PATH. 🐍
- **Google API Key**: Obtain one from Google to use the Gemini API. 🔑
- **A terminal**: CMD on Windows, Bash on Linux. 💻

## Required Packages 📦

Install these Python packages:

- **google-generativeai**: For interacting with the Gemini API. 🤖
- **colorama**: For colored output in the terminal. 🎨

Install them with:

```bash
pip install google-generativeai colorama
```

## Installation and Setup 🛠️
 
### On Linux (Bash) 🐧

**Clone the Repository:**

```bash
git clone https://github.com/Durgareddyp/gemini_chat.git
cd gemini_chat
```

**Make the Script Executable:**

```bash
chmod +x gemini_chat.py
```

**Set Environment Variables:**

Set your Google API key:

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

Optionally set the Gemini model (defaults to `gemini-2.0-flash`):

```bash
export GEMINI_MODEL="your-preferred-model"
```

To make these persistent, add them to `~/.bashrc` or `~/.zshrc` and run `source ~/.bashrc`.

**(Optional) Add to PATH:**

Move the script to a directory in your PATH:

```bash
sudo mv gemini_chat.py /usr/local/bin/gemini_chat
```

Now you can run `gemini_chat` from anywhere.

**Run the Tool:**

```bash
gemini_chat
```

Alternatively, if not in PATH:

```bash
python3 gemini_chat.py
```

### On Windows (CMD) 🖥️

**Clone the Repository:**

Download the ZIP from GitHub or use Git:

```cmd
git clone https://github.com/Durgareddyp/gemini_chat.git
cd gemini_chat
```

**Set Environment Variables:**

Set your Google API key:

```cmd
set GOOGLE_API_KEY=your-api-key-here
```

Optionally set the Gemini model:

```cmd
set GEMINI_MODEL=your-preferred-model
```

For persistence:

- Open "Environment Variables" (search in Windows). 🔍
- Add `GOOGLE_API_KEY` under "User Variables". ✏️
- Optionally add `GEMINI_MODEL`.

**Create a Batch File:**

In the same directory as `gemini_chat.py`, create `gemini_chat.bat` with:

```bat
@echo off
python "%~dp0gemini_chat.py" %*
```

**(Optional) Add to PATH:**

Move both `gemini_chat.py` and `gemini_chat.bat` to a directory (e.g., `C:\Users\YourUsername\Scripts`).

Add that directory to your PATH:

- Open "Environment Variables" (search in Windows). 🔧
- Edit "Path" under "User Variables" and add the directory.
- Restart CMD. 🔄

**Run the Tool:**

If in PATH:

```cmd
gemini_chat
```

Otherwise:

```cmd
python gemini_chat.py
```

## Usage 🎯

Run the tool:

- Linux: `gemini_chat`
- Windows: `gemini_chat` (after setup)

**Start chatting:**

Type your message and press Enter. ✍️

To exit, type `exit`, `quit`, or `bye`. 👋

Use `Ctrl+C` to interrupt gracefully.


## Example Output 📺

---

```plaintext
===========================================  
     Welcome to Gemini Chat!      
 (Type 'exit', 'quit', or 'bye' to end)  
===========================================  
You: hey  
-------------------------------------------  
**Gemini**: Hi there! How can I help you today?  
-------------------------------------------  
You: bye  
-------------------------------------------  
**Gemini**: Goodbye!  
-------------------------------------------
```

## Code Details 💻

**File:** `gemini_chat.py`

**Dependencies:**
- google.generativeai: For Gemini API access. 🤖
- colorama: For cross-platform colored output. 🌈

**Features:**
- Color-coded prompts and responses. 🎨
- Error handling for API issues and user interrupts. 🛠️
- Neat formatting with separators. 📏

## Troubleshooting 🐞

"Module not found" Error:  
> Ensure google-generativeai and colorama are installed. 📦

"API Key not set" Error: 

> Set GOOGLE_API_KEY in your environment variables. 🔑

Model Error:  
> Verify the model name (e.g., gemini-2.0-flash) is valid per Google's API docs. 📋

Colors Not Showing:  
> On Linux, ensure your terminal supports ANSI colors (most do). ✅

> On Windows, colorama should handle this; reinstall it if needed. 🔄

## Contributing 🤝

Feel free to fork this repository, submit issues, or send pull requests with improvements! 🌟

## License 📜

This project is open-source under the MIT [LICENSE](https://github.com/Durgareddyp/gemini_chat/blob/main/LICENSE)

## Author ✍️

Created by **Durga Reddy** 👨‍💻
