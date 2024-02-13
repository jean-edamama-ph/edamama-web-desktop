import pytest
import allure
import libraries.data.regressionTestSuite.profile.myProfile as dRegMyProfile

import libraries.util.appCommon.appComm as uAppComm
import libraries.util.common as uCommon
import libraries.util.profile.myProfile as uMyProfile
import libraries.data.common as dCommon


""" Author: cgrapa_20230613 Execution Time: 1m 2s - 1m 4s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that OTP pin is not validated when there is no input')
def test_AUTO_865_Pin_should_not_be_validated_when_there_is_no_input(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page)
    
    uCommon.log(0, 'Step 2 - Navigate to My Profile page')
    uAppComm.com.navigateToProfileMenu(page, dRegMyProfile.AUTO865.strMyProfile)
    dictData = uMyProfile.com.getMyProfileDetails(page)
    
    uCommon.log(0, 'Step 3 - Click Mobile Verification/Edit, enter a valid number and send code')
    uMyProfile.mn.editNumberAndValidateForm(page)
    uMyProfile.mn.inputNumberAndSendCode(page, dRegMyProfile.AUTO865.strMobileNumber)
    
    uCommon.log(0, 'Step 4 - Do not enter any value for OTP')
    uMyProfile.mn.validatePinFormAndClickVerifyCode(page)
    uAppComm.error.validatePopUpMsg(page, dRegMyProfile.AUTO865.strMsg)
    uMyProfile.com.closeAddEditForm(page)
    uMyProfile.mn.validateFailedMobileChange(page, dictData)
    uCommon.log(0, 'Test Completed')


""" Author: cgrapa_20230614 Execution Time: 21s - 24s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that the user is able to add attributes to their profile.')
def test_AUTO_866_User_should_be_able_to_add_attributes(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page)
    
    uCommon.log(0, 'Step 2 - Navigate to My Profile page')
    uAppComm.com.navigateToProfileMenu(page, dRegMyProfile.AUTO866.strMyProfile)
    
    uCommon.log(0, 'Step 3 - Scroll down to attributes section and click ADD/EDIT button')
    uMyProfile.at.validateAndAddAttributes(page, dRegMyProfile.AUTO866.intAddAttributes)
    uCommon.log(0, 'Test Completed')

    
""" Author: rmakiling_20230928 Execution Time: 17s - 23s"""
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that the user can update/edit Firstname and Lastname')
def test_AUTO_000_Verify_that_the_user_can_update_the_profile(page):
    uCommon.log(0, 'Step 1 - Open edamama websit and Login using valid user credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName1)

    uCommon.log(0, 'Step 2 - Navigate to the Profile tab.')
    uAppComm.com.navigateToProfileMenu(page, 'my profile')
    dictData = uMyProfile.com.getMyProfileDetails(page)

    uCommon.log(0, 'Step 3 - Click Edit button')
    uMyProfile.com.clickEditbtn(page)

    uCommon.log(0, 'Step 4 - Upload photo')
    uMyProfile.edp.uploadPhoto(page, dRegMyProfile.AUTO000.dictData['strPathUpdate'])

    uCommon.log(0, 'Step 5 - Update First Name and Last Name')
    uMyProfile.edp.fillDetails(page, dRegMyProfile.AUTO000.dictData)

    uCommon.log(0, 'Step 6 - Click Update button')
    uMyProfile.edp.clickUpdate(page)

    uCommon.log(0, 'Step 7 - Verify if the inputted first name and last name value is reflected in My Profile page')
    uMyProfile.edp.verifyFullname(page, dRegMyProfile.AUTO000.dictData)

    uCommon.log(0, '[Post condition Started]: Update to original values')
    uMyProfile.com.clickEditbtn(page)
    uMyProfile.edp.uploadPhoto(page, dRegMyProfile.AUTO000.dictData['strPathDefault'])
    arrData = dictData['strName'].split()
    newDictdata = {'strFName': arrData[0], 'strLName': arrData[1]}
    uMyProfile.edp.fillDetails(page, newDictdata)
    uMyProfile.edp.clickUpdate(page)
    uCommon.log(0, '[Post condition Completed]: Name returns to original values')


""" Author: abernal_20231001 Execution Time: 1m 06s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that user is able to add address.')
@allure.step('To verify that user is able to edit the details of an existing address.')
@allure.step('To verify that the user is able to delete existing address.')
# test_AUTO_874_1028_880_User_should_be_able_to_add_edit_delete_address
def test_ACQ_AUTO_874_User_should_be_able_to_add_edit_delete_address(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName2)
    
    uCommon.log(0, 'Step 2 - Click the profile on the header and click My Profile.')
    uAppComm.com.navigateToProfileMenu(page, dRegMyProfile.AUTO874.strMyProfile)
    
    uCommon.log(0, '[Pre-condition started]: Add new address.')
    strFullName1 = f'{dRegMyProfile.AUTO874.dictNewAddress["strFirstName"]} {dRegMyProfile.AUTO874.dictNewAddress["strLastName"]}'
    uMyProfile.com.deleteAddress(page, strFullName1)
    uMyProfile.com.clickAddressAddMore(page)
    uMyProfile.na.addAddress(page, dRegMyProfile.AUTO874.dictData)
    uMyProfile.na.clickAddNewAddress(page)

    uCommon.log(0, 'Step 3 - Click the kebab menu of an existing address and click Edit button.')
    strFullName2 = f'{dRegMyProfile.AUTO874.dictData["strFirstName"]} {dRegMyProfile.AUTO874.dictData["strLastName"]}'
    uMyProfile.ea.clickAddressEdit(page, strFullName2)

    uCommon.log(0, 'Step 4 - Edit the fields/details for contact person and delivery address and click the Update Address button.')
    uMyProfile.ea.editAddress(page, dRegMyProfile.AUTO874.dictNewAddress)
    uMyProfile.ea.clickUpdateAddress(page)

    uCommon.log(0, 'Step 5 - Verify if the new details are now displayed on the address that was edited.')
    uMyProfile.ea.verifyNewAddressDetails(page, dRegMyProfile.AUTO874.dictNewAddress)

    uCommon.log(0, '[Post condition started]: Click the kebab menu of an existing address and click Remove button. Click Yes button on confirmation modal.')
    uMyProfile.com.deleteAddress(page, strFullName1)


""" Author: abernal_20231001 Execution Time: 1m 25s """
@pytest.mark.acquiTestSuite()
@pytest.mark.regressionTestSuite()
@allure.step('To verify that the user can select a new default address.')
def test_ACQ_AUTO_877_User_should_be_able_to_change_default_address(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName3)
    
    uCommon.log(0, 'Step 2 - Click the profile on the header and click My Profile.')
    uAppComm.com.navigateToProfileMenu(page, dRegMyProfile.AUTO877.strMyProfile)
    
    uCommon.log(0, '[Pre-condition started]: Add default address and second address.')
    #Remove previous address if available
    strFullName1 = f'{dRegMyProfile.AUTO877.firstData["strFirstName"]} {dRegMyProfile.AUTO877.firstData["strLastName"]}'
    strFullName2 = f'{dRegMyProfile.AUTO877.secondData["strFirstName"]} {dRegMyProfile.AUTO877.secondData["strLastName"]}'
    uMyProfile.com.deleteAddress(page, strFullName1)
    uMyProfile.com.deleteAddress(page, strFullName2)
    uCommon.log(0, '[Pre-condition Completed]: Address are now deleted')
    
    uMyProfile.com.clickAddressAddMore(page)
    uMyProfile.na.addAddress(page, dRegMyProfile.AUTO877.firstData)
    uMyProfile.na.tickSetAsDefault(page)
    uMyProfile.na.clickAddNewAddress(page)

    uMyProfile.com.clickAddressAddMore(page)
    uMyProfile.na.addAddress(page, dRegMyProfile.AUTO877.secondData)
    uMyProfile.na.clickAddNewAddress(page)

    uCommon.log(0, 'Step 3 - Click the kebab menu of an existing address and click Edit button.')
    uMyProfile.ea.clickAddressEdit(page, strFullName2)
    
    uCommon.log(0, 'Step 4 - Tick the "Set as Default" and click Update Address button.')
    uMyProfile.na.tickSetAsDefault(page)
    uMyProfile.ea.clickUpdateAddress(page)

    uCommon.log(0, 'Step 5 - Verify if address has the Default label.')
    uMyProfile.com.verifyDefaultLabel(page, strFullName2)
    uCommon.log(0, 'Test Completed')

    uCommon.log(0, '[Post condition Started]: Click the kebab menu of an existing address and click Remove button. Click Yes button on confirmation modal.')
    uMyProfile.com.deleteAddress(page, strFullName1)
    uMyProfile.com.deleteAddress(page, strFullName2)
    uCommon.log(0, '[Post condition Completed]: Addresses added are now deleted.')


""" Author: abernal_20231009 Execution Time: 3m 09s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that user can add multiple delivery addresses.')
def test_ACQ_AUTO_871_User_should_be_able_to_add_multiple_delivery_addresses(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName4)
    
    uCommon.log(0, 'Step 2 - Click the profile on the header and click My Profile.')
    uAppComm.com.navigateToProfileMenu(page, dRegMyProfile.AUTO871.strMyProfile)

    uCommon.log(0, '[Pre-condition started]: Remove previous address if available.')
    strFullName1 = f'{dRegMyProfile.AUTO871.firstData["strFirstName"]} {dRegMyProfile.AUTO871.firstData["strLastName"]}'
    strFullName2 = f'{dRegMyProfile.AUTO871.secondData["strFirstName"]} {dRegMyProfile.AUTO871.secondData["strLastName"]}'
    strFullName3 = f'{dRegMyProfile.AUTO871.thirdData["strFirstName"]} {dRegMyProfile.AUTO871.thirdData["strLastName"]}'
    strFullName4 = f'{dRegMyProfile.AUTO871.fourthData["strFirstName"]} {dRegMyProfile.AUTO871.fourthData["strLastName"]}'
    strFullName5 = f'{dRegMyProfile.AUTO871.fifthData["strFirstName"]} {dRegMyProfile.AUTO871.fifthData["strLastName"]}'
    
    uMyProfile.com.deleteAddress(page, strFullName1)
    uMyProfile.com.deleteAddress(page, strFullName2)
    uMyProfile.com.deleteAddress(page, strFullName3)
    uMyProfile.com.deleteAddress(page, strFullName4)
    uMyProfile.com.deleteAddress(page, strFullName5)

    uCommon.log(0, 'Step 3 & 4 - Click Add More button. Populate all the information under Contact Person and Delivery Address and click Add Address button.')

    uMyProfile.com.clickAddressAddMore(page)
    uMyProfile.na.addAddress(page, dRegMyProfile.AUTO871.firstData)
    uMyProfile.na.clickAddNewAddress(page)

    uMyProfile.com.clickAddressAddMore(page)
    uMyProfile.na.addAddress(page, dRegMyProfile.AUTO871.secondData)
    uMyProfile.na.clickAddNewAddress(page)

    uMyProfile.com.clickAddressAddMore(page)
    uMyProfile.na.addAddress(page, dRegMyProfile.AUTO871.thirdData)
    uMyProfile.na.clickAddNewAddress(page)

    uMyProfile.com.clickAddressAddMore(page)
    uMyProfile.na.addAddress(page, dRegMyProfile.AUTO871.fourthData)
    uMyProfile.na.clickAddNewAddress(page)

    uMyProfile.com.clickAddressAddMore(page)
    uMyProfile.na.addAddress(page, dRegMyProfile.AUTO871.fifthData)
    uMyProfile.na.clickAddNewAddress(page)

    uCommon.log(0, 'Verify that all addresses were displayed on the list of addresses.')
    uMyProfile.ea.verifyNewAddressDetails(page, dRegMyProfile.AUTO871.firstData)
    uMyProfile.ea.verifyNewAddressDetails(page, dRegMyProfile.AUTO871.secondData)
    uMyProfile.ea.verifyNewAddressDetails(page, dRegMyProfile.AUTO871.thirdData)
    uMyProfile.ea.verifyNewAddressDetails(page, dRegMyProfile.AUTO871.fourthData)
    uMyProfile.ea.verifyNewAddressDetails(page, dRegMyProfile.AUTO871.fifthData)
    uCommon.log(0, 'Test Completed')

    uCommon.log(0, '[Post-condition started]: Remove previous addresses added.')
    uMyProfile.com.deleteAddress(page, strFullName1)
    uMyProfile.com.deleteAddress(page, strFullName2)
    uMyProfile.com.deleteAddress(page, strFullName3)
    uMyProfile.com.deleteAddress(page, strFullName4)
    uMyProfile.com.deleteAddress(page, strFullName5)

    
""" Author: abernal_20231011 Execution Time: 34s - 40s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that the user is able to add a child in the My Profile page.')
@allure.step('To verify that the user is able to edit child details.')
@allure.step('To verify that user is able to remove a child data via My Profile.')
# test_ACQ_AUTO_1025_User_should_be_able_to_edit_child_details
# test_ACQ_AUTO_1155_User_should_be_able_to_add_child
# test_ACQ_AUTO_1079_User_should_be_able_to_remove_a_child_via_My_Profile
def test_ACQ_AUTO_1025_User_should_be_able_to_add_edit_remove_child_details(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName5)
    
    uCommon.log(0, 'Step 2 - Navigate to My Profile page')
    uAppComm.com.navigateToProfileMenu(page, dRegMyProfile.AUTO1025.strMyProfile)
    
    uCommon.log(0, '[Pre-condition Started]: Delete existing child')
    uMyProfile.com.checkAndDeleteChild(page, dRegMyProfile.AUTO1025.newChildData["strChildName"])
    uMyProfile.com.checkAndDeleteChild(page, dRegMyProfile.AUTO1025.updatedChildData["strChildName"])
    uCommon.log(0, '[Pre-condition Completed]: Delete existing child')
    
    uCommon.log(0, '[AUTO-1025 Started]: Add New Child')
    uMyProfile.com.clickAddAChild(page)
    uMyProfile.ac.addChildDetails(page, dRegMyProfile.AUTO1025.newChildData)
    uCommon.log(0, '[AUTO-1025 Completed]: Added a new child') 

    uCommon.log(0, '[AUTO-1155 Started]: Edit New Child')
    uCommon.log(0, 'Step 3 - Scroll to Child Details section and click the kebab menu on a specific child.')
    uMyProfile.com.clickChildKebabMenu(page, dRegMyProfile.AUTO1025.newChildData["strChildName"])
    
    uCommon.log(0, 'Step 4 to 5 - Click Edit button. Edit any of the fields available and click Update button.​​​​')
    uMyProfile.com.clickEditChild(page)
    uMyProfile.ec.editChildDetails(page, dRegMyProfile.AUTO1025.updatedChildData)
    
    uCommon.log(0, 'Step 6 - Verify if the data of the child edited is updated.​​​​')
    uMyProfile.com.verifyUpdatedChildDetails(page, dRegMyProfile.AUTO1025.updatedChildData["strChildName"])
    uCommon.log(0, '[AUTO-1155 Completed]: Edit New Child')
    
    uCommon.log(0, '[AUTO-1079 Started]: Remove added child')
    uMyProfile.com.clickChildKebabMenu(page, dRegMyProfile.AUTO1025.updatedChildData["strChildName"])
    uMyProfile.com.clickDeleteChild(page, dRegMyProfile.AUTO1025.updatedChildData["strChildName"])
    uCommon.log(0, '[AUTO-1079 Completed]: Child removed')
    uCommon.log(0, 'Test Completed')
    
    
""" Author: abernal_20231011 Execution Time: 23s - 28s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that the user is able to update attributes.')
@allure.step('To verify that user is able to remove attributes.')
# test_ACQ_AUTO_1085_User_should_be_able_to_update_attributes
# test_ACQ_AUTO_1082_User_should_be_able_to_remove_attributes
def test_ACQ_AUTO_1085_User_should_be_able_to_update_remove_attributes(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName6)
    
    uCommon.log(0, 'Step 2 - Navigate to My Profile page')
    uAppComm.com.navigateToProfileMenu(page, dRegMyProfile.AUTO1085.strMyProfile)
    
    uCommon.log(0, '[Pre-condition Started]: Add attributes to profile.')
    uMyProfile.at.validateAndAddAttributes(page, dRegMyProfile.AUTO1085.intAddAttributes)
    uCommon.log(0, '[Pre-condition Completed]: Added attributes to profile.')
    
    uCommon.log(0, '[AUTO-1085 Started]: Update attributes')
    uCommon.log(0, 'Step 3 - If there are already 5 attributes selected, unselect the attributes you want to edit out.\
        Select any attributes that are not selected yet and click Submit button.')
    uMyProfile.at.updateAttributes(page, dRegMyProfile.AUTO1085.dictData)
    uCommon.log(0, '[AUTO-1085 Completed]: Updated attributes')
    
    uCommon.log(0, '[AUTO-1082 Started]: Remove attributes')
    uMyProfile.at.clearAttributes(page)
    uCommon.log(0, '[AUTO-1082 Completed]: Removed attributes')
    uCommon.log(0, 'Test Completed')


""" Author: jatregenio_20240123 Execution Time: 00s - 00s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that user is able to select only up to 5 attributes.')
def test_ACQ_AUTO_1388_Only_up_to_5_attributes_can_be_selected(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName7)
    
    uCommon.log(0, 'Step 2 - Navigate to the Profile tab.')
    uAppComm.com.navigateToProfileMenu(page, dRegMyProfile.AUTO1388.strMyProfile)
    
    uCommon.log(0, '[Pre-condition Started]: User should have 5 existing attributes.')
    uMyProfile.at.validateAndAddAttributes(page, dRegMyProfile.AUTO1388.intAddAttributes)
    uCommon.log(0, '[Pre-condition Completed]: 5 attributes were added to the user.')
    
    uCommon.log(0, 'Step 3 - Scroll down to attributes and click Edit My Attributes button and select another attribute.')
    uMyProfile.at.updateAttributes(page)
    uCommon.log(0, 'Test Completed')


""" Author: rmakiling_20240115 Execution Time: 29s - 30s """   
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that account should not be verified if pin provided is incorrect.')
def test_ACQ_AUTO_1103_User_should_not_be_able_to_verify_account_if_pin_provided_is_incorrect(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName8)
    
    uCommon.log(0, 'Step 2 - Navigate to My Profile page')
    uAppComm.com.navigateToProfileMenu(page, dRegMyProfile.AUTO1103.strMyProfile)
    dictDataBefore = uMyProfile.com.getMyProfileDetails(page)
    
    uCommon.log(0, 'Step 3 - Click edit mobile number button')
    uMyProfile.mn.clickEditMobileNumber(page)
    
    uCommon.log(0, 'Step 4 - Input Mobile Nubmer and send code')
    uMyProfile.mn.inputNumberAndSendCode(page, dRegMyProfile.AUTO1103.strMobileNumber)
    
    uCommon.log(0, 'Step 5 - Click Verify Code button')
    uMyProfile.mn.clickVerifyCode(page)
    
    uCommon.log(0, 'Step 7 - Verify if the Mobile Number is updated')  
    uMyProfile.mn.clickCloseBtn(page)
    dictDataAfter = uMyProfile.com.getMyProfileDetails(page)
    uCommon.stringCompare(dictDataBefore["strMobileNumber"], dictDataAfter["strMobileNumber"])
    uCommon.log(0, 'Test Completed')


""" Author: rmakiling_20240115 Execution Time: 16s - 22s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that user cannot update the name if it exceeds the maximum allowed characters.')
def test_ACQ_AUTO_1091_User_should_not_be_able_to_update_name_if_it_exceeds_the_maximum_allowed_characters(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName7)
    
    uCommon.log(0, 'Step 2 - Navigate to My Profile page')
    uAppComm.com.navigateToProfileMenu(page, dRegMyProfile.AUTO1091.strMyProfile)
    dictDataBefore = uMyProfile.com.getMyProfileDetails(page)

    uCommon.log(0, 'Step 3 - Click Edit button')
    uMyProfile.com.clickEditbtn(page)
 
    uCommon.log(0, 'Step 5 - Update First Name and Last Name')
    uMyProfile.edp.fillDetails(page, dRegMyProfile.AUTO1091.dictData)
    
    uCommon.log(0, 'Step 6 - Update First Name and Last Name')
    uMyProfile.edp.clickUpdate(page, True)
    
    uCommon.log(0, 'Step 7 - Verify if the First Name and Last Name is updated')
    uMyProfile.edp.clickCloseBtn(page)
    dictDataAfter = uMyProfile.com.getMyProfileDetails(page)
    uCommon.stringCompare(dictDataBefore["strName"], dictDataAfter["strName"])
    uCommon.log(0, 'Test Completed')
