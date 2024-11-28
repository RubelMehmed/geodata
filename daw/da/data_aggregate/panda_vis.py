import matplotlib.pyplot as plt
import pandas as pd

# Create a sample DataFrame for avocado sales data
data = {
    "date": [
        "2019-01-01", "2019-01-01", "2019-01-02", "2019-01-02",
        "2019-01-03", "2019-01-03", "2019-01-04", "2019-01-04",
        "2019-01-05", "2019-01-05"
    ],
    "nb_sold": [1500, 2000, 1700, 2200, 1600, 2100, 1800, 2300, 1750, 2400],
    "avg_price": [1.50, 1.20, 1.55, 1.25, 1.60, 1.30, 1.45, 1.35, 1.50, 1.40],
    "type": ["organic", "conventional", "organic", "conventional",
             "organic", "conventional", "organic", "conventional",
             "organic", "conventional"]
}

avocados = pd.DataFrame(data)

# Display the DataFrame
avocados


# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind="line")
# plt.plot(nb_sold_by_date.index, nb_sold_by_date.values)

plt.xlabel("Date")
plt.ylabel("Number of Avocados Sold")
plt.title("Total Avocados Sold Over Time")

# Show the plot
plt.show()

# Scatter plot of avg_price vs. nb_sold with title
plt.scatter(avocados["nb_sold"], avocados["avg_price"], color='blue', alpha=0.7)

# Add labels and title
plt.xlabel("Number of Avocados Sold")
plt.ylabel("Average Price (USD)")
plt.title("Number of Avocados Sold vs. Average Price")
plt.show()
#Or  the other way is call directly;  Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")

# Show the plot
plt.show()

# Histogram of conventional avg_price
avocados_conventional = avocados[avocados["type"] == "conventional"]
plt.hist(avocados_conventional["avg_price"], alpha=0.5, label="Conventional")

# Histogram of organic avg_price
avocados_organic = avocados[avocados["type"] == "organic"]
plt.hist(avocados_organic["avg_price"], alpha=0.5, label="Organic")

# Add a legend
plt.legend()

# Add titles and labels
plt.title("Histogram of Average Prices for Avocado Types")
plt.xlabel("Average Price")
plt.ylabel("Frequency")

# Show the plot
plt.show()

# Histogram of conventional avg_price 
avocados[avocados["type"] == "conventional"]["avg_price"].hist()

# Histogram of organic avg_price
avocados[avocados["type"] == "organic"]["avg_price"].hist()

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()