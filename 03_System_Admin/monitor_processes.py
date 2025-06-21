"""
Monitor Processes
Lists running processes using psutil.
"""

import psutil

print("Running processes:")
for proc in psutil.process_iter(['pid', 'name']):
    print(proc.info)
