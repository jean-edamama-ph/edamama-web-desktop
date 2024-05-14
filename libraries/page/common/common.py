xBtn = '//button[@class="mat_close"]'
edamamaImg = '//img[@alt="edamama logo"]'
edamama2Img = '//img[@src="assets/images/logo_wht_new.png"]'

class com:
    """COMMON"""
    edamamaImg = edamamaImg
    continueWithEdamamaLbl = '//h2[text()="Continue with edamama"]'
    pleaseSelectWhereLbl = '//span[normalize-space(text())="Please select where you want to proceed with edamama."]'
    openInAppBtn = '//button[normalize-space(text())="Open in App"]'
    continueViaWebBtn = '//button[normalize-space(text())="Continue via web"]'
    openBtn = '//a[text()="OPEN"]'

    cartIconBtn = '//nav[contains(@class,"navbar")]//span[text()="Signup"]//img[@src="./assets/images/header/cart.svg"]'
    giftBoxIconBtn = '//nav[contains(@class,"navbar")]//span[text()="Signup"]//img[@src="assets/images/header/gift-registry.svg"]'
    profileIcon = '//div[@class="profile-thumbnail"]//img'
    arrowDownBtn = '//mat-icon[text()="keyboard_arrow_down"]'
    cartCounterLbl = '//span[@id="cartCounter"]'

class header:
    """HEADER"""
    edamamaLogoImg = '//img[starts-with(@src,"https://media-v4.edamama.ph/pre-fetch/https://www.")][contains(@src,".edamamalabs.net/assets/images/logo_new.png")]'
    searchIconImg = '//mat-icon[text()="search"]'
    searchForYourFavTxt = '//input[@placeholder="Search for your favorite products and brands..."]'
    xBtn = '//button/mat-icon[text()="close"]'
    shopBtn = '//nav[contains(@class,"navbar")]//span[text()="Shop"]'
    discoverBtn = '//nav[contains(@class,"navbar")]//span[text()="Discover"]'
    ExploreBtn = '//nav[contains(@class,"navbar")]//span[text()="Explore"]'
    LoginBtn = '//nav[contains(@class,"navbar")]//span[text()="Login"]/..'
    signUpBtn = '//nav[contains(@class,"navbar")]//span[text()="Signup"]'
    cartIconBtn = '//img[@src="./assets/images/header/cart.svg"]'
    giftBoxIconBtn = '//img[@src="assets/images/header/gift-registry.svg"]'
       
class footer:
    """FOOTER"""
    edamamaFooterImg = '//footer[@id="edamama-footer"]'
    edamamaLogoImg = '//img[starts-with(@src,"https://media-v4.edamama.ph/pre-fetch/https://www.")][contains(@src,".edamamalabs.net/assets/images/footer/edamama-logo-white.png")]'
    shopBtn = '//a[text()="Shop"][@href="/shop"]'
    discoverBtn = '//a[text()="Discover"][@href="/discover"]'
    connectBtn = '//a[text()="Connect"][@href="/category/connect"]'
    aboutUsBtn = '//a[text()="About Us"][@href="/about-us"]'
    sellOnEdamamaBtn = '//a[text()=" Sell on edamama "][@href="https://edamama-phcs.freshdesk.com/support/solutions/articles/72000534612-i-want-to-partner-with-edamama-"]'
    helpCenterBtn = '//a[text()=" Help Center"][@href="https://edamama-phcs.freshdesk.com"]'  
    downloadTheAppLbl = '//p[text()="Download the app"]'
    appStoreIconBtn = '//footer//a[@href="https://apps.apple.com/app/edamama-mom-and-baby-shopping/id1545877212"]'
    googlePlayIconBtn = '//footer//a[@href="https://play.google.com/store/apps/details?id=com.edamama.app"]'
    appGaleryIconBtn = '//footer//img[@src="https://media-v4.edamama.ph/pre-fetch/https://www.kpc.edamamalabs.net/assets/images/badge/huawei-badge.png"]'
    connectWithUsLbl = '//p[text()="Connect with us"]'
    fbIconBtn = '//a[@href="https://www.facebook.com/edamama.ph"]'
    instagramIconBtn = '//a[@href="https://www.instagram.com/edamama.ph/"]'
    tiktokIconBtn = '//a[@href="https://www.tiktok.com/@edamama.ph/"]'
    youTubeIconBtn = '//a[@href="https://www.youtube.com/channel/UCUKcx-rUn_v0mz07FrKav9Q"]'
    needHelpLbl = '//p[text()=" Need help? Please Connect with us "]'
    hereLnk = '//a[@href="https://edamama-phcs.freshdesk.com/support/tickets/new"]'
    copyRightLbl = '//p[text()="© 2024 edamama.ph"]'
    termOfUseBtn = '//a[text()="Terms of Use"][@href="/terms-of-use"]'
    privacyAndPolicyBtn = '//a[text()=" Privacy Policy"][@href="/privacy-policy"]'

    
    
    
    
class pb:
    """PROFILE BUTTONS"""
    myProfileBtn = '//button[contains(text(),"My Profile")]'
    myBeansBtn = '//button[contains(text(),"My Beans")]'
    wishlistBtn = '//button[contains(text(),"Wishlist")]'
    myOrdersBtn = '//button[contains(text(),"My Orders")]'
    mySubscriptionBtn = '//button[contains(text(),"My Subscriptions")]'
    logOutBtn = '//button[contains(text(),"Logout")]'
    
class fp:
    """FORGOT PASSWORD"""
    sideScreenImg = '//div[@class="side-screen"]/img[@src="./assets/images/forgot_bg.jpg"]'
    edamamaImg = edamama2Img
    xBtn = xBtn
    forgotPasswordLbl = '//h2[contains(text(),"Forgot")][text()=" Password "]'
    forgotPasswordDescLbl = '//p[contains(text(),"Enter your registered email address, we\'ll send you the reset instructions.")]'
    emailAddressLbl = '//span[text()="Email Address"]'
    emailAddressTxt = '//input[@data-placeholder="Email Address"]'
    submitBtn = '//button/span[contains(text(),"Submit")]'
    
class rp:
    """RESET PASSWORD"""
    sideScreenImg = '//div[@class="side-screen"]/img[@src="./assets/images/reset_bg.jpg"]'
    edamamaImg = edamama2Img
    xBtn = xBtn
    forgotPasswordLbl = '//h2[contains(text(),"Reset")][text()=" Password "]'
    forgotPasswordDescLbl = '//p[contains(text(),"Enter your new password below to update your credentials.")]'
    newPasswordLbl = '//span[text()="New Password"]'
    newPasswordAsteriskLbl = f'{newPasswordLbl}/..//span[contains(text()," *")]'
    newPasswordVisibilityIconBtn = f'{newPasswordLbl}/../../../..//mat-icon[contains(text(),"visibility")]'
    newPasswordTxt = '//input[@data-placeholder="New Password"]'
    confirmPasswordLbl = '//span[text()="Confirm New Password"]'
    confirmPasswordAsteriskLbl = f'{newPasswordLbl}/..//span[contains(text()," *")]'
    confirmPasswordVisibilityIconBtn = f'{newPasswordLbl}/../../../..//mat-icon[contains(text(),"visibility")]'
    confirmPasswordTxt = '//input[@data-placeholder="Confirm New Password"]'
    submitBtn = '//button/span[contains(text(),"Submit")]/..'
    
class ps:
    """PASSWORD SUCCESSFULLY CHANGED"""
    xBtn = xBtn
    passwordChangedDescLbl = '//h3[text()="Your password has been successfully changed."]'
    proceedToLoginBtn  = '//button/span[contains(text(),"Proceed to Login")]'
    
class go:
    """GLOBAL OBJECT"""
    def getColIndex(strParent, strColName):
        return f'count(//td[contains(text(),"{strParent}")]/ancestor::div[1]//th[contains(text(),"{strColName}")]/preceding-sibling::th)+1'
    
class pp:
    """PRIVACY POLICY"""
    privacyPolicyTitleLbl = '//h2[text()="Privacy Policy"]'
    
class tu:
    """TERMS OF USE"""
    termsOfUseTitleLbl = '//h2[text()="Terms & Conditions"]'
    
class error:
    def genErrorLbl(strMsg):
        return f'//*[normalize-space(text())="{strMsg}"]'