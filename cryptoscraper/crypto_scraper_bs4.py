from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com"
web_page = requests.get(url)
html_document = web_page.text
soup = BeautifulSoup(html_document, "html.parser")
crypto_table_body = soup.tbody

table = []
for tr in crypto_table_body.contents:
    try:
        _, _, name, price, one_hr, one_day, one_week, market_cap, volume, circ_supply, week_chart, _ =tr.contents
    except ValueError:
        break
    processed_row = {
        'name' : name.p.text,
        'price' : price.span.text,
        'one_hr': round(float(one_hr.span.text.strip("%")),2),
        'one_day': round(float(one_day.span.text.strip("%")),2),
        'one_week': round(float(one_week.span.text.strip("%")),2),
        'market_cap':market_cap.find(name= "span", attrs={"data-nosnippet":"true"}).text,
        'volume': volume.p.text,
        'circ_supply': circ_supply.p.text,
        'week_chart': f"{url}{week_chart.a.get('href')}",
        
    }
    table.append(processed_row)
    for crypto in table:
        print(crypto)