from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_pages = response.text

soup = BeautifulSoup(yc_web_pages, "html.parser")
print(soup.title)
articles = soup.find_all(name="span",class_ ="titleline")
article_texts = []
article_links = []
for article_tag in articles:

    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvotes = [score.getText() for score in soup.find_all("span",class_="score")]
print(article_texts)
print(article_links)
print(article_upvotes)