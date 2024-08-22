import requests
import json

# EXAMPLE 1: lemonade with raspberry
print("\nPRODUCT EXAMPLE 1\n")
base_url = "https://api.upcitemdb.com/prod/trial/lookup"
parameters = {"upc": "025000044908"}
response = requests.get(base_url, params=parameters)
info = json.loads(response.text)

item = info["items"][0]
title = item["title"]
brand = item["brand"]
description = item["description"]

print("title:", title)
print("brand:", brand)
print(description)

# EXAMPLE 2: ridged potato chips
print("\nPRODUCT EXAMPLE 2\n")
base_url = "https://api.upcitemdb.com/prod/trial/lookup"
parameters = {"upc": "028400516686"}
response = requests.get(base_url, params=parameters)

item = info["items"][0]
title = item["title"]
brand = item["brand"]
description = item["description"]

print("title:", title)
print("brand:", brand)
print(description)