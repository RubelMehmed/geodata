import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



#  Load the dataset for histogram analysis

data = pd.read_csv('C:/Users/Mehrima/Downloads/geodata/daw/Data/Day-3 session-3.csv')  

X = data[['Study_Hour']]
y = data[['English_Score']]

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

print(model.summery())