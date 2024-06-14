# Here in this script I am going to verify the cards present in the shop

*** Settings ***
Documentation        Verifying all the available items in the shop
Library              SeleniumLibrary
Resource             ../Resources/resource2.robot

*** Variables ***


*** Test Cases ***
Verify all the items in the shop home page
    Open browser and go to rahulsheety page
    Fill the login form        ${User_name}      ${Valid_Password}
    Wait for the page to load    ${Home_Page}
    Verify the items in the shop




*** Keywords ***
Open browser and go to rahulsheety page
    Open Browser        ${URL}        chrome        ${Chrome_Driver_Path}
    Maximize Browser Window

Fill the login form
    [Arguments]    ${username}    ${password}
    Input Text        id:username    ${username}
    Input Password    id:password    ${password}
    Click Button    signInBtn
    
Wait for the page to load
    [Arguments]    ${element}
    Wait Until Element Is Visible     ${element}

Verify the items in the shop
    @{expected_List} =     Create List    iphone X    Samsung Note 8    Nokia Edge    Blackberry
    ${elements} =     Get WebElements        css:.card-title
    FOR    ${element}     IN    @{elements}
        Log    ${element.text}
    END

# Here in this script I have just printed the items names in the log using for loop in the next script we will verify
# all the items
