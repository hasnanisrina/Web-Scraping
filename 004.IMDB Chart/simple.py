#1.Import library
import pandas as pd
import requests
from bs4 import BeautifulSoup

#2.set base url and result
url = "https://www.imdb.com/chart/top/"
all_movies = []

#3.request raw html data
response = requests.get(url)

#4.parser html
soup = BeautifulSoup(response.text, "html.parser")

#5.find specific content
movies = soup.find_all("li", class_="ipc-metadata-list-summary-item")

#6.loop for every box
for box in movies:
    title = box.find("h3", class_="ipc-title__text ipc-title__text-reduced").get_text(strip=True)
    
    all_movies.append({"title":title})

print(all_movies)