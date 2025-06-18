"""
Bulk Rename Script
Renames all .txt files in a given directory to add a prefix.
"""

import os

FOLDER = "./"  # Current directory
PREFIX = "renamed_"

for filename in os.listdir(FOLDER):
    if filename.endswith(".txt"):
        old_path = os.path.join(FOLDER, filename)
        new_path = os.path.join(FOLDER, PREFIX + filename)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {PREFIX + filename}")
