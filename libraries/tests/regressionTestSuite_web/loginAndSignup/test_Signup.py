import pytest
import allure

import libraries.data.common as dCommon
import libraries.data.regressionTestSuite.loginAndSignUp.signup as dRegSignUp

import libraries.util.appCommon.appComm as uAppComm
import libraries.util.appCommon.signUp as uSignUp
import libraries.util.appCommon.email as uEmail
import libraries.util.common as uCommon

""" Author: cgrapa_20230604 Execution Time: 51s - 57s """
@pytest.mark.regressionTestSuite()
@allure.step('User is able to sign up manually')
def test_AUTO_834_Verify_that_user_is_able_to_sign_up_using_valid_email_and_password(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - Click Signup button on header')
    uSignUp.clickSignUp(page)
    uSignUp.validateSignUpPage(page)
    
    uCommon.log(0, 'Step 3 to 5 - Populate all required fields >> Click policy checkbox >> Click Continue button')
    arrData = uSignUp.fillandContinueSignUpPage(page, dCommon.signUp.dictData)
    uSignUp.validateAndClickOKinAccountVerification(page)
    
    uCommon.log(0, 'Step 6 to 7 - Navigate to Email >> Verify email address')
    uEmail.loginToGmail(page)
    uEmail.clickFirstConfirmEmail(page, arrData)
    uEmail.clickYesThisIsMyEmail(page)
    newWindow = uCommon.switchToWindow(page)
    uSignUp.validateEmailVerificationPageAndClickCompleteMyProfile(newWindow)
    uCommon.log(0, 'Test case completed')
    

""" Author: cgrapa_20230606 Execution Time: 27s - 29s """
@pytest.mark.regressionTestSuite()
@allure.step('User is unable to create an account with invalid values on required fields')
def test_AUTO_858_Verify_that_user_is_unable_to_create_an_account_with_invalid_values_on_required_fields(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - Click Signup button on header')
    uSignUp.clickSignUp(page)
    uSignUp.validateSignUpPage(page)
    
    uCommon.log(0, 'Step 3.1 - Leave all required fields blank')
    uSignUp.clickSignUpContinue(page)
    arrObj = vars(dRegSignUp.AUTO858)
    for item, value in arrObj.items():
        if item.endswith('Msg'):
            uAppComm.error.validatePopUpMsg(page, value)

    uCommon.log(0, 'Step 3.2 - Input invalid email and password')
    uSignUp.fillOutSignUpPage(page, dRegSignUp.AUTO858.dictData)
    for item, value in arrObj.items():
        if item.endswith('Invalid'):
            uAppComm.error.validatePopUpMsg(page, value)

    uCommon.log(0, 'Step 3.3 - Leave Accept Privacy Policy unchecked')
    uSignUp.fillOutSignUpPage(page, dRegSignUp.AUTO858.dictData2)
    uSignUp.clickSignUpContinue(page)
    uAppComm.error.validatePopUpMsg(page, dRegSignUp.AUTO858.strPrivacyPolicy)
    uSignUp.validateSignUpPage(page)
    uCommon.log(0, 'Test case completed')


""" Author: cgrapa_20230606 Execution Time: 25s - 28s """
@pytest.mark.regressionTestSuite()
@allure.step('Privacy Policy or Terms of Use is visible')
def test_AUTO_861_Verify_that_Privacy_Policy_or_Terms_of_Use_is_opening_in_their_corresponding_pages(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - Click Signup button on header')
    uSignUp.clickSignUp(page)
    uSignUp.validateSignUpPage(page)
    
    uCommon.log(0, 'Step 3 - Click Privacy Policy or Terms of Use')
    uSignUp.validatePolicyLinks(page)
    uCommon.log(0, 'Test case completed')


""" Author: cgrapa_20230606 Execution Time: 21s - 24s """
@pytest.mark.regressionTestSuite()
@allure.step('To verify that an error message is displayed when Email Field is empty.')
def test_AUTO_830_Error_message_should_be_displayed_when_Email_Field_is_empty(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - Click Signup button on header')
    uSignUp.clickSignUp(page)
    uSignUp.validateSignUpPage(page)
    
    uCommon.log(0, 'Step 3 - Populate fields except Email Address')
    uSignUp.fillOutSignUpPage(page, dRegSignUp.AUTO830.dictData)
    uAppComm.error.validatePopUpMsg(page, dRegSignUp.AUTO830.strMsg)
    uCommon.log(0, 'Test case completed')


""" Author: cgrapa_20230606 Execution Time: 22s - 29s """
@pytest.mark.regressionTestSuite()
@allure.step('To verify that an error message is displayed when First Name is empty.')
def test_AUTO_831_Error_message_should_be_displayed_when_First_Name_is_empty(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - Click Signup button on header')
    uSignUp.clickSignUp(page)
    uSignUp.validateSignUpPage(page)
    
    uCommon.log(0, 'Step 3 - Populate fields except First Name')
    uSignUp.fillOutSignUpPage(page, dRegSignUp.AUTO831.dictData)
    uAppComm.error.validatePopUpMsg(page, dRegSignUp.AUTO831.strMsg)
    uCommon.log(0, 'Test case completed')


""" Author: cgrapa_20230606 Execution Time: 23s - 31s """
@pytest.mark.regressionTestSuite()
@allure.step('To verify that an error message is displayed when Last Name is empty.')
def test_AUTO_832_Error_message_should_be_displayed_when_Last_Name_is_empty(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - Click Signup button on header')
    uSignUp.clickSignUp(page)
    uSignUp.validateSignUpPage(page)
    
    uCommon.log(0, 'Step 3 - Populate fields except Last Name')
    uSignUp.fillOutSignUpPage(page, dRegSignUp.AUTO832.dictData)
    uAppComm.error.validatePopUpMsg(page, dRegSignUp.AUTO832.strMsg)
    uCommon.log(0, 'Test case completed')


""" Author: cgrapa_20230606 Execution Time: 21s - 23s """
@pytest.mark.regressionTestSuite()
@allure.step('To verify that an error message is displayed when Password is empty.')
def test_AUTO_833_Error_message_should_be_displayed_when_Password_is_empty(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - Click Signup button on header')
    uSignUp.clickSignUp(page)
    uSignUp.validateSignUpPage(page)
    
    uCommon.log(0, 'Step 3 - Populate fields except Password')
    uSignUp.fillOutSignUpPage(page, dRegSignUp.AUTO833.dictData)
    uAppComm.error.validatePopUpMsg(page, dRegSignUp.AUTO833.strMsg)
    uCommon.log(0, 'Test case completed')