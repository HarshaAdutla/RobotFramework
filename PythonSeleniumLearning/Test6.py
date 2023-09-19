
# Handling checkboxes

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select

service_obj = Service()  # It will automatically download the suitable version and starts the execution
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# I need to select Option 2 check box

boxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in boxes:
    option = checkbox.find_element(By.XPATH, "parent::label").text
    if option == "Option2":
        selected_option = option
        checkbox.click()
        print(checkbox.is_selected())   # is_selected method prints boolean value, Here I am printing that value
        assert checkbox.is_selected()   # Here I kept assertion on is_selected method
        time.sleep(5)
        print(option + " is selected")
assert selected_option == "Option2"

# We can select this Option2 by suing get attribute method

"""
for checkbox in boxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        checkbox.is_selected()
        time.sleep(4)
        break
"""
