import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import os

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Sales Data Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------
# Dashboard Title
# ---------------------------
st.title("📊 Sales Data Analysis Dashboard")
st.write("Interactive Data Analytics Dashboard using Python, Pandas, Plotly and Streamlit")

# ---------------------------
# Load Dataset
# ---------------------------
file_path = os.path.join("model", "sales_cleaned.joblib")

if os.path.exists(file_path):
    df = joblib.load(file_path)
else:
    st.error("Dataset file not found!")
    st.stop()

# ---------------------------
# KPI Metrics
# ---------------------------
st.subheader("Key Performance Indicators")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", f"${df['Sales'].sum():,.2f}")

with col2:
    st.metric("Total Profit", f"${df['Profit'].sum():,.2f}")

with col3:
    st.metric("Total Orders", df.shape[0])

# ---------------------------
# Filters
# ---------------------------
st.sidebar.header("Filters")

region = st.sidebar.selectbox(
    "Select Region",
    options=["All"] + list(df["Region"].unique())
)

if region != "All":
    df = df[df["Region"] == region]

# ---------------------------
# Sales by Category Chart
# ---------------------------
st.subheader("Sales by Category")

category_sales = df.groupby("Category")["Sales"].sum().reset_index()

fig1 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category",
    title="Total Sales by Category"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------------------
# Sales by Region Chart
# ---------------------------
st.subheader("Sales by Region")

region_sales = df.groupby("Region")["Sales"].sum().reset_index()

fig2 = px.pie(
    region_sales,
    values="Sales",
    names="Region",
    title="Sales Distribution by Region"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# Monthly Sales Trend
# ---------------------------
st.subheader("Monthly Sales Trend")

df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Month"] = df["Order Date"].dt.month

monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()

fig3 = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------
# Profit vs Sales Scatter
# ---------------------------
st.subheader("Profit vs Sales")

fig4 = px.scatter(
    df,
    x="Sales",
    y="Profit",
    color="Category",
    title="Profit vs Sales Analysis"
)

st.plotly_chart(fig4, use_container_width=True)

# ---------------------------
# 3D Visualization
# ---------------------------
st.subheader("3D Sales Analysis")

fig5 = px.scatter_3d(
    df,
    x="Sales",
    y="Profit",
    z="Quantity",
    color="Category",
    title="3D Sales Visualization"
)

st.plotly_chart(fig5, use_container_width=True)

# ---------------------------
# Dataset Preview
# ---------------------------
st.subheader("Dataset Preview")

st.dataframe(df.head())

# ---------------------------
# Footer
# ---------------------------
st.write("---")
st.write("Developed using Python, Pandas, Plotly and Streamlit")
