import requests
from bs4 import BeautifulSoup
start_page = 1
end_page = 3
for pg in range(start_page, end_page+1):
    url =  f"https://librairie.cantook.com/search?q=book&options%5Bprefix%5D=last&options%5Bunavailable_products%5D=hide&type=product&page={pg}"
    response = requests.get(url, headers={"Accept": "text/html"})
    #print(response)
    parsed_response = BeautifulSoup(response.text, "html.parser")
    #print(parsed_response.prettify())
    print(f"\nThis is list of books in page {pg}")
    
    titles = parsed_response.find_all("h2", class_="p product-card__title")
    for title in titles:
        book_title = title.find("a").text.strip()
        print(book_title)