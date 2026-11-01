
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="E-Commerce Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

df = pd.read_csv("dataset/sales_data.csv")

st.title("📊 E-Commerce Sales Analytics Dashboard")
st.markdown("### Sales and Business Performance Overview")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
total_customers = df["Customer_ID"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"₹{total_sales:,.2f}")
col2.metric("Total Profit", f"₹{total_profit:,.2f}")
col3.metric("Total Orders", total_orders)
col4.metric("Total Customers", total_customers)

st.divider()

st.subheader("Sales Filters")

city = st.selectbox(
    "Select City",
    ["All"] + sorted(df["City"].unique().tolist())
)

category = st.selectbox(
    "Select Category",
    ["All"] + sorted(df["Category"].unique().tolist())
)

filtered_df = df.copy()

if city != "All":
    filtered_df = filtered_df[filtered_df["City"] == city]

if category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == category]

st.subheader("Filtered Business Summary")

c1, c2 = st.columns(2)
c1.metric("Filtered Sales", f"₹{filtered_df['Sales'].sum():,.2f}")
c2.metric("Filtered Profit", f"₹{filtered_df['Profit'].sum():,.2f}")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Category-wise Sales")
    category_sales = filtered_df.groupby("Category")["Sales"].sum()
    fig, ax = plt.subplots()
    category_sales.plot(kind="bar", ax=ax)
    ax.set_xlabel("Category")
    ax.set_ylabel("Sales")
    plt.xticks(rotation=0)
    st.pyplot(fig)
    plt.close(fig)

with right:
    st.subheader("City-wise Sales")
    city_sales = filtered_df.groupby("City")["Sales"].sum()
    fig, ax = plt.subplots()
    city_sales.plot(kind="bar", ax=ax)
    ax.set_xlabel("City")
    ax.set_ylabel("Sales")
    plt.xticks(rotation=45)
    st.pyplot(fig)
    plt.close(fig)

st.divider()

st.subheader("Monthly Sales Trend")

df["Order_Date"] = pd.to_datetime(df["Order_Date"])
monthly_sales = (
    filtered_df.assign(Order_Date=pd.to_datetime(filtered_df["Order_Date"]))
    .groupby(filtered_df["Order_Date"].astype(str).str[:7])["Sales"]
    .sum()
)

st.line_chart(monthly_sales)

st.subheader("Sales Data Table")
st.dataframe(filtered_df, use_container_width=True)

st.download_button(
    "Download Filtered Sales Data",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

st.success("Dashboard Loaded Successfully!")
