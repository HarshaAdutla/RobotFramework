# Here in this script I am going to keep all the variables and repeated keywords in another file which is Resources.
#I have created another directory for resources. To use that file we need to add the path of that file to this
# script in "Settings" section

*** Settings ***
Documentation    To validate the login form by passing the data through arguments
Resource         ./Resources/resource.robot
Test Teardown    Close Browser


*** Variables ***


*** Test Cases ***
Verify Unsuccessful Login
    Open browser and go to rahulsheety page
    Fill the login form        ${User_name}    ${Invalid_Password}
    Wait for the element to display    ${Error_Message}
    Validate the error message    ${Error_Message}

Verify Successful Login
    Open browser and go to rahulshetty page
    Fill the login form        ${User_name}    ${Valid_Password}
    Wait for the element to display    ${Home_Page}
    Validate the home page    ${Home_Page}
     
# Here in both test cases we are opening the browser and directing to rahulshetty page. So instead of writing the twice
# I am writing this test step in resources.
*** Keywords ***
# I have written the Open browser keyword in the resource so I am starting to fill the login form here.

# Here this keyword is also used twice for successful and Unsuccessful logins. So I am passing the username and 
# passwords as arguments to this test step.
Fill the login form
    [Arguments]    ${username}    ${password}
    Input Text        id:username    ${username}
    Input Password    id:password    ${password}
    Click Button      signIbBtn
# Here i have passed two arguments so I need to pass 2 arguments in the Testcases with required data.

Wait for the element to display
    [Arguments]    ${element}
    Wait Until Element is Visible    ${element}
    
Validate the error message
    [Arguments]    ${element}
    Element Text Should Be     ${element}     Incorrect username/password.
    
Validate the home page
    [Arguments]    ${element}
    Element Should Be Visible      ${element}    Home