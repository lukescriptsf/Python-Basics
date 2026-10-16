# Python-Basics
In this repository i'm documenting the basics of Python including Cheat-Sheets, Project creation, Isolation of Projects.

# My Python Journey & Git Basics 🚀

Welcome to my personal repository where I document my path of learning **Python** from the ground up, alongside the fundamental workflow of **Git and GitHub**. 

Whether you are just starting out or looking for a quick reference on setting up a development environment, this repository serves as my workspace, notes, and collection of early scripts.

---

## 🧭 About This Repository

This repo is structured to track my progress as I explore core programming concepts, write scripts, and build confidence in software development. Inside, you will find:
* Basic Python syntax and exercises.
* Small automation scripts and practical examples.
* Notes on setting up a clean, efficient development workflow.

---

## 🛠️ Getting Started with Python

To run the code in this repository, you'll need Python installed on your machine. Here is how to get your environment configured.

### 1. Installation
* **Windows:** Download the installer from the [official Python website](https://www.python.org/) and make sure to check the box **"Add Python to PATH"**.
* **macOS / Linux:** Python is often pre-installed, or easily installed via your package manager (e.g., `sudo apt install python3` on Ubuntu or `brew install python` on macOS).

Verify your installation by running this command in your terminal:
```bash
python3 --version
```

### 2. Setting Up a Virtual Environment (Recommended)
It is best practice to isolate your project dependencies using a virtual environment. Run the following commands in your project folder:

```bash
# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
# On macOS / Linux:
source venv/bin/activate
# On Windows (Command Prompt):
# venv\Scripts\activate.bat
# On Windows (PowerShell):
# .\venv\Scripts\Activate.ps1
```

---

## 🐙 Understanding Git & GitHub Basics

**Git** is a distributed version control system that tracks changes in your source code, while **GitHub** is a cloud-based hosting service where you can store, share, and collaborate on your repositories.

### Core Git Concepts
1. **Repository (Repo):** The project folder containing all your files and version history.
2. **Commit:** A snapshot of your project at a specific point in time. Think of it as a save point in a video game.
3. **Stage:** Selecting specific changes you want to include in your next commit before saving them.
4. **Push / Pull:** Uploading your local commits to GitHub (`push`) or downloading remote changes to your computer (`pull`).

### Essential Git Commands Cheat Sheet

| Action | Command | Description |
| :--- | :--- | :--- |
| **Clone** | `git clone <url>` | Download an existing repository from GitHub to your local machine. |
| **Status** | `git status` | Check the current state of your working directory and staged files. |
| **Add** | `git add <filename>` or `git add .` | Stage changes to prepare them for a commit. |
| **Commit** | `git commit -m "Your message"` | Save your staged changes with a descriptive message. |
| **Push** | `git push origin main` | Upload your local commits to your remote repository on GitHub. |
| **Pull** | `git pull` | Fetch and merge changes from the remote repository to your local machine. |

---

## 📂 Repository Structure

```text
├── .gitignore          # Files and folders for Git to ignore (e.g., venv/)
├── README.md           # Documentation for this repository
└── scripts/            # Collection of Python learning scripts and exercises
    ├── 01_basics.py
    └── 02_control_flow.py
```

---

## 📈 What's Next?
* Expanding into functions, data structures, and object-oriented programming in Python.
* Practicing branching and merging workflows in Git.

*Feel free to star ⭐ this repository if you find it helpful or are on a similar learning journey!*
