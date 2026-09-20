# Setting Up a new Project under MacOS

> A brief description of what this project does and the problem it solves.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your macOS machine:
- **Git** (Usually comes pre-installed with Xcode Command Line Tools)
- **Python 3** (Recommended to install via [Homebrew](https://brew.sh/): `brew install python`)

---

## 🚀 Local Setup & Development (macOS)

Follow these steps to set up the project locally on your Mac.

### 1. Clone the Repository
Open your terminal (Terminal.app or iTerm2) and clone this repository:
```zsh
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name
```

### 2. Set Up a Virtual Environment
It is highly recommended to use a virtual environment (`venv`) to keep project dependencies isolated from your macOS system packages. 

*(Note: On macOS, you often need to use `python3` instead of just `python`)*
```zsh
# Create the virtual environment
python3 -m venv venv
```

### 3. Activate the Virtual Environment
Activate the isolated environment for your current terminal session:
```zsh
source venv/bin/activate
```
*(You will know it worked when your terminal prompt starts with `(venv)`).*

### 4. Install Dependencies
Once the virtual environment is active, install all required packages using `pip`:
```zsh
pip install -r requirements.txt
```

*Note for developers: If you install new packages (e.g., `pip install flask`), remember to update the requirements file by running `pip freeze > requirements.txt`.*

### 5. Run the Project
Start the application or script. Once the virtual environment is active, you can use the standard `python` command:
```zsh
python main.py  # Replace 'main.py' with your actual starting script
```

---

## 🧹 Useful macOS Commands

If you need to leave the virtual environment, simply run:
```zsh
deactivate
```

If you ever need to completely reset your project dependencies, you can safely delete the virtual environment folder and recreate it:
```zsh
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
