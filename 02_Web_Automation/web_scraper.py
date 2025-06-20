"""
Basic Web Scraper
Fetches and prints the page title of a given URL.
"""

import requests
from bs4 import BeautifulSoup

URL = "https://example.com"

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

print(f"Page title: {soup.title.string}")
