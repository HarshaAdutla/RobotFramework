
# Alerts

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select


# Here I tried giving the input at the beginning of the script
alert_name1 = input("Enter name to send on alert message: ")
alert_name2 = input("Enter name to send on Second alert message: ")


service_obj = Service()  # It will automatically download the suitable version and starts the execution
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(alert_name1)
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='Alert']").click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(alert_name2)
time.sleep(2)
driver.find_element(By.ID, "confirmbtn").click()
alert_message = alert.text
print(alert_message)
assert alert_name2 in alert_message
time.sleep(2)
alert.dismiss() # If any alert pop up have Cancel and Okay CTA by writing like this we are rejecting the pop-up
time.sleep(2)
