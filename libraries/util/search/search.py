import libraries.page.common.common as pCommon
import libraries.util.common as uCommon
import libraries.util.appCommon.appComm as uAppComm

import libraries.util.shop as uShop
import libraries.page.search.search as pSearch

class com:
    """COMMON"""
    
    @uCommon.funcLog
    def setKeywordOnSearchBySendKeys(page, strKeyword):
        """ 
        Objective: Set keyword to be searched via sendkeys
        
        param strKeyword: Text 
        returns: None
        Author: jatregenio_20240219
        """
        uCommon.waitElemToBeVisible(page, pCommon.header.searchForYourFavTxt)
        uCommon.clickElem(page, pCommon.header.searchForYourFavTxt)
        for item in strKeyword:
            uCommon.sendKeys(page, item)
            
    @uCommon.funcLog
    def validateSearchDrawersIfVisible(page):
        """ 
        Objective: Verify if search drawers will be visible once keywords were set
        
        param: None
        returns: None
        Author: jatregenio_20240219
        """
        uCommon.waitElemToBeVisible(page, pSearch.com.shopDrawerPnl)
        uCommon.waitElemToBeVisible(page, pSearch.com.discoverDrawerPnl)
        

class plp:
    """SEARCH PRODUCT LISTING PAGE"""
    
    @uCommon.funcLog
    def searchAndValidatePlpElem(page, strType, strValue):
        """ 
        Objective: Search an by item name or brand and validate the PLP elements
        
        param strType: 'item' | 'brand'
        param strValue: Product to search
        returns: None
        Author: jatregenio_20240219
        """
        uShop.sp.searchAndValidateName(page, strType, strValue)
        arrObj = ['plpStatusLbl','colorSectionPnl', 'ageGroupSectionPnl', 'genderSectionPnl', 'brandSectionPnl', 'sortByLbl', 'relevanceBtn']
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pSearch.com.__dict__[item])

