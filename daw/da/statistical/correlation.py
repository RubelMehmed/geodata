import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



#  Load the dataset for histogram analysis

data = pd.read_csv('C:/Users/Mehrima/Downloads/geodata/daw/Data/Day-3 session-3.csv')  


correlation_coefficient = data['Math_Score'].corr(data['English_Score'])

print(correlation_coefficient)