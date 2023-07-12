import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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

crypto_rows = driver.find_elements(By.XPATH, '//tbody/tr')
for tr in crypto_rows:
    _, _, name, price, one_hr, one_day, one_week, market_cap, volume, circ_supply, week_chart, _ =tr.find_elements(By.XPATH,".//td")
    print(name.text)
    print(price.text)
    print(one_hr.text)
    print(one_day.text)
    print(one_week.text)
    print(market_cap.text)
    print(volume.text)
    print(circ_supply.text)
    print(week_chart.text)
    print("-" * 50)

