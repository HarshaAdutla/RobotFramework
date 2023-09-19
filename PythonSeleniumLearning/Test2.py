
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()  # It will automatically download the suitable version and starts the execution
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice")
time.sleep(2)
print(driver.title)
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Harsha")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("test@gmail.com")
time.sleep(2)
driver.find_element(By.ID, "exampleInputPassword1").send_keys("No Password")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
time.sleep(2)
# driver.find_element(By.ID, "exampleFormControlSelect1").click()
# time.sleep(4)
driver.execute_script("window.scrollTo(500,500)")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(4)
Message = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success!" in Message
print(Message)


driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Nothing")
time.sleep(4)
driver.execute_script("window.scrollTo(0,0)")
time.sleep(5)
with open("message.png", 'wb') as file:
    image = driver.find_element(By.CLASS_NAME, "alert-success").screenshot_as_png
    file.write(image)
print("Screenshot taken")









"""
-> Constructing an XPATH & CSS_Selectors for webelements:
HTML element : <input class="btn btn-success" type="submit" value="Submit">
               //tagname[@attribute = "attribute value"]   -> XPATH
               tagname[attribute = "attribute value"]      -> CSSSelector
               
               
-> For an ID we can write CSS also by giving # in front of the the id.
HTML element: <input class="form-control" id="exampleInputPassword1" placeholder="Password" type="password" xpath="1">
    CSS using id : #exampleInputPassword1
    

-> CSS Selector can be constructed by using any attribute in the class name.
HTML element : <div class="alert alert-success alert-dismissible" xpath="1"></div>
    CSS : .alert-success

"""