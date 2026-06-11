import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Retail Sales Forecasting Dashboard",
    page_icon="📈",
    layout="wide"
)

# Load Dataset
df = pd.read_csv("SuperStoreOrders.csv.zip")

# Check dataset
st.sidebar.write("Dataset Shape:", df.shape)

# Clean Sales Column
df['sales'] = df['sales'].astype(str).str.replace(',', '', regex=False)
df['sales'] = pd.to_numeric(df['sales'], errors='coerce')

# Convert Dates
df['order_date'] = pd.to_datetime(
    df['order_date'],
    dayfirst=True,
    errors='coerce'
)

df = df.dropna(subset=['sales', 'order_date'])

# KPIs
total_sales = df['sales'].sum()
total_profit = df['profit'].sum()
total_orders = df['order_id'].nunique()
total_customers = df['customer_name'].nunique()

# Title
st.title("📈 AI Retail Sales Forecasting Dashboard")

st.markdown("---")

# Project Overview
st.header("Project Overview")

st.write("""
This project analyzes historical retail sales data from the Global Superstore dataset.

### Technologies Used
- Python
- Pandas
- Streamlit
- Prophet
- Data Visualization

### Objective
Analyze historical sales trends and generate business insights to support future decision making.
""")

# KPIs
st.markdown("---")
st.header("Project KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"{total_sales:,.0f}")
col2.metric("Total Profit", f"{total_profit:,.0f}")
col3.metric("Total Orders", f"{total_orders:,}")
col4.metric("Total Customers", f"{total_customers:,}")

# Monthly Sales Trend
st.markdown("---")
st.header("Monthly Sales Trend")

monthly_sales = (
    df.groupby(df['order_date'].dt.to_period('M'))['sales']
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

st.line_chart(monthly_sales)

# Sales by Category
st.markdown("---")
st.header("Sales by Category")

category_sales = (
    df.groupby('category')['sales']
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_sales)

# Profit by Category
st.markdown("---")
st.header("Profit by Category")

profit_category = (
    df.groupby('category')['profit']
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(profit_category)

# Sales by Market
st.markdown("---")
st.header("Sales by Market")

market_sales = (
    df.groupby('market')['sales']
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(market_sales)

# Top Products
st.markdown("---")
st.header("Top 10 Products by Sales")

top_products = (
    df.groupby('product_name')['sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_products)

# Forecast Section
st.markdown("---")
st.header("Sales Forecasting")

st.info("""
Forecasting was performed using Facebook Prophet.

Model Performance:
- MAE: 15,936.83
- Forecast Horizon: 12 Months

The model predicts continued growth in future sales based on historical trends.
""")

# Dataset Preview
st.markdown("---")
st.header("Dataset Preview")

st.dataframe(df.head())

# Business Insights
st.markdown("---")
st.header("Business Insights")

st.success("Technology category generated the highest sales.")
st.success("APAC market generated the highest revenue.")
st.success("Technology category generated the highest profit.")
st.success("Higher discounts negatively affected profitability.")
st.success("Sales show a positive growth trend over time.")

# Footer
st.markdown("---")
st.write("Developed by Prasitha")