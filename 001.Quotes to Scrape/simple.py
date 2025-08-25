#1.Import library
import requests
from bs4 import BeautifulSoup
import pandas as pd

#2.set url and result
url = "https://quotes.toscrape.com/"
all_quotes = []

#3.request for get the raw data html
response = requests.get(url)

#4.parse with beautiful soup
soup = BeautifulSoup(response.text, 'html.parser')

#5.find specific data
quotes =soup.find_all("div",class_="quotes")

#6.loop for every box
for box in quotes:
    text = box.find("span", class_="text").get_text(strip=True)
    author = box.find("small", class_="author").get_text(strip=True)
    all_quotes.append({"text":text, "author":author})

print(all_quotes)

#7.save with the table structure
#data = pd.DataFrame (all_quotes)

#print(data)