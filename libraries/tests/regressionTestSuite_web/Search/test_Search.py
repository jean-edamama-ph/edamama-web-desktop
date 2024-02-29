import pytest
import allure

import libraries.util.appCommon.appComm as uAppComm
import libraries.util.common as uCommon
import libraries.util.search.search as uSearch
import libraries.data.regressionTestSuite.search.search as dSearch
import libraries.data.common as dCommon


""" Author: jatregenio_20240219 Execution Time: 33s - 35s """
@pytest.mark.regressionTestSuite()
@pytest.mark.findTestSuite()
@allure.step('Verify Search Bar UI in Shop Homepage and if clickable')
def test_FND_AUTO_1275_Search_001_Search_Bar_UI_in_Shop_Homepage(page):
     uCommon.log(0, 'Step 1 - Open edamama website')
     uAppComm.ln.goToEdamamaURL(page)
     
     uCommon.log(0, 'Step 2 - Check Search Bar UI in Shop Homepage and search for any products or brands')
     uSearch.plp.searchAndValidatePlpElem(page, dSearch.AUTO1275.strTypeItem, dSearch.AUTO1275.strItemName)
     uSearch.plp.searchAndValidatePlpElem(page, dSearch.AUTO1275.strTypeBrand, dSearch.AUTO1275.strBrand)
     uCommon.log(0, 'Test Completed.')


""" Author: jatregenio_20240219 Execution Time: 22s - 24s """
@pytest.mark.regressionTestSuite()
@pytest.mark.findTestSuite()
@allure.step('Verify Entered Searched Keyword (without clicking Search) and the Search Drawer contents')
def test_FND_AUTO_1281_Search_003_Entering_Search_Keyword_without_clicking_Search(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - Enter a Keyword in the Search Bar')
    uSearch.com.setKeywordOnSearchBySendKeys(page, dSearch.AUTO1281.strKeyword)
    uCommon.wait(page, 3)
    
    uCommon.log(0, 'Step 3 - Check Search Results in the Search Drawer')
    uSearch.com.validateSearchDrawersIfVisible(page)
    uCommon.log(0, 'Test Complete')


""" Author: jatregenio_20240228 Execution Time: 44s - 45s """
@pytest.mark.regressionTestSuite()
@pytest.mark.findTestSuite()
@allure.step('Verify if User will be redirected to Search Results PLP - Verify if Recent Searched Keywords is displayed in the Search Drawer')
def test_FND_AUTO_1293_Search_007_Search_for_a_Product_with_Discount_via_clicking_Search_Button(page):
#test_FND_AUTO_1693_Recent_Searches_Section_UI

    uCommon.log(0, 'Step 1 - Go to Edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName1)
    
    uCommon.log(0, '[AUTO-1293 Started] - Search for a Product with Discount via clicking Search Button')
    uCommon.log(0, 'Step 2 - Enter a Product Name or Brand Keyword with Discount in the Search Bar')
    uSearch.plp.searchAndValidatePlpElem(page, dSearch.AUTO1293.strTypeItem, dSearch.AUTO1293.strItemName)
    uSearch.com.clickSearchBar(page)
    uSearch.plp.searchAndValidatePlpElem(page, dSearch.AUTO1293.strTypeBrand, dSearch.AUTO1293.strBrand)
    uSearch.com.clickSearchBar(page)
    uSearch.plp.searchAndValidatePlpElem(page, dSearch.AUTO1293.strTypeKeyword, dSearch.AUTO1293.strKeyword)
    uSearch.com.clickSearchBar(page)
    uCommon.log(0, 'AUTO-1293 - Test Completed.')
    
    uCommon.log(0, '[AUTO-1693 Started] - Recent Searches Section UI')
    uCommon.log(0, 'Step 3 - Click Search Bar')
    uSearch.com.clickSearchBar(page)
    uCommon.wait(page, 1)
    
    uCommon.log(0, 'Step 4 - Check if the Recent Searched Keywords is displayed')
    uSearch.com.validateRecentSearchesIfVisible(page, dSearch.AUTO1293.strItemName)
    uSearch.com.validateRecentSearchesIfVisible(page, dSearch.AUTO1293.strBrand)
    uSearch.com.validateRecentSearchesIfVisible(page, dSearch.AUTO1293.strKeyword)
    
    
    uCommon.log(0, 'Step 5 - Check Sequence of Latest to Oldest Recent Searched Keyword follows from Left to Right')
    uSearch.com.validateRecentSearchesSequence(page, dSearch.AUTO1293.intSeqKeyword, dSearch.AUTO1293.strKeyword)
    uSearch.com.validateRecentSearchesSequence(page, dSearch.AUTO1293.intSeqBrand, dSearch.AUTO1293.strBrand)
    uSearch.com.validateRecentSearchesSequence(page, dSearch.AUTO1293.intSeqItem, dSearch.AUTO1293.strItemName)
    uCommon.log(0, '[AUTO-1693] - Test Completed')
    