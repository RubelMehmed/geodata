import pandas as pd

# Creating a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

print(df)

# Combo-attack: Subset, sort, and add a new column
# 1. Subset rows where Age is greater than 25
subset_df = df[df['Age'] > 25]

# 2. Sort by Age
sorted_subset_df = subset_df.sort_values(by='Age')

# 3. Add a new column for Age in 10 years
sorted_subset_df['Age in 10 Years'] = sorted_subset_df['Age'] + 10

print("Combo-attack result:")
print(sorted_subset_df)