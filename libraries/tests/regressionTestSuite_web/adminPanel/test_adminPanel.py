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
    

""" Author: abernal_20240417 Execution Time: 39s - 42s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that User should be able to do manual adjustment on AP via the Upload Rewards or Credit button and uploading csv')
def test_ACQ_AUTO_1761_User_should_be_able_to_do_manual_adjustment_on_AP_via_the_Upload_Rewards_or_Credit_button_and_uploading_csv(page): 
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, '[Pre-condition Started]: Get the current total rewards and credits of the users.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1761.dictData['strUser1'])
    newWindow = uCommon.switchToWindow(page)
    strOldTotalRewards = uAdminKpc.cu.getTotalRewardsValue(newWindow, strTotalRewards = '')
    strOldTotalCredits = uAdminKpc.cu.getTotalCreditsValue(newWindow, strTotalCredits = '')
    uCommon.closeWindow(newWindow)
    uCommon.log(0, '[Pre-condition Completed]: Get the current total rewards and credits of the users.')
    
    uCommon.log(0, 'Step 2 - Click the Upload Rewards or Credit button. Upload the file.')
    uAdminKpc.cu.uploadUserCreditsOrRewards(page, dAdmin.AUTO1761.strPath)
    
    uCommon.log(0, 'Step 3 - Search for an email from the list in the CSV file. Click the First Name and verify if the amount on the CSV file was credited.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1761.dictData['strUser1'])
    newWindow = uCommon.switchToWindow(page)
    uAdminKpc.cu.validateRewardsCreditsAddedFromUpload(newWindow, strOldTotalRewards, strOldTotalCredits, dAdmin.AUTO1761.rewardCredits)
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
    
""" Author: abernal_20240418 Execution Time: 36s - 39s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that Error message should be displayed when same balance for credit are credited to a user ID within 5 minutes of uploading a CSV file')
def test_ACQ_AUTO_1770_Error_message_should_be_displayed_when_same_balance_for_credit_are_credited_to_a_user_ID_within_5_minutes_of_uploading_a_CSV_file(page): 
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, '[Pre-condition Started]: Get the current total rewards and credits of the users.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1770.dictData['strUser1'])
    newWindow = uCommon.switchToWindow(page)
    strOldTotalRewards = uAdminKpc.cu.getTotalRewardsValue(newWindow, strTotalRewards = '')
    strOldTotalCredits = uAdminKpc.cu.getTotalCreditsValue(newWindow, strTotalCredits = '')
    uCommon.closeWindow(newWindow)
    uCommon.log(0, '[Pre-condition Completed]: Get the current total rewards and credits of the users.')
    
    uCommon.log(0, 'Step 2 - Click the Upload Rewards or Credit button. Upload the file.')
    uAdminKpc.cu.uploadUserCreditsOrRewards(page, dAdmin.AUTO1770.strPath)
    
    uCommon.log(0, 'Step 3 - Search for an email from the list in the CSV file. Click the First Name and verify if the amount on the CSV file was credited.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1770.dictData['strUser1'])
    newWindow = uCommon.switchToWindow(page)
    uAdminKpc.cu.validateRewardsCreditsAddedFromUpload(newWindow, strOldTotalRewards, strOldTotalCredits, dAdmin.AUTO1770.rewardCredits)
    uCommon.closeWindow(newWindow)
    
    uCommon.log(0, 'Step 4 - Reupload the file again and verify if error is encountered.')
    uAdminKpc.cu.verifyErrorRewardsCreditsAreAlreadyDeductedCredited(page, dAdmin.AUTO1770.strPath)
    uCommon.log(0, 'Test Completed')
    
    
""" Author: abernal_20240418 Execution Time: 36s - 39s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that Error message should be displayed when same balance for credit are deducted to a user ID within 5 minutes of uploading a CSV file')
def test_ACQ_AUTO_1773_Error_message_should_be_displayed_when_same_balance_for_credit_are_deducted_to_a_user_ID_within_5_minutes_of_uploading_a_CSV_file(page): 
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, '[Pre-condition Started]: Get the current total rewards and credits of the users.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1773.dictData['strUser1'])
    newWindow = uCommon.switchToWindow(page)
    strOldTotalRewards = uAdminKpc.cu.getTotalRewardsValue(newWindow, strTotalRewards = '')
    strOldTotalCredits = uAdminKpc.cu.getTotalCreditsValue(newWindow, strTotalCredits = '')
    uCommon.closeWindow(newWindow)
    uCommon.log(0, '[Pre-condition Completed]: Get the current total rewards and credits of the users.')
    
    uCommon.log(0, 'Step 2 - Click the Upload Rewards or Credit button. Upload the file.')
    uAdminKpc.cu.uploadUserCreditsOrRewards(page, dAdmin.AUTO1773.strPath)
    
    uCommon.log(0, 'Step 3 - Search for an email from the list in the CSV file. Click the First Name and verify if the amount on the CSV file was credited.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1773.dictData['strUser1'])
    newWindow = uCommon.switchToWindow(page)
    uAdminKpc.cu.validateRewardsCreditsDeductedFromUpload(newWindow, strOldTotalRewards, strOldTotalCredits, dAdmin.AUTO1770.rewardCredits)
    uCommon.closeWindow(newWindow)
    
    uCommon.log(0, 'Step 4 - Reupload the file again and verify if error is encountered.')
    uAdminKpc.cu.verifyErrorRewardsCreditsAreAlreadyDeductedCredited(page, dAdmin.AUTO1773.strPath)
    uCommon.log(0, 'Test Completed')
    

""" Author: abernal_20240418 Execution Time: 36s - 39s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that Error message should be displayed when same balance for rewards are credited to a user ID within 5 minutes of uploading a CSV file')
def test_ACQ_AUTO_1776_Error_message_should_be_displayed_when_same_balance_for_rewards_are_credited_to_a_user_ID_within_5_minutes_of_uploading_a_CSV_file(page): 
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, '[Pre-condition Started]: Get the current total rewards and credits of the users.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1776.dictData['strUser1'])
    newWindow = uCommon.switchToWindow(page)
    strOldTotalRewards = uAdminKpc.cu.getTotalRewardsValue(newWindow, strTotalRewards = '')
    strOldTotalCredits = uAdminKpc.cu.getTotalCreditsValue(newWindow, strTotalCredits = '')
    uCommon.closeWindow(newWindow)
    uCommon.log(0, '[Pre-condition Completed]: Get the current total rewards and credits of the users.')
    
    uCommon.log(0, 'Step 2 - Click the Upload Rewards or Credit button. Upload the file.')
    uAdminKpc.cu.uploadUserCreditsOrRewards(page, dAdmin.AUTO1776.strPath)
    
    uCommon.log(0, 'Step 3 - Search for an email from the list in the CSV file. Click the First Name and verify if the amount on the CSV file was credited.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1776.dictData['strUser1'])
    newWindow = uCommon.switchToWindow(page)
    uAdminKpc.cu.validateRewardsCreditsAddedFromUpload(newWindow, strOldTotalRewards, strOldTotalCredits, dAdmin.AUTO1776.rewardCredits)
    uCommon.closeWindow(newWindow)
    
    uCommon.log(0, 'Step 4 - Reupload the file again and verify if error is encountered.')
    uAdminKpc.cu.verifyErrorRewardsCreditsAreAlreadyDeductedCredited(page, dAdmin.AUTO1776.strPath)
    uCommon.log(0, 'Test Completed')
    

""" Author: abernal_20240418 Execution Time: 36s - 41s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that Error message should be displayed when same balance for rewards are deducted to a user ID within 5 minutes of uploading a CSV file')
def test_ACQ_AUTO_1779_Error_message_should_be_displayed_when_same_balance_for_rewards_are_deducted_to_a_user_ID_within_5_minutes_of_uploading_a_CSV_file(page): 
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, '[Pre-condition Started]: Get the current total rewards and credits of the users.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1779.dictData['strUser1'])
    newWindow = uCommon.switchToWindow(page)
    strOldTotalRewards = uAdminKpc.cu.getTotalRewardsValue(newWindow, strTotalRewards = '')
    strOldTotalCredits = uAdminKpc.cu.getTotalCreditsValue(newWindow, strTotalCredits = '')
    uCommon.closeWindow(newWindow)
    uCommon.log(0, '[Pre-condition Completed]: Get the current total rewards and credits of the users.')
    
    uCommon.log(0, 'Step 2 - Click the Upload Rewards or Credit button. Upload the file.')
    uAdminKpc.cu.uploadUserCreditsOrRewards(page, dAdmin.AUTO1779.strPath)
    
    uCommon.log(0, 'Step 3 - Search for an email from the list in the CSV file. Click the First Name and verify if the amount on the CSV file was credited.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1779.dictData['strUser1'])
    newWindow = uCommon.switchToWindow(page)
    uAdminKpc.cu.validateRewardsCreditsDeductedFromUpload(newWindow, strOldTotalRewards, strOldTotalCredits, dAdmin.AUTO1776.rewardCredits)
    uCommon.closeWindow(newWindow)
    
    uCommon.log(0, 'Step 4 - Reupload the file again and verify if error is encountered.')
    uAdminKpc.cu.verifyErrorRewardsCreditsAreAlreadyDeductedCredited(page, dAdmin.AUTO1779.strPath)
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
    
    
""" Author: abernal_20240418 Execution Time: 52s - 56s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that Error message should be displayed when userID does not exist.')
@allure.step('To verify that balances is not credited when there is a non-existent user that is part of the uploaded CSV file.')
#test_ACQ_AUTO_1797_Balances_should_not_be_credited_when_there_is_a_nonexistent_user_that_is_part_of_the_uploaded_CSV_file
def test_ACQ_AUTO_1782_Error_message_should_be_displayed_when_userID_does_not_exist(page): 
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, '[Pre-condition Started]: Get the current total rewards and credits of the users.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1782.dictData['strUser1'])
    newWindow = uCommon.switchToWindow(page)
    strOldTotalRewardsAboveError = uAdminKpc.cu.getTotalRewardsValue(newWindow, strTotalRewards = '')
    strOldTotalCreditsAboveError = uAdminKpc.cu.getTotalCreditsValue(newWindow, strTotalCredits = '')
    uCommon.closeWindow(newWindow)
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1782.dictData['strUser3'])
    newWindow = uCommon.switchToWindow(page)
    strOldTotalRewardsBelowError = uAdminKpc.cu.getTotalRewardsValue(newWindow, strTotalRewards = '')
    strOldTotalCreditsBelowError = uAdminKpc.cu.getTotalCreditsValue(newWindow, strTotalCredits = '')
    uCommon.closeWindow(newWindow)
    uCommon.log(0, '[Pre-condition Completed]: Get the current total rewards and credits of the users.')
    
    uCommon.log(0, '[AUTO-1782 Started]: Step 2 - Click the Upload Rewards or Credit button. Upload the file.')
    uAdminKpc.cu.verifyUserDoesNotExistErrorMsg(page, dAdmin.AUTO1782.strPath)
    uCommon.log(0, '[AUTO-1782 Completed]: Error message for userID does not exist is displayed.')
    
    uCommon.log(0, '[AUTO-1797 Started]: Step 3 - Search for an email from the list in the CSV file. Click the First Name and verify if the amount on the CSV file was credited.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1782.dictData['strUser1'])
    newWindow = uCommon.switchToWindow(page)
    uAdminKpc.cu.validateRewardsCreditsAreNotCredited(newWindow, strOldTotalRewardsAboveError, strOldTotalCreditsAboveError)
    uCommon.closeWindow(newWindow)
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1782.dictData['strUser3'])
    newWindow = uCommon.switchToWindow(page)
    uAdminKpc.cu.validateRewardsCreditsAreNotCredited(newWindow, strOldTotalRewardsBelowError, strOldTotalCreditsBelowError)
    uCommon.closeWindow(newWindow)
    uCommon.log(0, '[AUTO-1797 Completed]: Balances uploaded should not be credited.')
    uCommon.log(0, 'Test Completed')
    

""" Author: abernal_20240418 Execution Time: 52s - 56s """
@pytest.mark.netTest()
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that rows below the error from the CSV file should still be uploaded.')
@allure.step('To verify that rows above the error from the CSV file should still be uploaded.')
#test_ACQ_AUTO_1800_Rows_above_the_error_from_the_CSV_file_should_still_be_uploaded
def test_ACQ_AUTO_1794_Rows_below_the_error_from_the_CSV_file_should_still_be_uploaded(page): 
    uCommon.log(0, 'Step 1 - Login to Admin Panel and click the Customer module.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cu.clickCustomers(page)
    
    uCommon.log(0, '[Pre-condition Started]: Get the current total rewards and credits of the users.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1782.dictData['strUser1'])
    newWindow = uCommon.switchToWindow(page)
    strOldTotalRewardsAboveError = uAdminKpc.cu.getTotalRewardsValue(newWindow, strTotalRewards = '')
    strOldTotalCreditsAboveError = uAdminKpc.cu.getTotalCreditsValue(newWindow, strTotalCredits = '')
    uCommon.closeWindow(newWindow)
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1779.dictData['strUser3'])
    newWindow = uCommon.switchToWindow(page)
    strOldTotalRewards = uAdminKpc.cu.getTotalRewardsValue(newWindow, strTotalRewards = '')
    strOldTotalCredits = uAdminKpc.cu.getTotalCreditsValue(newWindow, strTotalCredits = '')
    uCommon.closeWindow(newWindow)
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1782.dictData['strUser4'])
    newWindow = uCommon.switchToWindow(page)
    strOldTotalRewardsBelowError = uAdminKpc.cu.getTotalRewardsValue(newWindow, strTotalRewards = '')
    strOldTotalCreditsBelowError = uAdminKpc.cu.getTotalCreditsValue(newWindow, strTotalCredits = '')
    uCommon.closeWindow(newWindow)
    uCommon.log(0, '[Pre-condition Completed]: Get the current total rewards and credits of the users.')
    
    uCommon.log(0, 'Step 2 - Click the Upload Rewards or Credit button. Upload the file.')
    uAdminKpc.cu.uploadUserCreditsOrRewards(page, dAdmin.AUTO1794.strPath1)
    
    uCommon.log(0, 'Step 3 - Search for an email from the list in the CSV file. Click the First Name and verify if the amount on the CSV file was credited.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1794.dictData['strUser3'])
    newWindow = uCommon.switchToWindow(page)
    uAdminKpc.cu.validateRewardsCreditsAddedFromUpload(newWindow, strOldTotalRewards, strOldTotalCredits, dAdmin.AUTO1794.rewardCredits)
    strNewTotalRewards = uAdminKpc.cu.getTotalRewardsValue(newWindow, strTotalRewards = '')
    strNewTotalCredits = uAdminKpc.cu.getTotalCreditsValue(newWindow, strTotalCredits = '')
    uCommon.closeWindow(newWindow)
    
    uCommon.log(0, 'Step 4 - Click the Upload Rewards or Credit button. Upload the second file.')
    uAdminKpc.cu.verifyErrorRewardsCreditsAreAlreadyDeductedCredited(page, dAdmin.AUTO1794.strPath2)
    
    uCommon.log(0, '[AUTO-1794 Started]: Step 5 - Search for an email (above the error) from the list in the CSV file. Click the First Name and verify if the amount on the CSV file was credited.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1794.dictData['strUser1'])
    newWindow = uCommon.switchToWindow(page)
    uAdminKpc.cu.validateRewardsCreditsAddedFromUpload(newWindow, strOldTotalRewardsAboveError, strOldTotalCreditsAboveError, dAdmin.AUTO1794.rewardCredits)
    uCommon.closeWindow(newWindow)
    uCommon.log(0, '[AUTO-1794 Completed]: Rewards and Credits should be added to the user.')
    
    uCommon.log(0, '[AUTO-1800 Started]: Step 6 - Search for an email (below the error) from the list in the CSV file. Click the First Name and verify if the amount on the CSV file was credited.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1794.dictData['strUser4'])
    newWindow = uCommon.switchToWindow(page)
    uAdminKpc.cu.validateRewardsCreditsAddedFromUpload(newWindow, strOldTotalRewardsBelowError, strOldTotalCreditsBelowError, dAdmin.AUTO1794.rewardCredits)
    uCommon.closeWindow(newWindow)
    uCommon.log(0, '[AUTO-1800 Completed]: Rewards and Credits should be added to the user.')
    
    uCommon.log(0, 'Step 6 - Search for an email from the list in the CSV file. Click the First Name and verify that the reward and credit is not added to the user anymore.')
    uAdminKpc.cu.searchCustomer(page, dAdmin.AUTO1794.dictData['strUser3'])
    newWindow = uCommon.switchToWindow(page)
    uAdminKpc.cu.validateRewardsCreditsAreNotCredited(newWindow, strNewTotalRewards, strNewTotalCredits)
    uCommon.closeWindow(newWindow)
    uCommon.log(0, 'Test Completed')
    