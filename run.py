import os
import sys
from pathlib import Path

# Locate GITHUB Automation directory
GITHUB_AUTO_DIR = Path(__file__).resolve().parent.parent / "GITHUB Automation"

if not GITHUB_AUTO_DIR.exists():
    # Try current directory or adjacent
    GITHUB_AUTO_DIR = Path(__file__).resolve().parent

if str(GITHUB_AUTO_DIR) not in sys.path:
    sys.path.insert(0, str(GITHUB_AUTO_DIR))

# Change current working directory to GITHUB Automation to ensure relative paths & DB are unified
os.chdir(str(GITHUB_AUTO_DIR))

# Forward directly to the unified runner
from run import main

if __name__ == "__main__":
    main()
