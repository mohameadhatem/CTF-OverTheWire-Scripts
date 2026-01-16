# CTF OverTheWire Scripts

Python automation scripts for solving **OverTheWire CTF challenges**, with a focus on the **Bandit** wargame.

The goal of this repository is to practice:
- SSH automation
- Linux command execution
- Text processing
- Security-oriented scripting

---

## Included Challenges
- **Bandit** (current)

Each script connects via SSH, executes the required commands, and extracts the next level password without storing any secrets.

---

## Technologies Used
- Python 3
- Paramiko (SSH automation)
- Linux command-line tools (`cat`, `grep`, `awk`, `find`)

---

## Repository Structure

```text
CTF-OverTheWire-Scripts/
├── bandit/
│   ├── bandit00.py
│   ├── bandit01.py
│   ├── bandit02.py
│   └── ...
├── README.md
└── .gitignore
```
---

## Usage
Run a script for the corresponding level:
```bash
python3 bandit00.py

---
## 👤 Author
Mohamed Hatem  
SOC & Cyber Security Learning Project

---