import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the ticker symbol for the stock you want to analyze
ticker = "AAPL"

# Retrieve the historical data for the specified ticker
data = yf.download(ticker, start="2022-01-01", end="2022-12-31")

# Calculate the moving average over a specified window size
window_size = 20
data["Moving Average"] = data["Close"].rolling(window=window_size).mean()

# Plot the closing price and moving average
plt.figure(figsize=(10, 6))
plt.plot(data["Close"], label="Close")
plt.plot(data["Moving Average"], label=f"Moving Average ({window_size} days)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.title(f"{ticker} Stock Price Analysis")
plt.legend()
plt.show()
