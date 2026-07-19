import pandas as pd

# Load dataset
df = pd.read_excel("data/SuperStore_Sales_DataSet.xlsx")

print("Initial Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())
# Fix weird column name
df.columns = df.columns.str.replace(r'\+.*', '', regex=True)

print("\nCleaned Columns:")
print(df.columns)
df.to_excel("data/cleaned_dataset.xlsx", index=False)
print("\nCleaned dataset saved.")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])