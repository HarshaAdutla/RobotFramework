# Here in this script I am going to verify the cards present in the shop

*** Settings ***
Documentation        Verifying all the available items in the shop
Library              SeleniumLibrary
Library              Collections
Library              BuiltIn


*** Variables ***
${Chrome_Driver_Path}       /Users/harsha/PycharmProjects/RobotFramework/RobotFramework/Drivers/chromedriver
${URL}                      https://rahulshettyacademy.com/loginpagePractise/
${User_name}                rahulshettyacademy
${Valid_Password}           learning
${Home_Page}                css:.nav-link




#Test Demo4:-


#*** Test Cases ***
#Verify all the items in the shop home page
#    Open browser and go to rahulsheety page
#    Fill the login form        ${User_name}      ${Valid_Password}
#    Wait for the page to load    ${Home_Page}
#    Verify the items in the shop
#
#
#
#*** Keywords ***
#Open browser and go to rahulsheety page
#    Open Browser        ${URL}        chrome        ${Chrome_Driver_Path}
#    Maximize Browser Window
#
#Fill the login form
#    [Arguments]    ${username}    ${password}
#    Input Text        id:username    ${username}
#    Input Password    id:password    ${password}
#    Click Button    signInBtn
#
#Wait for the page to load
#    [Arguments]    ${element}
#    Wait Until Element Is Visible     ${element}
#
#Verify the items in the shop
#    @{expected_List} =     Create List    iphone X    Samsung Note 8    Nokia Edge    Blackberry
#    ${elements} =     Get WebElements        css:.card-title
#    @{actual_List} =     Create List
#    FOR    ${element}     IN    @{elements}
#        Log    ${element.text}
#        Append To List     ${actual_List}     ${element.text}
#    END
#
#    Lists Should Be Equal      ${expected_List}     ${actual_List}


#TextDemo5:-


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
    Log List    ${actual_List}        # This will write all items in normal formate(1,2,3,..)
#    Log    The contents of list2 are: @{actual_List}    #This will write all items in List format


Add Item to Cart
    [Arguments]    ${cardName}
    ${elements} =     Get WebElements        css:.card-title
    ${index} =     Set Variable    1
    FOR    ${element}    IN    @{elements}
        Log    ${element.text}
        Exit For Loop If    '${cardName}' == '${element.text}'
        ${index} =     Evaluate    ${index} + 1
    END
    Click Button        (//*[@class='card-footer'])[${index}]/button
    Sleep    4s
