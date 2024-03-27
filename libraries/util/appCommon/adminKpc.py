
import libraries.page.common.adminKpc as pAdmin
import libraries.util.common as uCommon
import libraries.util.appCommon.appComm as uAppComm
import libraries.util.profile.myProfile as uMyProfile

class com:
    """COMMON"""
    @uCommon.ufuncLog 
    def checkProgressBar(page):
        """ 
        Objective: Check progress bar is successfully display the hidden
        
        param: None
        returns: None
        Author: ccapistrano_20230508
        """ 
        uCommon.waitElemNotToBeVisible(page, pAdmin.progressBarElm)





class fs:
    """FLASH SALE"""
    @uCommon.ufuncLog 
    def deleteFlashSale(page, strName):
        """ 
        Objective: Delete flash sale entry
        
        param strName: Flash sale name
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.wait(page, 3)
        if uCommon.verifyVisible(page, pAdmin.fs.deleteIconBtn(strName)) == True:
            uCommon.clickElem(page, pAdmin.fs.deleteIconBtn(strName))
            uCommon.clickElem(page, pAdmin.fs.yesBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.fs.sucCanceledMsg)
            uCommon.waitElemNotToBeVisible(page, pAdmin.fs.sucCanceledMsg)
    
    @uCommon.ufuncLog    
    def createFlashSale(page, strName, strPath):
        """ 
        Objective: Create flash sale entry
        
        param strName: Flash sale name
        param strPath: File Path 
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.log(0, 'Go to admin panel website >> Populate the following'
                   'using an valid ADMIN user credentials >> Click login button')
        uAppComm.ln.loginToAdminKPC(page)
        
        uCommon.log(0, 'Click Flash Sale from the side navigation bar')
        uCommon.waitAndClickElem(page, pAdmin.lp.flashSaleLbl)
        fs.deleteFlashSale(page, strName)
        
        uCommon.log(0, 'Click + Add button')
        uCommon.waitAndClickElem(page, pAdmin.fs.addBtn)
        
        uCommon.log(0, 'Populate Name field with valid values')
        uCommon.waitElemToBeVisible(page, pAdmin.fs.ap.nameTxt)
        uCommon.setElem(page, pAdmin.fs.ap.nameTxt, strName)
        
        uCommon.log(0, 'Click the Calendar icon of the Date field')
        uCommon.waitAndClickElem(page, pAdmin.fs.ap.calendarIconBtn)
        
        uCommon.log(0, 'Select a valid date')
        uCommon.waitAndClickElem(page, pAdmin.fs.ap.dateTodayLbl)
        
        uCommon.log(0, 'Select a time in the Time dropdown field')
        uCommon.waitAndClickElem(page, pAdmin.fs.ap.timeDdb)
        uCommon.waitAndClickElem(page, pAdmin.fs.ap.timeActiveLbl)
        
        uCommon.log(0, 'Click Spot light button')
        uCommon.waitAndClickElem(page, pAdmin.fs.ap.spotLightTgl)
        
        uCommon.log(0, 'Click Upload SKU\'s button >> Select a valid file to upload')
        uCommon.uploadFile(page, pAdmin.fs.ap.uploadSkuBtn, strPath)
        
        uCommon.log(0, 'Select Yes button in Is Featured Column')
        intCnt = uCommon.getArrayCount(page, pAdmin.fs.ap.allIsFeaturedDdb)
        for item in range(intCnt):
            uCommon.waitAndClickElem(page, pAdmin.fs.ap.isFeaturedDdb(item+1))
            uCommon.waitAndClickElem(page, pAdmin.fs.ap.yesBtn)
            uCommon.wait(page, .5)
        
        uCommon.log(0, 'Click Add button')
        uCommon.wait(page, 1)
        uCommon.waitAndClickElem(page, pAdmin.fs.ap.addBtn)
        uCommon.waitElemToBeVisible(page, pAdmin.fs.sucFlashSaleMsg)
        uCommon.waitElemNotToBeVisible(page, pAdmin.fs.sucFlashSaleMsg)
        uCommon.waitElemToBeVisible(page, pAdmin.fs.deleteIconBtn(strName))
        
   
    
    
        
class ds:
    """DISCOUNT SCHEDULER"""
    @uCommon.ufuncLog 
    def deleteDiscountScheduler(page, strName):
        """ 
        Objective: Delete discount scheduler entry
        
        param strName: Discount scheduler name
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.wait(page, 3)
        if uCommon.verifyVisible(page, pAdmin.ds.deleteIconBtn(strName)) == True:
            uCommon.clickElem(page, pAdmin.ds.deleteIconBtn(strName))
            uCommon.clickElem(page, pAdmin.ds.yesBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.ds.sucStatusUpdateMsg)
    
    @uCommon.ufuncLog 
    def createDiscountScheduler(page, strName, strPath, strType):
        """ 
        Objective: Create discount scheduler entry
        
        param strName: Discount scheduler name
        param strPath: File Path 
        param strType: RS | SNS
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.log(0, 'Go to admin panel website >> Populate the following'
                   'using an valid ADMIN user credentials >> Click login button')
        uAppComm.ln.loginToAdminKPC(page)
        
        uCommon.log(0, 'Click Discount Scheduler from the side navigation bar')
        uCommon.waitAndClickElem(page, pAdmin.lp.discountsSchedulerLbl)
        uCommon.wait(page, 5)
        
        if uCommon.verifyVisible(page, pAdmin.ds.deleteIconBtn(strName)) == False:
            uCommon.log(0, 'Click + Add button')
            uCommon.waitAndClickElem(page, pAdmin.ds.addBtn)
            
            uCommon.log(0, 'Populate Scheduler Name with valid values')
            uCommon.setElem(page, pAdmin.ds.ap.schedulerNameTxt, strName)
            
            uCommon.log(0, 'Step 7 - Select RS|SNS in Discount Type Dropdown Field')
            uCommon.waitAndClickElem(page, pAdmin.ds.ap.selectDiscountTypeDdb)
            if strType == 'RS':
                uCommon.waitAndClickElem(page, pAdmin.ds.ap.optionRSLbl)
            elif strType == 'SNS':
                uCommon.waitAndClickElem(page, pAdmin.ds.ap.optionSNSLbl)
            
            uCommon.log(0, 'Click the Calendar icon of the Valid from field >> Select a valid date and valid time')
            uCommon.waitAndClickElem(page, pAdmin.ds.ap.validFromCalIconBtn)
            for item in range(5):
                uCommon.waitAndClickElem(page, pAdmin.ds.ap.addMinutesIconBtn)
            if 'disabled' in uCommon.getElemAttribute(page, pAdmin.ds.ap.checkIconBtn, 'class'):
                uCommon.waitAndClickElem(page, pAdmin.ds.ap.addHoursIconBtn)
                if 'disabled' in uCommon.getElemAttribute(page, pAdmin.ds.ap.checkIconBtn, 'class'):
                    uCommon.waitAndClickElem(page, pAdmin.ds.ap.amPmBtn)
                
            uCommon.log(0, 'Click Check button')
            uCommon.waitAndClickElem(page, pAdmin.ds.ap.checkIconBtn)
            
            uCommon.log(0, 'Click the Calendar icon of the Valid Until field >> Select a valid date and valid time')
            uCommon.waitAndClickElem(page, pAdmin.ds.ap.validUntilCalIconBtn)
            for item in range(30):
                uCommon.waitAndClickElem(page, pAdmin.ds.ap.addMinutesIconBtn)
            if 'disabled' in uCommon.getElemAttribute(page, pAdmin.ds.ap.checkIconBtn, 'class'):
                uCommon.waitAndClickElem(page, pAdmin.ds.ap.addHoursIconBtn)
                if 'disabled' in uCommon.getElemAttribute(page, pAdmin.ds.ap.checkIconBtn, 'class'):
                    uCommon.waitAndClickElem(page, pAdmin.ds.ap.amPmBtn)

            uCommon.log(0, 'Click Check button')
            uCommon.waitAndClickElem(page, pAdmin.ds.ap.checkIconBtn)
            
            uCommon.log(0, 'Click Spot light toggle button')
            uCommon.clickOptElem(page, pAdmin.fs.ap.spotLightTgl)
            
            uCommon.log(0, 'Click Upload button >> Select a valid file to upload')
            uCommon.uploadFile(page, pAdmin.ds.ap.uploadBtn, strPath)
        
            uCommon.log(0, 'Select Yes button in Is Featured Column')
            for item in range(1):
                uCommon.clickElem(page, pAdmin.ds.ap.isFeaturedDdb(item+1))
                uCommon.waitAndClickElem(page, pAdmin.ds.ap.yesBtn)
            strProductName = uCommon.getElemText(page, pAdmin.ds.ap.firstProductNameYesLbl)
            strTotalDiscount = uCommon.getElemText(page, pAdmin.ds.ap.firstTotalDcPerLbl)
            strPriceOriginal = uCommon.getElemText(page, pAdmin.ds.ap.firstPriceOrigLbl)
            strPriceDiscounted = uCommon.getElemText(page, pAdmin.ds.ap.firstPriceDiscountedLbl)
            
            uCommon.log(0, 'Click Add button')
            uCommon.waitAndClickElem(page, pAdmin.ds.ap.addBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.ds.sucSchedulerMsg)
            uCommon.waitElemToBeVisible(page, pAdmin.ds.deleteIconBtn(strName))
        else:
            uCommon.waitAndClickElem(page, pAdmin.ds.editIconBtn(strName))
            uCommon.waitElemToBeVisible(page, pAdmin.ds.ap.firstProductNameYesLbl)
            strProductName = uCommon.getElemText(page, pAdmin.ds.ap.firstProductNameYesLbl)
            strTotalDiscount = uCommon.getElemText(page, pAdmin.ds.ap.firstTotalDcPerLbl)
            strPriceOriginal = uCommon.getElemText(page, pAdmin.ds.ap.firstPriceOrigLbl)
            strPriceDiscounted = uCommon.getElemText(page, pAdmin.ds.ap.firstPriceDiscountedLbl)
        uCommon.log(0, {'strName': strName, 'strProductName': strProductName, 'strTotalDiscount': strTotalDiscount, 'strPriceOriginal': strPriceOriginal, 'strPriceDiscounted': strPriceDiscounted})
        return {'strName': strName, 'strProductName': strProductName, 'strTotalDiscount': strTotalDiscount, 'strPriceOriginal': strPriceOriginal, 'strPriceDiscounted': strPriceDiscounted}





class sc:
    """SUBSCRIPTION"""
    def cancelAllOrders(page, strname):
        """ 
        Objective: Cancel All orders
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.waitAndClickElem(page, pAdmin.lp.subscriptionLbl)  
        uCommon.wait(page, 1)
        uCommon.waitElemToBeVisible(page, pAdmin.sc.searchTxt)
        uCommon.setElem(page, pAdmin.sc.searchTxt, strname)
        uCommon.waitAndClickElem(page, pAdmin.sc.searchIconBtn)
        uCommon.wait(page, 5)
        if uCommon.verifyVisible(page, pAdmin.sc.firstEditIconBtn) == True:
            intCnt = uCommon.getArrayCount(page, pAdmin.sc.editIconBtn)
            for item in range(intCnt):
                uCommon.waitAndClickElem(page, pAdmin.sc.firstEditIconBtn) 
                window = uCommon.switchToWindow(page)
                uCommon.wait(page, 2)
                uCommon.waitAndClickElem(window, pAdmin.sc.cancelBtn) 
                uCommon.wait(page, 4)
                uCommon.closeWindow(window)
                uCommon.reloadPage(page)
                uCommon.waitElemToBeVisible(page, pAdmin.sc.searchTxt)
                uCommon.setElem(page, pAdmin.sc.searchTxt, strname)
                uCommon.waitAndClickElem(page, pAdmin.sc.searchIconBtn)
                uCommon.wait(page, 5)
    
    def cancelOrdersByUserName(page):
        """ 
        Objective: Cancel All orders by username
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uAppComm.com.navigateToProfileMenu(page, 'my profile')
        dictData = uMyProfile.com.getMyProfileDetails(page)
        # strName = dictData['strName'] # NOTE: search via Customer Name in AP not working -enable this once fix
        strName = dictData['strName']
        uAppComm.ln.loginToAdminKPC(page)
        uCommon.wait(page, 2)
        sc.cancelAllOrders(page, strName)





class od:
    """ORDERS"""
    @uCommon.ufuncLog  
    def clickOrders(page):
        """ 
        Objective: Click orders
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.waitAndClickElem(page, pAdmin.lp.ordersLbl)
        com.checkProgressBar(page)

    @uCommon.ufuncLog  
    def validateCustomerName(page, strOrderID, strName):
        """ 
        Objective: Validate customer name
        
        param strOrderID: Order ID
        param strName: name
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.validateElemText(page, pAdmin.ol.customerNameValue(strOrderID), strName)
        
    @uCommon.ufuncLog  
    def validateDetails(page, strOrderID, dicDetails, blnCancel = False):
        """ 
        Objective: validate details
        
        param strOrderID: Order ID
        param dicDetails: Dictionary details
        param blnCancel: True | False
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.validateElemText(page, pAdmin.ol.orderIDValue(strOrderID), strOrderID)
        uCommon.validateElemText(page, pAdmin.ol.quantityValue(strOrderID), dicDetails['strQuantity'], False)
        uCommon.validateElemText(page, pAdmin.ol.paymentMethodValue(strOrderID), dicDetails['strModeOfPayment'])
        if blnCancel == True:
            uCommon.validateElemText(page, pAdmin.ol.shipPriceValue(strOrderID), '0')
            uCommon.validateElemText(page, pAdmin.ol.totalPriceValue(strOrderID), '0')
            uCommon.validateElemText(page, pAdmin.ol.returnCancelValue(strOrderID.replace('#', '')), 'Canceled By User')
        else:
            arrShipPrice = dicDetails['strShipPrice'].split('.')
            strShipPrice = arrShipPrice[0].replace('₱', '')
            uCommon.validateElemText(page, pAdmin.ol.shipPriceValue(strOrderID), strShipPrice)
            # strTotalPrice = ((dicDetails['strTotalPrice'].replace('₱', '')).replace(',', ''))[:-1]
            # uCommon.validateElemText(page, pAdmin.ol.totalPriceValue(strOrderID), strTotalPrice, False)
            strTotalPrice = ((dicDetails['strTotalPrice'].replace('₱', '')).replace(',', ''))[:-3]
            uCommon.validateElemText(page, pAdmin.ol.totalPriceValue(strOrderID), strTotalPrice, True)
            uCommon.validateElemText(page, pAdmin.ol.returnCancelValue(strOrderID.replace('#', '')), '-')
        return strOrderID

    @uCommon.ufuncLog  
    def validateRetunCancel(page, strOrderID, strValue):
        """ 
        Objective: Validate Return Cancel
        
        param strOrderID: Order ID
        param dicDetails: Dictionary details
        param blnCancel: True | False
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.waitElemToBeVisible(page, pAdmin.ol.returnCancelValue(strOrderID))
        if '#' in strOrderID:
            strOrderID = strOrderID.replace('#', '')
        uCommon.validateElemText(page, pAdmin.ol.returnCancelValue(strOrderID), strValue)

    @uCommon.ufuncLog  
    def clickMassUploadAndSelect(page, strMassUploadOption):
        """ 
        Objective: Click Mass Upload and select if Order Cancellation, Order Item Cancellation or Tracking Number
        
        param strMassUploadOption: Cancellation |Order Item Cancellation | Tracking Number
        returns: None
        Author: ccapistrano_20230510
        """
        uCommon.waitAndClickElem(page, pAdmin.ol.massUploadBtn)
        uCommon.waitAndClickElemText(page, strMassUploadOption)
    
    @uCommon.ufuncLog  
    def uploadMassCancellationFile(page, strPath):
        """ 
        Objective: Upload csv file to be cancel
        
        param strPath: Path directory
        returns: None
        Author: ccapistrano_20230510
        """
        uCommon.uploadFile(page, pAdmin.ol.selectFileBtn, strPath)

    @uCommon.ufuncLog 
    def clickUploadOrderCancellation(page):
        """ 
        Objective: Click Upload Order Cancellation successfully
        
        param: None
        returns: None
        Author: ccapistrano_20230510
        """    
        uCommon.hoverAndClickElem(page, pAdmin.ol.uploadOrderCancellationBtn)
        uCommon.waitElemToBeVisible(page, pAdmin.ol.massCancellationSuccessMsg)
        uCommon.waitElemNotToBeVisible(page, pAdmin.ol.massCancellationSuccessMsg)


    class od:
        """ORDER"""
        @uCommon.ufuncLog 
        def validateDeliveryDetails(page, dictData):
            """ 
            Objective: Validate deliver details are all correct
            
            param dictData: Dictionary Data
            returns: None
            Author: ccapistrano_20230512
            """    
            uCommon.waitElemToBeVisible(page, pAdmin.ol.od.receiverValueLbl)
            uCommon.validateElemText(page, pAdmin.ol.od.receiverValueLbl, f'{dictData["strFName"]} {dictData["strLName"]}')
            uCommon.validateElemText(page, pAdmin.ol.od.regionValueLbl, dictData["strProvince"])
            uCommon.validateElemText(page, pAdmin.ol.od.cityValueLbl, dictData["strCity"])
            uCommon.validateElemText(page, pAdmin.ol.od.barangayValueLbl, dictData["selectBarangay"])
            uCommon.validateElemText(page, pAdmin.ol.od.streetValueLbl, dictData["strLotStreet"])
            uCommon.validateElemText(page, pAdmin.ol.od.deliveryNotesValueLbl, dictData["strLandmark"])
            uCommon.validateElemText(page, pAdmin.ol.od.zipCodeValueLbl, dictData["strZipCode"])
            
            
        class pt:
            @uCommon.ufuncLog 
            def clickEdit(page):
                """ 
                Objective: Click Edit successfully
                
                param: None
                returns: None
                Author: ccapistrano_20230510
                """    
                uCommon.waitElemToBeVisible(page, pAdmin.ol.od.pt.editIconBtn)
                uCommon.hoverAndClickElem(page, pAdmin.ol.od.pt.editIconBtn)
                uCommon.waitElemToBeVisible(page, pAdmin.ol.od.pt.selectStatusLbl)
                 
            """PRODUCT TABLE"""
            @uCommon.ufuncLog 
            def clickAndSelectOrderStatus(page, strOrderStatus):
                """ 
                Objective: Select Order status( Accepted, Rejected, Refused To Accept, Canceled By Admin, Shipped)
                
                param strOrderStatus : Accepted | Rejected | Refused To Accept | Canceled By Admin | Shipped
                returns: None
                Author: ccapistrano_20230510
                """
                uCommon.waitAndClickElem(page, pAdmin.ol.od.pt.selectStatusLbl)
                uCommon.waitAndClickElemText(page, strOrderStatus)
            
            @uCommon.ufuncLog 
            def setTrackingAndCourier(page, strUrl, strNumber, strCourier):
                """ 
                Objective: Set Tracking Url, Numnber and Courier
                
                param strUrl : Tacking URL
                param strNumber : Tacking Number
                param strCourier : Courier
                returns: None
                Author: ccapistrano_20230510
                """
                uCommon.waitElemToBeVisible(page, pAdmin.ol.od.pt.trackingUrlLbl)
                uCommon.setElem(page, pAdmin.ol.od.pt.trackingUrlLbl, strUrl)
                uCommon.setElem(page, pAdmin.ol.od.pt.trackingNumberLbl, strNumber)
                uCommon.setElem(page, pAdmin.ol.od.pt.courierLbl, strCourier)
            
            @uCommon.ufuncLog 
            def clickUpdate(page):
                """ 
                Objective: Click Update successfully
                
                param: None
                returns: None
                Author: ccapistrano_20230510
                """    
                uCommon.hoverAndClickElem(page, pAdmin.ol.od.pt.updateBtn)
                com.checkProgressBar(page)
                uCommon.waitElemToBeVisible(page, pAdmin.ol.od.pt.statusUpdatedSuccessMsg)
                uCommon.waitElemNotToBeVisible(page, pAdmin.ol.od.pt.statusUpdatedSuccessMsg)  
           
           
           
           
                

class cp:
    """CURATED PRODUCTS"""     
    @uCommon.ufuncLog  
    def clickCuratedProducts(page):
        """ 
        Objective: Click Curated Products
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.wait(page, 1)
        uCommon.waitAndClickElem(page, pAdmin.lp.curatedProductsLbl)
        com.checkProgressBar(page)
        uCommon.waitElemToBeVisible(page, pAdmin.cp.rankBtn)

    @uCommon.ufuncLog  
    def clickRank(page):
        """ 
        Objective: Click Rank
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.waitAndClickElem(page, pAdmin.cp.rankBtn)
        uCommon.waitElemToBeVisible(page, pAdmin.cp.rankingNameIndex1Lbl)

    @uCommon.ufuncLog  
    def setRanking(page, blnReverse = False):
        """ 
        Objective: Click Rank
        
        param: None
        returns return: Dictionary Title
        Author: ccapistrano_20230327
        """
        intCnt = uCommon.getArrayCount(page, pAdmin.cp.allRankingTxt)
        for item in range(intCnt):
            if blnReverse == False:
                intCount = item + 1
                uCommon.setElem(page, pAdmin.cp.rankingIndexTxt(intCount), str(intCount))
            else:
                revCnt = intCnt - item
                intCount = item + 1
                uCommon.setElem(page, pAdmin.cp.rankingIndexTxt(intCount), str(revCnt))
        strTitle1 = uCommon.getElemText(page, pAdmin.cp.rankingNameIndex1Lbl)
        strTitle2 = uCommon.getElemText(page, pAdmin.cp.rankingNameIndex3Lbl)
        strTitle3 = uCommon.getElemText(page, pAdmin.cp.rankingNameIndex5Lbl)
        strTitle4 = uCommon.getElemText(page, pAdmin.cp.rankingNameIndex7Lbl)
        uCommon.log(0, {'strTitle1': strTitle1, 'strTitle2': strTitle2, 'strTitle3': strTitle3, 'strTitle4': strTitle4})
        return {'strTitle1': strTitle1, 'strTitle2': strTitle2, 'strTitle3': strTitle3, 'strTitle4': strTitle4}

    @uCommon.ufuncLog  
    def clickUpdate(page):
        """ 
        Objective: Click Update
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.waitAndClickElem(page, pAdmin.cp.updateBtn)
        uCommon.waitElemToBeVisible(page, pAdmin.cp.sucRankUpdatedMsg)
        uCommon.waitElemNotToBeVisible(page, pAdmin.cp.sucRankUpdatedMsg)
        
    @uCommon.ufuncLog 
    def searchTitle(page, strTitle):
        """ 
        Objective: Search Title is visible
        
        param strTitle: Title Name
        returns: None
        Author: ccapistrano_20230516
        """
        uCommon.waitElemToBeVisible(page, pAdmin.cp.searchTitleTxt)
        uCommon.setElem(page, pAdmin.cp.searchTitleTxt, strTitle)
        uCommon.wait(page, .5)
        pl.clickSearchIcon(page)
        com.checkProgressBar(page)
        uCommon.wait(page, .5)
        
    
    
    
    class pr:
        """PRODUCTS PAGE"""
        @uCommon.ufuncLog 
        def searchProduct(page, strItemName, blnSearch = True):
            """ 
            Objective: Search Item is visible
            
            param strItemName: Item Name
            returns: None
            Author: ccapistrano_20230516
            """
            uCommon.waitElemToBeVisible(page, pAdmin.cp.searchItemTxt)
            uCommon.setElem(page, pAdmin.cp.searchItemTxt, strItemName)
            uCommon.wait(page, .5)
            
            if uCommon.verifyVisible(page, pAdmin.cp.noRecordFoundLbl) == True:
              blnVisible = False
            else:
              blnVisible = True
            return blnVisible
        
        @uCommon.ufuncLog 
        def searchAndClickProduct(page, strItemName, blnSearch = True):
            """ 
            Objective: Search Item is visible
            
            param strItemName: Item Name
            returns: None
            Author: ccapistrano_20230516
            """
            cp.pr.searchProduct(page, strItemName, blnSearch = True)
            pl.clickSearchIcon(page, blnSearch)
            com.checkProgressBar(page)
            uCommon.wait(page, .5)
            
        @uCommon.ufuncLog  
        def clickProduct(page):
            """ 
            Objective: Click Product successfully
            
            param: None
            returns: None
            Author: ccapistrano_20230516
            """
            uCommon.waitAndClickElem(page, pAdmin.cp.productBtn)
            window2 = uCommon.switchToWindow(page)
            uCommon.wait(page, 1)
            uCommon.waitElemToBeVisible(window2, pAdmin.cp.pr.productsLbl)
            return window2
            
        @uCommon.ufuncLog  
        def clickCheckBox(page):
            """ 
            Objective: Click CheckBox successfully
            
            param: None
            returns: None
            Author: ccapistrano_20230516
            """
            uCommon.waitAndClickElem(page, pAdmin.cp.pr.firstChk)
            uCommon.wait(page, .5)
            uCommon.getAttributeAndCheckIfContainsText(page, f'{pAdmin.cp.pr.firstChk}/../..', 'class', 'checked')
            
        @uCommon.ufuncLog  
        def clickAdd(page):
            """ 
            Objective: Click Add successfully
            
            param: None
            returns: None
            Author: ccapistrano_20230516
            """
            uCommon.waitAndClickElem(page, pAdmin.cp.pr.addBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.cp.pr.confirmationLbl)
            

        @uCommon.ufuncLog  
        def clickYes(page, BlnAdd = True):
            """ 
            Objective: Click Yes successfully
            
            param: None
            returns: None
            Author: ccapistrano_20230516
            """
            uCommon.waitAndClickElem(page, pAdmin.cp.pr.yesBtn)
            if BlnAdd == True:
                uCommon.waitElemToBeVisible(page, pAdmin.cp.pr.productAddedSuccessMsg)
                uCommon.waitElemNotToBeVisible(page, pAdmin.cp.pr.productAddedSuccessMsg)
            else:
                uCommon.waitElemToBeVisible(page, pAdmin.cp.pr.productRemovedSuccessMsg)
                uCommon.waitElemNotToBeVisible(page, pAdmin.cp.pr.productRemovedSuccessMsg)
        
        @uCommon.ufuncLog  
        def clickAssociatedTab(page):
            """ 
            Objective: Click Associated Tab successfully
            
            param: None
            returns: None
            Author: ccapistrano_20230516
            """
            uCommon.waitAndClickElem(page, pAdmin.cp.pr.associatedTabLbl)
            uCommon.waitElemToBeVisible(page, pAdmin.cp.pr.removeBtn)
            
        @uCommon.ufuncLog  
        def clickRemove(page):
            """ 
            Objective: Click Remove successfully
            
            param: None
            returns: None
            Author: ccapistrano_20230516
            """
            uCommon.waitAndClickElem(page, pAdmin.cp.pr.removeBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.cp.pr.confirmationLbl)
            






class pl:
    """PRODUCTS"""
    @uCommon.ufuncLog 
    def clickProductsThenSubMenu(page, strSubMenu = ''):
        """ 
        Objective: Click Products then Listing
        
        param strSubMenu: Sub Menu
        returns: None
        Author: ccapistrano_20230508
        """
        uCommon.waitAndClickElem(page, pAdmin.lp.productsLbl)
        if strSubMenu == '':
            uCommon.wait(page, 2)
            uCommon.waitAndClickElem(page, pAdmin.pl.listingIconBtn)
            com.checkProgressBar(page)
            uCommon.waitElemToBeVisible(page, pAdmin.pl.searchTxt)
        else:
            uCommon.log(2, f'Incorrect input of SubMenu. Kindly use any of the ff: "''" for Listing')
    
    @uCommon.ufuncLog 
    def clickSearchIcon(page, blnSearch = True):
        """ 
        Objective: Click Search icon successfully
        
        param: None
        returns: None
        Author: ccapistrano_20230508
        """  
        uCommon.waitAndClickElem(page, pAdmin.pl.searchIconBtn)
        com.checkProgressBar(page)
        if blnSearch == True:
            uCommon.waitElemToBeVisible(page, pAdmin.pl.tableRowElm)
            uCommon.expectElemNotToBeVisible(page, pAdmin.pl.noRecordFoundLbl)
        else:
            uCommon.waitElemToBeVisible(page, pAdmin.pl.noRecordFoundLbl)
            uCommon.expectElemNotToBeVisible(page, pAdmin.pl.tableRowElm)
    
    @uCommon.ufuncLog 
    def searchProduct(page, strItemName):
        """ 
        Objective: Search product is visible
        
        param strItemName: Item Name
        returns: None
        Author: ccapistrano_20230508
        """
        uCommon.waitElemToBeVisible(page, pAdmin.pl.searchTxt)
        uCommon.setElem(page, pAdmin.pl.searchTxt, strItemName)
        uCommon.wait(page, .5)
        pl.clickSearchIcon(page)
        com.checkProgressBar(page)
        uCommon.wait(page, 1)
    
    @uCommon.ufuncLog 
    def clickEditIcon(page):
        """ 
        Objective: Click Search icon successfully
        
        param: None
        returns: None
        Author: ccapistrano_20230508
        """  
        uCommon.waitAndClickElem(page, pAdmin.pl.editIconBtn)
        com.checkProgressBar(page)
    
    @uCommon.ufuncLog 
    def validatepublished(page, blnVisible = True):
        """ 
        Objective: validate published if visible or not vsible
        
        param: None
        returns: None
        Author: ccapistrano_20230508
        """  
        if blnVisible == True:
            uCommon.waitElemToBeVisible(page, pAdmin.pl.publishedIcon)
            uCommon.expectElemNotToBeVisible(page, pAdmin.pl.unpublishedIcon)
        else:
            uCommon.waitElemToBeVisible(page, pAdmin.pl.unpublishedIcon)
            uCommon.expectElemNotToBeVisible(page, pAdmin.pl.publishedIcon)
    
    @uCommon.ufuncLog 
    def clickDeleteIcon(page):
        """ 
        Objective: Click Delete icon successfully
        
        param: None
        returns: None
        Author: ccapistrano_20230508
        """  
        uCommon.waitAndClickElem(page, pAdmin.pl.deleteIconBtn)
        uCommon.waitElemToBeVisible(page, pAdmin.pl.confirmationlbl)
        uCommon.expectElemToBeVisible(page, pAdmin.pl.deleteMsg)
        uCommon.expectElemToBeVisible(page, pAdmin.pl.noBtn)
        uCommon.expectElemToBeVisible(page, pAdmin.pl.yesBtn)
        
    @uCommon.ufuncLog 
    def deleteProduct(page, BlnDelete = True):
        """ 
        Objective: Delete product successfully
        
        param: None
        returns: None
        Author: ccapistrano_20230508
        """  
        pl.clickDeleteIcon(page)
        if BlnDelete == True:
            uCommon.waitAndClickElem(page, pAdmin.pl.yesBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.pl.deleteSuccessMsg)
            uCommon.waitElemNotToBeVisible(page, pAdmin.pl.deleteSuccessMsg)
            uCommon.waitElemNotToBeVisible(page, pAdmin.pl.deleteIconBtn)
        else:
            uCommon.waitAndClickElem(page, pAdmin.pl.noBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.pl.deleteIconBtn)
        
    @uCommon.ufuncLog 
    def clickBlockOrUnblockIcon(page, blnWillBlock = True):
        """ 
        Objective: Click Block or Unblock icon 
        
        param blnWillBlock: True | False
        returns: None
        Author: ccapistrano_20230508
        """  
        uCommon.waitAndClickElem(page, pAdmin.pl.blockUnblockIconBtn)
        objTemp = pAdmin.pl.blockMsg if blnWillBlock else pAdmin.pl.unblockMsg
        uCommon.waitElemToBeVisible(page, objTemp)         
        uCommon.waitElemToBeVisible(page, pAdmin.pl.confirmationlbl)
        uCommon.waitElemToBeVisible(page, pAdmin.pl.noBtn)
        uCommon.waitElemToBeVisible(page, pAdmin.pl.yesBtn)
    
    @uCommon.ufuncLog 
    def blockOrUnblockProduct(page, blnWillBlock = True, blnOption = True):
        """ 
        Objective: Block or Unblock product
        
        param blnWillBlock: True | False
        param blnOption: True | False
        returns: None
        Author: ccapistrano_20230508
        """  
        pl.clickBlockOrUnblockIcon(page, blnWillBlock)
        objTemp = pAdmin.pl.blockSuccessMsg if blnWillBlock else pAdmin.pl.unblockSuccessMsg
        if blnOption:
                uCommon.waitAndClickElem(page, pAdmin.pl.yesBtn)
                uCommon.waitElemToBeVisible(page, objTemp)
                uCommon.waitElemNotToBeVisible(page, objTemp)
        else:
            uCommon.waitAndClickElem(page, pAdmin.pl.noBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.pl.blockUnblockIconBtn)
    
    @uCommon.ufuncLog 
    def isProductBlockOrUnBlock(page):
        """ 
        Objective: Get text if Block or Unblock 
        
        param: None
        returns: None
        Author: ccapistrano_20230508
        """  
        strText = uCommon.getElemText(page, pAdmin.pl.blockUnblockIconBtn)
        return strText.strip()
    
    @uCommon.ufuncLog 
    def clickAdd(page):
        """ 
        Objective: Click Add successfully
        
        param: None
        returns: None
        Author: ccapistrano_20230508
        """  
        uCommon.wait(page, .5)
        uCommon.waitAndClickElem(page, pAdmin.pl.addBtn)
        uCommon.waitElemToBeVisible(page, pAdmin.pl.bi.productbasicInfoLbl)
    
    class bi:
        """BASIC INFORMATION"""
        @uCommon.ufuncLog 
        def setProductName(page, strProductName):
            """ 
            Objective: Set Product Name
            
            param strProductName: Product Name
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.clickElemAndDeleteText(page, pAdmin.pl.bi.productNameTxt)
            uCommon.waitAndSetElem(page, pAdmin.pl.bi.productNameTxt, strProductName)
            
        @uCommon.ufuncLog 
        def clickUpdateAndContinue(page):
            """ 
            Objective: Click Update & Continue successfully
            
            param: None
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.hoverAndClickElem(page, pAdmin.pl.bi.updateAndContinueBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.pl.bi.productSuccessMsg)
            uCommon.waitElemNotToBeVisible(page, pAdmin.pl.bi.productSuccessMsg)
            
        @uCommon.ufuncLog 
        def clickNext(page):
            """ 
            Objective: Click Next successfully
            
            param: None
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.hoverAndClickElem(page, pAdmin.pl.bi.nextBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.pl.cv.colorSelectionLbl)
            
        
        @uCommon.ufuncLog 
        def selectCategory(page, strCategory):
            """ 
            Objective: Click, set and select Category
            
            param strCategory: Category
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.waitAndClickElem(page, pAdmin.pl.bi.selectCategoryLbl)
            uCommon.setAndSelectFromSmartDropDown(page, pAdmin.pl.bi.searchCategoryTxt, strCategory)
            uCommon.waitAndClickElem(page, pAdmin.pl.bi.productbasicInfoLbl)
            com.checkProgressBar(page)
            uCommon.wait(page, 1)
            
        @uCommon.ufuncLog 
        def selectBrand(page, strBrand):
            """ 
            Objective: Click, set and select Brand
            
            param strBrand: Brand
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.waitAndClickElem(page, pAdmin.pl.bi.selectBrandLbl)
            uCommon.setAndSelectFromSmartDropDown(page, pAdmin.pl.bi.searchTxt, strBrand)
            com.checkProgressBar(page)
            uCommon.waitAndClickElem(page, pAdmin.pl.bi.productbasicInfoLbl)
            uCommon.wait(page, 1)
            
        @uCommon.ufuncLog 
        def selectVendor(page, strVendor):
            """ 
            Objective: Click, set and select Vendor
            
            param strVendor: Vendor
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.waitAndClickElem(page, pAdmin.pl.bi.selectVendorLbl)
            uCommon.setAndSelectFromSmartDropDown(page, pAdmin.pl.bi.searchTxt, strVendor)
            com.checkProgressBar(page)
            uCommon.wait(page, 2)
            uCommon.waitAndClickElem(page, pAdmin.pl.bi.productbasicInfoLbl)
            uCommon.wait(page, 1)

        @uCommon.ufuncLog 
        def selectBundleBuy(page, strBundleBuy):
            """ 
            Objective: Click and select Bundle Buy
            
            param strBundleBuy: BundleBuy
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.waitAndClickElem(page, pAdmin.pl.bi.bundleByLbl)
            uCommon.waitAndClickElemText(page, strBundleBuy)
            uCommon.waitAndClickElem(page, pAdmin.pl.bi.productbasicInfoLbl)
            com.checkProgressBar(page)
            uCommon.waitAndClickElem(page, pAdmin.pl.bi.productbasicInfoLbl)
            uCommon.wait(page, 1)
        
        @uCommon.ufuncLog 
        def selectAttributes(page, strAttributes):
            """ 
            Objective: Click, set and select Attributes
            
            param strAttributes: Attributes
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.waitAndClickElem(page, pAdmin.pl.bi.attributesLbl)
            uCommon.setAndSelectFromSmartDropDown(page, pAdmin.pl.bi.searchTxt, strAttributes)
            com.checkProgressBar(page)
            uCommon.waitAndClickElem(page, pAdmin.pl.bi.productbasicInfoLbl)
            uCommon.wait(page, 1)
            
        @uCommon.ufuncLog 
        def setDescriptionAndSpecification(page, strDesc, strSpec):
            """ 
            Objective: Click, set and select Attributes
            
            param strAttributes: Attributes
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.setElem(page, pAdmin.pl.bi.descriptionTxt, strDesc)
            uCommon.setElem(page, pAdmin.pl.bi.specificationTxt, strSpec)
        
        @uCommon.ufuncLog 
        def clickSaveAndContinue(page):
            """ 
            Objective: Click Save & Continue successfully
            
            param: None
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.hoverAndClickElem(page, pAdmin.pl.bi.saveAndContinueBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.pl.bi.addedSuccessMsg)
            uCommon.waitElemNotToBeVisible(page, pAdmin.pl.bi.addedSuccessMsg)
            
            
    class cv:
        """COLOR & VARIANTS"""
        @uCommon.ufuncLog 
        def addColor(page, strColor, strImagePath):
            """ 
            Objective: Add Color in Color Selection
            
            param: None
            returns: None
            Author: ccapistrano_20230508
            """    
            uCommon.waitAndClickElem(page, pAdmin.pl.cv.selectColorlbl)
            uCommon.setAndSelectFromSmartDropDown(page, pAdmin.pl.cv.searchTxt, strColor)
            uCommon.uploadFile(page, pAdmin.pl.cv.colorAddIconBtn, strImagePath)
            uCommon.wait(page, 3)
            uCommon.waitAndClickElem(page, pAdmin.pl.cv.selectBtn)
            uCommon.wait(page, .5)
            uCommon.waitAndClickElem(page, pAdmin.pl.cv.addColorBtn)
            uCommon.wait(page, .5)
            com.checkProgressBar(page)
            uCommon.wait(page, 1)
            
        @uCommon.ufuncLog 
        def clickUpdateAndContinue(page):
            """ 
            Objective: Click Update & Continue successfully
            
            param: None
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.hoverAndClickElem(page, pAdmin.pl.cv.updateAndContinueBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.pl.cv.productSuccessMsg)
            uCommon.waitElemNotToBeVisible(page, pAdmin.pl.cv.productSuccessMsg)
            
        @uCommon.ufuncLog 
        def deleteColor(page, strColor):
            """ 
            Objective: delete color via specified text color
            
            param: None
            returns: None
            Author: ccapistrano_20230508
            """    
            if ' ' in strColor:
                strColor = strColor.replace(' ', '%20')
            uCommon.waitAndClickElem(page, pAdmin.pl.cv.deleteIconBtn(strColor))
            uCommon.waitAndClickElem(page, pAdmin.pl.cv.yesBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.pl.cv.colorOptRemoveMsg)
            uCommon.waitElemNotToBeVisible(page, pAdmin.pl.cv.colorOptRemoveMsg)
        
        @uCommon.ufuncLog 
        def checkAndDeleteColor(page, strColor):
            """ 
            Objective: Check color if exist then delete color via specified text color
            
            param: None
            returns: None
            Author: ccapistrano_20230508
            """
            if ' ' in strColor:
                strColor = strColor.replace(' ', '%20')
            if uCommon.verifyVisible(page, pAdmin.pl.cv.deleteIconBtn(strColor)) == True:
                uCommon.waitAndClickElem(page, pAdmin.pl.cv.deleteIconBtn(strColor))
                uCommon.waitAndClickElem(page, pAdmin.pl.cv.yesBtn)
                uCommon.waitElemToBeVisible(page, pAdmin.pl.cv.colorOptRemoveMsg)
                uCommon.waitElemNotToBeVisible(page, pAdmin.pl.cv.colorOptRemoveMsg)
                
        @uCommon.ufuncLog 
        def clickNext(page):
            """ 
            Objective: Click Next successfully
            
            param: None
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.hoverAndClickElem(page, pAdmin.pl.cv.nextBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.pl.sp.publishedLbl)
         
        @uCommon.ufuncLog 
        def selectVariant(page, strVariant):
            """ 
            Objective: Click, set and select Variant
            
            param strVariant: Variant
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.hoverElem(page, pAdmin.pl.cv.selectVariantLbl)
            uCommon.waitAndClickElem(page, pAdmin.pl.cv.selectVariantLbl)
            uCommon.setAndSelectFromSmartDropDown(page, pAdmin.pl.cv.searchTxt, strVariant)
            com.checkProgressBar(page)
            uCommon.waitAndClickElem(page, pAdmin.pl.cv.colorSelectionLbl)
            uCommon.wait(page, 1)   
            
        @uCommon.ufuncLog 
        def selectDisplayType(page, strDisplayType):
            """ 
            Objective: Click and select DisplayType
            
            param strDisplayType: DisplayType
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.waitAndClickElem(page, pAdmin.pl.cv.selectTypeLbl)
            uCommon.waitAndClickElemText(page, strDisplayType)
            uCommon.wait(page, 1)
            
        @uCommon.ufuncLog 
        def selectSelectTypeOptions(page, strOptions):
            """ 
            Objective: Click and select  Select Type Options
            
            param strOptions: Options
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.waitAndClickElem(page, pAdmin.pl.cv.selectTypeOptionsLbl)
            uCommon.waitAndClickElemText(page, strOptions)
            uCommon.waitAndClickElem(page, pAdmin.pl.cv.variantProductOptLbl)
            uCommon.wait(page, 1)
            
        @uCommon.ufuncLog 
        def clickAddVariant(page):
            """ 
            Objective: Click Update & Continue successfully
            
            param: None
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.hoverAndClickElem(page, pAdmin.pl.cv.addVariantBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.pl.cv.variantSuccessMsg)
            uCommon.waitElemNotToBeVisible(page, pAdmin.pl.cv.variantSuccessMsg)
        
        @uCommon.ufuncLog 
        def selectSelectFilters(page, strSelectFilters):
            """ 
            Objective: Click, set and select SelectFilters
            
            param strSelectFilters: SelectFilters
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.hoverElem(page, pAdmin.pl.cv.selectFiltersLbl)
            uCommon.waitAndClickElem(page, pAdmin.pl.cv.selectFiltersLbl)
            uCommon.waitAndClickElemText(page, strSelectFilters)
            # uCommon.setAndSelectFromSmartDropDown(page, pAdmin.pl.cv.searchTxt, strSelectFilters) # possible defect for confirmation
            com.checkProgressBar(page)
            uCommon.waitAndClickElem(page, pAdmin.pl.cv.filterCategoryOptLbl)
            uCommon.wait(page, 1)  
            
        @uCommon.ufuncLog 
        def selectFiltersOptions(page, strOptions):
            """ 
            Objective: Click and select Filters Options
            
            param strOptions: Options
            returns: None
            Author: ccapistrano_20230508
            """
            uCommon.wait(page, 1)
            uCommon.waitAndClickElem(page, pAdmin.pl.cv.filtersOptionsLbl)
            uCommon.waitAndClickElemText(page, strOptions)
            uCommon.waitAndClickElem(page, pAdmin.pl.cv.variantProductOptLbl)
            uCommon.wait(page, 2)
            
        @uCommon.ufuncLog 
        def clickAddFilters(page):
            """ 
            Objective: Click Add Filters successfully
            
            param: None
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.waitAndClickElem(page, pAdmin.pl.cv.addFilterBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.pl.cv.filtersSuccessMsg)
            uCommon.waitElemNotToBeVisible(page, pAdmin.pl.cv.filtersSuccessMsg)
            uCommon.wait(page, 1)
            
            
    class sp:
        """STOCK & PRICE"""
        @uCommon.ufuncLog 
        def setMRPpriceViaVariantname(page, strVariantName, strPrice):
            """ 
            Objective: Set MRP price via Variant Name
            
            param: None
            returns: None
            Author: ccapistrano_20230508
            """    
            uCommon.waitElemToBeVisible(page, pAdmin.pl.sp.mrpPriceTxt(strVariantName))
            uCommon.setElem(page, pAdmin.pl.sp.mrpPriceTxt(strVariantName), strPrice)
            
        @uCommon.ufuncLog 
        def clickUpdateAndContinue(page):
            """ 
            Objective: Click Update & Continue successfully
            
            param: None
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.hoverAndClickElem(page, pAdmin.pl.sp.updateAndContinueBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.pl.sp.productSuccessMsg)
            uCommon.waitElemNotToBeVisible(page, pAdmin.pl.sp.productSuccessMsg)
            
        @uCommon.ufuncLog 
        def clickPublished(page):
            """ 
            Objective: Click Published successfully
            
            param: None
            returns: None
            Author: ccapistrano_20230508
            """  
            uCommon.hoverAndClickElem(page, pAdmin.pl.sp.publishedTgl)
            uCommon.waitElemToBeVisible(page, pAdmin.pl.sp.publishedLbl)
        
    class at:
        """Attributes"""
        @uCommon.ufuncLog 
        def clickSave(page):
            """ 
            Objective: Click Save successfully
            
            param: None
            returns: None
            Author: ccapistrano_20230508
            """    
            uCommon.hoverAndClickElem(page, pAdmin.pl.at.saveBtn)
            uCommon.waitElemToBeVisible(page, pAdmin.pl.at.productSuccessMsg)
            uCommon.waitElemNotToBeVisible(page, pAdmin.pl.at.productSuccessMsg)





class cu:
    """CUSTOMERS"""     
    @uCommon.ufuncLog  
    def clickCustomers(page):
        """ 
        Objective: Click Customers successful
        
        param: None
        returns: None
        Author: ccapistrano_20230511
        """
        uCommon.waitAndClickElem(page, pAdmin.lp.customerLbl)
        com.checkProgressBar(page)
        uCommon.waitElemToBeVisible(page, pAdmin.cu.customersLbl)
    
    @uCommon.ufuncLog  
    def searchCustomer(page, strEmail):
        """ 
        Objective: Click Customers search result
        
        :param: None
        :returns: None
        Author: cgrapa_20230613
        """
        uCommon.waitElemToBeVisible(page, pAdmin.cu.searchByTxt)
        uCommon.setElem(page, pAdmin.cu.searchByTxt, strEmail)
        uCommon.waitAndClickElem(page, pAdmin.cu.searchIconBtn)
        uCommon.wait(page, 2)
        uCommon.waitAndClickElem(page, pAdmin.cu.customerResultBtn)
        
    @uCommon.ufuncLog  
    def verifyUploadRewardsOrCreditButton(page):
        """ 
        Objective: Verify that Upload Rewards or Credit button is displayed.
        
        param: None
        returns: None
        Author: abernal_20240318
        """
        if uCommon.verifyVisible(page, pAdmin.cu.uploadCreditRewardBtn) == True:
            uCommon.log(1, f'Upload Rewards or Credit button is visible.') 
        elif uCommon.verifyVisible(page, pAdmin.cu.uploadCreditRewardBtn) == False:
            uCommon.log(2, f'Upload Rewards or Credit button is not visible.') 
            
    @uCommon.ufuncLog  
    def verifyTotalCreditAndRewardFields(page):
        """ 
        Objective: Verify that Total Credit and Total Reward fields are displayed.
        
        param: None
        returns: None
        Author: abernal_20240318
        """
        if uCommon.verifyVisible(page, pAdmin.cu.totalCreditLbl) == True:
            uCommon.log(1, f'Total Credit is visible.') 
        if uCommon.verifyVisible(page, pAdmin.cu.totalRewardLbl) == True:
            uCommon.log(1, f'Total Reward is visible.') 
            
    @uCommon.ufuncLog  
    def editTotalRewardsValue(page, strValue):
        """ 
        Objective: To edit the Total Rewards value.
        
        param strValue: Text
        returns: None
        Author: abernal_20240318
        """
        uCommon.waitAndClickElem(page, pAdmin.cu.totalRewardEditBtn)
        uCommon.waitAndSetElem(page, pAdmin.cu.rewardEditLbl, strValue)
        uCommon.waitAndClickElem(page, pAdmin.cu.editEnterBtn)
        uCommon.waitElemToBeVisible(page, pAdmin.cu.confirmationModal)
        uCommon.waitAndClickElem(page, pAdmin.cu.confirmationYesBtn)
        
    @uCommon.ufuncLog  
    def editTotalCreditsValue(page, strValue):
        """ 
        Objective: To edit the Total Credits value.
        
        param strValue: Text
        returns: None
        Author: abernal_20240318
        """
        uCommon.waitAndClickElem(page, pAdmin.cu.totalCreditEditBtn)
        uCommon.waitAndSetElem(page, pAdmin.cu.creditEditLbl, strValue)
        uCommon.waitAndClickElem(page, pAdmin.cu.editEnterBtn)
        uCommon.waitElemToBeVisible(page, pAdmin.cu.confirmationModal)
        uCommon.waitAndClickElem(page, pAdmin.cu.confirmationYesBtn)
        
            


class re:
    """REWARDS"""
    @uCommon.ufuncLog  
    def clickRewardsModule(page):
        """ 
        Objective: Click Rewards module.
        
        param: None
        returns: None
        Author: abernal_20240318
        """
        uCommon.waitAndClickElem(page, pAdmin.lp.rewardsLbl)
        if uCommon.verifyVisible(page, pAdmin.rm.beanRewardsLbl) == True:
            uCommon.log(1, f'Bean Rewards label is visible.') 
        elif uCommon.verifyVisible(page, pAdmin.rm.beanRewardsLbl) == False:
            uCommon.log(2, f'Bean Rewards label is not visible.') 
