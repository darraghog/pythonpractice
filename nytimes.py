# New York Times Articles list
#
import requests
from bs4 import BeautifulSoup

nytimes_url = "https://www.nytimes.com"

r = requests.get(nytimes_url)

if (r.status_code != 200):
    print("Error code" + r.status_code + " returned.")
    exit(1)

html = r.text

soup = BeautifulSoup(html,'html.parser').body

#print(soup.prettify())
#exit(0)
spans = soup.find_all('span')

for article in spans:
    if not article.attrs:
        print(article.contents[0])
    

