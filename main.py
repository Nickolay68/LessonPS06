import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://www.divan.ru/nalchik/'

driver.get(url)

time.sleep(5)

sale = driver.find_element(By.CSS_SELECTOR, 'div.class=mk_t7')

parsed_data = []

for sale in sale:
    try:
        title = sale.find_element(By.CSS_SELECTOR, 'div.VyQMt')
        furniture = sale.find_element(By.CSS_SELECTOR, 'Pk6w8 fJEzt')
        priсe = sale.find_element(By.CSS_SELECTOR, 'ui-LD-ZU rCNq4')