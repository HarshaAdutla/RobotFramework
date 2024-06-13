*** Settings ***
Documentation        To validate the Login Form
Library              SeleniumLibrary
Resource             resource.robot
Test Teardown        Close Browser Session


*** Variables ***
${CHROME_DRIVER_PATH}    /Users/harsha/Downloads/chromedriver-mac-arm64   # Update this to your actual path if not in PATH
${Error_Message_Login}    css:.alert-danger

*** Test Cases ***
Validate UnSuccessful Login
    open the login page with rahulsheety login practise page with url
    Fill the login form
    wait until it checks and display error message
    verify error message is correct

*** Keywords ***
Fill the login form
    Input Text        id:username    ${user_name}
    Input Password    id:password    ${invalid_password}
    Click Button      id:signInBtn

wait until it checks and display error message
    Wait Until Element Is Visible         ${Error_Message_Login}

verify error message is correct
#    ${result}=    Get Text    ${Error_Message_Login}
#    Sleep    2s
#    Should Be Equal As Strings    ${result}    Incorrect username/password.
#    Sleep     3s
    Element Text Should Be    ${Error_Message_Login}    Incorrect username/password.

    