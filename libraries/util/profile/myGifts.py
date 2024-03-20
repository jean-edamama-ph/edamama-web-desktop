import libraries.page.profile.myGifts as pMyGifts
import libraries.page.checkOut as pCheckOut
import libraries.page.common.common as pCommon
import libraries.page.shop as pShop

import libraries.util.common as uCommon
import libraries.util.appCommon.appComm as uAppComm
import libraries.util.shop as uShop
import libraries.data.deploymentChecklist as dDepChklist


class com:
    """COMMON"""
    @uCommon.ufuncLog  
    def clickGiftBox(page, blnFirstGL = False):
        """ 
        Objective: Click Gift Box successfully
        param blnFirstGL: True | False | 'opt'
        returns: None
        Author: ccapistrano_20230515
        updated: jatregenio_20240110
        """
        uCommon.waitAndClickElem(page, pCommon.header.giftBoxIconBtn)
        uCommon.wait(page, 1)
        if blnFirstGL == 'opt':
            blnFirstGL= com.checkIfFirstGL(page)
        
        if blnFirstGL == False:
            uCommon.waitElemToBeVisible(page, pMyGifts.ml.welcomeGiftListLbl)
        elif blnFirstGL == True:
            uCommon.waitElemToBeVisible(page, pMyGifts.ml.howGiftRegistryWorksLbl)
            uCommon.waitAndClickElem(page, pMyGifts.ml.xIconBtn)
        
    @uCommon.ufuncLog  
    def checkAndDelete(page):
        """ 
        Objective: Delete all the existing gift list before executing the next test steps
        param: None
        returns: None
        Author: rmakiling_20231009
        """
        intCount = uCommon.getArrayCount(page, pMyGifts.ml.allMeatBallsIconBtn)
        if intCount > 0:
            for item in range(intCount):
                com.deleteGiftList(page, True)
        uCommon.waitElemToBeVisible(page, pMyGifts.ml.addIconBtn)


    @uCommon.ufuncLog       
    def setOccassion(page, strText):
        """ 
        Objective: Set Gift Note    
        param strText: Text
        param: None
        returns: None
        Author: ccapistrano_20230515
        """
        uCommon.setElem(page, pMyGifts.cr.whatsTheOccasionTxt, strText)
    
    @uCommon.ufuncLog       
    def setWhenIsYourEventHappening(page, intDate = ''):
        """ 
        Objective: Set When Is Your Event Happening
        param intDate: Date
        returns: None
        Author: ccapistrano_20230515
        Updated: rmakiling_20231011
        """
        if uCommon.verifyVisible(page, pMyGifts.cr.addressPlusIconBtn) == True:
            uCommon.waitAndClickElem(page, pMyGifts.cr.calendarIcobnBtn)
            uCommon.wait(page, 1)
            if uCommon.verifyVisible(page, pMyGifts.cr.TwelfthActiveDate) == False:
                    uCommon.waitAndClickElem(page, pMyGifts.cr.nextIconBtn)
            uCommon.waitAndClickElem(page, pMyGifts.cr.TwelfthActiveDate)
            uCommon.waitAndClickElem(page, pMyGifts.cr.confirmBtn)
        else:
            strAddress = uCommon.waitAndGetElemText(page, pMyGifts.cr.addressLbl)
            arrAddress = strAddress.split(", ")
            uCommon.waitAndClickElem(page, pMyGifts.cr.calendarIcobnBtn)
            if arrAddress[4] == 'METRO MANILA':
                if intDate == '':
                    uCommon.wait(page, 1)
                    if uCommon.verifyVisible(page, pMyGifts.cr.seventhActiveDate) == False:
                        uCommon.waitAndClickElem(page, pMyGifts.cr.nextIconBtn)
                    uCommon.waitAndClickElem(page, pMyGifts.cr.seventhActiveDate)
                    uCommon.waitAndClickElem(page, pMyGifts.cr.confirmBtn)
            else:
                if intDate == '':
                    uCommon.wait(page, 1)
                    if uCommon.verifyVisible(page, pMyGifts.cr.TwelfthActiveDate) == False:
                        uCommon.waitAndClickElem(page, pMyGifts.cr.nextIconBtn)
                    uCommon.waitAndClickElem(page, pMyGifts.cr.TwelfthActiveDate)
                    uCommon.waitAndClickElem(page, pMyGifts.cr.confirmBtn)


    @uCommon.ufuncLog       
    def setTellUsMoreAboutYourEvent(page, strText):
        """ 
        Objective: Set Tell Us More About Your Event
        param strText: Text
        param: None
        returns: None
        Author: ccapistrano_20230515
        """
        uCommon.setElem(page, pMyGifts.cr.tellUsMoreAboutYourEventTxt, strText)
        
    @uCommon.ufuncLog  
    def createNewGiftList(page, dictData, intCountGL = 0):
        """ 
        Objective: Create New Gift List successfully
        param dictData: Text
        param intDate: Date | ''
        returns: None
        Author: ccapistrano_20230515
        Update: rmakiling_20231010
        Update: jatregenio_20240109
        """
        if intCountGL > 0:
            uCommon.clickElem(page, pMyGifts.ml.createGiftListBtn)
        else:
            uCommon.wait(page, 3)
            uCommon.clickOptElem(page, pMyGifts.com.emailXIconBtn)
            uCommon.wait(page, .5)
            uCommon.waitAndClickElem(page, pMyGifts.ml.addIconBtn)
            
        if dictData["strOccassion"] == '' or dictData["strAbout"] == '':
            com.clickCreateGLAndVerifyInfoMsg
            uCommon.wait(page, 1)
        else:
            uCommon.waitForLoadState(page, 'networkidle')
            uCommon.wait(page, 2)
            if uCommon.verifyVisible(page, pMyGifts.cr.addressPlusIconBtn) == True:
                com.setEventDetails(page, dictData)
                com.clickCreateGLAndVerifyInfoMsg
                uCommon.wait(page, 1)
            else:
                com.setEventDetails(page, dictData)
                uCommon.hoverAndClickElem(page, pMyGifts.cr.createGiftListBtn)
                uCommon.wait(page, .5)
                if intCountGL == 0:
                    uCommon.waitElemToBeVisible(page, pMyGifts.cr.newGiftListCreatedLbl)
                    uCommon.wait(page, .5)
                    uCommon.waitAndClickElem(page, pMyGifts.ml.xIconBtn)
                    uCommon.wait(page, .5)
        
    @uCommon.ufuncLog  
    def clickGiftList(page, blnFirstAddProduct = True):
        """ 
        Objective: Click Gift List successfully
        param:
        returns: None
        Author: ccapistrano_20230515
        """
        uCommon.wait(page, 1)
        uCommon.waitAndClickElem(page, pMyGifts.com.firstGiftList)
        if blnFirstAddProduct == True:
            uCommon.waitElemToBeVisible(page, pMyGifts.com.addProductIconBtn)
        else:
            uCommon.waitElemToBeVisible(page, pMyGifts.com.registeredGiftsLbl)
        
    @uCommon.ufuncLog
    def clickEditGiftList(page):
        """ 
        Objective: Click Edit Gift List successfully
        param: None
        returns: None
        Author: jatregenio_20231222
        """
        uCommon.hoverAndClickElem(page, pMyGifts.ml.editGiftListBtn)
        uCommon.waitElemToBeVisible(page, pMyGifts.ml.editGiftListLbl)
        
    @uCommon.ufuncLog
    def clickUpdateGiftList(page):
        """ 
        Objective: Click Update Gift List successfully
        param: None
        returns: None
        Author: jatregenio_20231222
        """
        uCommon.waitAndClickElem(page, pMyGifts.ep.updateGiftListBtn)
        uCommon.waitElemToBeVisible(page, pMyGifts.ep.giftListUpdatedLbl)
        uCommon.waitElemNotToBeVisible(page, pMyGifts.ep.giftListUpdatedLbl)
    
    @uCommon.ufuncLog  
    def addNewProductInGiftList(page):
        """ 
        Objective: Add New Product In Gift List successfully
        param: None
        returns strItemName: Item Name
        Author: ccapistrano_20230515
        """ 
        uCommon.waitAndClickElem(page, pMyGifts.com.addProductIconBtn)
        uCommon.wait(page, 5)
        uShop.sp.searchName(page, dDepChklist.strItemName)
        uCommon.waitAndClickElem(page, pShop.sl.itemNameLbl(1))
        uCommon.waitAndClickElem(page, pShop.pf.quantityPlusIconBtn)
        uCommon.wait(page, 1)
        strItemName = uCommon.getElemText(page, pShop.pf.itemNameLbl)
        arrName = strItemName.split('  ')
        strItemName = arrName[0]
        uCommon.waitAndClickElem(page, pShop.pf.giftBtn)
        uCommon.waitAndClickElem(page, pMyGifts.com.addToGLIconBtn)
        uCommon.waitElemToBeVisible(page, pMyGifts.com.productAddedSuccessMsg)
        uCommon.waitElemNotToBeVisible(page, pMyGifts.com.productAddedSuccessMsg)
        uCommon.waitAndClickElem(page, pCommon.header.giftBoxIconBtn)
        uCommon.wait(page, 1)
        return strItemName
    
    @uCommon.ufuncLog  
    def deleteProductFromGiftList(page):
        """ 
        Objective: Delete Product From Gift List successfully
        param: None
        returns: None
        Author: ccapistrano_20230515
        """ 
        uCommon.wait(page, .5)
        uCommon.waitAndClickElem(page, pMyGifts.com.moreIconBtn)
        uCommon.wait(page, .5)
        uCommon.waitAndClickElem(page, pMyGifts.com.removeFromGiftListBtn)
        uCommon.waitElemNotToBeVisible(page, pMyGifts.com.moreIconBtn)
        
    @uCommon.ufuncLog  
    def deleteGiftList(page, blnCleanUp = False):
        """ 
        Objective: Delete Gift List successfully
        param: None
        returns: None
        Author: ccapistrano_20230515
        """ 
        uCommon.wait(page, 1)
        if blnCleanUp == False:
            uCommon.waitAndClickElem(page, pMyGifts.ml.moreIconBtn)
            uCommon.wait(page, .5)
            uCommon.waitAndClickElem(page, pMyGifts.ml.removeGiftListBtn)
            uCommon.waitElemNotToBeVisible(page, pMyGifts.ml.moreIconBtn)
        else:
            if uCommon.verifyVisible(page, pMyGifts.ml.moreIconBtn) == True:
                uCommon.waitAndClickElem(page, pMyGifts.ml.moreIconBtn)
                uCommon.wait(page, .5)
                uCommon.waitAndClickElem(page, pMyGifts.ml.removeGiftListBtn)
                uCommon.waitElemNotToBeVisible(page, pMyGifts.ml.moreIconBtn)
                uCommon.wait(page, .5)
                uCommon.clickOptElem(page, pMyGifts.com.emailXIconBtn)
                
    @uCommon.ufuncLog
    def editEventTitle(page, strEventTitle):
        """ 
        Objective: Edit event title or occassion
        param strEventTitle: Text
        returns: None
        Author: jatregenio_20231222
        """
        uCommon.clickElemAndDeleteText(page, pMyGifts.ep.eventTitleTxt)
        uCommon.waitAndSetElem(page, pMyGifts.ep.eventTitleTxt, strEventTitle)
        
    @uCommon.ufuncLog
    def editEventDescription(page, strDescription):
        """ 
        Objective: Edit event title or occassion
        param strDescription: Text
        returns: None
        Author: jatregenio_20231222
        """
        uCommon.clickElemAndDeleteText(page, pMyGifts.ep.eventDescriptionTxt)
        uCommon.waitAndSetElem(page, pMyGifts.ep.eventDescriptionTxt, strDescription)
    
    @uCommon.ufuncLog
    def updateGLDetails(page, strEvent, strDescription):
        """ 
        Objective: Update details of the existing Gift List
        param strEvent: Text
        param strDescription: Text
        returns: None
        Author: jatregenio_20240110
        """
        uCommon.waitAndClickElem(page, pMyGifts.ep.photoCoverImg2Btn)
        com.editEventTitle(page,strEvent)
        com.setWhenIsYourEventHappening(page)
        com.editEventDescription(page, strDescription)
        

    @uCommon.ufuncLog
    def clickEditUpdateAndVerifyGL(page, strEvent, strDescription):
        """ 
        Objective: Edit Gift List successfully
        param strEvent: Text
        param strDescription: Text
        returns: None
        Author: jatregenio_20231221
        """
        uCommon.waitAndClickElem(page, pMyGifts.ml.moreIconBtn)
        com.clickEditGiftList(page)
        com.updateGLDetails(page, strEvent, strDescription)
        com.clickUpdateGiftList(page)
        com.verifyEventDetails(page, strEvent, strDescription)
        
    @uCommon.ufuncLog  
    def createGLandAddProduct(page, dictData):
        """ 
        Objective: Create Gift List and Add Product
        param strOccassion: Text
        param strAbout: Text
        returns: None
        Author: ccapistrano_20230516
        """ 
        com.createNewGiftList(page, dictData)
        com.clickGiftList(page)
        strItemName = com.addNewProductInGiftList(page)
        com.clickGiftBox(page)
        com.clickGiftList(page, False)
        return strItemName
        
    @uCommon.ufuncLog  
    def sendInvitesViaEmail(page, strEmailAddress):
        """ 
        Objective: Send Invites via Email
        param: None
        returns: None
        Author: ccapistrano_20230516
        """ 
        uCommon.setElem(page, pMyGifts.com.enterEmailAddressTxt, strEmailAddress)
        uCommon.waitAndClickElem(page, pMyGifts.com.emailAddIconBtn)
        uCommon.waitElemToBeVisible(page, pMyGifts.com.emailXIconBtn)
        uCommon.waitAndClickElem(page, pMyGifts.com.sendInvitesBtn)
        uCommon.waitElemToBeVisible(page, pMyGifts.com.giftListSharedSuccessMsg)
        uCommon.waitElemNotToBeVisible(page, pMyGifts.com.giftListSharedSuccessMsg)
        
    @uCommon.ufuncLog
    def verifyEventDetails(page, strEventTitle, strDescription):
        """
        Objective: Verify details of the event
        param: strEventTitle: Text
        param: strDescription: Text
        returns: None
        Author jatregenio_20240110
        """
        uCommon.waitElemToBeVisible(page,pMyGifts.ml.giftListTitlelbl(strEventTitle))
        uCommon.waitElemToBeVisible(page,pMyGifts.ml.giftListDesclbl(strDescription))
        
        
    @uCommon.ufuncLog
    def verifyAndOpenNewlyCreatedGiftList(page, strEventTitle, strDescription):
        """
        Objective: Verifying the newly created gift list
        param: strEventTitle: Text
        param: strDescription: Text
        returns: None
        Author jatregenio_20240110
        """
        com.verifyEventDetails(page, strEventTitle, strDescription)
        com.clickGiftList(page)
        
    @uCommon.ufuncLog
    def verifyGiftListProductCount(page, strExpectedCount):
        """ 
        Objective: Verifying product count in Gift List
        param strExpectedCount: Text
        returns: None
        Author: rmakiling_20231008
        """
        uCommon.validateElemText(page, pMyGifts.com.productCounterLbl, strExpectedCount)
    
    @uCommon.ufuncLog
    def verifyGiftListProducts(page, strItemName):
        """ 
        Objective: Verifying the products inside the Gift list
        param strItemName: Text
        returns: None
        Author: rmakiling_20231008
        Update: jatregenio_20240111
        """
        uCommon.validateElemText(page, pMyGifts.gl.addedProdLbl(strItemName), strItemName)
        
    @uCommon.ufuncLog
    def updateGiftListStatus(page, blnArchived):
        """ 
        Objective: Updating the Gift List status
        param blnArchived: True | False
        returns: None
        Author: rmakiling_20231013
        """
        if blnArchived == True:
            uCommon.waitAndClickElem(page, pMyGifts.ml.moreIconBtn)
            uCommon.wait(page, .5)
            uCommon.waitAndClickElem(page, pMyGifts.ml.archiveGiftListBtn)
        elif blnArchived == False:
            uCommon.wait(page, .5)
            uCommon.waitAndClickElem(page, pMyGifts.ml.moreIconBtn)
            uCommon.wait(page, .5)
            uCommon.waitAndClickElem(page, pMyGifts.ml.unarchiveGiftListBtn)
        else:
            uCommon.log(2, f'Incorrect parameter. Kindly use True or False')
            
    @uCommon.ufuncLog
    def verifyGiftListStatus(page, blnClickable):
        """ 
        Objective: Verifying the Gift List status
        param blnClickable: True | False
        returns: None
        Author: rmakiling_20231013
        """
        uCommon.wait(page, 1)
        if blnClickable == False:
            uCommon.waitElemToBeVisible(page, pMyGifts.ml.archivedLbl)
            uCommon.clickElem(page, pMyGifts.com.firstGiftList)
            uCommon.verifyOptElem(page, pMyGifts.com.addProductIconBtn)
            uCommon.waitElemToBeVisible(page, pMyGifts.ml.archivedLbl)
        elif blnClickable == True:
            uCommon.waitElemNotToBeVisible(page, pMyGifts.ml.archivedLbl)
            uCommon.clickElem(page, pMyGifts.com.firstGiftList)
            uCommon.waitElemToBeVisible(page, pMyGifts.com.addProductIconBtn)
        else:
            uCommon.log(2, f'Incorrect parameter. Kindly use True or False')
            
    @uCommon.ufuncLog
    def getCountOfExistingGL(page):
        """ 
        Objective: Get the number of existing gift list
        param: None
        returns intCountGL: Integer
        Author: jatregenio_20240109
        """
        intCountGL = uCommon.getArrayCount(page, pMyGifts.ml.allMeatBallsIconBtn)
        return intCountGL
    
    @uCommon.ufuncLog
    def getCountAndCreateGL(page, dictData):
        """ 
        Objective: Get the number of existing gift list and create GL
        param dictData: Text
        param intDate: Date of Event
        returns: None
        Author: jatregenio_20230109
        """
        intCountGL = com.getCountOfExistingGL(page)
        com.createNewGiftList(page, dictData, intCountGL)

    @uCommon.ufuncLog
    def checkIfFirstGL(page):
        """ 
        Objective: Check if this will be the first time to create gift list after clicking 'Gift Box' button
        param: None
        returns blnVisible: True | False
        Author: jatregenio_20240110
        """
        blnVisible = False
        uCommon.wait(page, 3)
        blnVisible = uCommon.verifyVisible(page, pMyGifts.ml.howGiftRegistryWorksLbl)
        return blnVisible
    
    @uCommon.ufuncLog
    def verifyIfGLIsRemoved(page, dictData):
        """ 
        Objective: Verify if Gift List was successfully removed
        param dictData: Text
        returns: None
        Author: jatregenio_20240111
        """
        uCommon.waitElemNotToBeVisible(page, pMyGifts.ml.giftListTitlelbl(dictData["strOccassion"]))
        
    @uCommon.ufuncLog
    def setEventDetails(page, dictData):
        """ 
        Objective: Set details of the Event to be created
        param dictData: Text
        returns: None
        Author: jatregenio_20240116
        """
        com.setOccassion(page, dictData["strOccassion"])
        com.setWhenIsYourEventHappening(page)
        com.setTellUsMoreAboutYourEvent(page, dictData["strAbout"])
        uCommon.wait(page, 1)
    
    @uCommon.ufuncLog
    def clickCreateGLAndVerifyInfoMsg(page):
        """ 
        Objective: Click 'Create Gift List' button and verify info message to be displayed: 'Please Complete Form'
        param: None
        returns: None
        Author: jatregenio_20240116
        """
        uCommon.hoverAndClickElem(page, pMyGifts.cr.createGiftListBtn)
        uCommon.waitElemToBeVisible(page, pMyGifts.cr.plsCompleteFormLbl)
        uCommon.waitElemNotToBeVisible(page, pMyGifts.cr.plsCompleteFormLbl)
            
        
        


class ml:
    """MY LIST"""
    @uCommon.ufuncLog       
    def tickBuyGift(page):
        """ 
        Objective: Tick Buy Gift successful
        param: None
        param: None
        returns: None
        Author: ccapistrano_20230515
        """
        uCommon.wait(page, 1)
        uCommon.waitAndClickElem(page, pMyGifts.ml.buyGiftChk)
        uCommon.wait(page, .5)
        uCommon.getAttributeAndCheckIfContainsText(page, f'{pMyGifts.ml.buyGiftChk}/../../..', 'class', 'checked')
        
    @uCommon.ufuncLog       
    def setGiftNote(page, strText):
        """ 
        Objective: Set Gift Note
        param strText: Text
        param: None
        returns: None
        Author: ccapistrano_20230515
        """
        uCommon.setElem(page, pMyGifts.ml.AddNameMessageHereTxt, strText)
            
    @uCommon.ufuncLog       
    def clickBuySelectedGifts(page, blnSignIn = True, blnOwner = False):
        """ 
        Objective: Click Buy Selected Gifts successful
        param blnSignIn: True | False
        param: None
        returns: None
        Author: ccapistrano_20230515
        """
        uCommon.waitAndClickElem(page, pMyGifts.ml.buySelectedGiftsBtn)
        if blnSignIn == True:
            if blnOwner == False:
                uCommon.waitElemToBeVisible(page, pCheckOut.pm.placeOrderBtn)
            else:
                uCommon.wait(page, 3)
                if uCommon.verifyVisible(page, pCheckOut.pm.placeOrderBtn) == True:
                    uCommon.log(2, f'Existing Defect https://edamama.atlassian.net/browse/SNSGR-90"')# NOTE: Add pop-up message for user not allowing to buy on his/her own Gift List - Open defect https://edamama.atlassian.net/browse/SNSGR-90
                    uCommon.expectElemNotToBeVisible(page, pCheckOut.pm.placeOrderBtn)
                
        else:
            uAppComm.ln.validateLoginPage(page)
            
            
            
            
    
class sh:
    """SHARED"""
    @uCommon.ufuncLog       
    def clickSharedWithMe(page):
        """ 
        Objective: Click Shared With Me successfully
        param: None
        param: None
        returns: None
        Author: ccapistrano_20230516
        """
        uCommon.wait(page, 1)
        uCommon.waitAndClickElem(page, pMyGifts.sh.sharedWithMeBtn)
        uCommon.waitElemToBeVisible(page, pMyGifts.sh.shareGiftListLbl)
    