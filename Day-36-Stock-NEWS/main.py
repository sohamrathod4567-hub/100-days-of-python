import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "NYZHCZ7J7B1OUWZX"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "3ad6fd44b5f148478a79d0d527d760ff"


stock_parameters = {
    "function":"TIME_SERIES_DAILY" ,
    "symbol":STOCK_NAME,
    "apikey":STOCK_API,
    "outputsize":"compact"
}

news_parameters = {
    "apiKey":NEWS_API,
    "qInTitle":COMPANY_NAME,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_response_json = stock_response.json()
print(stock_response_json)
data = stock_response_json["Time Series (Daily)"]


# print(stock_response_json)
# opening_price = stock_response_json["Time Series (Daily)"]["2026-07-31"]["1. open"]
# closing_price = stock_response_json["Time Series (Daily)"]["2026-07-30"]["4. close"]
# print(closing_price)
# print(opening_price)


data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

diff_percent = (difference / float(yesterday_closing_price))*100
print(diff_percent)

if diff_percent > 0.5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_response_json = news_response.json()["articles"]
    three_articles = articles[0:3]  # used the slice function



    formatted_articles = [f"HeadLine:{article['title']}. \n Brief: {article['description']}." for article in three_articles]
    print(formatted_articles)
