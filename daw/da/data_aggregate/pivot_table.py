import pandas as pd
# Sample DataFrame with missing values
data = {
    'Store': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [200, 300, 250, None, 150]
}

df = pd.DataFrame(data)

# Fill missing values with 0 and pivot table with sales by store
df['Sales'].fillna(0, inplace=True)
sales_by_store = df.pivot_table(index='Store', values='Sales', aggfunc='sum')

print(sales_by_store)