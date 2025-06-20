"""
Auto Login Demo (using requests)
Submits login form data to a website.
"""

import requests

LOGIN_URL = "https://example.com/login"
DASHBOARD_URL = "https://example.com/dashboard"

session = requests.Session()

payload = {
    "username": "your_username",
    "password": "your_password"
}

response = session.post(LOGIN_URL, data=payload)

if response.ok:
    dashboard = session.get(DASHBOARD_URL)
    print("Logged in successfully! Dashboard content snippet:")
    print(dashboard.text[:200])
else:
    print("Login failed.")
