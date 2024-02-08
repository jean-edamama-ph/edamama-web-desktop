import libraries.page.common.signUp as pSignUp
import libraries.page.common.common as pCommon

import libraries.util.common as uCommon
import libraries.util.appCommon.appComm as uAppComm

@uCommon.ufuncLog
def clickSignUp(page):
    """ 
    Objective: Click sign up
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    # uCommon.waitForLoadState(page, 'networkidle')
    uCommon.waitAndClickElem(page, pCommon.header.signUpBtn)
    uCommon.waitForLoadState(page, 'networkidle')
    uCommon.waitElemToBeVisible(page, pSignUp.com.firstNameTxt)

@uCommon.ufuncLog
def clickSignUpContinue(page, blnRegistered = False):
    """ 
    Objective: Click sign up page Continue button
    
    param: None
    returns: None
    Author: cgrapa_20230609
    """
    uCommon.waitAndClickElem(page, pSignUp.com.continueBtn)
    if blnRegistered == True:
        uCommon.waitElemToBeVisible(page, pSignUp.com.emailErrorMsg)
    else:
        uCommon.wait(page, 1)

@uCommon.ufuncLog  
def validateSignUpPage(page):
    """ 
    Objective: Validate sign up page elements
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    arrObj = ['edamamaImg','loginBtn', 'signUpBtn', 'creditsDescLbl', 'learnMoreLnk', 'firstNameLbl', 'emailAddressAsteriskLbl', 'firstNameTxt',
              'lastNameLbl', 'lastAsteriskLbl', 'lastNameTxt', 'emailAddressLbl', 'emailAddressAsteriskLbl', 'emailAddressTxt', 'passwordAddressLbl', 
              'passwordAddressAsteriskLbl', 'passwordAddressTxt', 'visibilityOffIconBtn', 'acceptChk', 'acceptLbl', 'privacyPolicyLnk', 'termsOfUseLnk',
              'continueBtn', 'continueWithFacebookBtn', 'facebookImg', 'magSignInSaGoogleBtn']
    for item in arrObj:
        uCommon.waitElemToBeVisible(page, pSignUp.com.__dict__[item])

@uCommon.ufuncLog  
def validateAccountVerificationPage(page):
    """ 
    Objective: Validate account verification page elements
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    arrObj = ['xBtn','accountVerificationLbl', 'aLinkHasBeenSentLbl', 'verifyYourEmailLbl', 'okBtn']
    uCommon.waitElemToBeVisible(page, pSignUp.av.xBtn)
    for item in arrObj:
        uCommon.expectElemToBeVisible(page, pSignUp.av.__dict__[item])

@uCommon.ufuncLog  
def validateAndClickOKinAccountVerification(page):
    """ 
    Objective: Validate account verification page elements and Click OK
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    validateAccountVerificationPage(page)
    uCommon.clickElem(page, pSignUp.av.okBtn)

@uCommon.ufuncLog  
def fillOutSignUpPage(page, dictData):
    """ 
    Objective: Fill out sign up page
    
    param dictData: {strFirstName, strLastName, strEmailAddress, strPassword}
    returns: None
    Author: ccapistrano_20230327
    """
    uCommon.waitAndClickElem(page, pSignUp.com.firstNameTxt)
    if dictData['strFirstName'] != '':
        uCommon.setElem(page, pSignUp.com.firstNameTxt, dictData['strFirstName'])
    uCommon.waitAndClickElem(page, pSignUp.com.lastNameTxt)
    if dictData['strLastName'] != '':
        uCommon.setElem(page, pSignUp.com.lastNameTxt, dictData['strLastName'])
    uCommon.waitAndClickElem(page, pSignUp.com.emailAddressTxt)
    if dictData['strEmailAddress'] != '':
        uCommon.setElem(page, pSignUp.com.emailAddressTxt, dictData['strEmailAddress'])
    uCommon.waitAndClickElem(page, pSignUp.com.passwordAddressTxt)
    if dictData['strPassword'] != '':
        uCommon.setElem(page, pSignUp.com.passwordAddressTxt, dictData['strPassword'])
    uCommon.waitAndClickElem(page, pSignUp.com.passwordAddressLbl)
    return {'strFirstName': dictData['strFirstName'], 'strLastName': dictData['strLastName'], 'strEmailAddress': dictData['strEmailAddress'], 'strPassword': dictData['strPassword']}

@uCommon.ufuncLog  
def fillandContinueSignUpPage(page, objData):
    """ 
    Objective: Fill out sign up page and click Continue
    
    param dictData: {strFirstName, strLastName, strEmailAddress, strPassword}
    returns: None
    Author: ccapistrano_20230327
    """
    arrData = fillOutSignUpPage(page, objData)
    uCommon.hoverAndClickElem(page, pSignUp.com.acceptChk)
    uCommon.wait(page, .5)
    clickSignUpContinue(page)
    return arrData

@uCommon.ufuncLog  
def validateEmailVerificationPage(page):
    """ 
    Objective: Validate email verification page
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    arrObj = ['successIconImg','xBtn', 'emailVerificationSuccessfullLbl', 'userEmailLbl', 'youHaveEarnedLbl',
              'fiveBeansLbl', 'startShoppingBtn', 'getadditionalLbl', 'tenBeansLbl', 'completeMyProfileBtn', 'rightArrowBtn']
    for item in arrObj:
        uCommon.expectElemToBeVisible(page, pSignUp.ev.__dict__[item])

@uCommon.ufuncLog     
def validateEmailVerificationPageAndClickCompleteMyProfile(page):
    """ 
    Objective: Validate email verification page and click Complete My Profile
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    validateEmailVerificationPage(page)
    uCommon.clickElem(page, pSignUp.ev.rightArrowBtn)

@uCommon.ufuncLog  
def validateAddChildPage(page):
    """ 
    Objective: Validate add child page 
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    arrObj = ['edamamaImg','childNameLbl', 'childNameTxt', 'birthDateLbl', 'birthDateTxt',
              'calendarIconImg', 'genderLbl', 'boyLbl', 'boyRdb', 'girlLbl', 'girlRdb',
              'ratherNotToSayLbl', 'ratherNotToSayRdb', 'addChildBtn', 'skipBtn', 'nextBtn']
    for item in arrObj:
        uCommon.expectElemToBeVisible(page, pSignUp.ac.__dict__[item])

@uCommon.ufuncLog        
def fillAndAddChild(page):
    """ 
    Objective: Fill and add child 
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    uCommon.setElem(page, pSignUp.ac.childNameTxt, 'testChild')
    uCommon.waitAndClickElem(page, pSignUp.ac.calendarIconImg)
    uCommon.wait(page, .5)
    uCommon.waitAndClickElem(page, pSignUp.ac.yearLbl('2023'))
    uCommon.waitAndClickElem(page, pSignUp.ac.monthLbl('MAR'))
    uCommon.waitAndClickElem(page, pSignUp.ac.dateLbl('20'))
    uCommon.wait(page, .5)
    uCommon.waitAndClickElem(page, pSignUp.ac.girlLbl)
    uCommon.wait(page, .5)
    uCommon.clickElem(page, pSignUp.ac.addChildBtn)
    uCommon.waitElemToBeVisible(page, pSignUp.ac.childAddSuccessfullyMsg)

@uCommon.ufuncLog  
def validateAlmostDonePage(page):
    """ 
    Objective: Validate almost done page 
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    arrObj = ['edamamaImg','almostDoneLbl', 'pickAttributesDescLbl', 'rewardOnCompletingDescLbl', 'learnMoreLnk',
              'activeMamaBtn', 'activeMamaLbl', 'careerMamaBtn', 'careerMamaLbl', 'craftyMamaBtn', 'craftyMamaLbl',
              'dealQueenBtn', 'dealQueenLbl', 'expectingMamaBtn', 'expectingMamaLbl', 'fashionistaBtn', 'fashionistaLbl',
              'firstTimeMamaBtn', 'firstTimeMamaLbl', 'mamaChefBtn', 'mamaChefLbl', 'mamaTeacherBtn', 'mamaTeacherLbl', 'mamasteBtn',
              'mamasteLbl', 'modernMamaBtn', 'modernMamaLbl', 'naturalMamaBtn', 'naturalMamaLbl', 'notAMamaBtn', 'notAMamaLbl',
              'partyPlannerBtn', 'partyPlannerLbl', 'stayAtHomeMamaBtn', 'stayAtHomeMamaLbl', 'skipBtn', 'nextBtn']
    for item in arrObj:
        uCommon.expectElemToBeVisible(page, pSignUp.ad.__dict__[item])

@uCommon.ufuncLog  
def validateThankYouPage(page):
    """ 
    Objective: validate Thank you page 
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    arrObj = ['xBtn','thankYouLbl', 'thankYouDescLbl', 'continueBtn']
    for item in arrObj:
        uCommon.waitElemToBeVisible(page, pSignUp.ty.__dict__[item])

@uCommon.ufuncLog  
def validateThankYouAndClickContinue(page):
    """ 
    Objective: validate Thank you page and click Continue
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    validateThankYouPage(page)
    uCommon.waitAndClickElem(page, pSignUp.ty.continueBtn)

@uCommon.ufuncLog  
def clickNotAMama(page):
    """ 
    Objective: Click Not a mama
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    uCommon.clickElem(page, pSignUp.ad.notAMamaBtn)
    
@uCommon.ufuncLog  
def clickSubmit(page):
    """ 
    Objective: Click Submit
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    uCommon.clickElem(page, pSignUp.ad.submitBtn)

        
@uCommon.ufuncLog
def clickPrivacyPolicyAndValidatePage(page):
    """ 
    Objective: Click Privacy Policy link and validate page

    param: None
    returns: None
    Author: cgrapa_20230605
    """
    uCommon.waitAndClickElem(page, pSignUp.com.privacyPolicyLnk)
    window = uCommon.switchToWindow(page)
    uCommon.waitForLoadState(window)
    uCommon.waitElemToBeVisible(window, pCommon.pp.privacyPolicyTitleLbl)
    uCommon.closeWindow(page)
    
@uCommon.ufuncLog
def clickTermsOfUseAndValidatePage(page):
    """ 
    Objective: Click Terms of Use link and validate page

    param: None
    returns: None
    Author: cgrapa_20230605
    """
    uCommon.waitAndClickElem(page, pSignUp.com.termsOfUseLnk)
    window = uCommon.switchToWindow(page)
    uCommon.waitForLoadState(window)
    uCommon.waitElemToBeVisible(window, pCommon.tu.termsOfUseTitleLbl)
    uCommon.closeWindow(page)
    
@uCommon.ufuncLog
def validatePolicyLinks(page):
    """ 
    Objective: Validate Privacy Policy and Terms of Use links

    param: None
    returns: None
    Author: cgrapa_20230605
    """
    clickPrivacyPolicyAndValidatePage(page)
    clickTermsOfUseAndValidatePage(page)

uCommon.ufuncLog
def clickPrivPolAndTermsOfUseCheckBox(page):
    """ 
    Objective: To Click the Privacy Policy and Terms of Use check box

    param: None
    returns: None
    Author: rmakiling_20240117
    """
    uCommon.hoverAndClickElem(page, pSignUp.com.acceptChk)
    
@uCommon.ufuncLog
def verifyIfAlreadyRegistered(page, dictData):
    """ 
    Objective: Verify if the Email is already registered

    param: None
    returns: None
    Author: rmakiling_20240117
    """
    uAppComm.ln.loginToEdamama(page, dictData)
    uCommon.waitElemToBeVisible(page, pSignUp.com.profileIcon)


