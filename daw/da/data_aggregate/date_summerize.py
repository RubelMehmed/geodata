import pandas as pd
# Sample DataFrame with dates
data = {
    'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-03']),
    'Sales': [200, 300, 250, 400]
}

df = pd.DataFrame(data)

# Summarize sales by date
daily_sales = df.groupby('Date')['Sales'].sum()

print(daily_sales)