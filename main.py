import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://www.divan.ru/nalchik/'

driver.get(url)

time.sleep(5)

sale = driver.find_elements(By.CLASS_NAME, 'div.yo4lA wcwtp')

parsed_data = []

for sale in sale:
    try:
        title = sale.find_element(By.CSS_SELECTOR, 'div.page-category').text
        furniture = sale.find_element(By.CSS_SELECTOR, 'div.NuViy S5rWI').text
        priсe = sale.find_element(By.CSS_SELECTOR, 'span.class="ui-An69V"').text
    except:
        print("произошла ошибка при парсинге")
        continue

        parsed_data.append([title, furniture, price])

driver.quit()

with open("hh.csv", 'w', newline='',  encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['название, наборы мебели, цена'])
    writer.writerows(parsed_data)
