"""
Log Parser
Finds and prints lines with the word ERROR.
"""

with open("application.log") as f:
    for line in f:
        if "ERROR" in line:
            print(line.strip())
