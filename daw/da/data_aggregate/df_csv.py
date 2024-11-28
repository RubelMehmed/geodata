import pandas as pd

# Create the airline_bumping DataFrame
data = {
    "airline": [
        "DELTA AIR LINES",
        "VIRGIN AMERICA",
        "JETBLUE AIRWAYS",
        "UNITED AIRLINES",
        "HAWAIIAN AIRLINES",
    ],
    "year": [2017, 2017, 2017, 2017, 2017],
    "nb_bumped": [679, 165, 1475, 2067, 92],
    "total_passengers": [99796155, 6090029, 27255038, 70030765, 8422734],
}

airline_bumping = pd.DataFrame(data)

# Load the dataset
# airline_bumping = pd.read_csv("airline_bumping.csv")

# Display the first few rows of the dataset
print("Airline Bumping Data:")
print(airline_bumping.head())

# Group by airline and calculate totals
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()

# Add column for bumps per 10,000 passengers
airline_totals["bumps_per_10k"] = (airline_totals["nb_bumped"] / airline_totals["total_passengers"]) * 10000

# Display the aggregated data
print("\nAirline Totals with Bumps per 10k:")
print(airline_totals)
