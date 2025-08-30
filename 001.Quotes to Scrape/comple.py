#1.Import Library
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

#2.set base url
BASE_URL = "https://quotes.toscrape.com/"

#3.Function 1.feth url
def fetch_page(url):
    """Download HTML and return BeautifulSoup object (with error handling)."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return none
    
#4.Function 2.Parse html
def parse_quotes(soup):
    """Extract quotes from a page"""
    all_quotes = []
    if soup:
        for box in quotes:
            text = box.find("span", class_="text").get_text(strip=True)
            author = box.find("small", class_="author").get_text(strip=True)
            all_quotes.append({"text":text, "author":author})
    return all_quotes
