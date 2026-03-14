import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

st.title("📊 Sales Data Analysis Dashboard")

# Load cleaned dataset
df = joblib.load("model/sales_cleaned.joblib")

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Sales by Category
st.subheader("Sales by Category")
sales_category = df.groupby("Category")["Sales"].sum().reset_index()
fig1 = px.bar(sales_category, x="Category", y="Sales", color="Category")
st.plotly_chart(fig1)

# Sales by Region
st.subheader("Sales by Region")
sales_region = df.groupby("Region")["Sales"].sum().reset_index()
fig2 = px.bar(sales_region, x="Region", y="Sales", color="Region")
st.plotly_chart(fig2)

# Category Distribution
st.subheader("Category Distribution")
fig3 = px.pie(df, names="Category")
st.plotly_chart(fig3)

# Monthly Sales Trend
st.subheader("Monthly Sales Trend")
monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()
fig4 = px.line(monthly_sales, x="Month", y="Sales")
st.plotly_chart(fig4)

# Profit vs Sales
st.subheader("Profit vs Sales")
fig5 = px.scatter(df, x="Sales", y="Profit", color="Category")
st.plotly_chart(fig5)

# 3D Sales Chart
st.subheader("3D Sales Analysis")
fig6 = px.scatter_3d(
    df,
    x="Sales",
    y="Profit",
    z="Quantity",
    color="Category"
)
st.plotly_chart(fig6)