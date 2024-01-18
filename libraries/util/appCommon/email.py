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
    uMyGifts.sh.clickSharedWithMe(window)
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
    