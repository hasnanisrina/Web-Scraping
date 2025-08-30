import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/chart/top"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movies = []

for movie in soup.select("td.titleColumn"):
    title = movie.select("a")[0].text
    year = movie.select("span")[0].text
    rating = movie.select("strong")[0].text
    movies.append((title, year, rating))

df = pd.DataFrame(movies, columns=["Title", "Year", "Rating"])
print(df)