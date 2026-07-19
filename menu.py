from visualizations import *

while True:

    print("\n===== GRAPH MENU =====")
    print("1 Sales by Region")
    print("2 Sales by Category")
    print("3 Profit by Category")
    print("4 Top 5 Products by Sales")
    print("5 Sales vs Profit")
    print("6 Order Quantity Distribution")
    print("7 Profit Distribution")
    print("8 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        sales_by_region()

    elif choice == 2:
        sales_by_category()

    elif choice == 3:
        profit_by_category()

    elif choice == 4:
        top_products()

    elif choice == 5:
        sales_vs_profit()

    elif choice == 6:
        order_distribution()

    elif choice == 7:
        profit_distribution()

    elif choice == 8:
        break

    else:
        print("Invalid choice")