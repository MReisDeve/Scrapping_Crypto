from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
web_page = requests.get(url)
html_document = web_page.text
soup = BeautifulSoup(html_document, "html.parser")


crypto_table_body = soup.tbody
row = crypto_table_body.tr
_, _, name, price, one_hr, one_day, one_week, market_cap, volume, circ_supply, week, _ =row.find_all(name="td")

print(name.p.text)
print(price.span.text)
print(round(float(one_hr.span.text.strip("%")),2))
print(round(float(one_day.span.text.strip("%")),2))
print(round(float(one_week.span.text.strip("%")),2))
print(market_cap.find(name= "span", attrs={"data-nosnippet":"true"}).text)
print(volume.p.text)
print(circ_supply.p.text)
print(f"{url}{week.a.get('href')}")