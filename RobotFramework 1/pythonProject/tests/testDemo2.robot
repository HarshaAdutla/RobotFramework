*** Settings ***
Documentation    To validate the Login Form
Resource         resource.robot
#Test Teardown    Close Browser Session


*** Variables ***
${user_name}            rahulshettyacademy
${invalid_password}     1234567
${valid_password}       learning
#${error_message}        css:.alert-danger
${Error_Message_Login}    css:.alert-danger
${Shop_home_page}       css:.nav-link

*** Test Cases ***
validate Unsuccessful Login
    open the login page with rahulsheety login practise page with url
#    Set Selenium Speed    1s
    Fill the login form    ${user_name}    ${invalid_password}
    wait until element is displayed on the page      ${Error_Message_Login}
    verify error message is correct        ${Error_Message_Login}


Validate Successful Login
    open the login page with rahulsheety login practise page with url
    Fill the login form    ${user_name}    ${valid_password}
    wait until element is visible        ${Shop_home_page}


*** Keywords ***

Fill the login form
    [Arguments]    ${user_name}    ${password}
    Input Text        id:username    ${user_name}
    Input Text        id:password    ${password}
    Click Button       id:signInBtn
    
wait until element is displayed on the page
    [Arguments]    ${element}
    Wait Until Element Is Visible        ${element}
    
verify error message is correct
    [Arguments]    ${error_message}
    Element Text Should Be     ${error_message}       Incorrect username/password.