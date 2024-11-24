import pandas as pd

# Sample DataFrame
data = {
    'Store': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [200, 300, 250, 400, 150]
}

df = pd.DataFrame(data)

# Calculate mean and median sales
mean_sales = df['Sales'].mean()
median_sales = df['Sales'].median()

print(f"Mean Sales: {mean_sales}")
print(f"Median Sales: {median_sales}")