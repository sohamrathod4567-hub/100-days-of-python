from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_pages = response.text

soup = BeautifulSoup(yc_web_pages, "html.parser")
print(soup.title)
article = soup.find(name="a",class_ ="storyLink")
print(article)