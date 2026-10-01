# Bandit Python Security Demo

A small portfolio project that runs Bandit against an intentionally unsafe Python sample, explains the findings, and compares them with safer code.

> **Lab safety:** `app/intentionally_unsafe.py` is for static analysis only. Do not run it or pass real input to it. The file demonstrates unsafe patterns on purpose.

## What you will learn

- Set up a Python virtual environment.
- Install and run Bandit, a static analysis tool for Python.
- Read findings by severity, confidence, test ID, and source location.
- Compare unsafe patterns with safer alternatives.

## 1. Get the project ready

Install Python 3.10 or newer and Git. Download or clone this project, then open a terminal in its folder.

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, run Bandit without activating the environment:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\bandit.exe -r app -f screen
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 2. Run Bandit

```bash
bandit -r app -f screen
```

Save a report to a file:

```bash
bandit -r app -f txt -o bandit-report.txt
```

Bandit exits with a non-zero status when it finds issues. That is expected for this demo because the unsafe sample is included intentionally.

## 3. Review the expected findings

The exact output can vary by Bandit version. In a verification run with Bandit 1.9.4, the unsafe file produced one low-severity B404 review warning and two high-severity findings, B324 and B602. The intentionally unsafe file should raise findings for these patterns:

| Pattern | Typical Bandit test | Why it matters | Safer direction |
|---|---|---|---|
| Importing `subprocess` | B404 | Bandit flags process execution for review; the import alone does not prove a vulnerability. | Avoid launching a process when Python can do the task directly. If a process is necessary, review its executable, arguments, and input handling. |
| `hashlib.md5(...)` used as a digest | B324 | MD5 is not suitable for security-sensitive integrity or password storage. | Use SHA-256 for general integrity checks. For password storage, use a dedicated password-hashing algorithm such as Argon2id, scrypt, or bcrypt. |
| `subprocess.run(..., shell=True)` with user input | B602 | Shell interpretation can turn data into commands. | Prefer an argument list with `shell=False` (the default), and validate inputs against an allowlist. |

Review each result in the terminal output: note the filename and line number, test ID, severity, and confidence. Bandit reports suspicious code patterns; review the surrounding code before deciding whether a finding applies.

## 4. Compare the safer version

Open `app/safer_example.py`. It uses SHA-256 for a non-password digest and formats a message with Python directly, so it does not need an external process. Scan that file alone:

```bash
bandit app/safer_example.py -f screen
```

The safer example should produce no findings with the current project code. This is a teaching example, not a complete security review. If your real application needs a subprocess, a list of arguments with `shell=False` is generally safer than building a shell command, but Bandit may still report that process execution needs review.

## 5. Try an improvement

Make a copy of `app/intentionally_unsafe.py` and change one unsafe pattern at a time. Run Bandit again after each change and note which finding disappears. Do not remove the original sample from your project; it makes the before-and-after comparison clear.

## 6. Push it to GitHub

Create an empty repository on GitHub named `bandit-python-security-demo`. Leave **Add a README**, **Add .gitignore**, and **Choose a license** unchecked because this folder already contains those files. Then, from the project folder:

```bash
git init
git add .
git commit -m "Add Bandit Python security demo"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/bandit-python-security-demo.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. GitHub will ask you to authenticate; use the browser sign-in flow or GitHub CLI if installed. Do not put a password or access token in the remote URL or commit it into the project.

If Git asks for your name and email on the first commit, configure them once on your computer:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-github-email@example.com"
```

## Portfolio write-up

After scanning, add a short section to this README with your Bandit version, the findings you observed, what you changed, and what you learned. Do not claim the sample demonstrates a complete security audit.
