squares = "#"
squares = [x for x in squares * 5]
print(squares)

import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())