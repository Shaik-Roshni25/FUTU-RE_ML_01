import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("sales_data.csv", parse_dates=["Order Date"])

# Set plot style
sns.set(style="whitegrid")

# Create a figure and set the layout for 2x2 grid (you can adjust this to your needs)
fig, axes = plt.subplots(2, 2, figsize=(12, 8))  # Adjust the size as necessary

# Plot 1: Sum of Sales by Category (Bar Chart)
sns.barplot(data=df, x="Category", y="Sales", estimator=sum, ax=axes[0, 0])
axes[0, 0].set_title("Sum of Sales by Category")

# Plot 2: Sales over Time (Line Chart)
df_date = df.groupby("Order Date")["Sales"].sum().reset_index()
axes[0, 1].plot(df_date["Order Date"], df_date["Sales"], marker="o")
axes[0, 1].set_title("Sales Over Time")
axes[0, 1].set_xlabel("Date")
axes[0, 1].set_ylabel("Sales")
axes[0, 1].tick_params(axis="x", rotation=45)

# Plot 3: Sales vs Profit (Scatter Plot)
sns.scatterplot(data=df, x="Sales", y="Profit", ax=axes[1, 0])
axes[1, 0].set_title("Sales vs Profit")
axes[1, 0].set_xlabel("Sales")
axes[1, 0].set_ylabel("Profit")

# Plot 4: Sales Distribution by Category (Box Plot)
sns.boxplot(data=df, x="Category", y="Sales", ax=axes[1, 1])
axes[1, 1].set_title("Sales Distribution by Category")

# Adjust the layout to make sure everything fits properly
plt.tight_layout()

# Show all plots at once
plt.show()
