
# E-Commerce Sales Data Analysis

## Project Overview
This project analyzes E-Commerce sales data using Python, SQL, Excel, and Streamlit. It helps understand sales performance, profit, customer behavior, and city-wise business performance through data analysis and an interactive dashboard.

## Technologies Used
- Python
- Pandas
- Matplotlib
- MySQL
- Microsoft Excel
- Streamlit

## Dataset
- Total Records: 500
- Total Customers: 100
- Cities: 8
- Categories: 4
- Data Period: January 2025 – October 2026

Note: This project uses a synthetic dataset generated for learning and demonstration purposes.

## Key Features
- Sales and Profit Analysis
- City-wise Sales Analysis
- Category-wise Sales Analysis
- Monthly Sales Trends
- Top 5 Customers Analysis
- Profit Margin Analysis
- Interactive Dashboard
- City and Category Filters
- Download Filtered Sales Data

## Business Insights
- Total Sales: ₹13,700,652.75
- Total Profit: ₹3,766,052.75
- Total Orders: 500
- Total Customers: 100
- Highest Revenue Category: Electronics
- Highest Profit Margin Category: Fashion
- Highest Revenue City: Nagpur

## Project Structure
```text
Ecommerce-Sales-Analysis/
│
├── dataset/
│   └── sales_data.csv
│
├── excel/
│
├── sql/
│   └── analysis_queries.sql
│
├── python/
│   ├── analysis.py
│   └── generate_data.py
│
├── dashboard/
│   ├── app.py
│   ├── category_sales.png
│   └── city_sales.png
│
├── README.md
└── requirements.txt
```

## How to Run the Project

### 1. Clone the Repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Python Analysis
```bash
python python/analysis.py
```

### 4. Run Dashboard
```bash
python -m streamlit run dashboard/app.py
```

## Dashboard
The interactive dashboard displays:
- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Category-wise Sales
- City-wise Sales
- Monthly Sales Trends

## Author
Atharv Gharal

## Purpose
Data Analytics Learning Project
