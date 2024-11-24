import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    'Category':['A', 'B', 'C', 'D', 'E', 'F'],
    'Value': np.random.randint(50, 100, size=6)
}

df = pd.DataFrame(data)
df

plt.figure(figsize=(10, 6))
plt.bar(df['Category'], df['Value'], color='orange')

plt.title('Value by Category')
plt.xlabel('Category')
plt.ylabel('Value ')

plt.show()


data = pd.read_csv('/Data/Day-3 session-3.csv')


variable_to_plot = 'English_Score'

sns.histplot(data=data, x=variable_to_plot, kde=True)

plt.xlabel('English Score')
plt.ylabel('Frequency')
plt.title("histogram of English Score from Dataset")

plt.show()


plt.hist(data['English_Score'], bins=5, edgecolor='orange')
plt.title('Histogram of English Score from Dataset')
plt.xlabel('Values')
plt.ylabel('Frequency')

plt.show()