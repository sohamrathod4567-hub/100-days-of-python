from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_pages = response.text

soup = BeautifulSoup(yc_web_pages, "html.parser")
print(soup.title)
article_tag = soup.find(name="span",class_ ="titleline")
print(article_tag)
article_text = article_tag.getText()