from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
web_page = requests.get(url)
html_document = web_page.text
soup = BeautifulSoup(html_document, "html.parser")

# print(type(web_page))
# print(web_page)
# print(dir(web_page))
# print(web_page.text)