import libraries.page.profile.myWishlist as pMyWishlist

import libraries.util.common as uCommon
import libraries.util.shop as uShop

class com:
    """COMMON"""
    @uCommon.ufuncLog
    def removeItemOnMyWishlist(page, strItemName):
        """ 
        Objective: Remove Wishlist item on My Wishlist page
            
        param strItemName: Item name
        returns: None
        Author: cgrapa_20230615
        """
        uCommon.waitAndClickElem(page, pMyWishlist.com.itemHeartBtn(strItemName))
        uCommon.waitElemToBeVisible(page, pMyWishlist.com.confirmationDialogLbl)
        uCommon.waitAndClickElem(page, pMyWishlist.com.confirmationDialogYesBtn)
    
        
    @uCommon.ufuncLog
    def validateMyWishlist(page):
        """ 
        Objective: Validate Wishlist page
            
        param: None
        returns: None
        Author: cgrapa_20230615
        """
        uCommon.waitElemNotToBeVisible(page, pMyWishlist.com.loadingSpinnerImg)
        arrObj = ['savedItemsLbl', 'searchBtn', 'searchTxt']
        blnEmpty = uCommon.verifyVisible(page, pMyWishlist.com.noWishlistLbl)
        if blnEmpty == True: arrObj.extend(['noWishlistLbl'])
        else: uCommon.expectElemNotToBeVisible(page, pMyWishlist.com.noWishlistLbl)
        for item in arrObj: uCommon.waitElemToBeVisible(page, pMyWishlist.com.__dict__[item])
    
    @uCommon.ufuncLog
    def validateWishlistAndRemoveSameItem(page, strItemName):
        """ 
        Objective: Validate Wishlist page and remove item if the same item exists
            
        param strItemName: Item name
        returns: None
        Author: cgrapa_20230615
        """
        com.validateMyWishlist(page)
        blnItemExist = uCommon.verifyVisible(page, pMyWishlist.com.itemNameLbl(strItemName))
        if blnItemExist == True: com.removeItemOnMyWishlist(page, strItemName)
        else: uCommon.expectElemNotToBeVisible(page, pMyWishlist.com.itemNameLbl(strItemName))
    
    @uCommon.ufuncLog
    def validateAddedWishlistItem(page, strItemName, dictData):
        """ 
        Objective: Validate if item was successfully added to Wishlist
            
        param strItemName: Item name
        param dictData: strName, strBrand, strPrice
        returns: None 
        Author: cgrapa_20230615
        """
        uCommon.validateElemText(page, pMyWishlist.com.itemBrandLbl(strItemName), dictData['strBrand'])
        uCommon.validateElemText(page, pMyWishlist.com.itemNameLbl(strItemName), dictData['strName'])
        blnSaleLbl = uCommon.verifyVisible(page, pMyWishlist.com.itemSaleLbl(strItemName))
        if blnSaleLbl == True: uCommon.validateElemText(page, pMyWishlist.com.itemOriginalPriceLbl(strItemName), dictData['strPrice'])
        else: uCommon.validateElemText(page, pMyWishlist.com.itemDiscountedPriceLbl(strItemName), dictData['strPrice'])
    
    @uCommon.ufuncLog
    def validateRemovedWishlistItem(page, strItemName):
        """ 
        Objective: Validate if item is in My Wishlist page
            
        param strItemName: Item name
        returns: None
        Author: cgrapa_20230619
        """
        uCommon.waitElemNotToBeVisible(page, pMyWishlist.com.loadingSpinnerImg)
        uCommon.expectElemNotToBeVisible(page, pMyWishlist.com.itemNameLbl(strItemName))
    
    @uCommon.ufuncLog
    def clickItemAndValidatePdp(page, dictData):
        """ 
        Objective: Click item on Wishlist and validate PDP
            
        param dictData: strName, strBrand, strPrice
        returns: None
        Author: cgrapa_20230619
        """
        uCommon.waitAndClickElem(page, pMyWishlist.com.itemImg(dictData['strName']))
        uShop.pp.validateDetails(page, dictData)


        
    

