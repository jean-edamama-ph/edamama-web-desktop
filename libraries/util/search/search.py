from selenium.common.exceptions import NoSuchElementException
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

    @uCommon.funcLog
    def clickSearchBar(page):
        """ 
        Objective: Click the search bar header
        
        param: None
        returns: None
        Author: jatregenio_20240229
        """
        uCommon.waitAndClickElem(page, pCommon.header.searchForYourFavTxt)
        
    @uCommon.funcLog
    def validateRecentSearchesIfVisible(page, strValue):
        """ 
        Objective: Validate if previous search is existing in recent searches UI
        
        param strValue: Text
        returns: None
        Author: jatregenio_20240229
        """

        if uCommon.verifyVisible(page, pSearch.com.recentSearchLbl(strValue)) == False:
            NoSuchElementException
        
    @uCommon.funcLog
    def validateRecentSearchesSequence(page, intCtr, strValue):
        """ 
        Objective: Validate the sequence of the recent searches
        
        param intCtr: Integer
        param strValue: Text
        returns: None
        Author: jatregenio_20240229
        """
        if uCommon.verifyVisible(page, pSearch.com.recentSearchSequenceLbl(intCtr)) == False:
            NoSuchElementException
        else:
            uCommon.validateElemText(page, pSearch.com.recentSearchSequenceLbl(intCtr), strValue)




    
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
        uCommon.wait(page, 0.5)
        plp.validatePlpElem(page, strType)
            
    @uCommon.funcLog
    def validatePlpElem(page, strType):
        """ 
        Objective: validate the PLP elements
        
        param strType: brand|item|keyword
        returns: None
        Author: jatregenio_20240228
        """
        if strType == 'brand' or strType == 'keyword':
            arrObj = ['plpStatusLbl','colorSectionPnl', 'ageGroupSectionPnl', 'genderSectionPnl', 'brandSectionPnl', 'sortByLbl', 'relevanceBtn', 'priceFilterSectionPnl']
            for item in arrObj:
                uCommon.waitElemToBeVisible(page, pSearch.com.__dict__[item])          
                      
            arrObj = ['priceHeaderLbl', 'maxPriceLbl', 'minPesoSignLbl', 'maxPesoSignLbl', 'minPriceTxt', 'maxPriceTxt', 'applyBtn', 'colorHeaderLbl', 'ageGrpHeaderLbl',
                      'genderHeaderLbl', 'brandHeaderLbl']
            for item in arrObj:
                uCommon.waitElemToBeVisible(page, pSearch.flt.__dict__[item])
        else:
            arrObj = ['sortByLbl', 'relevanceBtn', 'priceFilterSectionPnl']
            for item in arrObj:
                uCommon.waitElemToBeVisible(page, pSearch.com.__dict__[item])     
            arrObj = ['priceHeaderLbl', 'minPriceLbl', 'maxPriceLbl', 'minPesoSignLbl', 'maxPesoSignLbl', 'minPriceTxt', 'maxPriceTxt', 'applyBtn']
            for item in arrObj:
                uCommon.waitElemToBeVisible(page, pSearch.flt.__dict__[item])
