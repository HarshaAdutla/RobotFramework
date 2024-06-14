# In resource file also we can have all the Four section ( Settings, Variables, Test Cases, Keywords)

*** Settings ***
Documentation        A Resource file with reusable keywords and variables
Library              SeleniumLibrary

*** Variables ***
${Chrome_Driver_Path}       /Users/harsha/PycharmProjects/RobotFramework/RobotFramework/Drivers/chromedriver
${URL}                      https://rahulshettyacademy.com/loginpagePractise/
${User_name}                rahulshettyacademy
${Invalid_Password}         12345678
${Valid_Password}           learning
${Error_Message}            .alert_danger
${Home_Page}                .nav-link
#*** Test Cases ***


*** Keywords ***
Open browser and go to rahulsheety page
    Open Browser        ${URL}        chrome        ${Chrome_Driver_Path}
    Maximize Browser Window