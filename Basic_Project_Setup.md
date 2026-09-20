# New Python Project Setup Guide

> A brief description of what this project does and the problem it solves.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your macOS machine:
- **Visual Studio Code**
- **Git** (Usually installed automatically when you type `git` in the terminal for the first time)
- **Python 3** (Recommended to install via [Homebrew](https://brew.sh/): `brew install python`)

---

## 🚀 Local Setup in VS Code (macOS)

Follow these steps to set up and run the project using Visual Studio Code.

### 1. Clone & Open the Repository
Open your standard macOS Terminal and clone the repository. Then, use the `code` command to open the folder directly in Visual Studio Code:
```zsh
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name
code .
```
*(VS Code will now open. You can close your external macOS terminal and do everything else inside VS Code).*

### 2. Open the VS Code Integrated Terminal
In Visual Studio Code, open the integrated terminal by pressing:
- **`⌃` + `` ` ``** (Control + Backtick) 
- Alternatively, go to the top menu: **Terminal > New Terminal**.

### 3. Set Up the Virtual Environment
In the VS Code terminal, create an isolated virtual environment (`venv`) for your project:
```zsh
python3 -m venv venv
```

**Important:** After running this command, VS Code might show a popup in the bottom right corner asking: *"We noticed a new environment has been created. Do you want to select it for the workspace folder?"* -> **Click "Yes"**.

### 4. Activate the Virtual Environment
Activate the environment in your current VS Code terminal:
```zsh
source venv/bin/activate
```
*(You will know it worked when your terminal prompt starts with `(venv)`).*

### 5. Install Dependencies
With the environment active, install all required packages:
```zsh
pip install -r requirements.txt
```

### 6. Run the Project
You can now run your code directly from the terminal:
```zsh
python main.py  # Replace 'main.py' with your actual starting script
```
*(Alternatively, you can use the "Run" button ▶️ in the top right corner of VS Code).*
