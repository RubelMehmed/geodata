import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


# _____Read the dataset from csv file group1.csv
data = pd.read_csv("C:/Users/Mehrima/Downloads/group-1.csv", sep=",")
print(data.head())
# Mapping values
gender_map = {1: "Female", 2: "Male"}
education_map = {1: "High School/College", 2: "Bachelors", 3: "Masters", 4: "Doctorate"}
marital_status_map = {1: "Single", 2: "Married", 3: "Divorced"}


# ____________Add value levels
data['Gender'] = data['Gender'].map(gender_map)
data['Educational Level'] = data['Educational Level'].map(education_map)
data['Marital Status'] = data['Marital Status'].map(marital_status_map)


# Check for missing values
missing_summary = data.isnull().sum()
print("Missing values:\n", missing_summary)

# Drop rows with missing values
data_cleaned = data.dropna()


# Bar diagram for Educational Level
data_cleaned['Educational Level'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Educational Level Distribution")
plt.xlabel("Educational Level")
plt.ylabel("Count")
plt.show()

# Pie charts for Gender and Marital Status
data_cleaned['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.show()

data_cleaned['Marital Status'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Marital Status Distribution")
plt.show()

# Histograms for spending score 
plt.hist(data_cleaned['Spending Score'], bins=10, color='green', alpha=0.7)
plt.title("Spending Score Distribution")
plt.xlabel("Spending Score")
plt.ylabel("Frequency")
plt.show()

# Histograms for  monthly saving(usd)

plt.hist(data_cleaned['Monthly Saving (USD)'], bins=10, color='purple', alpha=0.7)
plt.title("Monthly Saving Distribution")
plt.xlabel("Monthly Saving (USD)")
plt.ylabel("Frequency")
plt.show()

# Scatterplot for spending score and monthly saving
sns.scatterplot(x='Spending Score', y='Monthly Saving (USD)', data=data_cleaned)
plt.title("Spending Score vs Monthly Saving")
plt.xlabel("Spending Score")
plt.ylabel("Monthly Saving (USD)")
plt.show()


#Analyzinng Associations----------=>
# Correlation between Spending Score and Monthly Saving
correlation = data_cleaned[['Spending Score', 'Monthly Saving (USD)']].corr()
print("Correlation matrix:\n", correlation)




import statsmodels.api as sm

# Prepare independent and dependent variables
X = data_cleaned[['Age', 'Income', 'Spending Score']]
y = data_cleaned['Monthly Saving (USD)']

# Add a constant to the independent variables
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Summary of the regression model
print(model.summary())
