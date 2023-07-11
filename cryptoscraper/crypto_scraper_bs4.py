from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
web_page = requests.get(url)
html_document = web_page.text
soup = BeautifulSoup(html_document, "html.parser")
crypto_table = soup.find(name="table", attrs="sc-996d6db8-3 cOXNvh cmc-table")

# print(type(web_page))
# print(web_page)
# print(dir(web_page))
# print(web_page.text)