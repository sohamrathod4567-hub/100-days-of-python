import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "NYZHCZ7J7B1OUWZX"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_parameters = {
    "function":"TIME_SERIES_DAILY" ,
    "symbol":STOCK_NAME,
    "apikey":STOCK_API,
    "outputsize":"compact"
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_response_json = stock_response.json()
# print(stock_response_json)
opening_price = stock_response_json["Time Series (Daily)"]["2026-07-31"]["1. open"]
closing_price = stock_response_json["Time Series (Daily)"]["2026-07-30"]["4. close"]
print(closing_price)
print(opening_price)

