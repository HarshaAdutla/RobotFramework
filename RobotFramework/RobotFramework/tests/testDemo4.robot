# In the last script we just printed(logged) the names of the items. In this script we are extracting the names and
# comparing them with the expected list items names.
# All the variables and Test cases are same as last script just added some logics in this script

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



# Here we have created a list to store the expected items.
# Now we need to create one more list to store the items which we got from the for loop(from web elements)
# Now after creating a new list we need to append the item names to that list which we extracted from the for loop
#  To do that we used "Append To List" keyword, this is not coming from selenium library or RobotFramework it is from 
# "Collections" library so we need to import this library as we did for selenium in "Settings" section.

# To compare two list we need to use "List Should Be Equal" keyword it is also from collections.

Note:-
#    If we observe while creating a list I have used " @ " but when I am using it I have used " $ " which means that
#    we should use " @ " only while creating a new list once we created we treat it as a list of variables so we should
#    use " $ ".

#    Create List               -> Built In
#    Append To List            -> Collections
#    Lists Should Be Equal     -> Collections

List Should Be Equal is writing the False. -> Need to check