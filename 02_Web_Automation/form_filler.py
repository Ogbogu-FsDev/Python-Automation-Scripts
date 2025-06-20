"""
Form Filler
Submits a simple contact form to a test server.
"""

import requests

FORM_URL = "https://httpbin.org/post"

payload = {
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Hello from Python!"
}

response = requests.post(FORM_URL, data=payload)

print("Server response:")
print(response.json())
