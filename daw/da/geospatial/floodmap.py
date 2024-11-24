import os

# Set GDAL and PROJ environment variables
os.environ['GDAL_DATA'] = r'C:\Users\Mehrima\miniconda3\envs\geo\Library\share\gdal'
os.environ['PROJ_LIB'] = r'C:\Users\Mehrima\miniconda3\envs\geo\Library\share\proj'

import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString
import pandas as pd

# Load the shapefile for Bangladesh from the local path
# bangladesh_shapefile = "Data\admin_ne\ne_110m_admin_0_countries.shp"  # Adjust path
bangladesh_shapefile = r'C:\Users\Mehrima\Downloads\geodata\daw\Data\admin_ne\ne_110m_admin_0_countries.shp'

world = gpd.read_file(bangladesh_shapefile)
# Load the world dataset (make sure to download it properly)

# Print columns of the GeoDataFrame to see the available attributes
print(world.columns)

# Check the first few rows to verify the data
print(world.head())
# Filter Bangladesh data from the world map
# bangladesh = world[world.name == "Bangladesh"]
bangladesh = world[world['SOVEREIGNT'] == 'Bangladesh']


# Example DataFrame for flood-prone areas (Longitude, Latitude, Flood Risk Level)
data = {
    'Longitude': [90.4125, 91.0000, 92.0000],
    'Latitude': [23.8103, 24.2000, 25.5000],
    'Flood Risk Level': [3, 2, 1]  # 3 = High, 2 = Medium, 1 = Low
}
df = pd.DataFrame(data)

# Create GeoDataFrame from the DataFrame
geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
geo_df = gpd.GeoDataFrame(df, geometry=geometry)

# Plotting flood-prone areas in Bangladesh on a map
fig, ax = plt.subplots(figsize=(12, 10))

# Plot Bangladesh boundary
bangladesh.plot(ax=ax, color='lightgrey')

# Plot flood-prone regions, color-coded by Flood Risk Level
geo_df.plot(ax=ax, column='Flood Risk Level', cmap='coolwarm', markersize=100, legend=True, alpha=0.7)

# Add a title and labels
plt.title('Flood Prone Areas in Bangladesh', fontsize=16)
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Show the map
plt.show()

# Define rivers (Ganges, Brahmaputra, Meghna) as lines
rivers = [
    LineString([(88, 23.5), (90, 24.5), (92, 25)]),  # Ganges River path
    LineString([(88.5, 25), (90, 26), (91, 27)]),    # Brahmaputra River path
    LineString([(91, 22), (92, 23), (93, 24)]),      # Meghna River path
]

# Create a GeoDataFrame for rivers
rivers_gdf = gpd.GeoDataFrame(geometry=rivers)

# Plot everything together
fig, ax = plt.subplots(figsize=(12, 10))

# Plot Bangladesh boundary
bangladesh.plot(ax=ax, color='lightgrey')

# Plot flood-prone regions
geo_df.plot(ax=ax, column='Flood Risk Level', cmap='coolwarm', markersize=100, legend=True, alpha=0.7)

# Plot rivers
rivers_gdf.plot(ax=ax, color='blue', linewidth=2)

# Add a title and labels
plt.title('Flood Prone Areas with Major Rivers in Bangladesh', fontsize=16)
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Show the map
plt.show()
