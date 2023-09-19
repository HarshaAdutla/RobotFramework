
# Radio Button and is_displayed method

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select

service_obj = Service()  # It will automatically download the suitable version and starts the execution
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radio_buttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
for button in radio_buttons:
    if button.get_attribute("value") == "radio2":
        button.click()
        time.sleep(4)
        assert button.is_selected()

driver.execute_script("window.scrollTo(200,200)")
assert driver.find_element(By.ID, "displayed-text").is_displayed()  # It should pass bcz the edit box is displayed
driver.find_element(By.ID, 'hide-textbox').click()  # Here I am clicking on the hide box so the edit box won't be displayed
# Now I am again checking whether the edit box is displayed or not


time.sleep(3)
# assert driver.find_element(By.ID, "displayed-text").is_displayed()  # Script will fail here
assert not driver.find_element(By.ID, "displayed-text").is_displayed()