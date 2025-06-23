"""
JSON Data Sync
Fetches JSON data from an API and saves it locally.
"""

import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()

with open("posts.json", "w") as f:
    json.dump(data, f, indent=2)

print("Data saved to posts.json")
