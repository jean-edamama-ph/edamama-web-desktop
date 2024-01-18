import libraries.util.common as uCommon
import libraries.page.profile.mySubscription as pMySubcription
from datetime import datetime, timedelta



class com:
    """COMMON"""
    @uCommon.ufuncLog  
    def validateDetails(page, arrCartDetails):
        """ 
        Objective: Validate correct details
        
        param dictData: Dictionary data
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.validateElemText(page, pMySubcription.at.productnameLbl, arrCartDetails[1])
        uCommon.validateElemText(page, pMySubcription.at.itemDisPriceLbl, arrCartDetails[2])
        uCommon.validateElemText(page, pMySubcription.at.deliversEveryLbl, f'Quantity - {arrCartDetails[3]}', False)
        
        intDays = int(uCommon.getElemText(page, pMySubcription.at.daysLbl).replace(' Days', ''))
        strSubscribeOn = uCommon.getElemText(page, pMySubcription.at.subscribeOnDateLbl)
        strSubscribeOn = datetime.strptime(strSubscribeOn, '%b %d, %Y')
        strExpectedDate = strSubscribeOn + timedelta(days=intDays)
        
        strNextOrder = uCommon.getElemText(page, pMySubcription.at.nextOrderDateLbl)
        strActualDate = datetime.strptime(strNextOrder, '%b %d, %Y')
        assert strExpectedDate == strActualDate, f'Next Order Date should be "{strExpectedDate}" not "{strActualDate}"'   
        
    @uCommon.ufuncLog  
    def clickSkipOrder(page):
        """ 
        Objective: Click Skip Order
        
        param: None
        returns: None
        Author: ccapistrano_20230517
        """
        uCommon.waitAndClickElem(page, pMySubcription.com.skipOrderBtn)
        uCommon.waitElemToBeVisible(page, pMySubcription.com.skipAnOrderLbl)
        
    @uCommon.ufuncLog  
    def clickYesSkipOrder(page):
        """ 
        Objective: Click Yes Skip Order
        
        param: None
        returns strNextOrderDate: Date
        Author: ccapistrano_20230517
        """
        uCommon.waitAndClickElem(page, pMySubcription.com.yesSkipOrderBtn)
        uCommon.waitElemToBeVisible(page, pMySubcription.com.yesSkipOrderBtn)
        uCommon.waitElemToBeVisible(page, pMySubcription.com.yourNextOrderWillBeOnLbl)
        strNextOrderDate = uCommon.getElemText(page, pMySubcription.com.nextOrderDateLbl)
        uCommon.waitAndClickElem(page, pMySubcription.com.gotItBtn)
        return strNextOrderDate.strip()
    
    @uCommon.ufuncLog  
    def clickChangeProduct(page):
        """ 
        Objective: Click Change Product
        
        param: None
        returns: None
        Author: ccapistrano_20230522
        """
        uCommon.waitAndClickElem(page, pMySubcription.com.changeProductBtn)
        uCommon.waitElemToBeVisible(page, pMySubcription.cp.changeProductLbl)  

    @uCommon.ufuncLog  
    def clickCancelSubscription(page):
        """ 
        Objective: Click Cancel Subsciption
        
        param: None
        returns: None
        Author: ccapistrano_20230522
        """
        uCommon.waitAndClickElem(page, pMySubcription.com.cancelSubscriptionBtn)
        uCommon.waitElemToBeVisible(page, pMySubcription.com.cs.askForAssistancecBtn)  
        
    @uCommon.ufuncLog  
    def clickAskForAssisctance(page):
        """ 
        Objective: Click AskForAssistance
        
        param: None
        returns window2: window 2
        Author: ccapistrano_20230522
        """
        uCommon.waitAndClickElem(page, pMySubcription.com.cs.askForAssistancecBtn)
        window2 = uCommon.switchToWindow(page)
        uCommon.waitElemToBeVisible(window2, pMySubcription.st.submitATicketLbl) 
        return window2




class at:
    """ACTIVE TAB"""
    @uCommon.ufuncLog  
    def clickEditSubscription(page):
        """ 
        Objective: Click Edit Subscription
        
        param: None
        returns: None
        Author: ccapistrano_20230517
        """
        uCommon.waitAndClickElem(page, pMySubcription.at.editSubscriptionBtn)
        uCommon.waitElemToBeVisible(page, pMySubcription.com.updateSubscriptionBtn)    
        
    @uCommon.ufuncLog  
    def validateNextOrder(page, strNextOrderDate):
        """ 
        Objective: Validate Next Order date is correct
        
        param strNextOrderDate: Date
        returns: None
        Author: ccapistrano_20230517
        """
        uCommon.waitElemToBeVisible(page, pMySubcription.at.nextOrderDateLbl)  
        uCommon.validateElemText(page, pMySubcription.at.nextOrderDateLbl, strNextOrderDate)
        
    @uCommon.ufuncLog  
    def validateDetails(page, dictDetails):
        """ 
        Objective: validate all necessary details
        
        param dictDetails: Dictionary Details
        returns: None
        Author: ccapistrano_20230522
        """
        uCommon.waitElemToBeVisible(page, pMySubcription.at.productnameLbl)
        uCommon.validateElemText(page, pMySubcription.at.productnameLbl, dictDetails['strNewProductname'])   
        uCommon.validateElemText(page, pMySubcription.at.itemDisPriceLbl, dictDetails['strDiscountedPrice'])
        uCommon.validateElemText(page, pMySubcription.at.deliversEveryLbl, dictDetails['strFrequency'].replace('E', 'e'), False)
        uCommon.validateElemText(page, pMySubcription.at.deliversEveryLbl, dictDetails['strQuantity'], False)
              




class cp:
    """CHANGE PRODUCT"""
    @uCommon.ufuncLog  
    def clickApplyChanges(page):
        """ 
        Objective: Click Apply Changes
        
        param: None
        returns: None
        Author: ccapistrano_20230522
        """
        uCommon.waitAndClickElem(page, pMySubcription.cp.cp.applyChangesBtn)
        uCommon.waitElemToBeVisible(page, pMySubcription.cp.us.applyChangesBtn)
        
    @uCommon.ufuncLog  
    def getDetails(page):
        """ 
        Objective: Get all necessary details
        
        param: None
        returns dictDetails: Dictionary Details
        Author: ccapistrano_20230522
        """
        uCommon.waitElemToBeVisible(page, pMySubcription.cp.cp.oldProductNameLbl)
        strOldProductname = uCommon.getElemText(page, pMySubcription.cp.cp.oldProductNameLbl)
        strNewProductname = uCommon.getElemText(page, pMySubcription.cp.cp.newProductNameLbl)
        strFrequency = uCommon.getElemText(page, pMySubcription.cp.cp.frequencyValueLbl)
        strQuantity = uCommon.getElemText(page, pMySubcription.cp.cp.quantityValueLbl)
        strDiscountedPrice = uCommon.getElemText(page, pMySubcription.cp.cp.discountedPriceLbl)
        strOriginalPrice = uCommon.getElemText(page, pMySubcription.cp.cp.originalPriceLbl)
        dictDetails = {'strOldProductname': strOldProductname, 'strNewProductname': strNewProductname, 'strFrequency': strFrequency,
                       'strQuantity': strQuantity, 'strDiscountedPrice': strDiscountedPrice, 'strOriginalPrice': strOriginalPrice}
        return dictDetails
        




class us:
    """UPDATE SUBSCRIPTION"""
    @uCommon.ufuncLog  
    def clickApplyChanges(page):
        """ 
        Objective: Click Apply Changes
        
        param: None
        returns: None
        Author: ccapistrano_20230522
        """
        uCommon.waitAndClickElem(page, pMySubcription.cp.us.applyChangesBtn)
        uCommon.waitElemToBeVisible(page, pMySubcription.at.nextOrderDateLbl)   
        
    @uCommon.ufuncLog  
    def validateDetails(page, dictDetails):
        """ 
        Objective: validate all necessary details
        
        param dictDetails: Dictionary Details
        returns: None
        Author: ccapistrano_20230522
        """
        uCommon.waitElemToBeVisible(page, pMySubcription.cp.us.updateSubscriptionLbl)
        uCommon.validateElemText(page, pMySubcription.cp.us.oldProductNameLbl, dictDetails['strOldProductname'])
        uCommon.validateElemText(page, pMySubcription.cp.us.newProductNameLbl, dictDetails['strNewProductname'])   
        uCommon.validateElemText(page, pMySubcription.cp.us.newProductPriceLbl, dictDetails['strDiscountedPrice'])