import requests

base_url = "http://api.openweathermap.org/data/2.5/forecast"

parameters = {"q": "Kuala Lumpur,MY", 
              "appid": "1bf20ea9960dc27c6711a92a66bc51e4"}

response = requests.get(base_url, params = parameters)

print(response.text)