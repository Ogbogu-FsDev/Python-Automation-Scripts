"""
Batch Install Packages
Installs a list of Python packages using pip.
"""

import subprocess

packages = ["requests", "beautifulsoup4", "pandas"]

for pkg in packages:
    subprocess.run(["pip", "install", pkg])
    print(f"Installed {pkg}")
