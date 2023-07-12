import time
from selenium.webdriver.common.by import By

def get_tag_percentage_value(tag):
    percentage_delta = round(float(tag.text.strip("%")),2)

    if "down" in tag.span.get("class")[0]:
        percentage_delta = percentage_delta * -1

    return percentage_delta + 0

def sort_by_field(table,field, reverse=True):
    def _select_field(row):
        return row[field]

    return sorted(table, key=_select_field, reverse=reverse)

def get_webelemente_percentage_value(we):
    percentage_delta = round(float(we.text.strip("%")),2)

    if "down" in we.find_element(By.XPATH,".//span/span").get_attribute("class"):
        percentage_delta = percentage_delta * -1

    return percentage_delta + 0

def get_money_as_number(money_str, number_type=float):

    return number_type(money_str.strip("$").replace(",",""))

def get_custom_index(coin_data):

    market_cap = get_money_as_number(money_str=coin_data["market_cap"])
    perc_delta = coin_data["one_week"]
    price=get_money_as_number(money_str=coin_data["price"])

    return (market_cap * perc_delta)/price

def add_custom_index_cell(table):
    for row in table:
        row["custom_index"] = round(get_custom_index(row), 2)