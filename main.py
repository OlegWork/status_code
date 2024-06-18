"""Check whether the site is available"""
import requests
r = requests.get('https://google.com')
print(r.status_code)
