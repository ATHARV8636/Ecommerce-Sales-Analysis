
import csv
import random
from datetime import datetime, timedelta

random.seed(42)

products = {
    "Electronics": [
        ("Laptop", 45000, 32000),
        ("Mobile", 18000, 12000),
        ("Headphones", 1500, 700),
        ("Keyboard", 900, 400)
    ],
    "Fashion": [
        ("Shirt", 1200, 600),
        ("Jeans", 1800, 900),
        ("Shoes", 2500, 1400),
        ("Watch", 2200, 1100)
    ],
    "Home": [
        ("Chair", 3000, 1800),
        ("Table", 5500, 3500),
        ("Lamp", 800, 350),
        ("Sofa", 15000, 10000)
    ],
    "Grocery": [
        ("Rice", 60, 40),
        ("Oil", 150, 110),
        ("Sugar", 45, 30),
        ("Tea", 250, 170)
    ]
}

cities = [
    "Kolhapur", "Pune", "Mumbai",
    "Sangli", "Satara", "Nashik",
    "Nagpur", "Solapur"
]

customers = [f"CUST{1000+i}" for i in range(100)]

start_date = datetime(2025, 1, 1)

with open("dataset/sales_data.csv", "w", newline="",
          encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Order_ID", "Order_Date", "Customer_ID",
        "City", "Category", "Product",
        "Quantity", "Unit_Price", "Unit_Cost",
        "Discount", "Sales", "Profit"
    ])

    for i in range(1, 501):

        category = random.choice(list(products.keys()))
        product, price, cost = random.choice(products[category])

        quantity = random.randint(1, 8)
        discount = random.choice([0, 0.05, 0.10, 0.15])

        order_date = start_date + timedelta(
            days=random.randint(0, 669)
        )

        sales = round(quantity * price * (1-discount), 2)
        profit = round(sales - quantity * cost, 2)

        writer.writerow([
            f"ORD{i:04d}",
            order_date.strftime("%Y-%m-%d"),
            random.choice(customers),
            random.choice(cities),
            category,
            product,
            quantity,
            price,
            cost,
            discount,
            sales,
            profit
        ])

print("Dataset created successfully!")
print("Total Records: 500")
print("File: dataset/sales_data.csv")
