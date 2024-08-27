import libraries.page.profile.myOrders as pMyOrders
import libraries.page.common.common as pCommon
import libraries.util.common as uCommon
import libraries.data.deploymentChecklist as dDepChkLst

@uCommon.ufuncLog  
def validateMyOrders(page, strOrderID, blnCoupon = False):
    """ 
    Objective: validate my orders page
    
    param strOrderID: Order ID
    param blnCoupon: True | False
    returns: None
    Author: ccapistrano_20230327
    """
    arrObj = ['myOrdersLbl','searchBtn', 'searchTxt', 'searchIconImg', 'placedOrderLbl','filterListBtn']
    for item in arrObj:
        uCommon.expectElemToBeVisible(page, pMyOrders.com.__dict__[item]) 
    arrObj = ['Order Id','Order Placed', 'Product/s Price', 'Shipping Price', 'Total Price' ,'Ship To']
    for item in arrObj:
        uCommon.expectElemToBeVisible(page, pMyOrders.com.myOrdersDataLbl(strOrderID, item)) 
    if blnCoupon == True:
        uCommon.expectElemToBeVisible(page, pMyOrders.com.myOrdersDataLbl(strOrderID, 'Coupon/s Used'))
    
    strParentElem = pMyOrders.com.parentTDOrderDetails(strOrderID)
    arrObj = ['ItemPictureImg','itemBrandLbl', 'itemNameLbl', 'itemQuantityLbl', 'itemQuantityCountLbl', 
              'itemPriceLbl', 'cancelBtn', 'needHelpBtn', 'statusLbl', 'statusDescLbl', 'editDeliveryDetailsBtn']
    for item in arrObj:
        uCommon.expectElemToBeVisible(page, pMyOrders.com.__dict__[item](strParentElem)) 
    arrObj = ['expressDeliveryLbl', 'expressDeliveryIconBtn', 'reviewsLbl']
    for item in arrObj:
        uCommon.expectOptElemToBeVisible(page, pMyOrders.com.__dict__[item](strParentElem))
 
@uCommon.ufuncLog         
def validateMyOrderDetails(page, strOrderID, arrCartDetails, arrCODetails, strVoucherDisc = "", strCouponType = "", strCouponTag = "", blnCoupon = False):
    """ 
    Objective: validate my orders details page
    
    param strOrderID: Order ID
    param arrCartDetails: [Brand, Name, Price, Quantity]
    param: [Product Price, Shopping Price, Item Price, User Name]
    param blnCoupon: True | False
    returns: None
    Author: ccapistrano_20230327
    """
    validateMyOrders(page, strOrderID, blnCoupon)
    strParentElem = pMyOrders.com.parentTDOrderDetails(strOrderID)
    uCommon.validateElemText(page, pMyOrders.com.itemBrandLbl(strParentElem), arrCartDetails[0])
    uCommon.validateElemText(page, pMyOrders.com.itemNameLbl(strParentElem), arrCartDetails[1])
    uCommon.validateElemText(page, pMyOrders.com.itemPriceLbl(strParentElem), arrCartDetails[2])
    uCommon.validateElemText(page, pMyOrders.com.itemQuantityCountLbl(strParentElem), arrCartDetails[3])
    uCommon.validateElemText(page, pMyOrders.com.myOrdersDataLbl(strOrderID, 'Product/s Price'), arrCODetails[0])
    uCommon.validateElemText(page,  pMyOrders.com.myOrdersDataLbl(strOrderID, 'Shipping Price'), arrCODetails[1].replace('Shipping Amount: ', ''), False)
    uCommon.validateElemText(page, pMyOrders.com.myOrdersDataLbl(strOrderID, 'Total Price'), arrCODetails[2].replace('Collectible Total: ', ''), False)
    uCommon.validateElemText(page, pMyOrders.com.myOrdersDataLbl(strOrderID, 'Ship To'), arrCODetails[3])
    if arrCartDetails[1] == dDepChkLst.strItemName2 or arrCartDetails[1] == dDepChkLst.strItemName3:
        uCommon.expectElemNotToBeVisible(page, pMyOrders.com.couponUsedLbl(strOrderID))
    else:
        if blnCoupon == True:
            if strCouponType == "" and (strCouponTag == "Brand Sponsored" or strCouponTag == "Edamama Sponsored") and strVoucherDisc != '':
                uCommon.validateElemText(page, pMyOrders.com.myOrdersDataLbl(strOrderID, ' Vouchers Used '), strVoucherDisc)

@uCommon.ufuncLog       
def cancelOrder(page, strOrderID):
    """ 
    Objective: Perform Cancel Order
    
    param strOrderID: Order ID
    returns: None
    Author: ccapistrano_20230327
    """
    strParentElem = pMyOrders.com.parentTDOrderDetails(strOrderID)
    for item in range(10):
        uCommon.waitAndClickElem(page, pMyOrders.com.cancelBtn(strParentElem))
        uCommon.wait(page, 0.5)
        if uCommon.verifyVisible(page, pMyOrders.co.OthersLbl) == True:
            uCommon.waitAndClickElem(page, pMyOrders.co.OthersLbl)
            uCommon.waitForLoadState(page)
            break
        else:
            uCommon.waitAndClickElem(page, pMyOrders.co.xBtn)
            uCommon.reloadPage(page)

    uCommon.setElem(page, pMyOrders.co.writeMsgHereTxt, 'test Only')
    uCommon.waitAndClickElem(page, pMyOrders.co.cancelOrderBtn)
    uCommon.waitElemNotToBeVisible(page, pMyOrders.com.cancelBtn(strParentElem))
    return strOrderID

@uCommon.ufuncLog       
def getMyOrderDetails(page, strOrderID, dictData):
    """ 
    Objective: get My Order details
    
    param strOrderID: Order ID
    param dictData: Dictionary data
    returns dicDetails: Dictionary details
    Author: ccapistrano_20230327
    """
    uCommon.clickElem(page, pMyOrders.com.filterListBtn)
    uCommon.wait(page, 0.5)
    if dictData["blnCancel"] == True:
        uCommon.waitAndClickElem(page, pMyOrders.com.cancelFilterBtn)
    strParentElem = pMyOrders.com.parentTDOrderDetails(strOrderID)
    strQuantity = uCommon.getElemText(page, pMyOrders.com.itemQuantityCountLbl(strParentElem))
    if dictData["strMOP"] == 'CASH ON DELIVERY':
        strModeOfPayment  = 'COD'
    elif dictData["strMOP"] == 'GCASH':
        strModeOfPayment  = 'Xendit Gcash'
    elif dictData["strMOP"] == 'GRAB PAY':
        strModeOfPayment  = 'Xendit Grab Pay'
    elif dictData["strMOP"] == 'MAYA':
        strModeOfPayment  = 'Xendit Maya'
    elif dictData["strMOP"] == 'CREDIT CARD':
        strModeOfPayment  = 'Xendit Credit Card'
    strShipPrice = uCommon.getElemText(page, pMyOrders.com.myOrdersDataLbl(strOrderID, 'Shipping Price'))
    strTotalPrice = uCommon.getElemText(page, pMyOrders.com.myOrdersDataLbl(strOrderID, 'Product/s Price'))
    strStatus = '0'
    strPriceInfo = uCommon.getElemText(page, pMyOrders.com.myOrdersDataLbl(strOrderID, 'Total Price'))
    uCommon.log(0, {'strQuantity': strQuantity, 'strModeOfPayment': strModeOfPayment, 'strShipPrice': strShipPrice, 'strTotalPrice': strTotalPrice, 'strStatus': strStatus, 'strPriceInfo': strPriceInfo})
    return {'strQuantity': strQuantity, 'strModeOfPayment': strModeOfPayment, 'strShipPrice': strShipPrice, 'strTotalPrice': strTotalPrice, 'strStatus': strStatus, 'strPriceInfo': strPriceInfo}

@uCommon.ufuncLog       
def validateOrderStatus(page, strOrderID, strExpValue):
    """ 
    Objective: validate Order Status is correct
    
    param strOrderID: Order ID
    param strExpValue: Expected Value
    returns: None
    Author: ccapistrano_20230510
    """
    strParentElem = pMyOrders.com.parentTDOrderDetails(strOrderID)
    uCommon.validateElemText(page, pMyOrders.com.statusDescLbl(strParentElem), strExpValue)
    
@uCommon.ufuncLog       
def clickEditDeliveryDetails(page, strOrderID, blnChangeDeilvery = False):
    """ 
    Objective: Click Edit Delivery Details successful
    
    param strOrderID: Order ID
    param blnChangeDeilvery: True ? False
    returns: None
    Author: ccapistrano_20230511
    """
    strParentElem = pMyOrders.com.parentTDOrderDetails(strOrderID)
    uCommon.waitAndClickElem(page, pMyOrders.com.editDeliveryDetailsBtn(strParentElem))
        
    if blnChangeDeilvery == False:
        uCommon.waitElemToBeVisible(page, pMyOrders.di.addNewAddressBtn)
    #Commenting this out since Edit Address has still some issues
    #else:
    #    uCommon.waitElemToBeVisible(page, pMyOrders.com.oneTimeDeliveryChangeMsg)
    #    uCommon.waitElemNotToBeVisible(page, pMyOrders.com.oneTimeDeliveryChangeMsg)
    

class di:
    """DELIVER INFORMATION"""
    @uCommon.ufuncLog       
    def clickAddNewAddress(page,):
        """ 
        Objective: Click Add New Address successful
        
        param: None
        param: None
        returns: None
        Author: ccapistrano_20230511
        """
        uCommon.waitAndClickElem(page, pMyOrders.di.addNewAddressBtn)
        uCommon.waitElemToBeVisible(page, pMyOrders.di.na.newAddressLbl)
    
    @uCommon.ufuncLog       
    def clickAddresstoBeDeleted(page, strname):
        """ 
        Objective: Click Address to be deleted
        
        param strname: Name
        param: None
        returns: None
        Author: ccapistrano_20230512
        """
        uCommon.waitAndClickElemText(page, strname, pMyOrders.di.parentDIVName)
        
        
    @uCommon.ufuncLog       
    def clickUpdateDeliveryInfo(page):
        """ 
        Objective: Click Update Delivery Information successful
        
        param: None
        param: None
        returns: None
        Author: ccapistrano_20230512
        """
        uCommon.waitAndClickElem(page, pMyOrders.di.updateDeliveryInfoBtn)
        uCommon.waitElemToBeVisible(page, pMyOrders.di.confirmationAddressChangeLbl)
        
    @uCommon.ufuncLog       
    def clickConfirm(page):
        """ 
        Objective: Click Confirm     successful in Confirmation of Address Change pop-up
        
        param: None
        param: None
        returns: None
        Author: ccapistrano_20230512
        """
        uCommon.waitAndClickElem(page, pMyOrders.di.confirmBtn)
        uCommon.waitElemToBeVisible(page, pMyOrders.di.orderUpdateDelAddSuccessMsg)
        uCommon.waitElemNotToBeVisible(page, pMyOrders.di.orderUpdateDelAddSuccessMsg)
        
    class na:
        """NEW ADDRESS"""
        @uCommon.ufuncLog       
        def fillOutNewAddress(page, dictData):
            """ 
            Objective: Fill Out New Address details successful
            
            param dictData: Dictionary data
            param: None
            returns: None
            Author: ccapistrano_20230511
            """
            uCommon.setElem(page, pMyOrders.di.na.firstNameTxt, dictData["strFName"])
            uCommon.setElem(page, pMyOrders.di.na.lastNameTxt, dictData["strLName"])
            uCommon.setElem(page, pMyOrders.di.na.mobileNumberTxt, dictData["strMobile"])
            di.na.selectProviceDistrict(page, dictData["strProvince"])
            di.na.selectCity(page, dictData["strCity"])
            uCommon.setElem(page, pMyOrders.di.na.zipCodeTxt, dictData["strZipCode"])
            di.na.selectBarangay(page, dictData["selectBarangay"])
            uCommon.setElem(page, pMyOrders.di.na.lotUnitStreetTxt, dictData["strLotStreet"])
            uCommon.setElem(page, pMyOrders.di.na.landmarkTxt, dictData["strLandmark"])
            
        @uCommon.ufuncLog 
        def selectProviceDistrict(page, strProvince):
            """ 
            Objective: Click, set and select Provice or District
            
            param strProvince: Provice | District
            returns: None
            Author: ccapistrano_20230511
            """  
            uCommon.wait(page, .5)
            uCommon.waitAndClickElem(page, pMyOrders.di.na.provinceDistrictDownIconBtn)
            uCommon.setAndSelectFromSmartDropDown(page, pMyOrders.di.na.searchTxt, strProvince, pMyOrders.di.na.parentDIVListBox)
            uCommon.wait(page, 1)
            
        @uCommon.ufuncLog 
        def selectCity(page, strCity):
            """ 
            Objective: Click, set and select City
            
            param strCity: City
            returns: None
            Author: ccapistrano_20230511
            """  
            uCommon.waitAndClickElem(page, pMyOrders.di.na.cityDownIconBtn)
            uCommon.setAndSelectFromSmartDropDown(page, pMyOrders.di.na.searchTxt, strCity, pMyOrders.di.na.parentDIVListBox)
            uCommon.wait(page, 1)
            
        @uCommon.ufuncLog 
        def selectBarangay(page, strBarangay):
            """ 
            Objective: Click, set and select Barangay or Village
            
            param strBarangay: Barangay | Village
            returns: None
            Author: ccapistrano_20230511
            """  
            uCommon.waitAndClickElem(page, pMyOrders.di.na.barangayVillageDownIconBtn)
            uCommon.setAndSelectFromSmartDropDown(page, pMyOrders.di.na.searchTxt, strBarangay, pMyOrders.di.na.parentDIVListBox)
            
        @uCommon.ufuncLog       
        def clickAddNewAddress(page):
            """ 
            Objective: Click Add New Address successful
            
            param: None
            param: None
            returns: None
            Author: ccapistrano_20230511
            """
            uCommon.waitAndClickElem(page, pMyOrders.di.na.addNewAddressBtn)
            uCommon.waitElemToBeVisible(page, pMyOrders.di.na.addressAddedSuccessMsg)
            uCommon.waitElemNotToBeVisible(page, pMyOrders.di.na.addressAddedSuccessMsg)