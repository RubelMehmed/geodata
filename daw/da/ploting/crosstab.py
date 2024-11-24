import pandas as pd

data = {
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
    'Purchased': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No']
}


df = pd.DataFrame(data)

cross_tab = pd.crosstab(df['Gender'], df['Purchased'])

print(cross_tab)