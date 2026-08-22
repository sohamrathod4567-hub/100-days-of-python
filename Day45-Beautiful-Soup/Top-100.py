import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
top_web_page = response.text

soup = BeautifulSoup(top_web_page, "html.parser")

# print(soup.title)
movie_titles = soup.find_all(name ="h3",class_ ="title")
movies= []

for title in movie_titles:
    movies.append(title.text)


movies.reverse() #Because the list is in the reverse order
print(movies)
with open('movies.txt', 'w', encoding="utf-8") as file:
    file.write("\n".join(movies))