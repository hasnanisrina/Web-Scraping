#1.Import library
import pandas as pd
import requests
from bs4 import BeautifulSoup

#2.set base url and result
url = "https://books.toscrape.com/"
all_books = []

#3.request raw html data
response = requests.get(url)

#4.parser html
soup = BeautifulSoup(response.text, "html.parser")

#5.find specific content
books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

#6.loop for every box
for box in books:
    title = box.find("h3").get_text(strip=True)
    price = box.find("p", class_="price_color").get_text(strip=True)
    status = box.find("p",class_="instock availability").get_text(strip=True)
    all_books.append({"title":title,"price":price,"status":status})

print(all_books)