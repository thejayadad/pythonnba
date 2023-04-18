
import requests


STOCK_NAME = "PSEC"
COMPANY_NAME = "Prospect Capital Corporation"
STOCK_API_KEY = "G1HNCDQLS97VTIUR"
STOCK_END_POINT = "https://www.alphavantage.co/query?"
NEWS_ENDPOINT = ""

#G1HNCDQLS97VTIUR


import requests



stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

r = requests.get(STOCK_END_POINT, params=stock_params)
data = r.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_closing_data = data_list[0]
day_prior_closing = data_list[1]
# print(day_prior_closing)
print("Data List")
print(data_list)
print("yesterday data")
print(yesterday_closing_data)
