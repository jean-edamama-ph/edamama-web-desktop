class gm:
    """GMAIL""" 
    class ln: # LOGIN
        """LOGIN"""
        signInBtn = '//a[text()="Sign in"]'
        emailNameTxt = '//input[@name="identifier"]'
        nextBtn = '//button/span[text()="Next"]/..'
        passwordTxt = '//input[@name="Passwd"] | //input[@name="password"]'
        useAnotherAccountBtn = '//div[text()="Use another account"]'
        
    class rp: # RIGHT PANEL
        """RIGHT PANEL"""
        firstConfirmEmailDescLbl = '(//span[@class="bog"]//span[contains(text(),"You\'re almost ready for a new shopping experience at edamama! - Click here to confirm your email address.")])[1]'
        yesThisIsMyEmailBtn = '//div[contains(text(),"Confirm Email Address")]'
        nextBtn = '//button//span[text()="Next"]'
        passwordTxt = '//input[@name="Passwd"]'
        firstPasswordChangemEmaildescLbl = '(//span[@class="bog"]//span[contains(text(),"] Password change for edamama")])[1]'
        resetPasswordBtn = '//div[contains(text(),"Reset Password")]'
        def weGotYourOrderLbl(strOrderID):
            return f'//span[contains(text(),"We got your order!")][contains(text(),"{strOrderID}")]'
        def successfullCreatedGiftListLbl(strUsername):
            return f'(//span[contains(text(),"{strUsername}")]/..//span[text()="[KPC] You\'ve successfully created your Gift List!"])[1]'
        def invitedGiftListLbl(strUsername):
            return f'(//span[contains(text(),"{strUsername}")]/..//span[text()="[KPC] You\'ve been invited to a Gift List!"])[1]'
        viewGiftListBtn = '//a//td[contains(text(),"View Gift List")]'
        def subscriptionDetailsChangedLbl(strUsername):
            return f'(//span[contains(text(),"{strUsername}")]/..//span[text()="[KPC] Subscription Details Changed!"])[1]'
        divOrderDetailsElm = '//div[contains(@class,"order-details-wrapper")]'
        closeIconBtn = '//button[@aria-label="Close"]'
        firstNameLbl = '//div[contains(@class,"msg")]//span[contains(text(), "Hello there")]'
     
class fb:
    """FACEBOOK"""   
    emailPhoneTxt = '//input[@name="email"]'
    passwordTxt = '//input[@name="pass"]'
    loginBtn = '//input[@name="login"]'
    mobileRdb = '(//div[@data-visualcompletion="ignore-dynamic"]//i[@data-visualcompletion="css-img"])[1]'
    continueBtn = '//span[text()="Continue"]'