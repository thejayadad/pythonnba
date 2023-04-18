
import requests


API_KEY = 'G1HNCDQLS97VTIUR'


STOCK_SYMBOL = "PSEC"
STOCK_END_POINT = 'https://www.alphavantage.co/query?'

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_SYMBOL,
    "apikey": API_KEY
}

r = requests.get(STOCK_END_POINT, params = stock_params)

data = r.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

print(data_list[0])
