import libraries.data.common as dCommon
import libraries.page.common.social as pSocial
import libraries.page.profile.myGifts as pMyGifts
import libraries.util.common as uCommon
import libraries.util.appCommon.appComm as uAppComm
import libraries.util.profile.myGifts as uMyGifts


@uCommon.ufuncLog  
def goToGmailURL(page):
    uCommon.goToURL(page, dCommon.url.strUrlGmail)

@uCommon.ufuncLog  
def loginToGmail(page):
    """ 
    Objective: login to Gmail
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    goToGmailURL(page)
    uCommon.clickElem(page, pSocial.gm.ln.signInBtn)
    uCommon.wait(page, 2)
    if uCommon.verifyVisible(page, pSocial.gm.ln.useAnotherAccountBtn) == True:
        uCommon.clickElem(page, pSocial.gm.ln.useAnotherAccountBtn)
    uAppComm.ln.fillAndClickGM(page) 
    
@uCommon.ufuncLog  
def clickFirstConfirmEmail(page, dictData):
    """ 
    Objective: Click first confirm email
    
    param dictData: {strFirstName, strLastName, strEmailAddress, strPassword}
    returns: None
    Author: ccapistrano_20230327
    """
    strFirstName = dictData['strFirstName']
    uCommon.waitAndClickElem(page, pSocial.gm.rp.firstConfirmEmailDescLbl)
    uCommon.waitAndValidateElemText(page, pSocial.gm.rp.firstNameLbl, strFirstName, False)
      
@uCommon.ufuncLog  
def clickYesThisIsMyEmail(page):
    """ 
    Objective: Click Yes this is my email
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    uCommon.waitAndClickElem(page, pSocial.gm.rp.yesThisIsMyEmailBtn)
    
@uCommon.ufuncLog  
def validateWeGotYourOrderEmail(page, strOrderID):
    """ 
    Objective: Validate we got your order email notification
    
    param strOrderID: Order ID
    returns: None
    Author: ccapistrano_20230327
    """
    uCommon.waitElemToBeVisible(page, pSocial.gm.rp.weGotYourOrderLbl(strOrderID))
    
@uCommon.ufuncLog  
def validatecreatedGiftListEmail(page, strUsername):
    """ 
    Objective: Validate created Gift List email notification
    
    param strUsername: User Name
    returns: None
    Author: ccapistrano_20230516
    """
    uCommon.waitElemToBeVisible(page, pSocial.gm.rp.successfullCreatedGiftListLbl(strUsername))
    
@uCommon.ufuncLog  
def validateAndClickInvitedGiftListEmail(page, strUsername):
    """ 
    Objective: Validate and cLickinvited Gift List email notification
    
    param strUsername: User Name
    returns: None
    Author: ccapistrano_20230516
    """
    uCommon.wait(page, 1)
    uCommon.waitAndClickElem(page, pSocial.gm.rp.invitedGiftListLbl(strUsername))
    uCommon.waitAndClickElem(page, pSocial.gm.rp.viewGiftListBtn)
    window = uCommon.switchToWindow(page)
    uCommon.waitElemToBeVisible(window, pMyGifts.ml.buySelectedGiftsBtn)
    uCommon.reloadPage(window)
    uCommon.backToWindow(window)
    
@uCommon.ufuncLog  
def validateAndClickSubscriptionDetailsChangedEmail(page, strUsername, strProductName):
    """ 
    Objective: Validate and cLickinvited Gift List email notification
    
    param strUsername: User Name
    returns: None
    Author: ccapistrano_20230516
    """
    uCommon.wait(page, 1)
    uCommon.clickOptElem(page, pSocial.gm.rp.closeIconBtn)
    uCommon.waitAndClickElem(page, pSocial.gm.rp.subscriptionDetailsChangedLbl(strUsername))
    uCommon.waitAndClickElemText(page, strProductName, pSocial.gm.rp.divOrderDetailsElm)
    

@uCommon.ufuncLog  
def clickYouveBeanRewardChild(page, dictData):
    """ 
    Objective: Click "You've BEAN rewarded" for adding a child.
    
    param dictData: {strFirstName, strLastName, strEmailAddress, strPassword}
    returns: None
    Author: abernal_20240312
    """
    uCommon.wait(page, 1)
    strFirstName = dictData['strFirstName']
    uCommon.waitAndClickElem(page, pSocial.gm.rp.youveBeanRewardedChildLbl)
    uCommon.waitElemToBeVisible(page, pSocial.gm.rp.successfulBeanRewardChildLbl)
    uCommon.waitAndValidateElemText(page, pSocial.gm.rp.congratulationsFirstNameLbl, strFirstName, False)
    

@uCommon.ufuncLog  
def clickBackButtonOnEmail(page):
    """ 
    Objective: Click back button on email
    
    param: None
    returns: None
    Author: abernal_20240313
    """
    uCommon.wait(page, 1)
    uCommon.waitAndClickElem(page, pSocial.gm.rp.inboxBtn)
    
@uCommon.ufuncLog  
def clickYouveBeanRewardAttribute(page, dictData):
    """ 
    Objective: Click "You've BEAN rewarded" for adding a attribute.
    
    param dictData: {strFirstName, strLastName, strEmailAddress, strPassword}
    returns: None
    Author: abernal_20240313
    """
    uCommon.wait(page, 1)
    strFirstName = dictData['strFirstName']
    uCommon.waitAndClickElem(page, pSocial.gm.rp.youveBeanRewardedAttributesLbl)
    uCommon.waitElemToBeVisible(page, pSocial.gm.rp.successfulBeanRewardAttributesLbl)
    uCommon.waitAndValidateElemText(page, pSocial.gm.rp.congratulationsFirstNameLbl, strFirstName, False)
    
@uCommon.ufuncLog  
def clickYouveBeanRewardRegistration(page, dictData):
    """ 
    Objective: Click "You've BEAN rewarded" for registration.
    
    param dictData: {strFirstName, strLastName, strEmailAddress, strPassword}
    returns: None
    Author: abernal_20240313
    """
    uCommon.wait(page, 1)
    strFirstName = dictData['strFirstName']
    uCommon.waitAndClickElem(page, pSocial.gm.rp.youveBeanRewardedRegisterLbl)
    uCommon.waitElemToBeVisible(page, pSocial.gm.rp.successfulBeanRewardRegisterLbl)
    uCommon.waitAndValidateElemText(page, pSocial.gm.rp.congratulationsFirstNameLbl, strFirstName, False)
    
@uCommon.ufuncLog  
def clickYouveBeanRewardPurchasing(page):
    """ 
    Objective: Click "You've BEAN rewarded" for purchasing a product.
    
    param: None
    returns: None
    Author: abernal_20240314
    """
    uCommon.wait(page, 1)
    uCommon.waitAndClickElem(page, pSocial.gm.rp.youveBeanRewardedPurchaseLbl)
    uCommon.waitElemToBeVisible(page, pSocial.gm.rp.successfulBeanRewardPurchaseLbl)