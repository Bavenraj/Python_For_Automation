import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
url =  "https://www.brickz.my/"
ua = UserAgent()
#print(ua.chrome)
header = {'User-Agent':f"{ua.chrome}"}
response_with_user_agent = requests.get(url, headers=header)
response_without_user_agent = requests.get(url, headers={"Accept": "text/html"})


print(response_without_user_agent) #result in 403 forbidden status
print(response_with_user_agent) #result in 200 status