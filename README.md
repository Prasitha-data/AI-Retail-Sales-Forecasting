# 📈 AI Retail Sales Forecasting

## Project Overview

This project analyzes historical retail sales data from the Global Superstore dataset and predicts future sales trends using machine learning and time-series forecasting techniques.

The objective is to help businesses understand sales performance, identify profitable categories and markets, and support data-driven decision-making through forecasting and interactive dashboards.

---

## Problem Statement

Retail businesses need accurate sales forecasting to optimize inventory management, improve business planning, and maximize profitability.

This project uses historical sales data to analyze business performance and forecast future sales trends using Facebook Prophet.

---

## Dataset Information

**Dataset:** Global Superstore

**Records:** 51,290

**Features:** 21

The dataset contains information such as:

- Order ID
- Order Date
- Ship Date
- Customer Name
- Product Name
- Category
- Market
- Region
- Sales
- Profit
- Discount
- Quantity

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Facebook Prophet
- Streamlit
- Power BI

---

## Features

### Data Analysis
- Sales Analysis
- Profit Analysis
- Market Analysis
- Category Analysis
- Product Performance Analysis

### Dashboard Development
- Interactive Streamlit Dashboard
- Power BI Dashboard
- KPI Monitoring
- Business Insights Visualization

### Sales Forecasting
- Time Series Forecasting
- Future Sales Prediction
- Trend Analysis
- Forecast Visualization

---

## Key Performance Indicators (KPIs)

| KPI | Value |
|------|------|
| Total Sales | 4,865,671 |
| Total Profit | 577,692 |
| Total Orders | 10,086 |
| Total Customers | 795 |

---

## Business Insights

- Technology category generated the highest sales.
- Technology category generated the highest profit.
- APAC market generated the highest revenue.
- Higher discounts negatively affected profitability.
- Sales showed a positive growth trend over time.
- Historical patterns indicate continued sales growth potential.

---

## Dashboard Screenshots

### Streamlit Dashboard Overview

![Overview](screenshots/streamlit_overview.png)

### Streamlit Analytics Dashboard

![Analytics](screenshots/streamlit_analytics.png)

### Sales Forecasting

![Forecasting](screenshots/streamlit_forecasting.png)

### Power BI Dashboard

![Power BI Dashboard](screenshots/powerbi_dashboard.png)

---

## Project Structure

```text
AI_RETAIL_SALES_FORECASTING
│
├── screenshots/
│   ├── powerbi_dashboard.png
│   ├── streamlit_analytics.png
│   ├── streamlit_forecasting.png
│   └── streamlit_overview.png
│
├── app.py
├── Sales_Forecasting.ipynb
├── SuperStoreOrders.csv.zip
├── AI_Retail_Sales_Forecasting.pbix
├── README.md
├── requirements.txt
├── .gitignore
└── venv/
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Navigate to Project Folder

```bash
cd AI_Retail_Sales_Forecasting
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

## Power BI Dashboard

A Power BI dashboard was developed to provide:

- Sales Performance Analysis
- Category-wise Analysis
- Market-wise Analysis
- KPI Monitoring
- Business Intelligence Reporting

File:

```text
AI_Retail_Sales_Forecasting.pbix
```

---

## Future Enhancements

- Advanced Forecasting Models
- Real-Time Data Integration
- Customer Segmentation
- Inventory Optimization
- Interactive Forecast Filters
- Cloud Deployment

---

## Developed By

**Prasitha**
