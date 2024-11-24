# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [200, 220, 250, 275, 300, 320],
    'Profit': [50, 60, 70, 80, 90, 100]
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Plotting Sales and Profit
plt.figure(figsize=(10, 6))

# Plot sales data
plt.plot(df['Month'], df['Sales'], label='Sales', color='blue', marker='o')

# Plot profit data
plt.plot(df['Month'], df['Profit'], label='Profit', color='green', marker='s')

# Adding title and labels
plt.title('Sales and Profit Over Time')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.legend()

# Show the plot
plt.show()
