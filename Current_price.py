from alpha_vantage.timeseries import TimeSeries
import json

api_key = '2SR2GRZD96F7MMRV'

symbol = 'TSLA'

ts = TimeSeries(key=api_key, output_format='json')

data, meta_data = ts.get_quote_endpoint(symbol=symbol)

current_price = data['05. price']

print(f"The current price of {symbol} is: ${current_price}")
