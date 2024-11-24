
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('/Data/sample_data.csv')

# Print the data
print(data)

# Create a simple plot
plt.figure(figsize=(10, 6))
plt.scatter(data['longitude'], data['latitude'], s=data['value']*10, alpha=0.5)
plt.title('Sample Geospatial Data Visualization')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid()
plt.show()
