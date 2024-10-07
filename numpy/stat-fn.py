# Statistical Functions with NumPy Arrays
import numpy as np

# Define the np_city array with sample data
# Columns: [column_0, column_1]
np_city = np.array([
    [70, 150],
    [68, 160],
    [72, 170],
    [75, 180],
    [78, 190]
])

# Define the np_baseball array with sample data
# Columns: [height, weight, age]
np_baseball = np.array([
    [74, 200, 25],
    [72, 180, 30],
    [76, 220, 28],
    [70, 160, 26],
    [75, 210, 27]
])

# Mean of the first column of np_city
mean_city = np.mean(np_city[:, 0])
print("Mean of np_city[:, 0]:", mean_city)

# Median of the first column of np_city
median_city = np.median(np_city[:, 0])
print("Median of np_city[:, 0]:", median_city)

# Correlation Coefficient between the two columns of np_city
correlation_coefficient = np.corrcoef(np_city[:, 0], np_city[:, 1])
print("Correlation Coefficient:\n", correlation_coefficient)

# Standard Deviation of the first column of np_city
std_dev_city = np.std(np_city[:, 0])
print("Standard Deviation of np_city[:, 0]:", std_dev_city)

# Create np_height_in from np_baseball (first column)
np_height_in = np_baseball[:, 0]

# Print out the mean of np_height_in
print("Mean of np_height_in:", np.mean(np_height_in))

# Print out the median of np_height_in
print("Median of np_height_in:", np.median(np_height_in))
