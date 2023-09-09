# Import the necessary modules.
import pandas as pd
import numpy as np

# Load the historical data for AAPL stock.
data = pd.read_csv('AAPL.csv')

# Calculate the 200-day moving average of the closing price.
ma = data['Close'].rolling(200).mean()

# Calculate the difference between the closing price and the moving average.
diff = data['Close'] - ma

# Identify points where the difference is greater than 2 standard deviations from the mean.
signals = diff[diff > diff.mean() + 2 * diff.std()]

# Print the number of signals identified.
print(f"{len(signals)} signals identified")