import time
from utils import get_webelemente_percentage_value, sort_by_field,add_custom_index_cell,get_money_as_number,write_to_csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from mail_sender import Mail_Sender

service = Service(executable_path="Users/Public/Downloads/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get('https://coinmarketcap.com')

height = driver.execute_script("return document.body.scrollHeight")
scroll = 0
while True:
    scroll+=1
    driver.execute_script(f"window.scrollTo(0,{1080 * scroll})")
    if scroll*1080 >= height:
        break
    time.sleep(1)

table = []
crypto_rows = driver.find_elements(By.XPATH, '//tbody/tr')
for tr in crypto_rows:
    _, _, name, price, one_hr, one_day, one_week, market_cap, volume, circ_supply, week_chart, _ =tr.find_elements(By.XPATH,".//td")
    processed_row = {
        'name' : name.text.split("\n")[0],
        'price' : price.text,
        'one_hr': get_webelemente_percentage_value(one_hr),
        'one_day': get_webelemente_percentage_value(one_day),
        'one_week': get_webelemente_percentage_value(one_week),
        'market_cap':market_cap.text,
        'volume': volume.text.split("\n")[0],
        'circ_supply': circ_supply.text.split(" ")[0],
        'week_chart': week_chart.find_element(By.TAG_NAME, "a").get_attribute("href"),
        
    }
    table.append(processed_row)

add_custom_index_cell(table)

print("A criptomoeda que mais valorizou foi: ")
print(f"\tna ultima hora:{sort_by_field(table=table,field='one_hr')[0]}")
print(f"\tno ultimo dia:{sort_by_field(table=table,field='one_day')[0]}")
print(f"\tna ultima semana:{sort_by_field(table=table,field='one_week')[0]}")

print("A criptomoeda que mais desvalorizou foi: ")
print(f"\tna ultima hora:{sort_by_field(table=table,field='one_hr',reverse=False)[0]}")
print(f"\tno ultimo dia:{sort_by_field(table=table,field='one_day',reverse=False)[0]}")
print(f"\tna ultima semana:{sort_by_field(table=table,field='one_week',reverse=False)[0]}")


print("As moedas que mais valorizaram foram:")
for row in sort_by_field(table=table,field='custom_index')[:10]:
    print(f"{row['name']} - {row['price']} - {row['custom_index']}")

write_to_csv(table)

# crypto_mail = Mail_Sender(
#         mail_server='smtp.gmail.com',
#         port=465,
#         sender='matheusereis44@gmail.com',
#         receiver='kayoleanndro2@gmail.com',
#         subject=f'Dados cripto com arquivo',
#         body_msg='Esse é o arquivo data csv em anexo',
#         attachment_file_path='crypto_data.csv'
#     )

# crypto_mail.send_mail()
