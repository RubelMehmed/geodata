import pandas as pd

# Sample DataFrame
data = {
    'Store': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [200, 300, 250, 400, 150]
}

df = pd.DataFrame(data)

# Efficient summaries using .agg()
summary = df.groupby('Store')['Sales'].agg(['mean', 'sum', 'count'])

print(summary)