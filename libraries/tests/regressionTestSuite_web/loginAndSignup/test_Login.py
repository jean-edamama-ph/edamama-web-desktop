import pytest
import allure

import libraries.data.common as dCommon
import libraries.data.regressionTestSuite.loginAndSignUp.login as dRegLogin

import libraries.util.appCommon.appComm as uAppComm
import libraries.util.common as uCommon


""" Author: cgrapa_20230523 Execution Time: 23s - 26s """
@pytest.mark.regressionTestSuite()
@allure.step('User is able to login in edamama website manually')
def test_AUTO_742_Verify_user_is_able_to_login_manually(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 to 3 - Click Login and enter credentials')
    uAppComm.ln.clickLoginAndFillDetails(page, dCommon.user.strUserName6, dCommon.user.strPassword1)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: cgrapa_20230523 Execution Time: 27s - 29s """
@pytest.mark.regressionTestSuite()
@allure.step('User is able to login in edamama through Google SSO')
def test_AUTO_746_Verify_user_is_able_to_login_using_Google_SSO(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 to 4 - Click Login >> Click Google Login >> Enter Gmail credentials')
    uAppComm.ln.loginAndFillViaSocial(page, dRegLogin.AUTO746.strGmail)
    uCommon.log(0, 'Test case completed')


""" Author: cgrapa_20230523 Execution Time: 27s - 29s """
@pytest.mark.regressionTestSuite()
@allure.step('User is able to login in edamama through Facebook SSO')
def test_AUTO_750_Verify_user_is_able_to_login_using_Facebook_SSO(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 to 4 - Click Login >> Click Facebook Login >> Enter Gmail credentials')
    uAppComm.ln.loginAndFillViaSocial(page, dRegLogin.AUTO750.strFb)
    uCommon.log(0, 'Test case completed')


""" Author: cgrapa_20230523 Execution Time: 21s - 24s """
@pytest.mark.regressionTestSuite()
@allure.step('User is is not able to login if the email field is empty')
def test_AUTO_758_Verify_that_user_is_not_able_to_login_if_the_email_field_is_empty(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 to 5 - Click Login >> Input password only >> Verify Field Error and Failed Login') 
    uAppComm.ln.validateLoginFormError(page, dRegLogin.AUTO758.strField)
    uCommon.log(0, 'Test Case Completed')


""" Author: cgrapa_20230523 Execution Time: 21s - 25s """
@pytest.mark.regressionTestSuite()
@allure.step('User is  is not able to login if the password field is empty')
def test_AUTO_761_Verify_that_user_is_not_able_to_login_if_the_password_field_is_empty(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 to 5 - Click Login >> Input email only >> Verify Field Error and Failed Login')
    uAppComm.ln.validateLoginFormError(page, dRegLogin.AUTO761.strField)
    uCommon.log(0, 'Test Case Completed')