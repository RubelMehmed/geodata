import pandas as pd
# Sample DataFrame
data = {
    'Store': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [200, 300, 250, 400, 150]
}

df = pd.DataFrame(data)

# Calculate percent of sales by store
total_sales = df['Sales'].sum()
sales_percent = df.groupby('Store')['Sales'].sum() / total_sales * 100

# Group by store and calculate total sales
total_sales_by_store = df.groupby('Store')['Sales'].sum()

print(total_sales_by_store)
print(sales_percent)
