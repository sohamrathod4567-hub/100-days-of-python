from bs4 import BeautifulSoup

with open("website.html") as file :
    contents = file.read()

soup = BeautifulSoup(contents , "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.a)
all_anchor_tags = soup.find_all(name = "a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name = "h1" , id = "name")  # This is to find the
print(heading)

section_heading = soup.find(name="h3", class_=("heading")) # This is Done using the Class
print(section_heading)

company_url = soup.select_one(selector="#name") # This is done used selector
print(company_url)

headings = soup.select(".heading") # This is how headings is used
print(headings)