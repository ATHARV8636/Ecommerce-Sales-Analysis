
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/sales_data.csv")

print("ECOMMERCE SALES DATA ANALYSIS")
print("--------------------------------")

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nTotal Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("Total Orders:", df["Order_ID"].nunique())

print("\nCategory-wise Sales:")
print(df.groupby("Category")["Sales"].sum())

print("\nCity-wise Sales:")
print(df.groupby("City")["Sales"].sum())

print("\nCategory-wise Profit:")
print(df.groupby("Category")["Profit"].sum())

category_sales = df.groupby("Category")["Sales"].sum()

category_sales.plot(kind="bar", title="Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("dashboard/category_sales.png")
plt.show()

city_sales = df.groupby("City")["Sales"].sum()

city_sales.plot(kind="bar", title="City-wise Sales")
plt.xlabel("City")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("dashboard/city_sales.png")
plt.show()

print("\nAnalysis Completed Successfully!")
