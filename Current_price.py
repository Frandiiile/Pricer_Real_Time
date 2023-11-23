from alpha_vantage.timeseries import TimeSeries
import json

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
api_key = '2SR2GRZD96F7MMRV'

# Replace 'AAPL' with the stock symbol of the company you're interested in
symbol = 'TSLA'

# Initialize Alpha Vantage API object
ts = TimeSeries(key=api_key, output_format='json')

# Get the stock price data
data, meta_data = ts.get_quote_endpoint(symbol=symbol)

# Extract the current stock price
current_price = data['05. price']

# Print the result
print(f"The current price of {symbol} is: ${current_price}")
