
# Handling Dynamic dropdowns

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select

service_obj = Service()  # It will automatically download the suitable version and starts the execution
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(3)
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        time.sleep(4)
        break
print("India Selected")

driver.find_element(By.ID, "autosuggest").clear()
time.sleep(5)
driver.find_element(By.ID, "autosuggest").send_keys("Sau")
time.sleep(3)
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']")
print(len(countries))
for country in countries:
    country_name = country.text
    if country_name == "Saudi Arabia":
        country.click()
        time.sleep(3)
        break
name = driver.find_element(By.ID, "autosuggest").get_attribute("value")
print("Selected country name is: " + name)
assert name == "Saudi Arabia"
