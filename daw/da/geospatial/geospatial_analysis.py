# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Simulate geospatial data for various regions
data = {
    'Region': ['Region A', 'Region B', 'Region C', 'Region D', 'Region E', 'Region F', 'Region G', 'Region H', 'Region I', 'Region J'],
    'Latitude': [34.05, 40.71, 51.51, 48.85, 39.90, 52.52, 35.68, 41.88, 33.44, 34.21],
    'Longitude': [-118.25, -74.01, -0.12, 2.35, 116.38, -0.13, 139.69, -87.63, -112.07, -118.47],
    'Population': [1000000, 8500000, 8000000, 2200000, 1400000, 10000000, 5000000, 1800000, 2200000, 1500000],
    'Area (sq km)': [1300, 780, 600, 1050, 2500, 500, 900, 800, 1500, 1100],
    'Urbanization Rate (%)': [89, 92, 80, 85, 75, 97, 90, 80, 83, 78],
    'Transportation Index': [7.5, 8.2, 6.5, 8.0, 6.0, 9.0, 8.5, 7.8, 6.8, 7.0]
}

# Convert data into a pandas DataFrame
df = pd.DataFrame(data)

# Calculate Population Density (Population / Area)
df['Population Density'] = df['Population'] / df['Area (sq km)']

# Print the DataFrame
print(df)


# Plotting Population Density vs Transportation Index
plt.figure(figsize=(10, 6))

# Use scatter plot to show relationship between Population Density and Transportation Index
scatter = plt.scatter(df['Population Density'], df['Transportation Index'], 
                      c=df['Urbanization Rate (%)'], cmap='viridis', s=100, edgecolors='k', alpha=0.7)

# Adding color bar to represent Urbanization Rate
plt.colorbar(scatter, label='Urbanization Rate (%)')

# Adding titles and labels
plt.title('Population Density vs Transportation Index', fontsize=14)
plt.xlabel('Population Density (People per sq km)', fontsize=12)
plt.ylabel('Transportation Index (0 to 10)', fontsize=12)

# Show the plot
plt.grid(True)
plt.show()

# Now, let's plot the population density on a map-like plot
import geopandas as gpd
from shapely.geometry import Point

# Create GeoDataFrame from the DataFrame
geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
geo_df = gpd.GeoDataFrame(df, geometry=geometry)

# Plotting the population density on a map-like scatter plot
fig, ax = plt.subplots(figsize=(12, 8))

# Create a world basemap
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.plot(ax=ax, color='lightgrey')

# Plot our GeoDataFrame with population density as the color
geo_df.plot(ax=ax, column='Population Density', cmap='coolwarm', markersize=100, legend=True, alpha=0.7)

# Add titles and labels
plt.title('Population Density by Region', fontsize=16)
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Show the plot
plt.show()
