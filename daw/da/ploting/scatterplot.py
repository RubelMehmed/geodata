import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



#  Load the dataset for histogram analysis

data = pd.read_csv('C:/Users/Mehrima/Downloads/geodata/daw/Data/Day-3 session-3.csv')  


# Update with the actual file path
variable_to_plot = 'English_Score'

sns.scatterplot(data=data, x='Math_Score', y='English_Score')

plt.xlabel('Math Score')
plt.ylabel('English Score')
plt.title('Scatteredplot of math Score vs English Score')

plt.show()