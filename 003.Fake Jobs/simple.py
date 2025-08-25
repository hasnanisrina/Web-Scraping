#1.Import library
import pandas as pd
import requests
from bs4 import BeautifulSoup

#2.set base url and result
url = "https://realpython.github.io/fake-jobs/"
all_jobs = []

#3.request raw html data
response = requests.get(url)

#4.parser html
soup = BeautifulSoup(response.text, "html.parser")

#5.find specific content
jobs = soup.find_all("div", class_="column is-half")

#6.loop for every box
for box in jobs:
    title = box.find("h2", class_="title is-5").get_text(strip=True)
    company = box.find("h3", class_="subtitle is-6 company").get_text(strip=True)
    location = box.find("p",class_="location").get_text(strip=True)
    all_jobs.append({"title":title,"company":company, "location":location})

print(all_jobs)