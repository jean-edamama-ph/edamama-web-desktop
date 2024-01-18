import pytest
import allure

import libraries.data.common as dCommon
import libraries.data.regressionTestSuite.profile.myWishlist as dRegMyWishlist

import libraries.util.appCommon.appComm as uAppComm
import libraries.util.common as uCommon
import libraries.util.profile.myWishlist as uMyWishlist
import libraries.util.shop as uShop

""" Author: cgrapa_20230613 Execution Time: 30s - 34s """
@pytest.mark.regressionTestSuite()
@allure.step('To verify that the user is able to add items to their wishlist via PDP')
def test_AUTO_889_User_should_be_able_to_add_items_to_their_wishlist_via_PDP(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page)
    
    uCommon.log(0, 'Step 2 to 3 - Navigate to Profile >> My Wishlist')
    uAppComm.com.navigateToProfileMenu(page, dRegMyWishlist.com.strMyWishlist)
    uMyWishlist.com.validateWishlistAndRemoveSameItem(page, dRegMyWishlist.AUTO889.strItemName)
    
    uCommon.log(0, 'Step 4 - Search and open an item')
    uShop.sp.searchName(page, dRegMyWishlist.AUTO889.strItemName)
    dictData = uShop.lp.getItemDetailsAndClick(page, dRegMyWishlist.AUTO889.strItemName)
    
    uCommon.log(0, 'Step 5 - Click the heart icon')
    uShop.pp.addItemToWishlist(page)
    uAppComm.error.validatePopUpMsg(page, dRegMyWishlist.com.strAddedMsg)
    
    uCommon.log(0, 'Step 6 - Verify that item is added to My Wishlist')
    uAppComm.com.navigateToProfileMenu(page, dRegMyWishlist.com.strMyWishlist)
    uMyWishlist.com.validateAddedWishlistItem(page, dRegMyWishlist.AUTO889.strItemName, dictData)
    uCommon.log(0, 'Test Completed')


""" Author: cgrapa_20230613 Execution Time: 22s - 26s """
@pytest.mark.regressionTestSuite()
@allure.step('To verify that the user is able to add items to their wishlist via Shop page')
def test_AUTO_892_User_should_be_able_to_add_items_to_their_wishlist_via_Shop_page(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page)
    
    uCommon.log(0, 'Step 2 to 3 - Navigate to Profile >> My Wishlist')
    dictData = uShop.sp.getShopItemDetails(page, dRegMyWishlist.AUTO892.strShopSection)
    uAppComm.com.navigateToProfileMenu(page, dRegMyWishlist.com.strMyWishlist)
    uMyWishlist.com.validateWishlistAndRemoveSameItem(page, dictData['strName'])
    
    uCommon.log(0, 'Step 4 - Navigate back to homepage and click heart icon')
    uShop.com.clickShop(page)
    uShop.sp.addShopItemToWishlist(page, dRegMyWishlist.AUTO892.strShopSection)
    uAppComm.error.validatePopUpMsg(page, dRegMyWishlist.com.strAddedMsg)
    
    uCommon.log(0, 'Step 5 - Verify that item is added to My Wishlist')
    uAppComm.com.navigateToProfileMenu(page, dRegMyWishlist.com.strMyWishlist)
    uMyWishlist.com.validateAddedWishlistItem(page, dictData['strName'], dictData)
    uCommon.log(0, 'Test Completed')


""" Author: cgrapa_20230613 Execution Time: 33s - 37s """
@pytest.mark.regressionTestSuite()
@allure.step('To verify that the item via PDP is removed from the wishlist')
def test_AUTO_895_User_should_be_able_to_remove_items_from_their_wishlist_via_PDP(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName7, dCommon.user.strPassword1)
    
    uCommon.log(0, '[Precondtion Started] - Add item to Wishlist')
    uShop.sp.searchName(page, dRegMyWishlist.AUTO895.strItemName)
    dictData = uShop.lp.getItemDetailsAndClick(page, dRegMyWishlist.AUTO895.strItemName)
    uShop.pp.addItemToWishlist(page)
    uAppComm.error.validatePopUpMsg(page, dRegMyWishlist.com.strAddedMsg)
    uCommon.log(0, '[Precondtion Completed] - Add item to Wishlist successful')
    
    uCommon.log(0, 'Step 2 to 3 - Navigate to Profile >> My Wishlist')
    uAppComm.com.navigateToProfileMenu(page, dRegMyWishlist.com.strMyWishlist)
    uMyWishlist.com.validateAddedWishlistItem(page, dRegMyWishlist.AUTO895.strItemName, dictData)
    
    uCommon.log(0, 'Step 4 to 5 -  Take note of item in Wishlist >> Click the product')
    uMyWishlist.com.clickItemAndValidatePdp(page, dictData)

    uCommon.log(0, 'Step 6 - Click the heart icon')
    uShop.pp.removeItemFromWishlist(page)
    uAppComm.error.validatePopUpMsg(page, dRegMyWishlist.com.strRemovedMsg)
    
    uCommon.log(0, 'Step 6 - Verify that item is removed in My Wishlist')
    uAppComm.com.navigateToProfileMenu(page, dRegMyWishlist.com.strMyWishlist)
    uMyWishlist.com.validateRemovedWishlistItem(page, dRegMyWishlist.AUTO895.strItemName)
    uCommon.log(0, 'Test Completed')


""" Author: cgrapa_20230613 Execution Time: 24s - 28s """
@pytest.mark.regressionTestSuite()
@allure.step('To verify that the item via shop page is removed from the wishlist')
def test_AUTO_898_User_should_be_able_to_remove_items_from_their_wishlist_via_Shop_page(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName7, dCommon.user.strPassword1)
    
    uCommon.log(0, '[Precondtion Started] - Add item to Wishlist')
    dictData = uShop.sp.getShopItemDetails(page, dRegMyWishlist.AUTO898.strShopSection)
    uShop.sp.addShopItemToWishlist(page, dRegMyWishlist.AUTO898.strShopSection)
    uAppComm.error.validatePopUpMsg(page, dRegMyWishlist.com.strAddedMsg)
    uCommon.log(0, '[Precondtion Completed] - Add item to Wishlist successful')
    
    uCommon.log(0, 'Step 2 to 3 - Navigate to Profile >> My Wishlist')
    uAppComm.com.navigateToProfileMenu(page, dRegMyWishlist.com.strMyWishlist)
    uMyWishlist.com.validateAddedWishlistItem(page, dictData['strName'], dictData)
    
    uCommon.log(0, 'Step 4 to 5 -  Take note of item in Wishlist >> Click the product')
    uShop.com.clickShop(page)
    uShop.sp.removeShopItemFromWishlist(page, dRegMyWishlist.AUTO898.strShopSection)
    uAppComm.error.validatePopUpMsg(page, dRegMyWishlist.com.strRemovedMsg)
    
    uCommon.log(0, 'Step 6 - Verify that item is removed in My Wishlist')
    uAppComm.com.navigateToProfileMenu(page, dRegMyWishlist.com.strMyWishlist)
    uMyWishlist.com.validateRemovedWishlistItem(page, dictData['strName'])
    uCommon.log(0, 'Test Completed')


""" Author: cgrapa_20230613 Execution Time: 26s - 30s """
@pytest.mark.regressionTestSuite()
@allure.step('To verify that the user is able to remove product from the wishlist')
def test_AUTO_901_User_should_be_able_to_remove_product_from_the_wishlist(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page)
    
    uCommon.log(0, '[Precondtion Started] - Add item to Wishlist')
    uShop.sp.searchName(page, dRegMyWishlist.AUTO901.strItemName)
    dictData = uShop.lp.getItemDetailsAndClick(page, dRegMyWishlist.AUTO901.strItemName)
    uShop.pp.addItemToWishlist(page)
    uAppComm.error.validatePopUpMsg(page, dRegMyWishlist.com.strAddedMsg)
    uCommon.log(0, '[Precondtion Completed] - Add item to Wishlist successful')
    
    uCommon.log(0, 'Step 2 to 3 - Navigate to Profile >> My Wishlist')
    uAppComm.com.navigateToProfileMenu(page, dRegMyWishlist.com.strMyWishlist)
    uMyWishlist.com.validateAddedWishlistItem(page, dRegMyWishlist.AUTO901.strItemName, dictData)
    
    uCommon.log(0, 'Step 4 - Remove item from My Wishlist')
    uMyWishlist.com.removeItemOnMyWishlist(page, dictData['strName'])
    uAppComm.error.validatePopUpMsg(page, dRegMyWishlist.com.strRemovedItemMsg)
    uMyWishlist.com.validateRemovedWishlistItem(page, dRegMyWishlist.AUTO901.strItemName)
    uCommon.log(0, 'Test Completed')


""" Author: rmakiling_20231005 Execution Time:  """
@pytest.mark.regressionTestSuite()
@allure.step('To verify that the user is able to view the Product Detail via My Wishlist page.')
def test_AUTO_1037_User_should_be_able_to_view_product_detail_via_my_wishlist_page(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName1)

    uCommon.log(0, '[Pre-condition Started]: Add product to wishlist')
    dictData = uShop.sp.getShopItemDetails(page, dRegMyWishlist.AUTO1037.strShopSection)
    uShop.sp.addShopItemToWishlist(page, dRegMyWishlist.AUTO1037.strShopSection)
    uAppComm.error.validatePopUpMsg(page, dRegMyWishlist.com.strAddedMsg)
    uCommon.log(0, '[Pre-condition Completed]: - Add item to Wishlist successful')

    uCommon.log(0, 'Step 2 - Navigate to Profile tab >> My wishlist')
    uAppComm.com.navigateToProfileMenu(page, dRegMyWishlist.com.strMyWishlist)
    uMyWishlist.com.validateAddedWishlistItem(page, dictData['strName'], dictData)

    uCommon.log(0, 'Step 3 - Click Product Card of the recently added product to wishlist')
    uMyWishlist.com.clickItemAndValidatePdp(page, dictData)

    uCommon.log(0, '[Post condition Started]: Remove item from My Wishlist')
    uAppComm.com.navigateToProfileMenu(page, dRegMyWishlist.com.strMyWishlist)
    uMyWishlist.com.removeItemOnMyWishlist(page, dictData['strName'])
    uAppComm.error.validatePopUpMsg(page, dRegMyWishlist.com.strRemovedItemMsg)
    uMyWishlist.com.validateRemovedWishlistItem(page, dRegMyWishlist.AUTO1037.strItemName)
    uCommon.log(0, '[Post condition Completed]: Item remove from the My Wishlist')






    

 

