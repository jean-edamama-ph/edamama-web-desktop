import pytest
import allure

import libraries.util.appCommon.appComm as uAppComm
import libraries.util.common as uCommon
import libraries.util.appCommon.adminKpc as uAdminKpc
import libraries.data.common as dCommon
import libraries.data.regressionTestSuite.adminPanel.adminPanel as dAdmin
import libraries.util.profile.myProfile as uMyProfile
import libraries.util.profile.myBeans as uMyBeans
import libraries.util.cart as uCart
import libraries.util.checkOut as uCheckOut

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
    uAdminKpc.re.clickRewardsModule(page)
    uCommon.log(0, 'Test Completed')
    
    
""" Author: abernal_20240318 Execution Time: 41s - 43s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that user is able to manually credit rewards via editing Total Rewards.')
@allure.step('To verify that Credited rewards and credits should show on Beans History.')
#test_ACQ_AUTO_1791_Credited_rewards_and_credits_should_show_on_Beans_History
def test_ACQ_AUTO_1785_User_should_be_able_to_manually_credit_rewards_via_editing_Total_Rewards(page):
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, 'Step 2 - Search for a user and click the First Name')
    uAdminKpc.cu.searchCustomer(page, dCommon.user.strUserName)
    newWindow = uCommon.switchToWindow(page)
    
    uCommon.log(0, '[AUTO-1785 Started]: Update the value of the total credit field.')
    uCommon.log(0, 'Step 3 - Click the pen on the Total Rewards field and adjust the value.')
    uAdminKpc.cu.editTotalRewardsValue(newWindow, dAdmin.AUTO1785.strRewards)
    uCommon.log(0, '[AUTO-1785 Completed]: Updated the value of the total credit field.')
    
    uCommon.log(0, '[AUTO-1791 Started]: Check if reward is shown on Beans History page.')
    uCommon.log(0, 'Step 4 - Verify on My Beans page if rewards was credited to account.')
    uAppComm.ln.loginToEdamama(newWindow, dCommon.user.strUserName)
    uAppComm.com.navigateToProfileMenu(newWindow, 'my profile')
    uMyProfile.com.clickMyBeansTab(newWindow)
    uMyBeans.com.verifyOnEdamamaRewards(newWindow, dAdmin.AUTO1785.strRewards)
    uCommon.log(0, '[AUTO-1791 Completed]: Checked if reward is shown on Beans History page.')
    uCommon.log(0, 'Test Completed')
    

""" Author: abernal_20240318 Execution Time: 41s - 42s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that user is able to manually credit credits via editing Total Rewards.')
@allure.step('To verify that Credited rewards and credits should show on Beans History.')
#test_ACQ_AUTO_1791_Credited_rewards_and_credits_should_show_on_Beans_History
def test_ACQ_AUTO_1788_User_should_be_able_to_manually_credit_Credit_via_editing_Total_Credits(page):
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, 'Step 2 - Search for a user and click the First Name')
    uAdminKpc.cu.searchCustomer(page, dCommon.user.strUserName)
    newWindow = uCommon.switchToWindow(page)
    
    uCommon.log(0, '[AUTO-1788 Started]: Update the value of the total credit field.')
    uCommon.log(0, 'Step 3 - Click the pen on the Total Credit field and adjust the value.')
    uAdminKpc.cu.editTotalCreditsValue(newWindow, dAdmin.AUTO1788.strCredits)
    uCommon.log(0, '[AUTO-1788 Completed]: Updated the value of the total credit field.')
    
    uCommon.log(0, '[AUTO-1791 Started]: Check if reward is shown on Beans History page.')
    uCommon.log(0, 'Step 4 - Verify on My Beans page if credits was credited to account.')
    uAppComm.ln.loginToEdamama(newWindow, dCommon.user.strUserName)
    uAppComm.com.navigateToProfileMenu(newWindow, 'my profile')
    uMyProfile.com.clickMyBeansTab(newWindow)
    uMyBeans.com.verifyOnEdamamaCredits(newWindow, dAdmin.AUTO1788.strCredits)
    uCommon.log(0, '[AUTO-1791 Completed]: Checked if reward is shown on Beans History page.')
    uCommon.log(0, 'Test Completed')


""" Author: abernal_20240318 Execution Time: 25s - 27s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that error message is encountered when user deducts more than the beans available in the users credits or rewards via customers details page.')
def test_ACQ_AUTO_1803_Error_message_is_encountered_when_user_deducts_more_than_the_beans_available_in_the_users_credits_or_rewards(page):
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, 'Step 2 - Search for a user and click the First Name')
    uAdminKpc.cu.searchCustomer(page, dCommon.user.strUserName)
    newWindow = uCommon.switchToWindow(page)
    
    uCommon.log(0, '[Pre-condition Started]: Get the total rewards and credits available from the user.')
    strOldTotalRewards = uAdminKpc.cu.getTotalRewardsValue(newWindow, strTotalRewards = "")
    strOldTotalCredits = uAdminKpc.cu.getTotalCreditsValue(newWindow, strTotalCredits = "")
    uCommon.log(0, '[Pre-condition Completed]: Get the total rewards and credits available from the user.')
    
    uCommon.log(0, 'Step 3 - Edit the value wherein the amount to be deducted is more than the amount of balance on the users credits/rewards.')
    uAdminKpc.cu.deductMoreThanTotalRewardCreditValue(newWindow, strOldTotalRewards, strType = "Rewards")
    uAdminKpc.cu.deductMoreThanTotalRewardCreditValue(newWindow, strOldTotalCredits, strType = "Credits")
    
    uCommon.log(0, '[Post-condition Started]: Return the deducted amount of rewards/credits.')
    uAdminKpc.cu.editTotalRewardsValue(newWindow, strOldTotalRewards)
    uAdminKpc.cu.editTotalCreditsValue(newWindow, strOldTotalCredits)
    uCommon.log(0, '[Post-condition Completed]: Returned the deducted amount of rewards/credits.')
    uCommon.log(0, 'Test Completed')


""" Author: abernal_20240416 Execution Time: 54s - 57s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that manually credited rewards and credits should reflect as expected on checkout page')
def test_ACQ_AUTO_1812_Manually_credited_rewards_and_credits_should_reflect_as_expected_on_checkout_page(page):
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, 'Step 2 - Search for a user and click the First Name')
    uAdminKpc.cu.searchCustomer(page, dCommon.user.strUserName)
    newWindow = uCommon.switchToWindow(page)
    
    uCommon.log(0, 'Step 3 - Click the pen on the Total Credit field and Total Rewards field and adjust the value.')
    uAdminKpc.cu.addTotalRewardCreditValue(newWindow, dAdmin.AUTO1812.strRewards, strType = "Rewards")
    uAdminKpc.cu.addTotalRewardCreditValue(newWindow, dAdmin.AUTO1812.strCredits, strType = "Credits")
    strTotalRewards = uAdminKpc.cu.getTotalRewardsValue(newWindow, strTotalRewards = "")
    strTotalCredits = uAdminKpc.cu.getTotalCreditsValue(newWindow, strTotalCredits = "")
    
    uCommon.log(0, 'Step 4 - Navigate to edamama site > My Cart > Proceed to checkout. Verify the amount on Total Rewards and Total Credit is the same as the value on checkout.')
    uAppComm.ln.loginToEdamama(newWindow, dCommon.user.strUserName)
    uCheckOut.checkOutItem(newWindow, dAdmin.AUTO1812.dictData['strItemName'], dAdmin.AUTO1812.dictData["strType"])
    uCheckOut.validateTotalRewardsAndCredit(newWindow, strTotalRewards, strTotalCredits)
    uCommon.log(0, 'Test Completed')
    

""" Author: abernal_20240416 Execution Time: 15s - 16s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that Activity Logs should be displayed below on the Customer Module page')
def test_ACQ_AUTO_1991_Activity_Logs_should_be_displayed_below_on_the_Customer_Module_page(page):
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, 'Step 2 - Verify the Activity Logs below the Customer module.')
    uAdminKpc.cu.validateActivityLogs(page)
    uCommon.log(0, 'Test Completed')
    

""" Author: abernal_20240417 Execution Time: 47s - 53s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that Activity log should updated when user manually credit rewards via editing Total Rewards.')
@allure.step('To verify that Activity log should updated when user manually credit rewards via editing Total Credits.')
#test_ACQ_AUTO_2023_Activity_log_should_be_updated_when_user_manually_credit_rewards_via_editing_Total_Credits
def test_ACQ_AUTO_2019_Activity_log_should_be_updated_when_user_manually_credit_rewards_via_editing_Total_Rewards(page):
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, 'Step 2 - Search for a user and click the First Name.')
    uAdminKpc.cu.searchCustomer(page, dCommon.user.strUserName)
    newWindow = uCommon.switchToWindow(page)
    
    uCommon.log(0, '[AUTO-2019 and AUTO-2023 Started]: Step 3 - Click the pen on the Total Rewards and Credits field and adjust the value.')
    uAdminKpc.cu.addTotalRewardCreditValue(newWindow, dAdmin.AUTO2019.strRewards, strType = "Rewards")
    uAdminKpc.cu.addTotalRewardCreditValue(newWindow, dAdmin.AUTO2019.strCredits, strType = "Credits")
    uCommon.closeWindow(newWindow)
    uCommon.reloadPage(page)
    
    uCommon.log(0, 'Step 4 - Navigate back to Customers module and verify if the activity was recorded on Bean Rewards tab.')
    uAdminKpc.cu.verifyAddedBeansActivityLog(page, dAdmin.AUTO2019.strRewards, dCommon.user.strUserName)
    uAdminKpc.cu.verifyAddedCreditsActivityLog(page, dAdmin.AUTO2019.strCredits, dCommon.user.strUserName)
    
    uCommon.log(0, '[Post-condition Started]: Deduct the added amount of rewards/credits.')
    uAdminKpc.cu.searchCustomer(page, dCommon.user.strUserName)
    newWindow = uCommon.switchToWindow(page)
    uAdminKpc.cu.deductRewardCreditValue(newWindow, dAdmin.AUTO2019.strRewards, strType = "Rewards")
    uAdminKpc.cu.deductRewardCreditValue(newWindow, dAdmin.AUTO2019.strCredits, strType = "Credits")
    uCommon.log(0, '[Post-condition Completed]: Deducted the added amount of rewards/credits.')
    uCommon.log(0, 'Test Completed')