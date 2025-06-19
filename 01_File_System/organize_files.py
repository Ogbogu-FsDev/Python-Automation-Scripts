"""
Organize Files Script
Moves files into folders by their file extension.
"""

import os
import shutil

SOURCE_DIR = "./"

for filename in os.listdir(SOURCE_DIR):
    if os.path.isfile(filename):
        ext = filename.split(".")[-1]
        folder = os.path.join(SOURCE_DIR, ext + "_files")
        os.makedirs(folder, exist_ok=True)
        shutil.move(filename, folder)
        print(f"Moved {filename} to {folder}")
