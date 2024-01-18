import pytest
import allure

import libraries.data.common as dCommon
import libraries.data.deploymentChecklist as dDepChkLst

import libraries.util.appCommon.adminKpc as uAdminKpc
import libraries.util.appCommon.appComm as uAppComm
import libraries.util.appCommon.email as uEmail
import libraries.util.appCommon.signUp as uSignUp
import libraries.util.common as uCommon
import libraries.util.cart as uCart
import libraries.util.checkOut as uCheckOut
import libraries.util.shop as uShop


""" Author: ccapistrano_20230322 Execution Time: 23s - 1m 16s """
@pytest.mark.RegPrep()
@pytest.mark.smokeTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify that user can login manually using his/her email address and password')
def test_AUTO_220_Login_Manually(page):
    uCommon.log(0, 'Step 1 to 4.1 - Go to https://www.kpc.edamamalabs.net/shop >>  Click login button >> Verify that profile icon was displayed')
    uAppComm.ln.loginToEdamama(page)
    
    uCommon.log(0, 'Step 4.2 - Verify that homepage was displayed')
    uAppComm.com.validateWebHeaderTabsAdFooter(page)
    uShop.sp.validateShopPage(page)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230327 Execution Time: 50s - 1m 20s """
@pytest.mark.smokeTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Missing Objective')
def test_AUTO_230_Login_SSO(page):
    # Remove SSO via FB for Manual testing
    # uCommon.log(0, 'Step 1 to 4 - Go to edamama app/website >> Click "Login" >> Click "Continue with Facebook')
    # uAppComm.ln.loginToEdamamaViaSocial(page, dDepChkLst.AUTO230.strFb)
    
    # uCommon.log(0, 'Step 5 - Click "Logout"')
    # uAppComm.lo.logOutToEdamama(page)
    
    uCommon.log(0, 'Step 6 to 8 - Click "Login" >> Click "Sign in with Google" >> Enter gmail credentials. >> Click "Login"')
    uAppComm.ln.loginToEdamamaViaSocial(page, dDepChkLst.AUTO230.strGmail)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230327 Execution Time: 1m 20s - 2m """
@pytest.mark.smokeTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify that user can recover his/her account via "Forgot Password"')
def test_AUTO_225_Forgot_Password(page):
    uCommon.log(0, 'Step 1 to 3 - Go to https://www.kpc.edamamalabs.net/shop >> Click Login >> Click Forgot your password? button ')
    uCommon.log(0, 'Step 4 to 6 - Enter Email address then click submit ?>> In Email - click verification button >> Input new password and confirm password then click submit')
    page = uAppComm.rp.resetPassword(page, dDepChkLst.AUTO225.strUserName, dDepChkLst.AUTO225.strNewPassword)
    
    uCommon.log(0, 'Step 7 to 8 - Click Proceed to Login >> Input email address and new password then click continue')
    uAppComm.ln.clickLoginAndFillDetails(page, dDepChkLst.AUTO225.strUserName, dDepChkLst.AUTO225.strNewPassword)
    uCommon.log(0, 'Test case completed')
    
    uCommon.log(0, '[Postcondition Started] - Revert password to defaultf password')
    uAppComm.lo.logOutToEdamama(page)
    page = uAppComm.rp.resetPassword(page, dDepChkLst.AUTO225.strUserName, dDepChkLst.AUTO225.strOldPassword) 
    uCommon.log(0, '[Postcondition Completed] - Password successfully reverted to default password')
    
    
""" Author: ccapistrano_20230329 Execution Time: 2m """
@pytest.mark.smokeTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify if Shop Homepage Sections and buttons are working')
def test_AUTO_215_Shop_Homepage_UI(page):
    uCommon.log(0, '[Precondition Started] Create Flash Sale')
    uAdminKpc.fs.createFlashSale(page, dDepChkLst.AUTO215.strName, dDepChkLst.AUTO215.strPath)
    uCommon.log(0, '[Precondition Completed] Flash Sale created successfully')
    
    uCommon.log(0, 'Step 1 - Go to https://www.kpc.edamamalabs.net/signup')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName1)
    uCommon.maximize(page)
    
    uCommon.log(0, 'Step 2 - Verify that the following sections were displayed')
    uAppComm.com.validateAllCategoriesTabLevel(page) 
    
    uCommon.log(0, 'Step 3 - Scroll down and check shop homepage')
    uShop.sp.validateShopPage(page)
    uShop.sp.validateFlashSale(page)
    uShop.sp.validateDiscover(page)
    uShop.sp.validateSubscribeAndSave(page)
    
    uCommon.log(0, 'Step 4 - Verify that carousel banner is working')
    uShop.sp.validateCarouselBanner(page)
    uCommon.log(0, 'Test case completed')
    

""" Author: ccapistrano_20230330 Execution Time: 1m 14s - 2m 42s """
@pytest.mark.smokeTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify that user can sign-up manually')
def test_AUTO_210_Register_Manual_Signup(page):
    uCommon.log(0, 'Step 1 - Go to https://www.kpc.edamamalabs.net/shop')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - Click Sign Up button')
    uSignUp.clickSignUp(page)
    uSignUp.validateSignUpPage(page)
    uAppComm.com.validateWebHeaderAndFooter(page, False)
    
    uCommon.log(0, 'Step 3 to 5 - Input Required fields >> Click policy checkbox >> Click Continue button')
    dictData = uSignUp.fillandContinueSignUpPage(page, dCommon.signUp.dictData)
    
    uCommon.log(0, 'Step 6 - In Email - verify Account in qa@edamama.ph mailbox. Click the link to verify the account')
    uSignUp.validateAndClickOKinAccountVerification(page)

    uCommon.log(0, 'Step 7 to 8 - Verify correct email was displayed >> Click completed my profile')
    uEmail.loginToGmail(page)
    uEmail.clickFirstConfirmEmail(page, dictData)
    uEmail.clickYesThisIsMyEmail(page)
    page = uCommon.switchToWindow(page)
    uSignUp.validateEmailVerificationPageAndClickCompleteMyProfile(page)
    uSignUp.validateAddChildPage(page)
    
    uCommon.log(0, 'Step 9 to 10 - Input Required fields Child Name/Alias, Birthdate/Due Date, Gender >> Click Add Child')
    uSignUp.fillAndAddChild(page)
    uSignUp.validateAlmostDonePage(page)
    
    uCommon.log(0, 'Step 11 - Select attributes')
    uSignUp.clickNotAMama(page)
    
    uCommon.log(0, 'Step 12 - Click Submit')
    uSignUp.clickSubmit(page)
    
    uCommon.log(0, 'Step 13 - Click Continue button')
    uSignUp.validateThankYouAndClickContinue(page)
    uShop.sp.validateShopPage(page)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230330 Execution Time: 41s """
@pytest.mark.smokeTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify if User can search for Products or Brands')
def test_AUTO_240_Search_for_a_Product_or_Brand(page):
    uCommon.log(0, 'Step 1 to 3 - Go to https://www.kpc.edamamalabs.net/shop >> Click Profile icon >> Login your credentials')
    uAppComm.ln.loginToEdamama(page)
    
    uCommon.log(0, 'Step 4 - In Search bar -> search  any brand ex. (Anko, Cetaphil, etc ) then click search or enter')
    uShop.sp.searchAndValidateName(page, dDepChkLst.AUTO240.strType1, dDepChkLst.AUTO240.strName1)
    
    uCommon.log(0, 'Step 5 - In Search bar -> search  any item .> then click search or enter')
    uShop.sp.searchAndValidateName(page, dDepChkLst.AUTO240.strType2, dDepChkLst.AUTO240.strName2)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230331 Execution Time: 52s - 1m 1s """
@pytest.mark.smokeTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify if User can Add Products in their Cart')
def test_AUTO_255_Add_Product_to_Cart(page):
    uAppComm.ln.loginToEdamama(page)
    uCart.checkAndDeleteAddToCartItems(page)
    uShop.sp.clickFPfirstItem(page)
    uCheckOut.clickFirstSize(page, True)
    uShop.pp.clickAddToBag(page, 'opt')
    uAppComm.com.validateCountInCart(page, dDepChkLst.AUTO255.strCount)
    uCart.deleteAddToCartItems(page)
    

""" Author: ccapistrano_20230331 Execution Time: 29s - 52s """
@pytest.mark.smokeTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify if PDP Page is accessible and all button functions are working')
def test_AUTO_345_PDP_Page_UI(page):
    uCommon.log(0, 'Step 1 to 3- Open Edamama app >> Click Profile icon >> Login your credentials')
    uAppComm.ln.loginToEdamama(page)
    
    uCommon.log(0, 'Step 4 - In shop page click any product you want to purchase')
    uShop.sp.validateFeaturedProducts(page)
    dictDetails = uShop.sp.getShopItemDetails(page, dDepChkLst.AUTO345.strShopSection)
    uShop.sp.clickFPfirstItem(page)
    
    uCommon.log(0, 'Step 5  - Verify the image of the product, brand and product name and unit price is displayed properly')
    uShop.pp.validateProductForm(page)
    uAppComm.com.validateWebHeaderTabsAdFooter(page)
    uShop.pp.validateDetails(page, dictDetails)
    
    uCommon.log(0, 'Step 5.4 - Verify below tabs are displayed: Product Description, Product Specification')
    uShop.sp.validateProductDescriptionAndSpecification(page)
    uCommon.log(0, 'Test case completed')
    

""" Author: ccapistrano_20230404 Execution Time: 1m 22s """
@pytest.mark.smokeTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify if Product Cards and all buttons in Product Listing Page is working and displaying correctly')
def test_AUTO_235_Product_Listing_Page_UI(page): 
    uCommon.log(0, 'Step 1 - Go to https://www.kpc.edamamalabs.net/shop')  
    uAppComm.ln.loginToEdamama(page)
    
    uCommon.log(0, 'Step 2 to 3 - In Search Bar, Search for any Keywords >> Check Search Result Listing Page')  
    uShop.sp.searchAndValidateName(page, dDepChkLst.AUTO235.strType1, dDepChkLst.AUTO235.strName1)
    uShop.lp.validateListingPage(page, True)
    
    uCommon.log(0, 'Step 4 to 5 - In Category Navigation Bar, Click for any L1, L2 or L3 Category >> Check Category Listing Page') 
    uCommon.maximize(page) 
    uAppComm.com.goToViaCategory(page, dDepChkLst.AUTO235.strCategoryName, dDepChkLst.AUTO235.strLvl3Name)
    uShop.lp.validateListingPage(page)
    uCommon.log(0, 'Test case completed')
    

""" Author: ccapistrano_20230403 Execution Time: 1m 11s -1m 14s """
@pytest.mark.smokeTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Missing Objective')
def test_AUTO_250_Add_SS_product_to_cart(page):
    uCommon.log(0, 'Step 1 to 2 - Go to https://www.kpc.edamamalabs.net/shop >> Login to your account') 
    uAppComm.ln.loginToEdamama(page)
    
    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uCart.checkAndDeleteAddToCartItems(page)
    
    uCommon.log(0, 'Step 3 - Scroll down and go to "Subscribe and Save" section >> Select an SnS product')  
    uShop.sp.validateSubscribeAndSave(page)
    dictDetails = uShop.sp.getShopItemDetails(page, dDepChkLst.AUTO250.strTitle)
    uShop.sp.clickSSfirstItem(page)
    
    uCommon.log(0, 'Step 4 - Verify the following were displayed')  
    uShop.pp.validateProductForm(page, dDepChkLst.AUTO250.strTitle)
    uShop.sp.validateProductDescriptionAndSpecification(page)
    uAppComm.com.validateWebHeaderTabsAdFooter(page)
    uShop.pp.validateDetails(page, dictDetails)
    
    uCommon.log(0, 'Step 5 - Click "Add to Bag"')
    uShop.pp.clickAddToBag(page, False)
    uShop.ss.validateSubsAndSavePrompt(page)
    
    uCommon.log(0, 'Step 6 - Click "Confirm and Add to Cart" button')
    uShop.ss.clickConfirmAddToCart(page)
    
    uCommon.log(0, 'Step 7 - Verify that item was added to bag successfully')
    uAppComm.com.validateCountInCart(page, dDepChkLst.AUTO250.strCount)
    uCommon.log(0, 'Test case completed')
    
    uCommon.log(0, '[Postcondition Started] - Revert password to defaultf password')
    uCart.deleteAddToCartItems(page)
    uCommon.log(0, '[Postcondition Completed] - Password successfully reverted to default password')