import pandas as pd
# Sample Data ```python
data = {
    'Region': ['North', 'South', 'North', 'South', 'North'],
    'Store': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [200, 300, 250, 400, 150]
}

df = pd.DataFrame(data)

# Group by region and store, and calculate total sales
total_sales_by_region_store = df.groupby(['Region', 'Store'])['Sales'].sum()

print(total_sales_by_region_store)