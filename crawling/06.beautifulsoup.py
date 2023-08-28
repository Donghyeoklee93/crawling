from bs4 import BeautifulSoup as BS
import requests as req

url = "https://naver.com"
res = req.get(url)
# print(res.text)

soup = BS(res.text, "html.parser")

print(soup.title)
print(soup.title.string)
