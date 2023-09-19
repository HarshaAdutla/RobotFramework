
# Invoking different browsers

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service

# Chrom driver - Chrome browser

service_obj = Service()  # It will automatically download the suitable version and starts the execution
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com")
time.sleep(5)



# Firefox driver - Firefox browser

# firefox_obj = Service()  # It will automatically download the suitable version and starts the execution
# driver = webdriver.Firefox(service=firefox_obj)
# driver.get("https://rahulshettyacademy.com")
# time.sleep(5)



# Edge driver - Edge browser

# edge_obj = Service()  # It will automatically download the suitable version and starts the execution
# driver = webdriver.Edge(service=edge_obj)
# driver.get("https://rahulshettyacademy.com")
# time.sleep(5)



""" If we want to download drivers and use it then we can follow the below steps"""
# -> Chrome driver
# service_obj = Service("/Users/harsha/Web Drivers/chromedriver/chromedriver")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://rahulshettyacademy.com")      -> An example URL to redirect

# -> Firefox driver
# service_obj = Service("/Users/harsha/Web Drivers/geckodriver/geckodriver")
# driver = webdriver.Firefox(service=service_obj)

# -> Edge driver
# service_obj = Service("/Users/harsha/Web Drivers/msedgedriver/msedgedriver")s
# driver = webdriver.Edge(service=service_obj)

"""
A Service class that is responsible for starting and stopping the chromedriver
"""