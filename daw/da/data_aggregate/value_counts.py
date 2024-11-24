import pandas as pd
# Sample DataFrame
data = {
    'Store': ['A', 'B', 'A', 'B', 'A'],
}

df = pd.DataFrame(data)

# Count occurrences of each store
store_counts = df['Store'].value_counts()

print(store_counts)