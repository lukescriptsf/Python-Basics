# How to Start a New Python Project from Scratch (VS Code & macOS)

This guide walks you through setting up a brand new Python project locally and preparing it for GitHub. 

## 1. Create the Project Folder
Open your macOS Terminal and create a new, empty folder for your project. Then, open it directly in Visual Studio Code:
```zsh
mkdir my-new-project
cd my-new-project
code .
```
*(You can now close the macOS terminal and do everything else inside the integrated VS Code terminal: `⌃` + `` ` ``)*

## 2. Initialize Git & Create `.gitignore`
Before writing any code, turn this folder into a Git repository. 
```zsh
git init
```

**Crucial:** You must tell Git to ignore certain files so they don't get uploaded to the internet. Create a file named `.gitignore` in your project folder and add these lines:
```text
venv/
__pycache__/
.DS_Store
.env
```

## 3. Set Up the Virtual Environment
Create your isolated Python environment so your installed packages don't mess with your macOS system:
```zsh
# Create the environment
python3 -m venv venv

# Activate it
source venv/bin/activate
```
*(Your terminal prompt should now start with `(venv)`).*

## 4. Install Initial Packages
Install the libraries you need for your new project (for example, Flask or Requests):
```zsh
pip install flask requests
```

Once installed, generate your requirements file. This allows other developers to know exactly which packages your project needs:
```zsh
pip freeze > requirements.txt
```

## 5. Write Your First Code
Create your main Python file, usually called `app.py` or `main.py`, and write your initial code. You can run it anytime to test:
```zsh
python main.py
```

---

## 6. Upload to GitHub for the First Time
Once you have written some code and are ready to save it online, follow these steps:

1. Go to [GitHub.com](https://github.com/) and click **"New"** repository. 
2. Give it a name, leave it empty (do NOT check "Add a README" or ".gitignore" since you already made them locally), and click **Create**.
3. GitHub will show you a page with commands under the headline *"…or push an existing repository from the command line"*. Copy those commands and run them in your VS Code terminal. It usually looks like this:

```zsh
# Save your local progress
git add .
git commit -m "Initial commit: Project setup"

# Link your local folder to the new GitHub repository
git branch -M main
git remote add origin [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)

# Upload the code
git push -u origin main
```
