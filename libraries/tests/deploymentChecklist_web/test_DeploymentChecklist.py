import pytest
import allure

import libraries.data.common as dCommon
import libraries.data.deploymentChecklist as dDepChkLst
import libraries.data.regressionTestSuite.loginAndSignUp.signup as dRegSignUp

import libraries.util.appCommon.adminKpc as uAdminKpc
import libraries.util.appCommon.appComm as uAppComm
import libraries.util.common as uCommon
import libraries.util.profile.myOrders as uMyOrders
import libraries.util.cart as uCart
import libraries.util.shop as uShop
import libraries.util.tcTest as uTcTest
import libraries.util.profile.myProfile as uMyProfile
import libraries.util.profile.myGifts as uMyGifts
import libraries.util.appCommon.email as uEmail
import libraries.util.checkOut as uCheckOut
import libraries.util.profile.mySubscription as uMySubscription
import libraries.util.discover as uDiscover
import libraries.util.appCommon.signUp as uSignUp

    
""" Author: ccapistrano_20230322 Execution Time: 31s - 55s  """
@pytest.mark.deploymentChecklist()
@allure.step('Missing Objective')
def test_AUTO_206_Guest_Checkout_COD(page):
    uCommon.log(0, 'Step 1 - Go to https://www.edamama.ph/')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - Select an item/product. Click "Add to Bag"')
    uShop.sp.validateFeaturedProducts(page)
    dictDetails = uShop.sp.getShopItemDetails(page, dDepChkLst.AUTO206.strShopSection)
    uShop.sp.clickFPfirstItem(page)
    uShop.pp.validateProductForm(page)
    uAppComm.com.validateWebHeaderTabsAdFooter(page, False)
    uShop.pp.validateDetails(page, dictDetails)
    uShop.pp.clickAddToBag(page, 'opt')
    
    uCommon.log(0, 'Step 3 - Go to bag icon on the upper right corner of the screen')
    uAppComm.com.validateCountInCart(page, dDepChkLst.AUTO206.strCount)
    uAppComm.com.clickCartCount(page)

    uCommon.log(0, 'Step 4 - Click "Checkout" button')
    uCart.validateMyCartAndOrderDetails(page)
    uAppComm.com.validateWebHeaderAndFooter(page, False)
    uCart.validateYouHaveXProduct(page)
    uCart.validateMyCartdetails(page, dictDetails, dDepChkLst.AUTO206.strCount)
    uCart.clickCheckOut(page)
    uAppComm.ln.validateLoginPage(page)
    uCommon.log(0, 'Test case completed')
    

""" Author: ccapistrano_20230427 Execution Time: 1m 5s - 1m 40s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify that user can purchase and pay using Cash On Delivery and available beans - SNS')
def test_AUTO_417_SNS_Test_Purchase_COD_plus_beans(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName2)

    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO417.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230427 Execution Time: 1m 15s - 1m 52s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify that user can purchase and pay using Cash On Delivery and applied coupon - SNS')
def test_AUTO_422_SNS_Test_Purchase_COD_plus_1_edamama_Coupon(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName3)
    
    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO422.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230427 Execution Time: 1m 11s - 2m 1s """
@pytest.mark.deploymentChecklist()
@allure.step('Verifying that user can purchase and pay using Cash On Delivery with applied BEANBACK COUPON - SNS')
def test_AUTO_427_SNS_Test_Purchase_COD_plus_BEANBACK_COUPON(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName4)
    
    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO427.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230427 Execution Time: 1m 9s - 1m 54s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify that user can purchase and pay using Cash On Delivery with applied brand and edamama coupon - SNS')
def test_AUTO_432_SNS_Test_Purchase_COD_plus_1_Brand_plus_1_Edamama_coupon(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName5)
    
    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO432.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230502 Execution Time: 1m 23s - 1m 31s """
@pytest.mark.deploymentChecklist()
@allure.step('Verifying that user can purchase and pay using CC - SNS')
def test_AUTO_437_SNS_Test_Purchase_CC(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName6)
    
    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO437.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230502 Execution Time: 1m 2s - 1m 10s """
@pytest.mark.deploymentChecklist()
@allure.step('Verifying that user can purchase and pay using CC + beans - SNS')
def test_AUTO_442_SNS_Test_Purchase_CC_plus_beans(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName7)
    
    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO442.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230502 Execution Time: 1m 27s - 1m 46s """
@pytest.mark.deploymentChecklist()
@allure.step('Verifying that user can purchase and pay using CC with applied Brand coupon - SNS')
def test_AUTO_447_SNS_Test_Purchase_CC_Brand_Coupon(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName8)
    
    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO447.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230502 Execution Time: 57s - 1m 34s """
@pytest.mark.deploymentChecklist()
@allure.step('Verifying that user can purchase and pay using GCASH - SNS')
def test_AUTO_452_SNS_Test_Purchase_GCASH(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName9)

    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO452.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230502 Execution Time: 49s - 1m 26s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify that the user should be able to checkout with using gcash and their available beans. - SNS')
def test_AUTO_457_SNS_Test_Purchase_GCASH_plus_beans(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName10)
    
    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO457.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230502 Execution Time: 1m 14s - 1m 26s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify that the user should be able to checkout with using gcash and a beanback coupon. - SNS')
def test_AUTO_462_SNS_Test_Purchase_GCASH_plus_BEANBACK_COUPON(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName1)
    
    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO462.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230502 Execution Time: 1m 11s - 1m 29s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify that the user should be able to checkout with using gcash and adding a brand coupon. Brand coupon should only be used for items from the brand')
def test_AUTO_467_SNS_Test_Purchase_GCASH_plus_Brand_coupon(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials - SNS')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName2)

    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO467.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230503 Execution Time: 1m 9s - 1m 14s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify that the user should be able to checkout with using GrabPay - SNS')
def test_AUTO_472_SNS_Test_Purchase_GrabPay(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName3)

    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO472.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230503 Execution Time: 59s - 1m 12s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify that the user should be able to checkout with using GrabPay and their available beans - SNS')
def test_AUTO_477_SNS_Test_Purchase_GrabPay_plus_beans(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName4)
    
    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO477.dictData)
    uCommon.log(0, 'Test case completed')
    

""" Author: ccapistrano_20230503 Execution Time: 1m 27s - 1m 30s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify that the user should be able to checkout with using GrabPay and adding a coupon - SNS')
def test_AUTO_482_SNS_Test_Purchase_GrabPay_plus_coupon(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName5)
    
    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO482.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230503 Execution Time: 1m 33s - 1m 36s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify that the user should be able to checkout with using Maya - SNS')
def test_AUTO_487_SNS_Test_Purchase_Maya(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName6)
    
    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO487.dictData)
    uCommon.log(0, 'Test case completed')
    

""" Author: ccapistrano_20230503 Execution Time: 1m 12s - 1m 25s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify that the user should be able to checkout with using Maya and their available beans - SNS')
def test_AUTO_492_SNS_Test_Purchase_Maya_plus_beans(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName7)
    
    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO492.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230503 Execution Time: 1m 22s - 1m 39s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify if user should be able to checkout using Maya and with Maya Coupon - SNS')
def test_AUTO_497_SNS_Test_Purchase_Maya_plus_Maya_coupon(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName8)
    
    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO497.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230504 | Execution Time: 1m 25s - 5m 17s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify the if Admin Panel should be able to create a Discount Scheduler with RS discount type')
def test_AUTO_617_Create_DS_RS_in_Admin_Panel(page):
    uCommon.log(0, 'Step 1 - 18 - Create Discount Scheduler')
    dictDetails = uAdminKpc.ds.createDiscountScheduler(page, dDepChkLst.AUTO617.strName, dDepChkLst.AUTO617.strPath, dDepChkLst.AUTO617.strType)

    uCommon.log(0, 'Step 19 - Verify the recently created discount scheduler')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName9)
    uShop.sp.searchAndClickItem(page, dictDetails['strProductName'])
    uShop.pp.validateDiscountRate(page, dictDetails)
    uCommon.log(0, 'Test case completed')
    

""" Author: ccapistrano_20230504 | Execution Time: 51s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify the if Admin Panel should be able to create a Discount Scheduler with SNS discount type')
def test_AUTO_618_Create_DS_SNS_in_Admin_Panel(page):
    uCommon.log(0, 'Step 1 - 18 - Create Discount Scheduler')
    dictDetails = uAdminKpc.ds.createDiscountScheduler(page, dDepChkLst.AUTO618.strName, dDepChkLst.AUTO618.strPath, dDepChkLst.AUTO618.strType)
    
    uCommon.log(0, 'Step 19 - Verify the recently created discount scheduler')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName10)
    uShop.sp.searchAndClickItem(page, dictDetails['strProductName'])
    uShop.pp.validateDiscountRate(page, dictDetails)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230504 | Execution Time: 1m 24s - 1m 38s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify the if Admin Panel should be able to create a Flash Sale')
def test_AUTO_616_Create_FS_in_Admin_Panel(page):
    uCommon.log(0, 'Step 1 - 18 - Create Flash Sale')
    uAdminKpc.fs.createFlashSale(page, dDepChkLst.AUTO616.strName, dDepChkLst.AUTO616.strPath)
    
    uCommon.log(0, 'Step 19 - Verify the recently created Flash Sale')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName1)
    uShop.sp.validateFlashSale(page)
    uCommon.log(0, 'Test case completed')
    

""" Author: ccapistrano_20230508 | Execution Time: 1m 24s - 1m 44s """
@pytest.mark.deploymentChecklist()
@allure.step('Verifying if the admin panel user can update a product')
def test_AUTO_619_Update_Product_Admin_Panel_Listing(page):
    uCommon.log(0, 'Step 1 to 3 - Go to admin panel website and login')
    uAppComm.ln.loginToAdminKPC(page)
    
    uCommon.log(0, 'Step 4 to 5 - Click Products from the side navigation bar')
    uAdminKpc.pl.clickProductsThenSubMenu(page)
    
    uCommon.log(0, 'Step 6 - Click edit button of a specific product')
    uAdminKpc.pl.searchProduct(page, dDepChkLst.AUTO619.strName)
    uAdminKpc.pl.clickEditIcon(page)
    window = uCommon.switchToWindow(page)
    
    uCommon.log(0, 'Step 7 - Update Product Name')
    uAdminKpc.pl.bi.setProductName(window, dDepChkLst.AUTO619.dictData["strName"])
    
    uCommon.log(0, 'Step 8 - Click Update And Continue button')
    uAdminKpc.pl.bi.clickUpdateAndContinue(window)
    
    uCommon.log(0, 'Step 9 - Update Color')
    uAdminKpc.pl.cv.checkAndDeleteColor(window, dDepChkLst.AUTO619.dictData["strColor"])
    uAdminKpc.pl.cv.addColor(window, dDepChkLst.AUTO619.dictData["strColor"], dDepChkLst.AUTO619.strPath)
    
    uCommon.log(0, 'Step 10 - Click Update And Continue button')
    uAdminKpc.pl.cv.clickUpdateAndContinue(window)
    
    uCommon.log(0, 'Step 11 - Update MRP')
    uAdminKpc.pl.sp.setMRPpriceViaVariantname(window, dDepChkLst.AUTO619.dictData["strColor"], dDepChkLst.AUTO619.dictData["strPrice"])
    
    uCommon.log(0, 'Step 12 - Click Update And Continue button')
    uAdminKpc.pl.sp.clickUpdateAndContinue(window)
    
    uCommon.log(0, 'Step 13 to 14 - Click Save button')
    uAdminKpc.pl.at.clickSave(window)
    
    uCommon.log(0, 'Step 15 - Verify the recently updated product')
    uAppComm.ln.loginToEdamama(window, dCommon.user.strUserName2)
    # uShop.sp.searchAndClickItem(window, dDepChkLst.AUTO619.dictData["strName']) #Issue in Algolia replication
    uShop.sp.searchAndClickItem(window, dDepChkLst.AUTO619.strName)
    uShop.pp.clickColorBtn(window, dDepChkLst.AUTO619.dictData["strColor"])
    dDepChkLst.AUTO619.dictData["strPrice"] = f'₱{dDepChkLst.AUTO619.dictData["strPrice"]}.00'
    uShop.pp.validateDetails(window, dDepChkLst.AUTO619.dictData)
    uCommon.log(0, 'Test case completed')

    uCommon.log(0, 'Test Data revert')
    uCommon.closeWindow(page)
    uAdminKpc.pl.searchProduct(page, dDepChkLst.AUTO619.dictData["strName"])
    uAdminKpc.pl.clickEditIcon(page)
    window = uCommon.switchToWindow(page)
    uAdminKpc.pl.bi.setProductName(window, dDepChkLst.AUTO619.strName)
    uAdminKpc.pl.bi.clickUpdateAndContinue(window)
    uAdminKpc.pl.cv.deleteColor(window, dDepChkLst.AUTO619.dictData["strColor"])
    uAdminKpc.pl.cv.clickUpdateAndContinue(window)
    uCommon.log(0, 'Test Data revert completed')
    
    
""" Author: ccapistrano_20230508 | Execution Time: 3m 27s """
@pytest.mark.deploymentChecklist()
@allure.step('Verifying if the user can unpublished a published product in Admin Panel')
def test_AUTO_622_Unpublished_Product_Admin_Panel_Listing(page):
    uCommon.log(0, 'Step 1 to 3 - Go to admin panel website and login')
    uAppComm.ln.loginToAdminKPC(page)
    
    uCommon.log(0, 'Step 4 to 5 - Click Products from the side navigation bar')
    uAdminKpc.pl.clickProductsThenSubMenu(page)
    
    uCommon.log(0, 'Step 6 - Click edit button of a specific product')
    uAdminKpc.pl.searchProduct(page, dDepChkLst.AUTO622.strName)
    uAdminKpc.pl.clickEditIcon(page)
    window = uCommon.switchToWindow(page)
    
    uCommon.log(0, 'Step 7 - Click Next button')
    uAdminKpc.pl.bi.clickNext(window)
    
    uCommon.log(0, 'Step 8 - Click Next button')
    uAdminKpc.pl.cv.clickNext(window)
    
    uCommon.log(0, 'Step 9 to 10 - Click the toggle button of published field')
    uAdminKpc.pl.sp.clickPublished(window)
    uAdminKpc.pl.sp.clickUpdateAndContinue(window)
    
    uCommon.log(0, 'Step 11 - Click Save button')
    uAdminKpc.pl.at.clickSave(window)
    
    uCommon.log(0, 'Step 12 - Verify the recently updated product')
    uAppComm.ln.loginToEdamama(window, dCommon.user.strUserName3)
    uShop.sp.searchAndWaitItem(window,dDepChkLst.AUTO622.strName, dDepChkLst.AUTO622.blnNotVisible)
    uCommon.closeWindow(page)
    uAdminKpc.pl.searchProduct(page, dDepChkLst.AUTO622.strName)
    uAdminKpc.pl.validatepublished(page, dDepChkLst.AUTO622.blnNotVisible)
    uCommon.log(0, 'Test case completed')

    
    uCommon.log(0, 'Test Data revert')
    uAdminKpc.pl.clickEditIcon(page)
    window = uCommon.switchToWindow(page)
    uAdminKpc.pl.bi.clickNext(window)
    uAdminKpc.pl.cv.clickNext(window)
    uAdminKpc.pl.sp.clickPublished(window)
    uAdminKpc.pl.sp.clickUpdateAndContinue(window)
    uAdminKpc.pl.at.clickSave(window)
    uCommon.log(0, 'Test Data revert completed')


""" Author: ccapistrano_20230509 | Execution Time: 59s """
@pytest.mark.deploymentChecklist()
@allure.step('Verifying if the admin panel user can block a product')
def test_AUTO_620_Block_Product_Admin_Panel_Listing(page):
    uCommon.log(0, 'Step 1 to 3 - Go to admin panel website and login')
    uAppComm.ln.loginToAdminKPC(page)
    
    uCommon.log(0, 'Step 4 to 5 - Click Products from the side navigation bar')
    uAdminKpc.pl.clickProductsThenSubMenu(page)
    
    uCommon.log(0, 'Step 6 to 7 - Click the block button of a specific product >> Click Yes button')
    uAdminKpc.pl.searchProduct(page, dDepChkLst.AUTO620.strName)
    if uAdminKpc.pl.isProductBlockOrUnBlock(page) == 'unblock':
        uCommon.log(0, '[Precondition Started]: Unblock Product')
        uAdminKpc.pl.blockOrUnblockProduct(page, False)
        uCommon.log(0, '[Precondition Completed]: Product is now Unblocked')
    uAdminKpc.pl.blockOrUnblockProduct(page)
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName4)
    uShop.sp.searchAndWaitItem(page, dDepChkLst.AUTO620.strName, dDepChkLst.AUTO620.blnNotVisible)

    uCommon.goToURL(page, dCommon.url.strAdminUrl)
    uCommon.wait(page, 1)
    uAdminKpc.pl.clickProductsThenSubMenu(page)
    uAdminKpc.pl.searchProduct(page, dDepChkLst.AUTO620.strName)
    uCommon.log(0, 'Test case completed')

    uCommon.log(0, '[Post condition Started]: Unblock Product')
    uAdminKpc.pl.blockOrUnblockProduct(page, False)
    uCommon.log(0, '[Post condition Completed]: Product is now Unblocked')


""" Author: ccapistrano_20230509 | Execution Time: 6m 55s """
# NOTE: https://edamama.atlassian.net/browse/FIND-535
@pytest.mark.deploymentChecklist()
@allure.step('Verifying that the admin panel user can add a product')
def test_AUTO_635_Add_New_Product_in_Admin_Panel_Listing(page):
    uCommon.log(0, 'Step 1 to 3 - Go to admin panel website and login')
    uAppComm.ln.loginToAdminKPC(page)
    
    uCommon.log(0, 'Step 4 to 5 - Click Products from the side navigation bar')
    uAdminKpc.pl.clickProductsThenSubMenu(page)
    
    uCommon.log(0, 'Step 6 - Click add button')
    uAdminKpc.pl.clickAdd(page)
    
    uCommon.log(0, 'Step 7 - Populate the following required fields with valid values')
    uAdminKpc.pl.bi.setProductName(page, dDepChkLst.AUTO635.dictData["strName"])
    uAdminKpc.pl.bi.selectCategory(page, dDepChkLst.AUTO635.dictData["strCategory"])
    uAdminKpc.pl.bi.selectBrand(page, dDepChkLst.AUTO635.dictData["strBrand"])
    uAdminKpc.pl.bi.selectVendor(page, dDepChkLst.AUTO635.dictData["strVendor"])
    uAdminKpc.pl.bi.selectBundleBuy(page, dDepChkLst.AUTO635.dictData["strBundleBuy"])
    uAdminKpc.pl.bi.selectAttributes(page, dDepChkLst.AUTO635.dictData["strAttributes"])
    uAdminKpc.pl.bi.setDescriptionAndSpecification(page, 'test description', 'test specification')

    uCommon.log(0, 'Step 8 - Click save and continue button')
    uAdminKpc.pl.bi.clickSaveAndContinue(page)
    
    uCommon.log(0, 'Step 9 to 13 - Select a color in Color dropdown field >> Click Add color button')
    uAdminKpc.pl.cv.addColor(page, dDepChkLst.AUTO635.dictData["strColor"], dDepChkLst.AUTO635.dictData["strPath"])

    uCommon.log(0, 'Step 14 to 18 - Select a pattern in Pattern dropdown field >> Click Add Add pattern button')
    
    uCommon.log(0, 'Step 19 - Populate the following fields in Variant')
    uAdminKpc.pl.cv.selectVariant(page, dDepChkLst.AUTO635.dictData["strVariant"])
    uAdminKpc.pl.cv.selectDisplayType(page, dDepChkLst.AUTO635.dictData["strDisplayType"])
    uAdminKpc.pl.cv.selectSelectTypeOptions(page, dDepChkLst.AUTO635.dictData["strTypeOptions"])
    
    uCommon.log(0, 'Step 20 - Click Add Variant button')
    uAdminKpc.pl.cv.clickAddVariant(page)
    
    uCommon.log(0, 'Step 21 - Populate the following fields in Filter')
    uAdminKpc.pl.cv.selectSelectFilters(page, dDepChkLst.AUTO635.dictData["strSelectFilters"]) # DEFECT ON AP - https://edamama.atlassian.net/browse/AUTO-728
    uAdminKpc.pl.cv.selectFiltersOptions(page, dDepChkLst.AUTO635.dictData["strFiltersOptions"])
    
    uCommon.log(0, 'Step 22 - Click Add Filters button')
    uAdminKpc.pl.cv.clickAddFilters(page)
    
    uCommon.log(0, 'Step 23 - Click Update and Continue button')
    uAdminKpc.pl.cv.clickUpdateAndContinue(page)
    
    uCommon.log(0, 'Step 24 - Click Published toggle button')
    uAdminKpc.pl.sp.setMRPpriceViaVariantname(page, dDepChkLst.AUTO635.dictData["strColor"], dDepChkLst.AUTO635.dictData["strPrice"])
    uAdminKpc.pl.sp.clickPublished(page)
    
    uCommon.log(0, 'Step 25 - Click Next button')
    uAdminKpc.pl.sp.clickUpdateAndContinue(page)
    
    uCommon.log(0, 'Step 26 - Click Save button')
    uAdminKpc.pl.at.clickSave(page)
    
    uCommon.log(0, 'Step 27 - Verify the recently added product')
    uAdminKpc.pl.searchProduct(page, dDepChkLst.AUTO635.dictData["strName"])
    uAdminKpc.pl.validatepublished(page, dDepChkLst.AUTO635.dictData["blnVisible"])
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName5)
    uShop.sp.searchAndWaitItem(page,dDepChkLst.AUTO635.dictData["strName"], dDepChkLst.AUTO635.dictData["blnVisible"])
    
    uCommon.log(0, 'Test Data delete')
    # test_AUTO_621_Delete_Product_Admin_Panel_Listing
    uCommon.goToURL(page, dCommon.url.strAdminUrl)
    uCommon.wait(page, 1)
    uAdminKpc.pl.clickProductsThenSubMenu(page)
    uAdminKpc.pl.searchProduct(page, dDepChkLst.AUTO635.dictData["strName"])
    uAdminKpc.pl.deleteProduct(page)
    uCommon.log(0, 'Test Data delete completed')


""" Author: ccapistrano_20230510 | Execution Time: 1m 50s """
# NOTE: https://edamama.atlassian.net/browse/OPS-530
@pytest.mark.deploymentChecklist()
@allure.step('Verify that admin can do a mass cancellation in AP')
def test_AUTO_676_Mass_Cancellation_Admin(page):
    uCommon.log(0, '[Precondtion Started] - Create 2 Order ID')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName6)
    strOrderID1 = uTcTest.validateE2EMOP(page, dDepChkLst.AUTO676.dictData)
    uCommon.wait(page, 60)
    uAppComm.ln.goToEdamamaURL(page)
    strOrderID2 = uTcTest.validateE2EMOP(page, dDepChkLst.AUTO676.dictData)

    data = [
            ['order_number', 'reason'],
            [strOrderID1, 'Test Order'],
            [strOrderID2, 'Test Order']
            ]
    uCommon.createFile(dDepChkLst.AUTO676.strPath, data)
    uCommon.log(0, '[Precondtion Completed] - 2 Order ID was successfully created')
    
    uCommon.log(0, 'Step 1 - Navigate to the Admin Panel > Orders')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.od.clickOrders(page)
    
    uCommon.log(0, 'Step 2 - Click the Mass Upload button and select Mass Upload Order Cancellation')
    uAdminKpc.od.clickMassUploadAndSelect(page, dDepChkLst.AUTO676.strOrderCancellation)
    
    uCommon.log(0, 'Step 3 - Select a file and upload the CSV file')
    uAdminKpc.od.uploadMassCancellationFile(page, dDepChkLst.AUTO676.strPath)
    
    uCommon.log(0, 'Step 4 - Click the Upload Order Cancellation button')
    uAdminKpc.od.clickUploadOrderCancellation(page)
    
    uCommon.log(0, 'Step 5 - Search for the OID in the AP and verify if the order was cancelled')
    uAdminKpc.cp.clickCuratedProducts(page)
    uAdminKpc.od.clickOrders(page)
    uAdminKpc.od.validateRetunCancel(page, strOrderID1, 'Canceled By Admin')
    uAdminKpc.od.validateRetunCancel(page, strOrderID2, 'Canceled By Admin')
    
    uCommon.log(0, 'Step 6 - Verify if the order was cancelled on the Customer\'s end. Search for the OID in the My Orders page')
    uAppComm.ln.goToEdamamaURL(page)
    uAppComm.com.navigateToProfileMenu(page, dDepChkLst.AUTO676.strMyOrders)
    # NOTE: DEFECT - Status is not set "Cancelled By Admin in AP" - remove this once fix
    uMyOrders.validateOrderStatus(page, strOrderID1, dDepChkLst.AUTO676.strCancelledByAdmin)
    uMyOrders.validateOrderStatus(page, strOrderID2, dDepChkLst.AUTO676.strCancelledByAdmin)
    
    
""" Author: ccapistrano_20230510 | Execution Time: 1m 5s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify if admin can update tracking number on Orders')
def test_AUTO_671_Upload_Tracking_Number_Admin_Panel(page):
    uCommon.log(0, 'Step 1 - Go to the edamama website/app')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName7)
    
    uCommon.log(0, 'Step 1 to 7 - purchase a product and get Order ID')
    strOrderID = uTcTest.validateE2EMOP(page, dDepChkLst.AUTO671.dictData)

    uCommon.log(0, 'Step 8 - Navigate to the Admin Panel > Orders. Search for the OID and click the OID')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.od.clickOrders(page)
    uCommon.waitAndClickElemText(page, strOrderID)

    uCommon.log(0, 'Step 9 - Click the edit button under the action column for the item that you want to ship')
    window = uCommon.switchToWindow(page)
    uAdminKpc.od.od.pt.clickEdit(window)
    
    uCommon.log(0, 'Step 10 - Select Shipped and enter the ff details: Order Tracking Url, Order Tracking Number, Courier and click update')
    uAdminKpc.od.od.pt.clickAndSelectOrderStatus(window, 'Shipped')
    uAdminKpc.od.od.pt.setTrackingAndCourier(window, 'https.test.com', '12345678', 'Joy Angkas')
    uAdminKpc.od.od.pt.clickUpdate(window)
    uCommon.closeWindow(page)
    
    uCommon.log(0, 'Step 11 - Navigate back to the site/app and verify if the order was shipped')
    uAppComm.ln.goToEdamamaURL(page)
    uAppComm.com.navigateToProfileMenu(page, dDepChkLst.AUTO671.strMyOrders)
    uMyOrders.validateOrderStatus(page, strOrderID, dDepChkLst.AUTO671.strShipped)


""" Author: ccapistrano_20230512 | Execution Time: 1m 21s - 1m 25s """
#Note: Existing issue - https://edamama.atlassian.net/browse/MAR-1214
@pytest.mark.deploymentChecklist()
@allure.step('To verify that the user should be able to edit delivery address (once)')
def test_AUTO_666_Edit_Delivery_Address(page):
    uCommon.log(0, 'Step 1 - Go to the edamama website/app')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName8)
    uCommon.log(0, 'Test Data delete')
    uAppComm.com.navigateToProfileMenu(page, 'my profile')
    uMyProfile.com.deleteAddress(page, f'{dDepChkLst.AUTO666.dictNewAddress["strFName"]} {dDepChkLst.AUTO666.dictNewAddress["strLName"]}')
    uCommon.log(0, 'Test Data delete completed')

    uCommon.log(0, 'Step 1 to 10 - purchase a product and get Order ID')
    strOrderID = uTcTest.validateE2EMOP(page, dDepChkLst.AUTO666.dictData)

    uCommon.log(0, 'Step 11 - Click the Edit Delivery Details button')
    uMyOrders.clickEditDeliveryDetails(page, strOrderID)
    
    uCommon.log(0, 'Step 12 - Add a new address or if there is existing other addresses, select any other address and click Update Delivery Information button')
    uMyOrders.di.clickAddNewAddress(page)
    uMyOrders.di.na.fillOutNewAddress(page, dDepChkLst.AUTO666.dictNewAddress)
    uMyOrders.di.na.clickAddNewAddress(page)
    uMyOrders.di.clickAddresstoBeDeleted(page, f'{dDepChkLst.AUTO666.dictNewAddress["strFName"]} {dDepChkLst.AUTO666.dictNewAddress["strLName"]}')
    uMyOrders.di.clickUpdateDeliveryInfo(page)
    uMyOrders.di.clickConfirm(page)
    uMyOrders.clickEditDeliveryDetails(page, strOrderID, True)
    
    uCommon.log(0, 'Step 13 - Verify that the address was changed via WMS or Admin Panel')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.od.clickOrders(page)
    uCommon.waitAndClickElemText(page, strOrderID)
    window = uCommon.switchToWindow(page)
    uAdminKpc.od.od.validateDeliveryDetails(window, dDepChkLst.AUTO666.dictNewAddress)
    

""" Author: ccapistrano_20230515 | Execution Time: 20s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify if Guest User/Invitee can buy products from shared Gift List')
def test_AUTO_552_Guest_Checkout_GR_not_logged_In(page):
    uCommon.log(0, '[Precondtion Started] - Create and send gift list invitation')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName2)
    uMyGifts.com.clickGiftBox(page, dDepChkLst.AUTO716.blnFirstGL)
    uMyGifts.com.deleteGiftList(page, dDepChkLst.AUTO716.blnCleanUp)
    uMyGifts.com.createGLandAddProduct(page, dDepChkLst.AUTO716.dictDataGift)
    strUrl = uCommon.getURL(page)
    uAppComm.lo.logOutToEdamama(page)
    uCommon.log(0, '[Precondtion Completed] - Create and send gift list invitation was successfully complete')
    
    uCommon.log(0, 'Step 1 - Navigate to Edamama Website/Mobile App')
    uCommon.log(0, 'Step 2 - Paste the GL link in your URL tab then click "enter" key')
    uCommon.goToURL(page, strUrl)
    
    uCommon.log(0, 'Step 3 - Tick the "Buy Gift" checkbox within your added product information. Input Gift Note in the textfield')
    uMyGifts.ml.tickBuyGift(page)
    uMyGifts.ml.setGiftNote(page, dDepChkLst.AUTO552.strGiftNote)
    
    uCommon.log(0, 'Step 4 - Click "Buy Selected Gifts" button')
    uMyGifts.ml.clickBuySelectedGifts(page, False)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230515 | Execution Time: 38s - 42s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify if user can Add Product and Quantity to the Gift List')
def test_AUTO_706_Add_Product_and_Quantity_to_the_Gift_List(page):
    uCommon.log(0, '[Precondtion Started] - Create gift list')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName9)
    uMyGifts.com.clickGiftBox(page, dDepChkLst.AUTO706.blnFirstGL)
    uMyGifts.com.deleteGiftList(page, dDepChkLst.AUTO706.blnCleanUp)
    uMyGifts.com.createNewGiftList(page, dDepChkLst.AUTO706.dictData)
    uCommon.log(0, '[Precondtion Completed] - Create gift list was successfully complete')
    
    uCommon.log(0, 'Step 1 - Log in to your Edamama Account')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - clicking "Gift" icon')
    uMyGifts.com.clickGiftBox(page)
    
    uCommon.log(0, 'Step 3 - Click your Gift List on the listing page then click "+" button')
    uMyGifts.com.clickGiftList(page)
    
    uCommon.log(0, 'Step 4 - Click the "Gift" icon of your chosen product in PDP then click the "+" sign on the respective Gift List you want to add it')
    strItemName = uMyGifts.com.addNewProductInGiftList(page)
    
    uCommon.log(0, 'Step 5 - Click the "Gift" icon again then select your list >>Verify the added product')
    uMyGifts.com.clickGiftBox(page)
    uMyGifts.com.clickGiftList(page, False)
    uMyGifts.com.verifyGiftListProducts(page, strItemName)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230515 | Execution Time: 19s - 23s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify if user can Create Gift List')
def test_AUTO_701_Create_Gift_List(page):
    uCommon.log(0, 'Step 1 - Log in to your Edamama Account')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName10)
    uAppComm.com.navigateToProfileMenu(page, 'my profile')
    dictProfile = uMyProfile.com.getMyProfileDetails(page)
    strName = ((dictProfile['strName']).split(' '))[0]
    
    uCommon.log(0, 'Step 2 - clicking "Gift" icon')
    uMyGifts.com.clickGiftBox(page, dDepChkLst.AUTO701.blnFirstGL)
    uCommon.log(0, 'Test Data delete')
    uMyGifts.com.deleteGiftList(page, dDepChkLst.AUTO701.blnCleanUp)
    uCommon.log(0, 'Test Data delete completed')
    
    uCommon.log(0, 'Step 3 - Click the "+" button')
    uMyGifts.com.createNewGiftList(page, dDepChkLst.AUTO701.dictData)
    
    uCommon.log(0, 'Step 4 - Populate all compulsory fields then click "Create Gift List" button')
    uCommon.expectElemTextToBeVisible(page, dDepChkLst.AUTO701.dictData["strOccassion"])
    uCommon.expectElemTextToBeVisible(page, dDepChkLst.AUTO701.dictData["strAbout"])
    
    uEmail.loginToGmail(page)
    uEmail.validatecreatedGiftListEmail(page, strName)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230516 | Execution Time: 19s - 23s """
# NOTE: https://edamama.atlassian.net/browse/SNSGR-90"
@pytest.mark.deploymentChecklist()
@allure.step('Verify if user can buy their own Gift List')
def test_AUTO_711_GR_Owner_Buys_On_His_Her_Own_Gift_List(page):
    uCommon.log(0, '[Precondtion Started] - Create gift list')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName1)
    uMyGifts.com.clickGiftBox(page, dDepChkLst.AUTO711.blnFirstGL)
    uMyGifts.com.deleteGiftList(page, dDepChkLst.AUTO711.blnCleanUp)
    uMyGifts.com.createGLandAddProduct(page, dDepChkLst.AUTO711.dictData)
    uCommon.log(0, '[Precondtion Completed] - Create gift list was successfully complete')
    
    uCommon.log(0, 'Step 1 - Log in to your Edamama Account')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - clicking "Gift" icon')
    uMyGifts.com.clickGiftBox(page)
    
    uCommon.log(0, 'Step 3 - Select any list available')
    uMyGifts.com.clickGiftList(page, dDepChkLst.AUTO711.blnFirstAddProduct)
    
    uCommon.log(0, 'Step 4 - Tick the "Buy Gift" checkbox within your added product information >> Input Gift Note in the textfield')
    uMyGifts.ml.tickBuyGift(page)
    uMyGifts.ml.setGiftNote(page, dDepChkLst.AUTO711.dictData["strGiftNote"])
    
    uCommon.log(0, 'Step 5 - Click "Buy Selected Gifts" button')
    uMyGifts.ml.clickBuySelectedGifts(page, dDepChkLst.AUTO711.blnOwner, dDepChkLst.AUTO711.blnOwner)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230516 | Execution Time: 3m 17s - 4m"""
@pytest.mark.deploymentChecklist()
@allure.step('Verify if Invitee can buy products form shared Gift List')
def test_AUTO_716_Invitee_Buys_Item_from_Shared_Gift_List(page):
    uCommon.log(0, '[Precondtion Started] - Create and send gift list invitation')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName2)
    uMyGifts.com.clickGiftBox(page, dDepChkLst.AUTO716.blnFirstGL)
    uMyGifts.com.deleteGiftList(page, dDepChkLst.AUTO716.blnCleanUp)
    uMyGifts.com.createGLandAddProduct(page, dDepChkLst.AUTO716.dictDataGift)
    uMyGifts.com.sendInvitesViaEmail(page, dCommon.user.strUserName7)
    uAppComm.lo.logOutToEdamama(page)
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName7)
    uEmail.loginToGmail(page)
    uEmail.validateAndClickInvitedGiftListEmail(page, dDepChkLst.AUTO716.strOwnerUserName)
    uCommon.log(0, '[Precondtion Completed] - Create and send gift list invitation was successfully complete')

    uCommon.log(0, 'Step 1 - Log in to your Edamama Account')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - clicking "Gift" icon')
    uMyGifts.com.clickGiftBox(page, dDepChkLst.AUTO716.blnFalse)
    
    uCommon.log(0, 'Step 3 - Click "Shared With Me" tab')
    uMyGifts.sh.clickSharedWithMe(page)
    
    uCommon.log(0, 'Step 4 - Select any list available')
    uMyGifts.com.clickGiftList(page, False)
    
    uCommon.log(0, 'Step 5 - Tick the "Buy Gift" checkbox within your added product information >> Input Gift Note in the textfield')
    uMyGifts.ml.tickBuyGift(page)
    uMyGifts.ml.setGiftNote(page, dDepChkLst.AUTO716.dictDataGift["strGiftNote"])
    
    uCommon.log(0, 'Step 6 - Click "Buy Selected Gifts" button')
    uMyGifts.ml.clickBuySelectedGifts(page)

    uCommon.log(0, 'Step 7 - Select any MOP available then click "Place Order" button')
    uCheckOut.selectModeOfPaymentAndBeansOrPromo(page, dDepChkLst.AUTO716.dictData, dDepChkLst.AUTO716.dictData["strMOP"], dDepChkLst.AUTO716.dictData["strBeansPromo"], dDepChkLst.AUTO716.dictData["strPromoCode"])
    uCheckOut.clickPlaceOrderAndGetOrderID(page, dDepChkLst.AUTO716.dictData["strMOP"], dDepChkLst.AUTO716.dictData["strBeansPromo"])


""" Author: ccapistrano_20230515 | Execution Time: 14s - 23s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify Gift Registry Guest flow using Shared Link')
def test_AUTO_547_Gift_Registry_Shared_Link_Guest_flow(page):
    uCommon.log(0, '[Precondtion Started] - Create and send gift list invitation')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName2)
    uMyGifts.com.clickGiftBox(page, dDepChkLst.AUTO716.blnFirstGL)
    uMyGifts.com.deleteGiftList(page, dDepChkLst.AUTO716.blnCleanUp)
    uMyGifts.com.createGLandAddProduct(page, dDepChkLst.AUTO716.dictDataGift)
    strUrl = uCommon.getURL(page)
    uAppComm.lo.logOutToEdamama(page)
    uCommon.log(0, '[Precondtion Completed] - Create and send gift list invitation was successfully complete')
    
    uCommon.log(0, 'Step 1 - Navigate to Edamama Website/Mobile App')
    uCommon.log(0, 'Step 2 - Paste the GL link in your URL tab then click "enter" key')
    uCommon.goToURL(page, strUrl)
    
    uCommon.log(0, 'Step 3 - Tick the "Buy Gift" checkbox within your added product information. Input Gift Note in the textfield')
    uMyGifts.ml.tickBuyGift(page)
    uMyGifts.ml.setGiftNote(page, dDepChkLst.AUTO547.strGiftNote)
    
    uCommon.log(0, 'Step 4 - Click "Buy Selected Gifts" button')
    uMyGifts.ml.clickBuySelectedGifts(page, False)
    uCommon.log(0, 'Test case completed')

    
""" Author: ccapistrano_20230516 | Execution Time: 1m 35s - 1m 43s """
# NOTE: Possible defect  - Item still visible in curated collection after removing in AP
@pytest.mark.deploymentChecklist()
@allure.step('Verify if User can add Products in Curated Collection in Admin Panel')
@allure.step('Verify if User can remove Products in Curated Collection in Admin Panel')
# test_AUTO_681_Add_Product_in_Curated_Collections_Admin_Panel
def test_AUTO_661_Remove_Product_in_Curated_Collections_Admin_Panel(page):
    uCommon.log(0, '[Precondtion Started] - Get Curated title')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName4)
    strTitle = uShop.sp.waitAndGetCuratedTitle(page, dDepChkLst.AUTO661.intCuratedIndex)
    
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.cp.clickCuratedProducts(page)
    uAdminKpc.cp.searchTitle(page, strTitle)
    window2 = uAdminKpc.cp.pr.clickProduct(page)
    uAdminKpc.cp.pr.clickAssociatedTab(window2)
    blnVisible = uAdminKpc.cp.pr.searchProduct(window2, dDepChkLst.AUTO661.strItemName ,'search')
    if blnVisible == True:
        uAdminKpc.cp.pr.clickCheckBox(window2)
        uAdminKpc.cp.pr.clickRemove(window2)
        uAdminKpc.cp.pr.clickYes(window2, dDepChkLst.AUTO661.blnAdd)
    uCommon.closeWindow(window2)
    uCommon.log(0, '[Precondtion Completed] - Curated title is {strTitle}')

    uCommon.log(0, 'Step 1 to 2 - Open Admin Panel >> Login Credentials')
    # uAppComm.ln.loginToAdminKPC(page)
    
    uCommon.log(0, 'Step 3 - Go to Curated Products (Collections)')
    uAdminKpc.od.clickOrders(page)
    uAdminKpc.cp.clickCuratedProducts(page)
    uAdminKpc.cp.searchTitle(page, strTitle)
    
    uCommon.log(0, 'Step 4 - Click Products Hyperlink of the Curated Collection')
    window2 = uAdminKpc.cp.pr.clickProduct(page)
    uAdminKpc.cp.pr.searchAndClickProduct(window2, dDepChkLst.AUTO661.strItemName)
    
    uCommon.log(0, 'Step 5 - In All Tab, Tick Box of a Product')
    uAdminKpc.cp.pr.clickCheckBox(window2)
    
    uCommon.log(0, 'Step 6 - Click Add Button')
    uAdminKpc.cp.pr.clickAdd(window2)
    
    uCommon.log(0, 'Step 7 - Click Yes in Confirmation Window')
    uAdminKpc.cp.pr.clickYes(window2)
    uCommon.closeWindow(window2)
    
    uCommon.log(0, 'Step 8 - Check in Shop')
    uAppComm.ln.goToEdamamaURL(page)
    uCommon.wait(page, 10)
    uShop.sp.waitAndClickCuratedTitle(page, dDepChkLst.AUTO661.intCuratedIndex)
    uCommon.expectElemTextToBeVisible(page, dDepChkLst.AUTO661.strItemName)
    uCommon.log(0, 'Test case completed')
    
    
    uCommon.log(0, 'Step 1 - Open and login to Admin Panel')
    uCommon.goToURL(page, dCommon.url.strAdminUrl)
    uAdminKpc.com.checkProgressBar(page)
    
    uCommon.log(0, 'Step 2 - Go to Curated Products (Collections)')
    uAdminKpc.cp.clickCuratedProducts(page)
    uAdminKpc.cp.searchTitle(page, strTitle)
    
    uCommon.log(0, 'Step 3 - Click Products Hyperlink of the Curated Collection')
    window2 = uAdminKpc.cp.pr.clickProduct(page)
    
    uCommon.log(0, 'Step 4 - Click Associated Tab')
    uAdminKpc.cp.pr.clickAssociatedTab(window2)
    uAdminKpc.cp.pr.searchProduct(window2, dDepChkLst.AUTO661.strItemName)
    
    uCommon.log(0, 'Step 5 - Select and tick the box a product')
    uAdminKpc.cp.pr.clickCheckBox(window2)
    
    uCommon.log(0, 'Step 6 - Click Remove Button >> Click "Yes" on the confirmation message')
    uAdminKpc.cp.pr.clickRemove(window2)
    uAdminKpc.cp.pr.clickYes(window2, dDepChkLst.AUTO661.blnAdd)
    
    uCommon.log(0, 'Step 7 - Verify that the product were removed from the curated products')
    uAppComm.ln.goToEdamamaURL(window2)
    uCommon.wait(page, 15)
    uShop.sp.waitAndClickCuratedTitle(window2, dDepChkLst.AUTO661.intCuratedIndex)
    uCommon.expectElemTextNotToBeVisible(window2, dDepChkLst.AUTO661.strItemName)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230517 | Execution Time: 1m 54s - 1m 43s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify if user can skip through the next Order Cycle date')
def test_AUTO_721_User_edits_subscription_by_skipping_next_cycle_order_date(page):
    uCommon.log(0, '[Precondtion Started] - create SNS order')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName5)
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO721.dictData)
    uCommon.log(0, '[Precondtion Completed] - SNS order was successfully completed')
    
    uCommon.log(0, 'Step 1 to 2 - Log in to your Edamama Account >> Click your avatar icon > My Subscriptions')
    uAppComm.ln.goToEdamamaURL(page)
    uAppComm.com.navigateToProfileMenu(page, dDepChkLst.AUTO721.strMySubscription)
    
    uCommon.log(0, 'Step 3 - Click "Edit Subscription" button')
    uMySubscription.at.clickEditSubscription(page)
    
    uCommon.log(0, 'Step 4 - Browse on the page then click "Skip Order" button')
    uMySubscription.com.clickSkipOrder(page)
    
    uCommon.log(0, 'Step 5 - Click "YES, SKIP ORDER" button')
    strNextOrderDate = uMySubscription.com.clickYesSkipOrder(page)
    uMySubscription.at.validateNextOrder(page, strNextOrderDate)
    
    
""" Author: ccapistrano_20230518 Execution Time: 47s - 1m 1s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify that the order is displayed under the Order Module in Admin Panel')
def test_AUTO_557_Check_Checkout_OIDs_in_Admin_Panel_Orders_Module(page):
    uCommon.log(0, 'Step 1 - Go to the edamama website/app')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName6)
    
    uTcTest.checkCheckoutOIDsInAdminPanel(page, dDepChkLst.AUTO557.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230518 Execution Time: 59s - 1m 7s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify that the cancelled order is displayed under the Order Module in Admin Panel')
def test_AUTO_567_Check_Cancelled_OIDs_in_Admin_Panel_Orders_Module(page):
    uCommon.log(0, 'Step 1 - Go to the edamama website/app')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName7)
    
    uTcTest.checkCheckoutOIDsInAdminPanel(page, dDepChkLst.AUTO567.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230522 | Execution Time: 2m 12s - 2m 31s """
# NOTE: https://edamama.atlassian.net/browse/CNCSNSGR-349
@pytest.mark.deploymentChecklist()
@allure.step('Verify if user can edit the subscription by Changing the Product')
def test_AUTO_734_User_edit_subscription_by_changing_the_product(page):
    uCommon.log(0, '[Precondtion Started] - create SNS order')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName8)
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO734.dictData)
    uCommon.log(0, '[Precondtion Completed] - SNS order was successfully completed')
    
    uCommon.log(0, 'Step 1 to 2 - Log in to your Edamama Account >> Click your avatar icon > My Subscriptions')
    uAppComm.ln.goToEdamamaURL(page)
    uAppComm.com.navigateToProfileMenu(page, dDepChkLst.AUTO734.strMySubscription)
    
    uCommon.log(0, 'Step 3 - Click "Edit Subscription" button')
    uMySubscription.at.clickEditSubscription(page)

    uCommon.log(0, 'Step 4 - Click "Change Product" button')
    uMySubscription.com.clickChangeProduct(page)
    
    uCommon.log(0, 'Step 5 - Select any SNS product of your desired')
    uCommon.waitAndClickElemText(page, dDepChkLst.AUTO734.strNewProduct, '', 4)
    dictDetails = uMySubscription.cp.getDetails(page)
    
    uCommon.log(0, 'Step 6 - Click "Apply Changes" button')
    uMySubscription.cp.clickApplyChanges(page)
    uMySubscription.us.validateDetails(page, dictDetails)
    
    uCommon.log(0, 'Step 7 - Click "Confirm"')
    uMySubscription.us.clickApplyChanges(page)
    uMySubscription.at.validateDetails(page, dictDetails)
    uEmail.loginToGmail(page)
    uEmail.validateAndClickSubscriptionDetailsChangedEmail(page, dDepChkLst.AUTO734.strUsername, dDepChkLst.AUTO734.strNewProduct)

    
""" Author: ccapistrano_20230522 | Execution Time: 2m 31s - 3m 8s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify if user can Cancel the Entire Subscription')
def test_AUTO_730_User_edit_subscription_by_cancelling_the_entire_subscription(page):
    uCommon.log(0, '[Precondtion Started] - create SNS order')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName9)
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO730.dictData)
    uCommon.log(0, '[Precondtion Completed] - SNS order was successfully completed')
    
    uCommon.log(0, 'Step 1 to 2 - Log in to your Edamama Account >> Click your avatar icon > My Subscriptions')
    uAppComm.ln.goToEdamamaURL(page)
    uAppComm.com.navigateToProfileMenu(page, dDepChkLst.AUTO730.strMySubscription)
    
    uCommon.log(0, 'Step 3 - Click "Edit Subscription" button')
    uMySubscription.at.clickEditSubscription(page)
    
    uCommon.log(0, 'Step 4 - Browse on the page then click "Cancel Subscription" button')
    uMySubscription.com.clickCancelSubscription(page)
    
    uCommon.log(0, 'Step 5 - Click "ASK FOR ASSISTANCE" button')
    window2 = uMySubscription.com.clickAskForAssisctance(page)
    uCommon.closeWindow(window2)
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 6 to 10 - Login your Admin Panel credentials >> Navigate to Subscription >> click the "Edit" icon >> Click "Cancel" button"')
    uAdminKpc.sc.cancelOrdersByUserName(page)

    
""" Author: ccapistrano_20230522 Execution Time: 52s - 1m 10s """
@pytest.mark.deploymentChecklist()
@allure.step('Verify if user can cancel an order')
def test_AUTO_530_Cancel_order_by_user(page):
    uCommon.log(0, 'Step 1 to 2 - Navigate to Edamama Website/ Mobile App >> Log in to your Edamama Account')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName10)
    
    uCommon.log(0, 'Step 3 to 5 -  Browse any Categories >> Select MOP >> Click/Tap the "Place Order" button')
    strOrderID = uTcTest.validateE2EMOP(page, dDepChkLst.AUTO530.dictData)
    
    uCommon.log(0, 'Step 6 - Go to "My Orders" then click/tap "Cancel Order" button')
    uMyOrders.cancelOrder(page, strOrderID)
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.od.clickOrders(page)
    uAdminKpc.od.validateRetunCancel(page, strOrderID, 'Canceled By User')
    uCommon.log(0, 'Test case completed')

  
""" Author: ccapistrano_20230522 Execution Time: 2m 9s - 2m 29s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify that the order is displayed under the Order Module in WMS')
def test_AUTO_562_Check_Checkout_OIDs_in_WMS_Orders_Module(page):
    uCommon.log(0, 'Step 1 - Go to the edamama website/app')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName1)
    
    uTcTest.checkCheckoutOIDsInWMS(page, dDepChkLst.AUTO562.dictData) # 230602170012-226000
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230523 Execution Time: 2m 13s - 2m 27s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify that the cancelled order is displayed under the Order Module in WMS')
def test_AUTO_572_Check_Cancelled_OIDs_in_WMS_Orders_Module(page):
    uCommon.log(0, 'Step 1 - Go to the edamama website/app')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName2)
    
    uTcTest.checkCheckoutOIDsInWMS(page, dDepChkLst.AUTO572.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230523 Execution Time: 1m 18s - 1m 33s """
@pytest.mark.deploymentChecklist()
@allure.step('Edit Ranking of Curated Collections in Admin Panel')
def test_AUTO_656_Edit_Ranking_of_Curated_Collections_in_Admin_Panel(page):
    uCommon.log(0, 'Step 1 - Open  and login to Admin Panel: https://admin.kpc.edamamalabs.net/')
    uAppComm.ln.loginToAdminKPC(page)
    
    uCommon.log(0, 'Step 2 - Go to Curated Collections (Curated Products)')
    uAdminKpc.cp.clickCuratedProducts(page)

    uCommon.log(0, 'Step 3-click Rank Button')
    uAdminKpc.cp.clickRank(page)

    uCommon.log(0, 'Test Data preparation')
    dictTitle = uAdminKpc.cp.setRanking(page, True)
    uAdminKpc.cp.clickUpdate(page)
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName3)
    uShop.sp.expectCuratedTitleNotVisible(page, dictTitle['strTitle1'])
    uShop.sp.expectCuratedTitleNotVisible(page, dictTitle['strTitle2'])
    uShop.sp.expectCuratedTitleNotVisible(page, dictTitle['strTitle3'])
    uShop.sp.expectCuratedTitleNotVisible(page, dictTitle['strTitle4'])
    uCommon.log(0, 'Test Data preparation completed')

    uCommon.log(0, 'Step 4 - Update the ranking')
    uCommon.goToURL(page, dCommon.url.strAdminUrl)
    uCommon.wait(page, 1)
    uAdminKpc.cp.clickCuratedProducts(page)
    uAdminKpc.cp.clickRank(page)
    uAdminKpc.cp.setRanking(page)
    
    uCommon.log(0, 'Step 5 - Click Update Button')
    uAdminKpc.cp.clickUpdate(page)
    
    uCommon.log(0, 'Step 6 - Check in Shop Web or Mobile App')
    uAppComm.ln.goToEdamamaURL(page)
    uShop.sp.waitAndexpectCuratedTitleIsVisible(page, dictTitle['strTitle1'])
    uShop.sp.waitAndexpectCuratedTitleIsVisible(page, dictTitle['strTitle2'])
    uShop.sp.waitAndexpectCuratedTitleIsVisible(page, dictTitle['strTitle3'])
    uShop.sp.waitAndexpectCuratedTitleIsVisible(page, dictTitle['strTitle4'])
    uShop.sp.validateCuratedTitleIsVisible(page, 1, dictTitle['strTitle1'])
    uShop.sp.validateCuratedTitleIsVisible(page, 2, dictTitle['strTitle2'])
    uShop.sp.validateCuratedTitleIsVisible(page, 3, dictTitle['strTitle3'])
    uShop.sp.validateCuratedTitleIsVisible(page, 4, dictTitle['strTitle4'])
    uCommon.log(0, 'Test case completed')


""" Author: cgrapa_20230428 Execution Time: 1m - 1m 48s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify that user can explore the discover page in the web/app.')
def test_AUTO_542_Discover(page):
    uCommon.log(0, 'Step 1 - Navigate to the edamama website/app')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - Click the Discover tab in the header')
    uDiscover.com.navigateToDiscover(page)
    uDiscover.al.validateDiscover(page)
    
    uCommon.log(0, 'Step 3 - Click the Style tab')
    uDiscover.com.navigateToDiscoverCategories(page, dDepChkLst.AUTO542.strStyle)
    uDiscover.st.validateStyleCategory(page)
    
    uCommon.log(0, 'Step 4 - Click the Nurture tab')
    uDiscover.com.navigateToDiscoverCategories(page, dDepChkLst.AUTO542.strNurture)
    uDiscover.nu.validateNurtureCategory(page)
    
    uCommon.log(0, 'Step 5 - Click the Play & Learn tab')
    uDiscover.com.navigateToDiscoverCategories(page, dDepChkLst.AUTO542.strPlayAndLearn)
    uDiscover.pl.validatePlayAndLearnCategory(page)
    
    uCommon.log(0, 'Step 6 - Click any kind of article and verify the result')
    uDiscover.com.navigateToDiscoverCategories(page, dDepChkLst.AUTO542.strAll)
    uDiscover.ar.validateArticlesAndContents(page, dDepChkLst.AUTO542.strFeatured, dDepChkLst.AUTO542.intArticles)
    uDiscover.ar.validateArticlesAndContents(page, dDepChkLst.AUTO542.strNurture, dDepChkLst.AUTO542.intArticles)
    uDiscover.ar.validateArticlesAndContents(page, dDepChkLst.AUTO542.strPlayAndLearn, dDepChkLst.AUTO542.intArticles)
    uDiscover.ar.validateArticlesAndContents(page, dDepChkLst.AUTO542.strStyle, dDepChkLst.AUTO542.intArticles)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: abernal_20240325 Execution Time: 48s - 1m 19s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify Gift Card voucher is not applied when minimum requirements are not met.')
def test_AUTO_1948_Voucher_Gift_Card_should_not_be_applied_when_min_reqs_are_not_met(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName1)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO1948.dictData)
    uCommon.log(0, 'Test case completed')
    

""" Author: abernal_20240325 Execution Time: 48s - 1m 19s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify Brand Sponsored voucher is not applied when minimum requirements are not met.')
def test_AUTO_1951_Voucher_Brand_Sponsored_should_not_be_applied_when_min_reqs_are_not_met(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName2)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO1951.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: abernal_20240326 Execution Time: 57s - 58s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify Brand Sponsored voucher is not applied when brand of the item is not the same as the voucher.')
def test_AUTO_1954_Voucher_Brand_Sponsored_should_not_be_applied_when_item_is_not_the_same_brand(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName3)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO1954.dictData)
    uCommon.log(0, 'Test case completed')
    

""" Author: abernal_20240326 Execution Time: 53s - 58s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify Edamama Sponsored voucher is not applied when minimum requirements are not met.')
def test_AUTO_1960_Voucher_Edamama_Sponsored_should_not_be_applied_when_min_reqs_are_not_met(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName4)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO1960.dictData)
    uCommon.log(0, 'Test case completed')
    

""" Author: abernal_20240326 Execution Time: 58s - 60s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify MOP Edamama Sponsored voucher is not applied when minimum requirements are not met.')
def test_AUTO_1969_MOP_Voucher_Edamama_Sponsored_should_not_be_applied_when_min_reqs_are_not_met(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName5)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO1969.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: abernal_20240326 Execution Time: 58s - 60s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify Free Shipping voucher is not applied when minimum requirements are not met.')
def test_AUTO_1963_Voucher_Shipping_should_not_be_applied_when_min_reqs_are_not_met(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName6)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO1963.dictData)
    uCommon.log(0, 'Test case completed')
    

""" Author: abernal_20240326 Execution Time: 1m 53s - 1m 54s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify Referral Code voucher is not applied when minimum requirements are not met.')
def test_AUTO_1966_Voucher_Referral_Code_should_not_be_applied_when_min_reqs_are_not_met(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, '[Pre-condition started]: Create new account without adding attributes and child.')
    uSignUp.clickSignUp(page)
    uSignUp.validateSignUpPage(page)
    arrData = uSignUp.fillandContinueSignUpPage(page, dRegSignUp.AUTO1621.dictData)
    uSignUp.validateAndClickOKinAccountVerification(page)
    uEmail.loginToGmail(page)
    uEmail.clickFirstConfirmEmail(page, arrData)
    uEmail.clickYesThisIsMyEmail(page)
    newWindow = uCommon.switchToWindow(page)
    uSignUp.validateEmailVerificationPageAndClickStartShopping(newWindow)
    uCommon.log(0, '[Pre-condition Completed]: Account created.')
    
    uCommon.log(0, 'Step 2 - Add an address.')
    uAppComm.com.navigateToProfileMenu(newWindow, dDepChkLst.AUTO1966.strMyProfile)
    uMyProfile.com.clickAddressAddMore(newWindow)
    uMyProfile.na.addAddress(newWindow, dDepChkLst.AUTO1966.dictDataAddress)
    uMyProfile.na.clickAddNewAddress(newWindow)
    
    uCommon.log(0, 'Step 3 - Proceed to checkout.')
    uTcTest.validateE2EMOP(newWindow, dDepChkLst.AUTO1966.dictData)
    uCommon.log(0, 'Test case completed')
    

""" Author: abernal_20240326 Execution Time: 1m 01s - 1m 13s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify Gift Card voucher is applied when minimum requirements are met.')
def test_AUTO_1972_Voucher_Gift_Card_should_be_applied_when_min_reqs_are_met(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName7)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO1972.dictData)
    uCommon.log(0, 'Test case completed')
    

""" Author: abernal_20240326 Execution Time: 47s - 57s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify Brand Sponsored voucher is applied when minimum requirements are met.')
def test_AUTO_1975_Voucher_Brand_Sponsored_should_be_applied_when_min_reqs_are_met(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName8)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO1975.dictData)
    uCommon.log(0, 'Test case completed')
    

""" Author: abernal_20240326 Execution Time: 47s - 57s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify Brand Sponsored voucher is applied when minimum requirements are met.')
def test_AUTO_1975_Voucher_Brand_Sponsored_should_be_applied_when_min_reqs_are_met(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName8)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO1975.dictData)
    uCommon.log(0, 'Test case completed')
 
    
""" Author: abernal_20240326 Execution Time: 56s - 1m 05s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify Edamama Sponsored voucher is applied when minimum requirements are met.')
def test_AUTO_1978_Voucher_Edamama_Sponsored_should_be_applied_when_min_reqs_are_met(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName9)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO1978.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: abernal_20240326 Execution Time: 45s - 59s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify Free Shipping voucher is applied when minimum requirements are met.')
def test_AUTO_1981_Voucher_Shipping_should_be_applied_when_min_reqs_are_met(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName1)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO1981.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: abernal_20240326 Execution Time: 1m 49s - 2m 14s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify Referral Code is applied when minimum requirements are met.')
def test_AUTO_1984_Voucher_Referral_Code_should_be_applied_when_min_reqs_are_met(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, '[Pre-condition started]: Create new account without adding attributes and child.')
    uSignUp.clickSignUp(page)
    uSignUp.validateSignUpPage(page)
    arrData = uSignUp.fillandContinueSignUpPage(page, dRegSignUp.AUTO1621.dictData)
    uSignUp.validateAndClickOKinAccountVerification(page)
    uEmail.loginToGmail(page)
    uEmail.clickFirstConfirmEmail(page, arrData)
    uEmail.clickYesThisIsMyEmail(page)
    newWindow = uCommon.switchToWindow(page)
    uSignUp.validateEmailVerificationPageAndClickStartShopping(newWindow)
    uCommon.log(0, '[Pre-condition Completed]: Account created.')
    
    uCommon.log(0, 'Step 2 - Add an address.')
    uAppComm.com.navigateToProfileMenu(newWindow, dDepChkLst.AUTO1984.strMyProfile)
    uMyProfile.com.clickAddressAddMore(newWindow)
    uMyProfile.na.addAddress(newWindow, dDepChkLst.AUTO1984.dictDataAddress)
    uMyProfile.na.clickAddNewAddress(newWindow)
    
    uCommon.log(0, 'Step 3 - Proceed to checkout.')
    uTcTest.validateE2EMOP(newWindow, dDepChkLst.AUTO1984.dictData)
    uCommon.log(0, 'Test case completed')
    

""" Author: abernal_20240326 Execution Time: 50s - 56s """
@pytest.mark.deploymentChecklist()
@allure.step('To verify MOP Edamama Sponsored Voucher is applied when minimum requirements are met.')
def test_AUTO_1987_MOP_Voucher_Edamama_Sponsored_should_be_applied_when_min_reqs_are_met(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName2)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO1987.dictData)
    uCommon.log(0, 'Test case completed')