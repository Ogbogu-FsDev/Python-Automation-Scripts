"""
REST API Request
Performs a GET request to a public API.
"""

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.json())
