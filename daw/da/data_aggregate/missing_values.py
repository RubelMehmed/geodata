import pandas as pd

# Example dataset for avocados_2016
data = {
    "date": ["2016-01-03", "2016-01-10", "2016-01-17", "2016-01-24", "2016-01-31"],
    "avg_price": [1.33, 1.35, None, 1.40, 1.41],
    "total_volume": [64236.62, 54876.98, 118220.22, 78992.15, None],
    "type": ["conventional", "conventional", "conventional", "organic", "organic"],
    "region": ["Albany", "Albany", "Albany", "Albany", "Albany"]
}

avocados_2016 = pd.DataFrame(data)
print(avocados_2016)
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print("Missing values per cell:")
print(avocados_2016.isna())

# Check each column for missing values
print("\nMissing values in each column:")
print(avocados_2016.isna().any())

# Count total missing values in each column
missing_values = avocados_2016.isna().sum()

# Print missing values count
print("\nTotal missing values by column:")
print(missing_values)

# Bar plot of missing values by variable
missing_values.plot(kind="bar", color="orange", title="Missing Values by Column")

# Show plot
plt.xlabel("Columns")
plt.ylabel("Number of Missing Values")
plt.show()


# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
missing_values_check = avocados_complete.isna().any()

# Print the check result
print("Are there any missing values in avocados_complete?")
print(missing_values_check)

# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()


# Show the plot
plt.show()