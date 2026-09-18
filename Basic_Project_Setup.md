# Basics Python Project Setup

> In this File I explain the basic setup of a Python Project and how to locally run and pull the git Project.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your machine:
- **Python 3.x**
- **Git**

---

## 🚀 Local Setup & Development

Follow these steps to set up the project locally on your machine.

### 1. Clone the Repository
Open your terminal and clone this repository:
```bash
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name
```

### 2. Set Up a Virtual Environment
It is highly recommended to use a virtual environment (`venv`) to keep project dependencies isolated from your global system.

```bash
# Create the virtual environment
python -m venv venv
```

### 3. Activate the Virtual Environment
Depending on your terminal shell or operating system, run the corresponding command to enter the isolated environment:

**For Fish shell:**
```bash
source venv/bin/activate.fish
```

**For Bash / Zsh (macOS / Linux):**
```bash
source venv/bin/activate
```

**For Windows (Command Prompt / PowerShell):**
```cmd
.\venv\Scripts\activate
```

*(You will know it worked when your terminal prompt starts with `(venv)`).*

### 4. Install Dependencies
Once the virtual environment is active, install all required packages using `pip`:
```bash
pip install -r requirements.txt
```

*Note for developers: If you install new packages (e.g., `pip install requests`), remember to update the requirements file by running `pip freeze > requirements.txt`.*

### 5. Run the Project
Start the application or script:
```bash
python main.py  # Replace 'main.py' with your actual starting script
```

---

## 🔄 Git Workflow (For Contributors)

When you make changes to the code, use this standard workflow to save and upload your progress:

```bash
# 1. Stage all changes
git add .

# 2. Save a snapshot with a descriptive message
git commit -m "Add a clear description of what you changed"

# 3. Upload the changes to GitHub
git push origin main
```
