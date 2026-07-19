import pandas as pd
import matplotlib.pyplot as plt
import os

# ===== FIND PROJECT ROOT =====
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ===== PATHS =====
data_path = os.path.join(BASE_DIR, "data", "cleaned_dataset.xlsx")
visuals_path = os.path.join(BASE_DIR, "visuals")

# create visuals folder if missing
os.makedirs(visuals_path, exist_ok=True)

# ===== LOAD DATA =====
df = pd.read_excel(data_path)

# ============================
# SALES BY REGION
# ============================
def sales_by_region():

    region_sales = df.groupby("Region")["Sales"].sum().sort_values()

    region_sales.plot(kind="bar")

    plt.title("Sales by Region")
    plt.ylabel("Sales")

    save_path = os.path.join(visuals_path, "sales_by_region.png")
    plt.savefig(save_path)

    print("Saved:", save_path)

    plt.show()
    plt.close()


# ============================
# SALES BY CATEGORY
# ============================
def sales_by_category():

    category_sales = df.groupby("Category")["Sales"].sum().sort_values()

    category_sales.plot(kind="bar")

    plt.title("Sales by Category")

    save_path = os.path.join(visuals_path, "sales_by_category.png")
    plt.savefig(save_path)

    print("Saved:", save_path)

    plt.show()
    plt.close()


# ============================
# PROFIT BY CATEGORY
# ============================
def profit_by_category():

    category_profit = df.groupby("Category")["Profit"].sum().sort_values()

    category_profit.plot(kind="bar")

    plt.title("Profit by Category")

    save_path = os.path.join(visuals_path, "profit_by_category.png")
    plt.savefig(save_path)

    print("Saved:", save_path)

    plt.show()
    plt.close()


# ============================
# TOP 5 PRODUCTS
# ============================
def top_products():

    top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(5)

    top_products.plot(kind="bar")

    plt.title("Top 5 Products by Sales")

    save_path = os.path.join(visuals_path, "top_products.png")
    plt.savefig(save_path)

    print("Saved:", save_path)

    plt.show()
    plt.close()


# ============================
# SALES VS PROFIT
# ============================
def sales_vs_profit():

    plt.scatter(df["Sales"], df["Profit"])

    plt.xlabel("Sales")
    plt.ylabel("Profit")
    plt.title("Sales vs Profit")

    save_path = os.path.join(visuals_path, "sales_vs_profit.png")
    plt.savefig(save_path)

    print("Saved:", save_path)

    plt.show()
    plt.close()


# ============================
# ORDER QUANTITY DISTRIBUTION
# ============================
def order_distribution():

    df["Quantity"].plot(kind="hist", bins=20)

    plt.title("Order Quantity Distribution")

    save_path = os.path.join(visuals_path, "order_distribution.png")
    plt.savefig(save_path)

    print("Saved:", save_path)

    plt.show()
    plt.close()


# ============================
# PROFIT DISTRIBUTION
# ============================
def profit_distribution():

    df["Profit"].plot(kind="hist", bins=20)

    plt.title("Profit Distribution")

    save_path = os.path.join(visuals_path, "profit_distribution.png")
    plt.savefig(save_path)

    print("Saved:", save_path)

    plt.show()
    plt.close()