
# Handling Dynamic dropdowns
"""
To handle static dropdowns we need to import Select package from selenium.
If a dropdown has Select tag name then it must be a static dropdown.
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service()  # It will automatically download the suitable version and starts the execution
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice")

print(driver.title)
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Harsha")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("test@gmail.com")
time.sleep(2)
driver.find_element(By.ID, "exampleInputPassword1").send_keys("No Password")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
time.sleep(2)
driver.execute_script("window.scrollTo(200,200)")
time.sleep(3)

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))  # Using Select class
time.sleep(3)
dropdown.select_by_index(1)
time.sleep(3)
dropdown.select_by_visible_text("Male")
time.sleep(4)