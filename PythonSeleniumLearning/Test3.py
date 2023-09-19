import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()  # It will automatically download the suitable version and starts the execution
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client")

"""
-> Successfully Logged In

driver.find_element(By.XPATH, "//input[@type='email']").send_keys("testerone0507@gmail.com")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("Harshatest1")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@value='Login']").click()
time.sleep(3)
print(driver.title)

"""
# Forgot password flow

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
time.sleep(4)
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("testerone0507@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@ formcontrolname ='userPassword']").send_keys("Harsha0507")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@ formcontrolname ='confirmPassword']").send_keys("Harsha0507")
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
time.sleep(5)
driver.find_element(By.ID, "userEmail").send_keys("testerone0507@gmail.com")
time.sleep(2)
driver.find_element(By.ID, "userPassword").send_keys("Harsha0507")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(5)