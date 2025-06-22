"""
Excel Report Generator
Creates a simple Excel file with sample data.
"""

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [85, 90, 95]
}

df = pd.DataFrame(data)
df.to_excel("report.xlsx", index=False)

print("Excel report saved as report.xlsx")

