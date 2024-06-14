# In the last script we have extracted items and compared two list.
# Here in this script we are going to select one product from the shop home page

*** Settings ***
Documentation       Here we are extracting items names and comparing them with expected items names
Library             SeleniumLibrary
Library             Collections
Resource            ../Resources/resource2.robot



*** Variables ***


*** Test Cases ***
Verify all the items in the shop home page
    Open browser and go to rahulsheety page
    Fill the login form        ${User_name}      ${Valid_Password}
    Wait for the page to load    ${Home_Page}
    Verify the items in the shop
    Add Item to Cart        Blackberry


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
    @{actual_List} =     Create List
    FOR    ${element}     IN    @{elements}
        Log    ${element.text}
        Append To List     ${actual_List}     ${element.text}
    END

    Lists Should Be Equal     ${expected_List}     ${actual_List}


Add Item to Cart
    [Arguments]    ${cardName}
    ${elements} =     Get WebElements        css:.card-title
    ${index} =     Set Variable    1
    FOR    ${element}    IN    @{elements}
        Exit For Loop If    '${cardName}' == '${element.text}'
        ${index} =     Evaluate    ${index} + 1
    END
    Click Button        (//*[@class='card-footer'])[${index}]/button
    Sleep     4s

# In next Script I am going to create another Test case to click on radio buttons and handling dropdowns and alerts.