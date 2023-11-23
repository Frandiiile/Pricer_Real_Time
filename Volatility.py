from alpha_vantage.timeseries import TimeSeries
import numpy as np

api_key = '2SR2GRZD96F7MMRV'

symbol = 'TSLA'

ts = TimeSeries(key=api_key, output_format='json')

data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')

closing_prices = [float(data[date]['4. close']) for date in sorted(data.keys())]

returns = np.diff(closing_prices) / closing_prices[:-1]

volatility = np.std(returns)

print(f"The real-time volatility of {symbol} is: {volatility * 100:.2f}%")
