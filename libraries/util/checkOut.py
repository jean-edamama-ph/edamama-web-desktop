import libraries.data.common as dCommon
import libraries.data.deploymentChecklist as dDepChkLst

import libraries.page.cart as pCart
import libraries.page.checkOut as pCheckOut
import libraries.page.shop as pShop
import libraries.page.common.common as pCommon

import libraries.util.cart as uCart
import libraries.util.shop as uShop
import libraries.util.common as uCommon

import libraries.api.ap.util.apiCall.rewards as apiRewards
import libraries.api.ap.util.apiCall.login as apiLogin

@uCommon.ufuncLog  
def checkOutItem(page, strItemName = '', strType = 'fp'):   
    """ 
    Objective: Perform check out of an item
    
    param strItemName: Item Name
    returns: None
    Author: ccapistrano_20230327
    """
    uCart.checkAndDeleteAddToCartItems(page)
    if strItemName == '':
        strItemName = uCommon.getElemText(page, pShop.fp.firstItemNameLbl)
        strBrand = uCommon.getElemText(page, pShop.com.itemBrandNameLbl(strItemName))
        strName = uCommon.getElemText(page, pShop.com.itemNameLbl(strItemName))
        strPrice = uCommon.getElemText(page, pShop.com.itemPriceLbl(strItemName))
        uCommon.hoverAndClickElem(page, pShop.com.ItemPicImg(strItemName))
        uCommon.validateElemText(page, pShop.pf.itemBrandLbl, strBrand)
        uCommon.validateElemText(page, pShop.pf.itemNameLbl, strName)
        uCommon.validateElemText(page, pShop.pf.itemPriceLbl, strPrice)
    else:
        uShop.sp.searchAndClickItem(page, strItemName)
        strBrand = uCommon.getElemText(page, pShop.pf.itemBrandLbl)
        strName = uCommon.getElemText(page, pShop.pf.itemNameLbl)
        arrName = strName.split('  ')
        strName = arrName[0]
        if uCommon.verifyVisible(page, pShop.pf.itemDisPriceLbl) == True:
            strPrice = uCommon.getElemText(page, pShop.pf.itemDisPriceLbl)
            strOrigPrice = uCommon.getElemText(page, pShop.pf.itemPriceLbl)
            blnDiscount = True
        else:
            strPrice = uCommon.getElemText(page, pShop.pf.itemPriceLbl)
            blnDiscount = False

    uCommon.expectElemNotToBeVisible(page, pShop.pf.outOfStockBtn)
    if uCommon.verifyVisible(page, pShop.pf.firstSizeBtn) == True:
        uCommon.waitAndClickElem(page, pShop.pf.firstSizeBtn)
    if strType == 'fp':
        uCommon.waitElemToBeVisible(page, pShop.pf.quantityOutputLbl)
        #strQuantity = uCommon.getElemText(page, pShop.pf.quantityOutputLbl)
        strQuantity = '1'
        uShop.pp.clickAddToBag(page)
    if strType == 'ss':
        uShop.pp.clickAddToBag(page, False)
        uShop.ss.validateSubsAndSavePrompt(page)
        uShop.ss.clickConfirmAddToCart(page)
    uCommon.waitAndClickElem(page, pCommon.com.cartCounterLbl)
    uCommon.waitForLoadState(page)
    if uCommon.verifyVisible(page, pCart.mc.youHaveXProductLbl) == True:
        uCommon.validateElemText(page, pCart.mc.youHaveXProductLbl, strQuantity, False)
    uCommon.waitElemToBeVisible(page, pCart.mc.itemBrandLbl)
    uCommon.validateElemText(page, pCart.mc.itemBrandLbl, strBrand, False)
    uCommon.getElemText(page, pCommon.com.cartCounterLbl)
    uCommon.validateElemText(page, pCart.mc.itemNameLbl, strName)
    if strType == 'fp':
        uCommon.validateElemText(page, pCart.mc.quantityOutputLbl, strQuantity)
        if blnDiscount == True:
            uCommon.validateElemText(page, pCart.mc.itemPriceLbl, strOrigPrice)
            uCommon.validateElemText(page, pCart.od.subTotalAmountLbl, strOrigPrice)
        else:
            uCommon.validateElemText(page, pCart.mc.itemPriceLbl, strPrice)
            uCommon.validateElemText(page, pCart.od.subTotalAmountLbl, strPrice)
        uCommon.validateElemText(page, pCart.od.totalAmountLbl, strPrice)
    elif strType == 'ss':
        strQuantity = uCommon.getElemText(page, pCart.mc.quantityOutputLbl)
        if blnDiscount == True:
            uCommon.validateElemText(page, pCart.mc.itemPriceLbl, strOrigPrice)
            uCommon.validateElemText(page, pCart.od.subTotalAmountLbl, strOrigPrice)
        else:
            uCommon.validateElemText(page, pCart.mc.itemPriceLbl, strPrice)
            uCommon.validateElemText(page, pCart.od.subTotalAmountLbl, strPrice)
        uCommon.validateElemText(page, pCart.od.totalAmountLbl, strPrice)
        uCommon.validateElemText(page, pCommon.com.cartCounterLbl, strQuantity)
    uCommon.clickElem(page, pCart.od.checkOutBtn)
    uCommon.waitForLoadState(page)
    return [strBrand, strName, strPrice, strQuantity]

@uCommon.ufuncLog  
def validateSideMenu(page):
    """ 
    Objective: Validate side menu elements
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    uCommon.expectElemToBeVisible(page, pCheckOut.sm.checkOutLbl) 
    uCommon.expectElemToBeVisible(page, pCheckOut.sm.checkOutDescLbl) 

@uCommon.ufuncLog  
def validateDeliveryAddress(page):
    """ 
    Objective: Validate delivery address elements
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    arrObj = ['deliveryAddressLbl','selectYourAddressLbl', 'userIconImg', 'userNameLbl', 'defaultLbl','editBtn', 
              'phoneIconImg', 'phoneLbl', 'addressIconImg', 'addressLbl', 'newAddressBtn', 'changeAddressBtn']
    for item in arrObj:
        uCommon.expectElemToBeVisible(page, pCheckOut.co.__dict__[item]) 

@uCommon.ufuncLog  
def validateCartSummary(page):
    """ 
    Objective: Validate cart summary elements
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    arrObj = ['itemqQuantityLbl','itemBrandLbl', 'itemnameLbl', 'itemColorLbl', 'itemPriceLbl', 
              'discountedAmountLbl', 'shippingAmountLbl', 'creditUsedTotalLbl', 'collectibleTotalLbl']
    for item in arrObj:
        uCommon.expectElemToBeVisible(page, pCheckOut.co.__dict__[item])  
    
    arrObj = ['expressDeliveryLbl', 'expressDeliveryIconImg']
    for item in arrObj:
        uCommon.expectOptElemToBeVisible(page, pCheckOut.co.__dict__[item])

@uCommon.ufuncLog   
def validatePaymentMethod(page):
    """ 
    Objective: Validate payment method elements
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    arrObj = ['paymentLbl','selectPaymentLbl', 'creditCardLbl', 'creditCardRdb', 'gCashLbl','gCashRdb','grabPayLbl', 'grabPayRdb',
              'mayaLbl', 'mayaRdb', 'cashOnDeliveryLbl', 'cashOnDeliveryRdb']
    for item in arrObj:
        uCommon.expectElemToBeVisible(page, pCheckOut.pm.__dict__[item]) 
    
    arrObj = ['pickATreatLbl', 'minSpendOfLbl', 'allPickTreatItems']
    for item in arrObj:
        uCommon.expectOptElemToBeVisible(page, pCheckOut.pm.__dict__[item])

@uCommon.ufuncLog  
def validateBeansPromo(page):
    """ 
    Objective: Validate beans promo elements
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    arrObj = ['beansPromoDescLbl','useBeansLbl', 'useBeansRdb', 'totalBeanLbl', 'toalBeanImg','enterPromoCodeLbl','enterPromoCodeRdb', 'availablePromoCodeLbl', 'arrowForwardIconBtn']
    for item in arrObj:
        uCommon.expectElemToBeVisible(page, pCheckOut.pm.__dict__[item]) 
    
@uCommon.ufuncLog  
def validateOrderDetails(page):
    """ 
    Objective: Validate order details elements
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    arrObj = ['orderDetailsLbl','subTotalLbl', 'subTotalAmountLbl', 'giftWrapLbl', 'giftWrapAmountLbl','shippingLbl','shippingAmountLbl',
              'totalLbl', 'totalAmountLbl', 'xenditTestAmountLbl', 'xenditTestAmountTxt', 'placeOrderBtn']
    for item in arrObj:
        uCommon.expectElemToBeVisible(page, pCheckOut.pm.__dict__[item]) 

@uCommon.ufuncLog  
def validateCheckOutPage(page):
    """ 
    Objective: Validate check out page elements
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    validateSideMenu(page)
    validateDeliveryAddress(page)
    validateCartSummary(page)
    validatePaymentMethod(page)
    validateBeansPromo(page)
    validateOrderDetails(page)

@uCommon.ufuncLog  
def validateThankYouPage(page):
    """ 
    Objective: Validate thank you page elements
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    uCommon.waitForLoadState(page, 'networkidle')
    arrObj = ['orderSuccessImg','thankYouLbl', 'thankYouDescLbl', 'trackerOrderLbl', 'orderIDLbl', 'ordelIDCodeLbl','backToShoppingBtn','trackOrderBtn']
    for item in arrObj:
        uCommon.waitElemToBeVisible(page, pCheckOut.ty.__dict__[item]) 
     
@uCommon.ufuncLog   
def selectModeOfPaymentAndBeansOrPromo(page, dictData, strMOP = '', strBeansPromo = '', strPromoCode = ''):
    """ 
    Objective: Validate thank you page elements
    
    param strMOP: CASH ON DELIVERY | CREDIT CARD | GCASH | GRAB PAY | MAYA
    param strBeansPromo: beans | promo
    param strPromoCode: Promo Code
    returns: None
    Author: ccapistrano_20230327
    Updated By: abernal_20240326
    """
    uCommon.waitForLoadState(page)
    uCommon.waitForLoadState(page, 'networkidle')
    uCommon.wait(page, 2)
    if strMOP == 'CASH ON DELIVERY':
        uCommon.hoverAndClickElem(page, pCheckOut.pm.cashOnDeliveryLbl)
        uCommon.waitAndClickElem(page, pCheckOut.pm.cashOnDeliveryRdb)
    elif strMOP == 'CREDIT CARD':
        uCommon.hoverAndClickElem(page, pCheckOut.pm.creditCardRdb)
        uCommon.wait(page, 1)
        uCommon.setElem(page, pCheckOut.cc.cardHoldersNameTxt, dCommon.card.strName)
        uCommon.setElem(page, pCheckOut.cc.cardNumberTxt, dCommon.card.strNumber)
        uCommon.setElem(page, pCheckOut.cc.validThruTxt, dCommon.card.strDate)
        uCommon.setElem(page, pCheckOut.cc.cvvCnnTxt, dCommon.card.strCvv)
        uCommon.waitAndClickElem(page, pCheckOut.cc.billingAddressTgl)
        uCommon.waitAndClickElem(page, pCheckOut.cc.confirmBtn)
        uCommon.validateElemText(page, pCheckOut.pm.cardNumberLbl, dCommon.card.strNumber)
    elif strMOP == 'GCASH':
        uCommon.hoverAndClickElem(page, pCheckOut.pm.gCashLbl)
        uCommon.waitAndClickElem(page, pCheckOut.pm.gCashRdb)
    elif strMOP == 'GRAB PAY':
        uCommon.hoverAndClickElem(page, pCheckOut.pm.grabPayLbl)
        uCommon.waitAndClickElem(page, pCheckOut.pm.grabPayRdb)
    elif strMOP == 'MAYA':
        uCommon.hoverAndClickElem(page, pCheckOut.pm.mayaLbl)
        uCommon.waitAndClickElem(page, pCheckOut.pm.mayaRdb)
    else:
        uCommon.log(2, f'Incorrect input of Mode Of Payment. Kindly use any of the ff: "CASH ON DELIVERY", "CREDIT CARD", "GCASH", "GRAB PAY", "MAYA"')

    if strBeansPromo == 'beans':
        uCommon.waitAndClickElem(page, pCheckOut.pm.useBeansRdb)
        uCommon.getElemTextAndCheckIfContainsText(page, f'{pCheckOut.pm.useBeansRdb}/../div/span[2]', 'out of')
        strSubTotalAmt = uCommon.getElemText(page, pCheckOut.pm.subTotalAmountLbl).strip()
        floatSubTotalAmt = convertTotalAmtToFloat(strSubTotalAmt)
        blnIsMarkDownExist = uCommon.verifyVisible(page, pCheckOut.pm.markdownLbl)
        floatMarkDownTotalAmt = 0
        if blnIsMarkDownExist == True:
            strMarkdownTotalAmt = uCommon.getElemText(page, pCheckOut.pm.markdownTotalAmountLbl).strip()
            floatMarkDownTotalAmt = convertTotalAmtToFloat(strMarkdownTotalAmt)
        floatTotalSubAmt = floatSubTotalAmt + floatMarkDownTotalAmt
        apiLogin.postLogin()
        dictCreditsConfigurations = apiRewards.getCreditsConfigurations()
        floatRewardsPercentageCap = dictCreditsConfigurations['floatRewardsPercentageCap'] / 100
        floatComputedBeanToUse = floatTotalSubAmt * floatRewardsPercentageCap
        if floatComputedBeanToUse < dictCreditsConfigurations['floatRewardsAmountCap']:
            strComputedBeansToUse = str(int(floatComputedBeanToUse))
        else:
            strComputedBeansToUse = str(int(dictCreditsConfigurations['floatRewardsAmountCap']))
        uCommon.getElemTextAndCheckIfContainsText(page, pCheckOut.pm.totalBeanRewardToUseLbl, strComputedBeansToUse)
    elif strBeansPromo == 'promo':
        uCommon.waitAndClickElem(page, pCheckOut.pm.enterPromoCodeRdb)
        uCommon.waitAndSetElem(page, pCheckOut.pc.enterPromoCodeTxt, strPromoCode)
        uCommon.wait(page, 1.5) 
        uCommon.waitAndClickElem(page, pCheckOut.pc.applyBtn)
        uCommon.wait(page, 1) 
        subTotalLbl = uCommon.getElemText(page, pCheckOut.pm.subTotalAmountLbl)
        newSubTotalLbl = subTotalLbl.replace("₱", "").replace(",", "")
        if float(newSubTotalLbl) < 500:
            if dictData['strPromoCode'] == "EDRIBSCBTALA" and dictData['strItemName'] == dDepChkLst.strItemName2:
                uCommon.waitElemToBeVisible(page, pCheckOut.pm.promoCodeUsedInvalidErrorMsg)
                uCommon.expectElemNotToBeVisible(page, pCheckOut.pm.couponDiscountLbl)
            else:
                uCommon.waitElemToBeVisible(page, pCheckOut.pm.promoMinPurchaseErrorMsg)
                uCommon.expectElemNotToBeVisible(page, pCheckOut.pm.couponDiscountLbl)
        else:
            uCommon.expectElemNotToBeVisible(page, pCheckOut.pm.promoCodeDoesNotExistMsg)
            uCommon.waitElemToBeVisible(page, pCheckOut.pm.promoAmountLbl)
            uCommon.validateElemText(page, pCheckOut.pm.promoCodeLbl, strPromoCode)
        if strPromoCode == 'BEAN300' or strPromoCode == "EDRIBSCBTALA":
            uCommon.waitElemToBeVisible(page, pCheckOut.pm.promoDescLbl)
        else:
            uCommon.expectElemNotToBeVisible(page, pCheckOut.pm.promoDescLbl)
    elif strBeansPromo == '':
        uCommon.log(0, f'No selected Beans & Promo')
    else:
        uCommon.log(2, f'Incorrect input of Beans and Promo. Kindly use any of the ff: "beans" or "promo"')
    uCommon.wait(page, 1) 

@uCommon.ufuncLog   
def clickPlaceOrderAndGetOrderID(page, strMOP = '', strBeansPromo = ''):
    """ 
    Objective: Click Place Order and get Order ID
    
    param strMOP: CASH ON DELIVERY | CREDIT CARD | GCASH | GRAB PAY | MAYA
    param strBeansPromo: beans | promo
    returns strOrderID: Order ID
    Author: ccapistrano_20230327
    Updated by: jatregenio_20240204
    """
    strTotalColectible = uCommon.getElemText(page, pCheckOut.pm.totalAmountLbl)
    blnBeansFullPayment = False
    if strTotalColectible != '₱0.00':
        blnBeansFullPayment = True
    uCommon.hoverElem(page, pCheckOut.pm.placeOrderBtn)
    uCommon.wait(page, .5)
    uCommon.waitAndClickElem(page, pCheckOut.pm.placeOrderBtn)
    uCommon.waitForLoadState(page)
    if strMOP == 'CREDIT CARD':
        #if strBeansPromo != 'beans':
        if blnBeansFullPayment == True:
            uCommon.wait(page, 27)
            frame = uCommon.switchToFrame(page, pCheckOut.com.payerAuthenticationFrame)
            if uCommon.verifyVisible(frame, pCheckOut.com.paymentSecurityForm) == True:
                uCommon.setElem(frame, pCheckOut.com.enterCodeHereTxt, dCommon.card.strPassword)
                uCommon.clickElem(frame, pCheckOut.com.submitBtn)
                #else:
                #    uCommon.setElem(frame, pCheckOut.com.passwordTxt, dCommon.card.strPassword)
                #uCommon.clickElem(frame, pCheckOut.com.submitBtn)
            uCommon.waitForLoadState(page)
    elif strMOP == 'GCASH' or strMOP == 'GRAB PAY' or strMOP == 'MAYA':
        if strBeansPromo == 'beans':
            if blnBeansFullPayment == True:
                clickProceedToPay(page)
        else:
            clickProceedToPay(page)
    validateThankYouPage(page)
    strOrderID = uCommon.getElemText(page, pCheckOut.ty.ordelIDCodeLbl)
    return strOrderID

@uCommon.ufuncLog   
def clickProceedToPay(page):
    """ 
    Objective: Click Proceed To Pay successful
    
    param: None
    returns: None
    Author: ccapistrano_20230511
    Updated By: abernal_20240311
    """
    uCommon.wait(page, 5)
    uCommon.waitForLoadState(page, 'networkidle')
    uCommon.waitAndClickElem(page, pCheckOut.com.proceedToPayBtn)
    # uCommon.waitElemToBeVisible(page, '//mat-spinner[contains(@class,"mat-progress-spinner")]')
    # uCommon.waitElemNotToBeVisible(page, '//mat-spinner[contains(@class,"mat-progress-spinner")]')
    
@uCommon.ufuncLog   
def validateCheckOutDetails(page, arrCartDetails):
    """ 
    Objective: Click Place Order and get Order ID
    
    param arrCartDetails: [Brand, Name, Price, Quantity]
    returns strOrderID: Order ID
    Author: ccapistrano_20230327
    """
    uCommon.waitAndValidateElemText(page, pCheckOut.co.itemBrandLbl, arrCartDetails[0], False)
    uCommon.getElemText(page, pCheckOut.co.itemqQuantityLbl)
    uCommon.validateElemText(page, pCheckOut.co.itemnameLbl, arrCartDetails[1])
    if uCommon.verifyVisible(page, pCheckOut.co.itemDisPriceLbl) == True:
        uCommon.validateElemText(page, pCheckOut.co.itemDisPriceLbl, arrCartDetails[2])
    else:
        uCommon.validateElemText(page, pCheckOut.co.itemPriceLbl, arrCartDetails[2])
    
    uCommon.validateElemText(page, pCheckOut.co.itemqQuantityLbl, arrCartDetails[3], False)
    
    strProductPrice = arrCartDetails[2]
    strShoppingPrice = uCommon.getElemText(page, pCheckOut.pm.shippingAmountLbl)
    if strShoppingPrice == 'Free':
        strShoppingPrice = '₱0.00'
    strItemPrice = uCommon.waitAndGetElemText(page, pCheckOut.pm.totalAmountLbl)
    strUserName = uCommon.waitAndGetElemText(page, pCheckOut.co.userNameLbl)
    
    return [strProductPrice, strShoppingPrice, strItemPrice, strUserName]

@uCommon.ufuncLog   
def clickMyOrders(page):
    """ 
    Objective: Click My Orders
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """ 
    uCommon.clickElem(page, pCheckOut.ty.trackOrderBtn)
    
@uCommon.ufuncLog   
def clickFirstSize(page, blnOpt = False):
    """ 
    Objective: Click first size option
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """ 
    if blnOpt == True:
        uCommon.wait(page, 1)
        if uCommon.verifyVisible(page, pShop.pf.firstSizeBtn) == True:
            uCommon.waitAndClickElem(page, pShop.pf.firstSizeBtn)
    else:
        uCommon.waitAndClickElem(page, pShop.pf.firstSizeBtn)

@uCommon.ufuncLog
def convertTotalAmtToFloat(strTotalAmt):
    """ 
    Objective: Convert Total Amount either from order amount, beans or credits to Float with 2 decimal places.
    
    param strTotalAmt: Text
    returns strTotalAmtOnly: converted Total Amount
    Author: jatregenio_20240203
    """
    if '₱' in strTotalAmt:
        strTotalAmtOnly = strTotalAmt[1:(len(strTotalAmt))]
    elif '-₱' in strTotalAmt:
        strTotalAmtOnly = strTotalAmt[2:(len(strTotalAmt))]
    else:
        strTotalAmtOnly = strTotalAmt[0:(len(strTotalAmt))]
    if ',' in strTotalAmtOnly:
        strTotalAmtOnly = strTotalAmtOnly.replace(',', '')
    floatTotalAmount = float(strTotalAmtOnly)
    return round(floatTotalAmount, 2)

@uCommon.ufuncLog
def validateIfDefaultAddressByProvince(page, strProvince):
    """ 
    Objective: Verify the default delivery address by province in checkout page.
    
    param: None
    returns None
    Author: jatregenio_20240212
    """
    uCommon.validateElemText(page, pCheckOut.co.addressLbl, strProvince, False)
    
@uCommon.ufuncLog
def validateDeliveryAddressElemAndDefaultAddressByProv(page, strProv):
    """ 
    Objective: Verify the default delivery address by province and the elements in Delivery Address section in checkout page.
    
    param: None
    returns None
    Author: jatregenio_20240213
    """
    validateIfDefaultAddressByProvince(page, strProv)
    validateDeliveryAddress(page)
    
@uCommon.ufuncLog
def closeMobileVerificationModal(page):
    """ 
    Objective: To close the mobile verification modal (for non-verified users)
    
    param: None
    returns None
    Author: abernal_20240326
    """
    uCommon.wait(page, 2)
    if uCommon.verifyVisible(page, pCheckOut.co.mobileVerifModalLbl) == True:
        uCommon.clickElem(page, pCheckOut.co.mobileVerifCloseBtn)
        uCommon.waitElemNotToBeVisible(page, pCheckOut.co.mobileVerifModalLbl)