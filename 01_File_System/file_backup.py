"""
File Backup Script
Copies all .txt files to a backup folder.
"""

import os
import shutil

SOURCE_DIR = "./"
BACKUP_DIR = "./backup"

os.makedirs(BACKUP_DIR, exist_ok=True)

for filename in os.listdir(SOURCE_DIR):
    if filename.endswith(".txt"):
        shutil.copy2(os.path.join(SOURCE_DIR, filename), BACKUP_DIR)
        print(f"Backed up {filename} to {BACKUP_DIR}")
