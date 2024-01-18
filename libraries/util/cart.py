import libraries.page.cart as pCart
import libraries.page.common.common as pCommon
import libraries.util.common as uCommon
import libraries.util.appCommon.appComm as uAppComm


@uCommon.ufuncLog  
def validateMyCart(page):
    """ 
    Objective: Validate my cart elements
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    arrObj = ['myBagLbl','youHaveXProductLbl', 'itemSmallPicImg', 'itemBrandLbl', 'itemNameLbl', 'heartIconBtn', 'deleteIconBtn', 
              'colorLbl', 'giftWrapChk', 'giftWrapLbl', 'quantityMinusIconBtn', 'quantityOutputLbl', 'quantityPlusIconBtn', 'itemPriceLbl']
    for item in arrObj:
        uCommon.waitElemToBeVisible(page, pCart.mc.__dict__[item])

@uCommon.ufuncLog  
def validateOrderDetails(page):
    """ 
    Objective: Validate order details elements
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    arrObj = ['giftWrapBannerImg', 'orderDetailsLbl', 'subTotalLbl', 'subTotalAmountLbl',
              'giftWrapLbl', 'giftWrapAmountLbl', 'shippingLbl', 'shippingAmountLbl', 'totalLbl', 'totalAmountLbl', 'weWillProvideAnUpdateLbl', 'checkOutBtn']
    for item in arrObj:
        uCommon.waitElemToBeVisible(page, pCart.od.__dict__[item])

@uCommon.ufuncLog  
def validateMyCartAndOrderDetails(page):
    """ 
    Objective: Validate my cart and order details elements
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    validateMyCart(page)
    validateOrderDetails(page)

@uCommon.ufuncLog  
def validateConfirmationPrompt(page):
    """ 
    Objective: Validate confirmation prompt elements
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    arrObj = ['confirmationLbl','confirmationMsg', 'noBtn', 'yesBtn']
    for item in arrObj:
        uCommon.waitElemToBeVisible(page, pCart.cm.__dict__[item])

@uCommon.ufuncLog  
def validateAndClickYesInConfirmationPrompt(page):
    """ 
    Objective: Validate confirmation prompt elements and click Yes
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    validateConfirmationPrompt(page)
    uCommon.waitAndClickElem(page, pCart.cm.yesBtn)
    uCommon.wait(page, 1)
    uCommon.waitElemToBeVisible(page, pCart.com.yourBagsEmptyLbl)
    uCommon.waitElemToBeVisible(page, pCart.com.yourBagsEmptyDescLbl)
    uCommon.waitElemToBeVisible(page, pCart.com.startBrowsingBtn)

@uCommon.ufuncLog  
def deleteAddToCartItems(page):
    """ 
    Objective: Delete item added in Cart
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    uCommon.waitAndClickElem(page, pCommon.com.cartCounterLbl)
    uCommon.wait(page, 2)
    for item in range(10):
        uCommon.waitAndClickElem(page, pCart.mc.deleteIconBtn)
        uCommon.wait(page, 2)
        if uCommon.verifyVisible(page, pCart.cm.confirmationLbl) == False:
            uCommon.waitAndClickElem(page, pCart.mc.deleteIconBtn)
            uCommon.wait(page, 2)
        else:
            break
    validateAndClickYesInConfirmationPrompt(page)

@uCommon.ufuncLog  
def checkAndDeleteAddToCartItems(page):
    """ 
    Objective: Check and delete item added in Cart
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    uCommon.waitElemToBeVisible(page, pCommon.header.cartIconBtn)
    if uCommon.verifyVisible(page, pCommon.com.cartCounterLbl) == True:
        deleteAddToCartItems(page)
        uCommon.clickElem(page, pCommon.header.shopBtn)
        
@uCommon.ufuncLog  
def validateYouHaveXProduct(page, strCount = '1'):
    """ 
    Objective: Validate product count
    
    param strCount: Product count
    returns: None
    Author: ccapistrano_20230327
    """
    uCommon.validateElemText(page, pCart.mc.youHaveXProductLbl, strCount, False)
    
@uCommon.ufuncLog  
def validateMyCartdetails(page, dictDetails, strCount):
    """ 
    Objective: Click Add to Bag
    
    param dictDetails: dictDetails
    returns: None
    Author: ccapistrano_20230327
    """
    uCommon.validateElemText(page, pCart.mc.itemBrandLbl, dictDetails['strBrand'], False)
    uCommon.validateElemText(page, pCart.mc.itemNameLbl, dictDetails['strName'], False)
    uCommon.validateElemText(page, pCart.mc.quantityOutputLbl, strCount)
    uCommon.validateElemText(page, pCart.mc.itemPriceLbl, dictDetails['strPrice'])
    uCommon.validateElemText(page, pCart.od.subTotalAmountLbl, dictDetails['strPrice'])
    if uCommon.getElemText(page, pCart.od.totalAmountLbl) != dictDetails['strPrice']:
        strPrice = uCommon.getElemText(page, pCart.mc.itemDiscountedPrice)
        uCommon.validateElemText(page, pCart.od.totalAmountLbl, strPrice)
    else:
        uCommon.validateElemText(page, pCart.od.totalAmountLbl, dictDetails['strPrice'])
        uAppComm.com.validateCountInCart(page, strCount)

@uCommon.ufuncLog      
def clickCheckOut(page):
    """ 
    Objective: Click check out 
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    uCommon.clickElem(page, pCart.od.checkOutBtn)