"""
CSV Cleaner
Removes rows with missing data.
"""

import pandas as pd

df = pd.read_csv("input.csv")
df_clean = df.dropna()

df_clean.to_csv("cleaned.csv", index=False)
print("Cleaned CSV saved as cleaned.csv")
