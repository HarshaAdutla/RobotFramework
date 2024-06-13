# Here in this script I am writing code directly in single script which means providing all the variables directly
# in the test cases itself. In the Next script We will pass values through arguments.


*** Settings ***
Documentation        To validate the login form
Library              SeleniumLibrary
Test Teardown        Close Browser

*** Variables ***
${CHROME_DRIVER_PATH}    /Users/harsha/PycharmProjects/RobotFramework/RobotFramework/Drivers/chromedriver   # Update this to your actual path if not in PATH

*** Test Cases ***
Validate Unsuccessful Login
    Open the login page of rahulshetty practice page with url
    Fill the login form
    Wait for the error message to display
    Verify the error message

*** Keywords ***
Open the login page of rahulshetty practice page with url
    Open Browser    https://rahulshettyacademy.com/loginpagePractise/    chrome     ${CHROME_DRIVER_PATH}
    Maximize Browser Window
   
Fill the login form       
    Input Text            id:username        rahulshettyacademy
    Input Password        id:password        1234567
    Click Button            signInBtn
    
Wait for the error message to display
    Wait Until Element Is Visible        css:.alert-danger
    
Verify the error message 
    Element Text Should Be        css:.alert-danger        Incorrect username/password.