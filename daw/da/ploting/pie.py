import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('/Data/Day-3 session-3.csv')

print(data)

data['Gender'] = data['Gender'].map({1: "Female", 2: "Male"})

print(data)

gender_count = data['Gender'].value_counts()
print(gender_count)

#plot

plt.figure(figsize=(8,8))
plt.pie(gender_count, labels=gender_count.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')

plt.title('Gender Distribution in Educational Dataset')

plt.show()
