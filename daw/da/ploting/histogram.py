import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



#  Load the dataset for histogram analysis
try:
    data = pd.read_csv('C:/Users/Mehrima/Downloads/geodata/daw/Data/Day-3 session-3.csv')  # Update with the actual file path
    variable_to_plot = 'English_Score'

    # Check if the column exists
    if variable_to_plot not in data.columns:
        print(f"Column '{variable_to_plot}' not found in the dataset. Available columns: {list(data.columns)}")
    else:
        # Seaborn histogram with density plot
        sns.histplot(data=data, x=variable_to_plot, kde=True, color='blue')
        plt.xlabel('English Score')
        plt.ylabel('Frequency')
        plt.title('Histogram of English Score from Dataset (Seaborn)')
        plt.show()

        # Matplotlib histogram
        plt.hist(data[variable_to_plot], bins=5, edgecolor='orange', color='lightblue')
        plt.title('Histogram of English Score from Dataset (Matplotlib)')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.show()

except FileNotFoundError:
    print("The file '/Data/Day-3 session-3.csv' was not found. Please check the file path.")
except pd.errors.ParserError:
    print("There was an error parsing the CSV file. Ensure the file format is correct.")
