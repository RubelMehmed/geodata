import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Creating DataFrames
# Creating a DataFrame from a list of dictionaries
data = [
    {'Date': '2023-01-01', 'Size': 'Small', 'Price': 1.00, 'Sales': 100},
    {'Date': '2023-01-01', 'Size': 'Medium', 'Price': 1.50, 'Sales': 150},
    {'Date': '2023-01-01', 'Size': 'Large', 'Price': 2.00, 'Sales': 200},
    {'Date': '2023-01-02', 'Size': 'Small', 'Price': 1.10, 'Sales': 90},
    {'Date': '2023-01-02', 'Size': 'Medium', 'Price': np.nan, 'Sales': 160},  # Missing Price
    {'Date': '2023-01-02', 'Size': 'Large', 'Price': 2.10, 'Sales': 210},
]

df = pd.DataFrame(data)

# Step 2: Visualizing Your Data
# Visualizing the sales of different avocado sizes
plt.figure(figsize=(10, 5))
df.groupby('Size')['Sales'].sum().plot(kind='bar', color='skyblue')
plt.title('Total Sales by Avocado Size')
plt.xlabel('Avocado Size')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.show()

# Step 3: Handling Missing Values
# Finding missing values
print("\nMissing values in the DataFrame:")
print(df.isnull().sum())

# Replacing missing values with the mean price of the available sizes
mean_price = df['Price'].mean()
df['Price'].fillna(mean_price, inplace=True)

# Confirming that missing values have been replaced
print("\nDataFrame after replacing missing values:")
print(df)

# Step 4: Reading and Writing CSVs
# Writing the DataFrame to a CSV file
df.to_csv('avocado_sales.csv', index=False)

# Reading the CSV file back into a DataFrame
df_from_csv = pd.read_csv('avocado_sales.csv')
print("\nDataFrame read from CSV:")
print(df_from_csv)

# Step 5: Visualizing Changes in Sales Over Time
# Converting 'Date' to datetime format for better handling
df['Date'] = pd.to_datetime(df['Date'])

# Plotting changes in sales over time
plt.figure(figsize=(10, 5))
df.groupby('Date')['Sales'].sum().plot(kind='line', marker='o', color='orange')
plt.title('Changes in Avocado Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Step 6: Price of Conventional vs. Organic Avocados (Simulated Data)
# Adding a new column for avocado type
df['Type'] = ['Conventional', 'Organic', 'Conventional', 'Organic', 'Conventional', 'Organic']

# Visualizing price differences
plt.figure(figsize=(10, 5))
df.groupby('Type')['Price'].mean().plot(kind='bar', color='lightgreen')
plt.title('Average Price of Conventional vs. Organic Avocados')
plt.xlabel('Avocado Type')
plt.ylabel('Average Price')
plt.xticks(rotation=0)
plt.show()

# Wrap-up
print("\nFinal DataFrame:")
print(df)