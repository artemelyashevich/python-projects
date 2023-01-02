import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.21vek.by/notebooks/'

req = requests.get(url)
src = req.text

with open("index.html", "w", encoding="utf-8") as f:
    f.write(src)

with open("index.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
notebooks = soup.find_all(class_="b-recipes__item__link")

notebooks_dict = {}

for item in notebooks:
    item_text = item.text
    item_href = item.get('href')

    notebooks_dict[item_text] = item_href

with open("notebooks_dict.json", "w") as file:
    json.dump(notebooks_dict, file, indent=4, ensure_ascii=False)

with open("notebooks_dict.json") as file:
    notebooks = json.load(file)
