*** Settings ***
Documentation        A Resource file with reusable keywords and variables
...                  Writing multiple line of documentation.

Library        SeleniumLibrary

*** Variables ***
${user_name}            rahulshetty
${invalid_password}     1234567
${valid_password}       learning
${Error_Message_Login}    css:.alert-danger
#${error_message}        css:.alert-danger
${Shop_home_page}       css:.nav-link
${url}              https://rahulshettyacademy.com/loginpagePractise/
${CHROME_DRIVER_PATH}    /Users/harsha/Downloads/chromedriver-mac-arm64

*** Keywords ***
open the login page with rahulsheety login practise page with url
    Open Browser    ${url}    chrome    ${CHROME_DRIVER_PATH}
#    Create Webdriver    Chrome executable_path=/Users/harsha/PycharmProjects/RobotFramework/pythonProject/drivers/chromedriver
#    Go To    https://rahulshettyacademy.com/loginpagePractise/
    Maximize Browser Window
#    Sleep    3s

Close Browser Session
    Close Browser