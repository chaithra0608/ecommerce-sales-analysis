import pandas as pd

df = pd.read_excel("data/cleaned_dataset.xlsx")

print("Dataset Shape:", df.shape)
print(df.head())
print("\n===== BUSINESS OVERVIEW =====")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("\n===== SALES BY REGION =====")

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print(region_sales)
top_region = region_sales.idxmax()
top_value = region_sales.max()
print(f"\nTop performing region is {top_region} with sales of {top_value}")

print("\n===== SALES BY CATEGORY =====")

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print(category_sales)
top_category = category_sales.idxmax()
top_category_value = category_sales.max()
print(f"\nTop performing category is {top_category} with sales of {top_category_value}")
print("\n===== TOP 5 PRODUCTS BY SALES =====")

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head()
print(top_products)