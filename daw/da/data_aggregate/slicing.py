import pandas as pd
import numpy as np

# Exercise 1: Create a DataFrame for Products
data_products = {
    'Product': ['Apple', 'Banana', 'Cherry'],
    'Price': [1.2, 0.5, 2.0],
    'Quantity': [30, 50, 20]
}

df_products = pd.DataFrame(data_products)
df_products.set_index('Product', inplace=True)

# Subsetting to get the price of 'Banana'
banana_price = df_products.loc['Banana', 'Price']
print("Price of Banana:", banana_price)

# Exercise 2: Create a DataFrame for Sales
data_sales = {
    'Year': [2021, 2021, 2022, 2022],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Sales': [100, 150, 120, 180]
}

df_sales = pd.DataFrame(data_sales)
df_sales.set_index(['Year', 'City'], inplace=True)

# Slicing to get sales data for 'Los Angeles' in 2022
la_sales_2022 = df_sales.loc[(2022, 'Los Angeles')]
print("Sales for Los Angeles in 2022:", la_sales_2022['Sales'])


# Exercise 3: Create a time series DataFrame
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
df_time_series = pd.DataFrame(date_rng, columns=['date'])
df_time_series['Temperature'] = np.random.randint(20, 100, size=(len(df_time_series)))
df_time_series.set_index('date', inplace=True)

# Slicing the time series DataFrame for the first 5 days
slice_time_series = df_time_series.iloc[:5]
print("\nTemperature data for the first 5 days:")
print(slice_time_series)

# Exercise 4: Create a pivot table from the sales DataFrame
pivot_table = df_sales.pivot_table(index='City', columns='Year', values='Sales', aggfunc='sum')

# Subsetting the pivot table to get total sales for 'New York'
ny_sales = pivot_table.loc['New York']
print("\nTotal sales for New York:")
print(ny_sales)