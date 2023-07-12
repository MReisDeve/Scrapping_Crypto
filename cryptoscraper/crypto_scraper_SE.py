from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="Users/Public/Downloads/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get('https://coinmarketcap.com')
