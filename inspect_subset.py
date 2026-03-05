import pandas as pd

# Load the CSV you just created
df = pd.read_csv("msd_subset_metadata.csv")

print("Total rows:", len(df))
print("\nMissing values per column:")
print(df.isnull().sum())

print("\nBasic statistics:")
print(df.describe())

print("\nFirst few rows:")
print(df.head())