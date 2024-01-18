import pytest
import allure

import libraries.data.common as dCommon
import libraries.data.regressionTestSuite.profile.myGifts as dRegMyGifts

import libraries.util.appCommon.appComm as uAppComm
import libraries.util.common as uCommon
import libraries.util.profile.myGifts as uMyGifts
import libraries.util.shop as uShop
import libraries.util.profile.myProfile as uMyProfile


""" Author: rmakiling_20231008 Execution Time: 54s - 59s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@pytest.mark.thisTest()
@allure.step('To verify that the user is able to add producs to the Gift List')
def test_ACQ_AUTO_1053_User_should_be_able_to_add_products_to_the_gift_list(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName1)

    uCommon.log(0, '[Pre-condition Started]: Delete if there are existing Gift List and Create Gift list')
    uMyGifts.com.clickGiftBox(page)
    uMyGifts.com.checkAndDelete(page)
    uCommon.log(0, '[Pre-condition Completed]: Giftlist is Deleted')
    
    uCommon.log(0, 'Step 2 - Create Giflist and Add product')
    strItemName = uMyGifts.com.createGLandAddProduct(page, dRegMyGifts.AUTO1053.dictData)

    uCommon.log(0, 'Step 3 - Click the "Gift" icon again then select your list >> Verify Gift list product counter')
    uMyGifts.com.clickGiftBox(page)
    uMyGifts.com.verifyGiftListProductCount(page, dRegMyGifts.AUTO1053.dictData["strCount"])

    uCommon.log(0, 'Step 4 - Click the created Gift list >> Verify the added product')
    uMyGifts.com.clickGiftList(page, False)
    uMyGifts.com.verifyGiftListProducts(page, strItemName)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: rmakiling_20231012 Execution Time: 40s - 47s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@pytest.mark.thisTest()
@allure.step('To verify that user is able to archive and activate the gift list.')
def test_ACQ_AUTO_1056_And_AUTO_1049_User_should_be_able_to_archive_activate_the_gift_list(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName2)
    
    uCommon.log(0, '[Pre-condition Started]: Delete if there are existing Gift List and Create Gift list')
    uMyGifts.com.clickGiftBox(page)
    uMyGifts.com.checkAndDelete(page)
    uCommon.log(0, '[Pre-condition Completed]: Giftlist is Deleted')
  
    uCommon.log(0, 'Step 2 - Create Giflist')
    uMyGifts.com.createNewGiftList(page, dRegMyGifts.AUTO1056.dictData)

    uCommon.log(0, '[AUTO-1056 Started]: Archived Gift List')
    uCommon.log(0, 'Step 3 - Click the meatballs icon button and archive gift list')
    uMyGifts.com.updateGiftListStatus(page, dRegMyGifts.AUTO1056.blnArchived)

    uCommon.log(0, 'Step 4 - Verify the result')
    uMyGifts.com.verifyGiftListStatus(page, dRegMyGifts.AUTO1056.blnClickable)
    uCommon.log(0, '[AUTO-1056 Completed]: Gift list is archived')
    
    uCommon.log(0, '[AUTO-1049 Started]: Unarchived Gift List')
    uCommon.log(0, 'Step 6 - Click the meatballs icon button and activate gift list')
    uMyGifts.com.updateGiftListStatus(page, dRegMyGifts.AUTO1049.blnArchived)
    
    uCommon.log(0, 'Step 7 - Verify the result')
    uMyGifts.com.verifyGiftListStatus(page, dRegMyGifts.AUTO1049.blnClickable)
    uCommon.log(0, '[AUTO-1049 Completed]: Gift list is unarchived')
    uCommon.log(0, 'Test case completed')
  
    
""" Author: jatregenio_20231219 Execution Time: 35s - 40s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@pytest.mark.thisTest()
@allure.step('To verify that user is able to create a gift list.')
def test_ACQ_AUTO_1059_User_should_be_able_to_create_a_gift_list(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName3)
    
    uCommon.log(0, '[Pre-condition Started]: Delete if there are existing Gift List and Create Gift list')
    uMyGifts.com.clickGiftBox(page, 'opt')
    uMyGifts.com.checkAndDelete(page)
    uCommon.log(0, '[Pre-condition Completed]: Giftlist is Deleted')
    
    uCommon.log(0,'Step 2 - Click the Gift icon on the header.')
    uMyGifts.com.clickGiftBox(page)
    
    uCommon.log(0, 'Step 3 - Click the Create a Gift List button.')
    uCommon.log(0, 'Step 4 - Select a photo cover, enter event details, and select an address. Click Create Gift List button.')
    uMyGifts.com.createNewGiftList(page, dRegMyGifts.AUTO1059.dictData)
    
    uCommon.log(0, 'Step 5 - Verify if the newly created gift list is displayed with the expected details.')
    uMyGifts.com.verifyAndOpenNewlyCreatedGiftList(page, dRegMyGifts.AUTO1059.dictData["strOccassion"], dRegMyGifts.AUTO1059.dictData["strAbout"])
    uCommon.log(0, '[AUTO-1059 Completed]: Newly created gift list should be displayed with the correct details.')
    uCommon.log(0, 'Test case completed')


""" Author: jatregenio_20231219 Execution Time: 40s - 42s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@pytest.mark.thisTest()
@allure.step('To verify that the gift list can be edited.')
def test_ACQ_AUTO_1062_User_should_be_able_to_edit_a_gift_list(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName4)
    
    uCommon.log(0, 'Step 2 - Navigate to Profile tab > Gift Registry.')
    uMyGifts.com.clickGiftBox(page, 'opt')
    
    uCommon.log(0, '[Pre-condition Started]: Delete if there are existing Gift List and Create a new Gift list')
    uMyGifts.com.checkAndDelete(page)
    uMyGifts.com.createNewGiftList(page, dRegMyGifts.AUTO1062.dictData)
    uCommon.log(0, '[Pre-condition Completed]: Giftlist is created')
    
    uCommon.log(0, 'Step 3 - Click the kebab menu on the gift list and click Edit Gift List.')
    uCommon.log(0, 'Step 4 - Edit the details of the gift list and click Update Gift List button.')
    uCommon.log(0, 'Step 5 - Click the Gift List that was edited and very the details.')
    uMyGifts.com.clickEditUpdateAndVerifyGL(page, dRegMyGifts.AUTO1062.dictData["strEditOccassion"], dRegMyGifts.AUTO1062.dictData["strEditAbout"])
    uCommon.log(0, 'Test case completed')


""" Author: jatregenio_20231225 Execution Time: 1m 13s - 1m 19s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@pytest.mark.thisTest()
@allure.step('To verify that user is able to remove item from gift list.')
def test_ACQ_AUTO_1065_User_should_be_able_to_remove_an_item_from_gift_list(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName5)
    
    uCommon.log(0, 'Step 2 - Navigate to Profile tab > Gift Registry.')
    uMyGifts.com.clickGiftBox(page, 'opt')
    
    uCommon.log(0, '[Pre-condition Started]: Delete if there are existing Gift List. Create and add new items to the Gift List')
    uMyGifts.com.checkAndDelete(page)
    uMyGifts.com.createGLandAddProduct(page, dRegMyGifts.AUTO1065.dictData)
    uCommon.log(0, '[Pre-condition Completed]: Giftlist is created with gift items')
    
    uCommon.log(0, 'Step 3 - Click the kebab menu on the product and click the Remove from Gift List.')
    uMyGifts.com.deleteProductFromGiftList(page)
    uCommon.log(0, 'Test case completed')
    

""" Author: jatregenio_20240111 Execution Time: 33s - 35s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@pytest.mark.thisTest()
@allure.step('To verify that user is able to delete the gift list.')
def test_ACQ_AUTO_1068_User_should_be_able_to_remove_the_gift_list(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName6)
    
    uCommon.log(0, 'Step 2 - Navigate to Profile tab > Gift Registry and click a gift list.')
    uMyGifts.com.clickGiftBox(page, 'opt')
    
    uCommon.log(0, '[Pre-condition Started]: Create a Gift List. Click either, Plus sign button for users without existing gift lists or Create a Gift List button.')
    uMyGifts.com.getCountAndCreateGL(page, dRegMyGifts.AUTO1068.dictData)
    uCommon.log(0, '[Pre-condition Completed]: Giftlist is created with gift items')
    
    uCommon.log(0, 'Step 3 - Click the kebab menu on the upper right of the screen and click the Remove Gift List.')
    uMyGifts.com.deleteGiftList(page)
    
    uCommon.log(0, 'Step 4 - Verify the result.')
    uMyGifts.com.verifyIfGLIsRemoved(page, dRegMyGifts.AUTO1068.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: jatregenio_20240105 Execution Time: 26s - 28s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@pytest.mark.thisTest()
@allure.step('To verify that the user should not be able to create a gift list if mandatory fields are blank.')
def test_ACQ_AUTO_1071_User_should_not_be_able_to_create_a_gift_list_when_mandatory_fields_are_blank(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName7)
    
    uCommon.log(0, 'Step 2 - Click a gift list.')
    uMyGifts.com.clickGiftBox(page, 'opt')
    
    uCommon.log(0, 'Step 3 - Click either: Plus sign button for users without existing gift lists or Create a Gift List button.')
    uCommon.log(0, 'Step 4 - Do not select a photo cover and do not enter event details. Click Create Gift List button.')
    uMyGifts.com.getCountAndCreateGL(page, dRegMyGifts.AUTO1071.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: jatregenio_20240113 Execution Time: 00s - 00s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@pytest.mark.thisTest()
@allure.step('To verify that the user should not be able to create a gift list without selecting an address.')
def test_ACQ_AUTO_1074_User_should_not_be_able_to_create_a_gift_list_when_mandatory_fields_are_blank(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName8)
    
    uCommon.log(0, '[Pre-condition Started]: Delete existing address and delete if there are existing Gift List.')
    uAppComm.com.navigateToProfileMenu(page, dRegMyGifts.AUTO1074.strMyProfile)
    uMyProfile.com.deleteAllAddress(page)
    uCommon.log(0, '[Pre-condition Completed]: All existing address were deleted successfully.')
    
    uCommon.log(0, 'Step 2 - Click a gift list.')
    uMyGifts.com.clickGiftBox(page, 'opt')
    
    uCommon.log(0, 'Step 3 - Click Create a Gift List button.')
    uMyGifts.com.getCountAndCreateGL(page, dRegMyGifts.AUTO1074.dictData)
    
    uCommon.log(0, '[Post-condition Started]: Add the previous address.')
    uAppComm.com.navigateToProfileMenu(page, dRegMyGifts.AUTO1074.strMyProfile)
    uMyProfile.com.clickAddressAddMore(page)
    uMyProfile.na.addAddress(page, dRegMyGifts.AUTO1074.dictData)
    uMyProfile.na.clickAddNewAddress(page)
    uMyProfile.com.clickAddressAddMore(page)
    uMyProfile.na.addAddress(page, dRegMyGifts.AUTO1074.dictData2)
    uMyProfile.na.clickAddNewAddress(page)
    uCommon.log(0, '[Post-condition Completed]: Address were added successfully.')
    uCommon.log(0, 'Test case completed')