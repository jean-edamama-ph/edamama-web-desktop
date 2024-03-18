import pytest
import allure

import libraries.util.appCommon.appComm as uAppComm
import libraries.util.common as uCommon
import libraries.util.appCommon.adminKpc as uAdminKpc
import libraries.data.common as dCommon
import libraries.data.regressionTestSuite.adminPanel.adminPanel as dAdmin
import libraries.util.profile.myProfile as uMyProfile
import libraries.util.profile.myBeans as uMyBeans

""" Author: abernal_20240318 Execution Time: 15s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that Upload Rewards or Credit button is displayed on the Customers page in AP.')
def test_ACQ_AUTO_1758_Upload_Rewards_or_Credit_button_should_be_displayed_on_the_Customers_page_in_AP(page):
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, 'Step 2 - Verify that Upload Rewards or Credit button is displayed beside the Upload User Tags.')
    uAdminKpc.cu.verifyUploadRewardsOrCreditButton(page)
    uCommon.log(0, 'Test Completed')
    
""" Author: abernal_20240318 Execution Time: 19s - 23s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that Total Rewards and Total Credit fields are displayed on the customers details page.')
def test_ACQ_AUTO_1764_Total_Rewards_and_Total_Credit_fields_should_be_displayed_on_the_customers_details_page(page):
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, 'Step 2 - Search for a user and click the First Name')
    uAdminKpc.cu.searchCustomer(page, dCommon.user.strUserName)
    newWindow = uCommon.switchToWindow(page)
    
    uCommon.log(0, 'Step 3 - Verify if Total Rewards and Total Credits fields are displayed.')
    uAdminKpc.cu.verifyTotalCreditAndRewardFields(newWindow)
    uCommon.log(0, 'Test Completed')
    

""" Author: abernal_20240318 Execution Time: 14s - 15s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that Credits module is updated to Rewards module.')
def test_ACQ_AUTO_1767_Credits_module_should_be_updated_to_Rewards_module(page):
    uCommon.log(0, 'Step 1 - Login to Admin Panel.')
    uAppComm.ln.loginToAdminKPC(page)
    
    uCommon.log(0, 'Step 2 - Verify that credits module is updated to Rewards module.')
    uAdminKpc.rm.clickRewardsModule(page)
    uCommon.log(0, 'Test Completed')
    
    
""" Author: abernal_20240318 Execution Time: 41s - 43s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that user is able to manually credit rewards via editing Total Rewards.')
def test_ACQ_AUTO_1785_User_should_be_able_to_manually_credit_rewards_via_editing_Total_Rewards(page):
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, 'Step 2 - Search for a user and click the First Name')
    uAdminKpc.cu.searchCustomer(page, dCommon.user.strUserName)
    newWindow = uCommon.switchToWindow(page)
    
    uCommon.log(0, 'Step 3 - Click the pen on the Total Rewards field and adjust the value.')
    uAdminKpc.cu.editTotalRewardsValue(newWindow, dAdmin.AUTO1785.strRewards)
    
    uCommon.log(0, 'Step 4 - Verify on My Beans page if rewards was credited to account.')
    uAppComm.ln.loginToEdamama(newWindow, dCommon.user.strUserName)
    uAppComm.com.navigateToProfileMenu(newWindow, 'my profile')
    uMyProfile.com.clickMyBeansTab(newWindow)
    uMyBeans.com.verifyOnEdamamaRewards(newWindow, dAdmin.AUTO1785.strRewards)
    uCommon.log(0, 'Test Completed')
    

""" Author: abernal_20240318 Execution Time: 41s - 42s """
@pytest.mark.netTest()
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that user is able to manually credit credits via editing Total Rewards.')
def test_ACQ_AUTO_1788_User_should_be_able_to_manually_credit_Credit_via_editing_Total_Credits(page):
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, 'Step 2 - Search for a user and click the First Name')
    uAdminKpc.cu.searchCustomer(page, dCommon.user.strUserName)
    newWindow = uCommon.switchToWindow(page)
    
    uCommon.log(0, 'Step 3 - Click the pen on the Total Credit field and adjust the value.')
    uAdminKpc.cu.editTotalCreditsValue(newWindow, dAdmin.AUTO1788.strCredits)
    
    uCommon.log(0, 'Step 4 - Verify on My Beans page if credits was credited to account.')
    uAppComm.ln.loginToEdamama(newWindow, dCommon.user.strUserName)
    uAppComm.com.navigateToProfileMenu(newWindow, 'my profile')
    uMyProfile.com.clickMyBeansTab(newWindow)
    uMyBeans.com.verifyOnEdamamaCredits(newWindow, dAdmin.AUTO1788.strCredits)
    uCommon.log(0, 'Test Completed')
