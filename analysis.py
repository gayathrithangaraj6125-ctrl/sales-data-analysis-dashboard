import pandas as pd
import joblib

# Load dataset
file_path = r"data/Sample - Superstore.csv"

df = pd.read_csv(file_path, encoding="latin1")

print("Dataset Loaded Successfully\n")

# Convert dates (mixed formats)
df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed", dayfirst=False)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="mixed", dayfirst=False)

# Create Month column
df["Month"] = df["Order Date"].dt.month

# Missing values check
print("Missing Values:\n")
print(df.isnull().sum())

# Sales statistics
print("\nSales Statistics:\n")
print(df["Sales"].describe())

# Save processed dataset
joblib.dump(df, "model/sales_cleaned.joblib")

print("\nDataset saved using Joblib successfully!")


import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

print("\nCreating Charts...\n")

# 1️⃣ Sales by Category
sales_category = df.groupby("Category")["Sales"].sum()

plt.figure()
sales_category.plot(kind="bar", title="Sales by Category")
plt.ylabel("Total Sales")
plt.savefig("charts/sales_by_category.png")
plt.close()

# 2️⃣ Sales by Region
sales_region = df.groupby("Region")["Sales"].sum()

plt.figure()
sales_region.plot(kind="bar", title="Sales by Region")
plt.ylabel("Total Sales")
plt.savefig("charts/sales_by_region.png")
plt.close()

# 3️⃣ Category Distribution
plt.figure()
sales_category.plot(kind="pie", autopct="%1.1f%%", title="Category Distribution")
plt.ylabel("")
plt.savefig("charts/category_distribution.png")
plt.close()

# 4️⃣ Monthly Sales Trend
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure()
monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trend")
plt.ylabel("Sales")
plt.savefig("charts/monthly_sales.png")
plt.close()

# 5️⃣ Profit vs Sales Scatter
plt.figure()
sns.scatterplot(x="Sales", y="Profit", data=df)
plt.title("Profit vs Sales")
plt.savefig("charts/profit_vs_sales.png")
plt.close()

# 6️⃣ 3D Sales Chart
fig = px.scatter_3d(
    df,
    x="Sales",
    y="Profit",
    z="Quantity",
    color="Category",
    title="3D Sales Analysis"
)

fig.write_html("charts/3d_sales_chart.html")

print("Charts created successfully!")