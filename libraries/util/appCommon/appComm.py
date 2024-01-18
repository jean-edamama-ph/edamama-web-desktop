import libraries.data.common as dCommon

import libraries.page.common.common as pCommon
import libraries.page.common.login as pLogin
import libraries.page.profile.myOrders as pMyOrders
import libraries.page.profile.myProfile as pMyProfile
import libraries.page.profile.mySubscription as pMySubcription
import libraries.page.profile.myWishlist as pMyWishlist
import libraries.page.shop as pShop
import libraries.page.common.social as pSocial

import libraries.util.common as uCommon
import libraries.util.appCommon.email as uEmail
import libraries.util.shop as uShop

class ln:
    """LOGIN PAGE"""
    @uCommon.ufuncLog 
    def goToEdamamaURL(page):
        """ 
        Objective: Go to Edamama URL
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.goToURL(page, f'{dCommon.url.strBaseUrl}')
        uCommon.wait(page, 3)
        uCommon.waitElemToBeVisible(page, pShop.hs.whyMamasEdamamaLbl)

    @uCommon.ufuncLog  
    def loginToEdamama(page, strUserName =  dCommon.user.strUserName, strPassword = dCommon.user.strPassword1):
        """ 
        Objective: Login To Edamama
        
        param strUserName: User Name
        param strPassword: Password
        returns: None
        Author: ccapistrano_20230327
        """
        ln.goToEdamamaURL(page)
        ln.clickLoginAndFillDetails(page, strUserName, strPassword)
        uCommon.waitElemToBeVisible(page, pShop.hs.whyMamasEdamamaLbl)
        

    @uCommon.ufuncLog 
    def loginToAdminKPC(page):
        """ 
        Objective: Login To Admin KPC
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.goToURL(page, dCommon.url.strAdminUrl)
        uCommon.wait(page, 2)
        if uCommon.verifyVisible(page, pLogin.ak.adminPanelLbl) == False:
            uCommon.setElem(page, pLogin.ak.emailTxt, dCommon.user.adminKpc.strUserName)
            uCommon.setElem(page, pLogin.ak.passwordTxt, dCommon.user.adminKpc.strPassword)
            uCommon.waitAndClickElem(page, pLogin.ak.loginBtn)
        uCommon.waitForLoadState(page)
        uCommon.wait(page, 5)
        
    @uCommon.ufuncLog 
    def loginToWMS(page):
        """ 
        Objective: Login To WMS
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.goToURL(page, dCommon.url.strWMSUrl)
        uCommon.setElem(page, pLogin.wm.usernameTxt, dCommon.user.adminKpc.strUserName)
        uCommon.setElem(page, pLogin.wm.passwordTxt, dCommon.user.adminKpc.strPassword)
        uCommon.waitAndClickElem(page, pLogin.wm.loginBtn)
        uCommon.waitForLoadState(page)
        uCommon.wait(page, 2)
        uCommon.waitAndClickElem(page, pLogin.wm.stgEdamama)
        uCommon.waitForLoadState(page)
        uCommon.wait(page, 10)
        
    @uCommon.ufuncLog  
    def clickLoginAndFillDetails(page, strUserName, strPassword):
        """ 
        Objective: Click Login And Fill Details
        
        param strUserName: User Name
        param strPassword: Password
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.waitAndClickElem(page, pCommon.header.shopBtn)
        uCommon.waitForLoadState(page, 'networkidle')
        uCommon.waitAndClickElem(page, pCommon.header.LoginBtn)
        uCommon.waitElemToBeVisible(page, pLogin.com.emailAddressTxt)
        uCommon.setElem(page, pLogin.com.emailAddressTxt, strUserName)
        uCommon.setElem(page, pLogin.com.passwordAddressTxt, strPassword)
        uCommon.waitAndClickElem(page, pLogin.com.continueBtn)
        uCommon.waitForLoadState(page)
        uCommon.waitElemToBeVisible(page, pCommon.com.profileIcon)

    @uCommon.ufuncLog  
    def loginToEdamamaViaSocial(page, strSocial):
        """ 
        Objective: Login to Edamama via Gmail or FB
        
        param strSocial: GM | FB
        returns: None
        Author: ccapistrano_20230327
        """
        ln.goToEdamamaURL(page)
        ln.loginAndFillViaSocial(page, strSocial)

    @uCommon.ufuncLog  
    def validateLoginPage(page):
        """ 
        Objective: Validate Login Page Elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['xBtn','edamamaImg', 'loginBtn', 'signUpBtn', 'emailAddressTxt', 'emailAddressLbl', 'emailAddressAsteriskLbl', 'passwordAddressTxt', 'passwordAddressLbl', 
                'passwordAddressAsteriskLbl', 'visibilityOffIconBtn', 'continueBtn', 'forgotYourPasswordBtn', 'continueWithFacebookBtn', 'facebookImg', 'magSignInSaGoogleBtn']
        for item in arrObj:
            uCommon.expectElemToBeVisible(page, pLogin.com.__dict__[item])

    @uCommon.ufuncLog     
    def fillAndClickFB(page, strUsername=dCommon.user.email.strUserName, strPassword=dCommon.user.email.strPassword):
        """ 
        Objective: Fill Facebook user name and password and click Login
        
        param strUsername: User name
        param strPassword: Password
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.setElem(page, pSocial.fb.emailPhoneTxt, strUsername)
        uCommon.setElem(page, pSocial.fb.passwordTxt, strPassword)
        uCommon.clickElem(page, pSocial.fb.loginBtn)

    @uCommon.ufuncLog     
    def fillAndClickGM(page, strUsername=dCommon.user.email.strUserName, strPassword=dCommon.user.email.strPassword):
        """ 
        Objective: Fill Gmail user name and password and click Login
        
        param strUsername: User name
        param strPassword: Password
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.waitElemToBeVisible(page, pSocial.gm.ln.emailNameTxt)
        uCommon.setElem(page, pSocial.gm.ln.emailNameTxt, strUsername)
        uCommon.wait(page, 1)
        uCommon.waitAndClickElem(page, pSocial.gm.ln.nextBtn)
        uCommon.waitElemToBeVisible(page, pSocial.gm.ln.passwordTxt)
        uCommon.setElem(page, pSocial.gm.ln.passwordTxt, strPassword)
        uCommon.wait(page, 1)
        uCommon.waitAndClickElem(page, pSocial.gm.ln.nextBtn)
        uCommon.wait(page, 3)

    @uCommon.ufuncLog   
    def loginAndFillViaSocial(page, strSocial):
        """ 
        Objective: Click Login and fill details via GM or FB
        
        param strSocial: GM | FB
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.waitAndClickElem(page, pCommon.header.LoginBtn)
        uCommon.wait(page, 1)
        if strSocial == 'FB':
            uCommon.wait(page, 2)
            uCommon.waitAndClickElem(page, pLogin.com.continueWithFacebookBtn)
            uCommon.wait(page, 1)
            window = uCommon.switchToWindow(page)
            ln.fillAndClickFB(window)
            uCommon.backToWindow(window)
        elif strSocial == 'GM':
            uCommon.waitAndClickElem(page, pLogin.com.magSignInSaGoogleBtn)
            window = uCommon.switchToWindow(page)
            ln.fillAndClickGM(window)
            uCommon.backToWindow(window)
        uCommon.waitElemToBeVisible(page, pCommon.com.profileIcon)
    
    @uCommon.ufuncLog  
    def validateLoginFormError(page, strField):
        """ 
        Objective: Validate Login form field error

        param strField: Email | Password
        returns: None
        Author: cgrapa_20230601
        """
        uCommon.waitAndClickElem(page, pCommon.header.LoginBtn)
        if strField == "email":
            uCommon.setElem(page, pLogin.com.emailAddressTxt, dCommon.user.strUserName6)
            uCommon.waitAndClickElem(page, pLogin.com.continueBtn)
            uCommon.waitElemToBeVisible(page, pLogin.com.passwordErrorLbl)
        elif strField == "password":
            uCommon.setElem(page, pLogin.com.passwordAddressTxt, dCommon.user.strPassword1)
            uCommon.waitAndClickElem(page, pLogin.com.continueBtn)
            uCommon.waitElemToBeVisible(page, pLogin.com.emailErrorLbl)
        else:
            uCommon.log(2, f'Incorrect strField. Kindly use any of the ff: "email" or "password"')
        ln.validateLoginPage(page)
        
    def goToEdamamaAndValidateShop(page):
        """ 
        Objective: Go to Edamama URL and validate Shop page
        
        param: None
        returns: None
        Author: cgrapa_20230605
        """
        ln.goToEdamamaURL(page)
        uShop.sp.validateShopPage(page, False)
    
    def loginToEdamamaAndValidateShop(page):
        """ 
        Objective: Login to Edamama and validate Shop page
        
        param: None
        returns: None
        Author: cgrapa_20230605
        """
        ln.loginToEdamama(page)
        uShop.sp.validateShopPage(page)
    
    
     
     
class lo:
    """LOGOUT PAGE"""
    @uCommon.ufuncLog 
    def validateLogOutPage(page):
        """ 
        Objective: Validate log out page elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['logOutLbl','logOutMsg', 'noBtn', 'logOutBtn']
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pLogin.lo.__dict__[item])

    @uCommon.ufuncLog  
    def logOutToEdamama(page):
        uCommon.waitAndClickElem(page, pCommon.com.profileIcon)
        com.validateProfileButtons(page)
        uCommon.waitForLoadState(page, 'networkidle')
        uCommon.waitAndClickElem(page, pCommon.pb.logOutBtn)
        lo.validateLogOutPage(page)
        uCommon.waitAndClickElem(page, pLogin.lo.logOutBtn)
        uCommon.waitElemNotToBeVisible(page, pCommon.com.profileIcon)
    
 
 
 
 

class rp:
    """RESET PASSWORD PAGE"""
    @uCommon.ufuncLog 
    def validateForgotPasswordPage(page):
        """ 
        Objective: Validate forgot password page elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['sideScreenImg','edamamaImg', 'xBtn', 'forgotPasswordLbl', 'forgotPasswordDescLbl',
                'emailAddressLbl', 'emailAddressTxt', 'submitBtn']
        for item in arrObj:
            uCommon.expectElemToBeVisible(page, pCommon.fp.__dict__[item])
        
    @uCommon.ufuncLog 
    def validateResetPasswordPage(page):
        """ 
        Objective: Validate reset password page elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['sideScreenImg','edamamaImg', 'xBtn', 'forgotPasswordLbl', 'forgotPasswordDescLbl','newPasswordLbl', 'newPasswordAsteriskLbl', 'newPasswordVisibilityIconBtn',
                'newPasswordTxt', 'confirmPasswordLbl', 'confirmPasswordAsteriskLbl', 'confirmPasswordVisibilityIconBtn', 'confirmPasswordTxt', 'submitBtn']
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pCommon.rp.__dict__[item])

    @uCommon.ufuncLog   
    def validateAndClickProceedToLogin(page):
        """ 
        Objective: Validate and click proceed to login page elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['xBtn','passwordChangedDescLbl', 'proceedToLoginBtn']
        for item in arrObj:
            uCommon.expectElemToBeVisible(page, pCommon.ps.__dict__[item])
        uCommon.clickElem(page, pCommon.ps.proceedToLoginBtn)

    @uCommon.ufuncLog  
    def fillAndClickSubmitResetPassword(page, strNewPassword):
        """ 
        Objective: Fill reset password details and click Submit
        
        param strNewPassword: New password
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.setElem(page, pCommon.rp.newPasswordTxt, strNewPassword)
        uCommon.setElem(page, pCommon.rp.confirmPasswordTxt, strNewPassword)
        uCommon.clickElem(page, pCommon.rp.submitBtn)

    @uCommon.ufuncLog   
    def resetPassword(page, strUserName, strNewPassword):
        """ 
        Objective: Perform reset password
        
        param strUserName: User name
        param strNewPassword: New password
        returns: new window
        Author: ccapistrano_20230327
        """
        ln.goToEdamamaURL(page)
        uCommon.waitAndClickElem(page, pCommon.header.LoginBtn)
        uCommon.waitAndClickElem(page, pLogin.com.forgotYourPasswordBtn)
        rp.validateForgotPasswordPage(page)
        uCommon.setElem(page, pCommon.fp.emailAddressTxt, strUserName)
        uCommon.clickElem(page, pCommon.fp.submitBtn)
        uEmail.loginToGmail(page)
        uCommon.waitElemToBeVisible(page, pSocial.gm.rp.firstPasswordChangemEmaildescLbl)
        uCommon.reloadPage(page)
        uCommon.wait(page, 3) # wait 3 seconds to load and receive new email request
        uCommon.waitAndClickElem(page, pSocial.gm.rp.firstPasswordChangemEmaildescLbl)
        uCommon.waitAndClickElem(page, pSocial.gm.rp.resetPasswordBtn)
        window = uCommon.switchToWindow(page)
        uCommon.closeWindow(window, 0)
        rp.validateResetPasswordPage(window)
        rp.fillAndClickSubmitResetPassword(window, strNewPassword)
        rp.validateAndClickProceedToLogin(window)
        return window





class com:
    """COMMON"""
    @uCommon.ufuncLog 
    def validateWebHeader(page, blnIncLoginBtn = True):
        """ 
        Objective: Validate web header elements
        
        param blnIncLogin: True or False
        returns: None
        Author: ccapistrano_20230327
        """
        if blnIncLoginBtn == True:
            arrObj = ['edamamaLogoImg','searchIconImg', 'searchForYourFavTxt', 'shopBtn',
                'discoverBtn', 'cartIconBtn', 'giftBoxIconBtn']
            for item in arrObj:
                uCommon.expectElemToBeVisible(page, pCommon.header.__dict__[item])
            uCommon.waitElemToBeVisible(page, pCommon.com.profileIcon)
            uCommon.waitElemToBeVisible(page, pCommon.com.arrowDownBtn)  
            uCommon.expectElemNotToBeVisible(page, pCommon.header.LoginBtn)
            uCommon.expectElemNotToBeVisible(page, pCommon.header.signUpBtn)
        else:
            arrObj = ['edamamaLogoImg','searchIconImg', 'searchForYourFavTxt', 'shopBtn',
                'discoverBtn', 'LoginBtn', 'signUpBtn', 'cartIconBtn', 'giftBoxIconBtn']
            for item in arrObj:
                uCommon.expectElemToBeVisible(page, pCommon.header.__dict__[item])
            uCommon.expectElemNotToBeVisible(page, pCommon.com.profileIcon) 
            uCommon.expectElemNotToBeVisible(page, pCommon.com.arrowDownBtn)

    @uCommon.ufuncLog 
    def validateWebTabs(page):
        """ 
        Objective: Validate web tab elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['bannerDescLbl','allCategoriesBtn', 'diaperingBtn', 'fashionBtn', 'foodAndNutrition', 'nurseryBtn', 'feedingAndMealTimeBtn', 
                'mamaBtn', 'babyGearBtn', 'homeAndLifeStyleBtn', 'ToysAndLearningBtn', 'furmamaBtn', 'bathAndBodyBtn']
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pShop.tabs.__dict__[item])

    @uCommon.ufuncLog 
    def validateWebFooter(page):
        """ 
        Objective: Validate web footer elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['edamamaFooterImg','edamamaLogoImg', 'shopBtn', 'discoverBtn', 'connectBtn', 'aboutUsBtn', 
                'sellOnEdamamaBtn', 'helpCenterBtn', 'downloadTheAppLbl', 'appStoreIconBtn', 'googlePlayIconBtn', 'appGaleryIconBtn', 'connectWithUsLbl', 
                'fbIconBtn', 'instagramIconBtn', 'tiktokIconBtn', 'youTubeIconBtn', 'needHelpLbl', 'hereLnk', 'copyRightLbl', 'termOfUseBtn', 'privacyAndPolicyBtn']
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pCommon.footer.__dict__[item])

    @uCommon.ufuncLog 
    def validateWebHeaderAndFooter(page, blnIncLogin = True):
        """ 
        Objective: Validate web header and footer elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        com.validateWebHeader(page, blnIncLogin)
        com.validateWebFooter(page)

    @uCommon.ufuncLog 
    def validateWebHeaderTabsAdFooter(page, blnIncLogin = True):
        """ 
        Objective: Validate web header, tabs and footer elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        com.validateWebHeader(page, blnIncLogin)
        com.validateWebTabs(page)
        com.validateWebFooter(page)
        
    @uCommon.ufuncLog 
    def validateProfileButtons(page):
        """ 
        Objective: Validate profile elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['myProfileBtn','myBeansBtn', 'wishlistBtn', 'myOrdersBtn', 'mySubscriptionBtn', 'logOutBtn']
        for item in arrObj:
            uCommon.expectElemToBeVisible(page, pCommon.pb.__dict__[item])
    
    @uCommon.ufuncLog 
    def goToViaCategory(page, strCategoryName, strLvl3Name):
        """ 
        Objective: Navigate to page via category
        
        param strCategoryName: Category Name
        param strLvl3Name: level 3 name
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.hoverElem(page, pShop.tabs.categoryBtn(strCategoryName))
        uCommon.waitAndClickElem(page, pShop.tabs.lvl3Category(strLvl3Name))

    @uCommon.ufuncLog 
    def validateAllCategoriesTabLevel(page):  
        """ 
        Objective: Validate all categories elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.wait(page, 1)
        uCommon.expectElemToBeVisible(page, pShop.tabs.allCategoriesBtn)
        uCommon.hoverElem(page, pShop.tabs.allCategoriesBtn)
        arrObj = ['diaperingBtn','wipesBtn', 'diapersBagBtn', 'changingMatTablesBtn', 'changingMatTablesBtn', 'disposableDiapersBtn', 'clothDiapersBtn', 'fashionBtn', 
                'sleepWearBtn', 'womensFashionBtn', 'sweatShirtsJacketBtn', 'socksTightsBtn', 'innerWearBtn', 'onesieRomperBtn', 'shortSkirtsBtn', 'topBottomSetBtn', 'mensFashionBtn',
                'topsTshirtBtn', 'parentChildSetBtn', 'dressJumpsuitBtn', 'costumesBtn', 'swimWearBenchWearBtn', 'footWearBtn', 'kidsAccessoriesBtn', 'foodNutritionBtn', 
                'formulaMilkBtn','foodSnacksBtn', 'beveragesBtn', 'vitaminsSupplementsBtn', 'healthyAlternativesBtn', 'nurseryBtn', 'furnitueDecorBtn', 'childProofingBtn',
                'babyMonitorsBtn', 'cribEssentialsBtn', 'beddingEssentialsBtn', 'bouncersRockersSwingsBtn', 'playpensBtn', 'feedingMealtimeBtn', 'bottlesCupAccBtn', 'mealTimeBtn',
                'highChairsBtn', 'foodContainerUtensilsBtn', 'lunchBagsContainersBtn', 'feedingMatsBtn', 'feedingSetBtn', 'mamaBtn', 'lifeStyleWellnessBtn',  'breastFeedingBtn',
                'reproductiveHealthBtn', 'maternityBtn', 'babyGearBtn', 'carriersBtn', 'gearAccessoriesBtn', 'StrollerBtn', 'carSeatBtn', 'walkersBtn', 'boosterSeatsBtn', 
                'carryCotBtn', 'luggageBtn', 'homeLifeStyleBtn', 'homeDecorBtn', 'cleaningBtn', 'bedroomBtn', 'laundryBtn', 'appliancesElectornicsBtn', 'kitchenDiningBtn', 
                'outdoorGardenBtn', 'homeOfficeBtn', 'sportsTravelBtn', 'toysLearningBtn', 'artsCraftsBtn', 'toysBtn', 'booksBtn', 'outdoorBtn', 'homeSchoolingBtn', 
                'furmamaBtn', 'petFoodBtn', 'bathingGroomingBtn', 'petAccessoriesBtn', 'petHealthCareBtn','cleaningPottyBtn','bowlsFeedersBtn', 'petToysBtn']
        for item in arrObj:
            uCommon.expectElemToBeExist(page, pShop.tabs.ac.__dict__[item])

    @uCommon.ufuncLog  
    def validateCountInCart(page, strCount = 1):
        """ 
        Objective: Validate product count in Cart
        
        param strCount: Product count
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.validateElemText(page, pCommon.com.cartCounterLbl, strCount)
        
    @uCommon.ufuncLog  
    def clickCartCount(page):
        """ 
        Objective: Click the number of product in the cart
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.clickElem(page, pCommon.com.cartCounterLbl)
        
    @uCommon.ufuncLog  
    def clickProfile(page):
        """ 
        Objective: Click Profile
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.waitAndClickElem(page, pCommon.com.profileIcon)
        uCommon.waitElemToBeVisible(page, pCommon.pb.myProfileBtn)
        
    @uCommon.ufuncLog  
    def clickMyProfile(page):
        """ 
        Objective: Click My Profile
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.waitAndClickElem(page, pCommon.pb.myProfileBtn)
        uCommon.wait(page, 1)
        uCommon.waitElemToBeVisible(page, pMyProfile.com.nameLbl)

    @uCommon.ufuncLog  
    def clickMySubscription(page):
        """ 
        Objective: Click My Subscription
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.waitAndClickElem(page, pCommon.pb.mySubscriptionBtn)
        uCommon.waitElemToBeVisible(page, pMySubcription.at.editSubscriptionBtn)
        
    @uCommon.ufuncLog  
    def navigateToProfileMenu(page, strMenu):
        """ 
        Objective: Navigate to Profile and Click desired option
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        com.clickProfile(page)
        uCommon.wait(page, 1)
        match strMenu:
            case 'my profile':
                uCommon.waitAndClickElem(page, pCommon.pb.myProfileBtn)
                uCommon.wait(page, 1)
                uCommon.waitElemToBeVisible(page, pMyProfile.com.nameLbl)
            case 'my subscription':
                uCommon.waitAndClickElem(page, pCommon.pb.mySubscriptionBtn)
                uCommon.waitElemToBeVisible(page, pMySubcription.at.editSubscriptionBtn)
            case 'my orders':
                uCommon.waitAndClickElem(page, pCommon.pb.myOrdersBtn)
                uCommon.waitElemToBeVisible(page, pMyOrders.com.myOrdersLbl)
            case 'my wishlist':
                uCommon.waitAndClickElem(page, pCommon.pb.wishlistBtn)
                uCommon.waitElemToBeVisible(page, pMyWishlist.com.savedItemsLbl)
            case _:
                uCommon.log(2, f'Incorrect strMenu. Kindly use any of the ff: "my profile", "my subscription", "my orders" or "my wishlist"')          





class error:
    @uCommon.ufuncLog
    def validatePopUpMsg(page, strMsg):
        """
        Objective: Validate page popup message
        
        param strErrorMsg: Error message text
        returns: None
        Author: cgrapa_20230609
        """
        uCommon.waitAndValidateElemText(page, pCommon.error.genErrorLbl(strMsg), strMsg)