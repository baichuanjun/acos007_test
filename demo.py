import json

import requests



data = requests.get("https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/campaign-management/openapi#/campaign%20status")
print(data.content)
print(data.status_code)
print(json.loads(data.content))