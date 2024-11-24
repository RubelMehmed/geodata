import pandas as pd
# Sample DataFrame with duplicates
data = {
    'Store': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [200, 300, 200, 400, 150]
}

df = pd.DataFrame(data)

# Drop duplicates
df_unique = df.drop_duplicates()

print(df_unique)