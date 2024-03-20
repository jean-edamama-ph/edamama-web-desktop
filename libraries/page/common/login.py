class com:
    """COMMON"""
    xBtn = '//button[@class="close-btn"]'
    edamamaImg = '//img[@src="assets/images/edamamalogosquaregreen.png"]'
    loginBtn = '//div[text()="LOG IN"]'
    signUpBtn = '//div[text()="SIGN UP"]'
    emailAddressTxt = '//input[@data-placeholder="Email Address"]'
    emailAddressLbl = f'{emailAddressTxt}/..//span[text()="Email Address"]'
    emailAddressAsteriskLbl = f'{emailAddressLbl}/..//span[text()=" *"]'
    passwordAddressTxt = '//input[@data-placeholder="Password"]'
    passwordAddressLbl = f'{passwordAddressTxt}/..//span[text()="Password"]'
    passwordAddressAsteriskLbl = f'{passwordAddressLbl}/..//span[text()=" *"]'
    visibilityOffIconBtn = '//mat-icon[contains(text(),"visibility_off")]'
    continueBtn = '//button[@type="submit"]//span[normalize-space(text())="CONTINUE"][@class="mat-button-wrapper"]'
    forgotYourPasswordBtn = '//button[contains(text(),"Forgot your password ?")]'
    continueWithFacebookBtn = '//button[contains(text(),"Continue with Facebook")]'
    facebookImg = '//img[@src="assets/images/socials/facebook.png"]'
    magSignInSaGoogleBtn = '//span[text()="Mag-sign in sa Google"][1]'
    emailErrorLbl = '//mat-error[text()=" Email is required. "]'
    passwordErrorLbl = '//mat-error[text()=" Password is required. "]'
    
class lo:
    """LOGOUT"""
    logOutLbl = '//h1[text()="Logout"]'
    logOutMsg = '//p[text()="Do you wish to logout?"]'
    noBtn = '//button//span[contains(text(),"No")]'
    logOutBtn = '//button//span[contains(text(),"Logout")]'
    
    
class ak:
    """ADMIN KPC"""
    loginLbl = '//h1[contains(text(),"Login")]'
    emailTxt = '//input[@formcontrolname="email"]'
    passwordTxt = '//input[@formcontrolname="password"]'
    loginBtn = '//button//span[text()="Login"]'
    adminPanelLbl = '//h3[text()="Admin Panel (V1)"]'
    
class wm:
    """WMS"""
    usernameTxt = '//input[@id="username"]'
    passwordTxt = '//input[@id="password"]'
    loginBtn = '//input[@name="login"]'
    stgEdamama = '//div[@account-code="stgedamama"]'
    
    