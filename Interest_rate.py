import quandl

# Set your API key
quandl.ApiConfig.api_key = "1vZQ4fsag_MjNZeF949v"

# Define the dataset code for the risk-free rate you want (e.g., US 10-Year Treasury Yield)
dataset_code = "FRED/DGS10"


# Get risk-free rate data from the specified start date
risk_free_rate_data = quandl.get(dataset_code)
# Print the data
print(risk_free_rate_data)