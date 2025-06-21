"""
Check Disk Space
Prints free and total disk space.
"""

import shutil

total, used, free = shutil.disk_usage("/")

print(f"Total: {total // (2**30)} GiB")
print(f"Used: {used // (2**30)} GiB")
print(f"Free: {free // (2**30)} GiB")
