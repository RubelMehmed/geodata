import pandas as pd
# Sample DataFrame
data = {
    'Sales': [200, 300, 250, 400, 150]
}

df = pd.DataFrame(data)

# Calculate cumulative sum
df['Cumulative Sales'] = df['Sales'].cumsum()

print(df)