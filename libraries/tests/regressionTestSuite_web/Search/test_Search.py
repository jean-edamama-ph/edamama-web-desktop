import pytest
import allure

import libraries.util.appCommon.appComm as uAppComm
import libraries.util.common as uCommon
import libraries.util.search.search as uSearch
import libraries.data.regressionTestSuite.search.search as dSearch


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
@pytest.mark.thisTest()
@allure.step('Verify Entered Searched Keyword (without clicking Search) and the Search Drawer contents')
def test_FND_AUTO_1281_Search_003_Entering_Search_Keyword_without_clicking_Search(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - Enter a Keyword in the Search Bar')
    uSearch.com.setKeywordOnSearchBySendKeys(page, dSearch.AUTO1281.strKeyword)
    uCommon.wait(page, 3)
    
    uCommon.log(0, 'Step 3 - Check Search Results in the Search Drawer')
    uSearch.com.verifySearchDrawersIfVisible(page)
    uCommon.log(0, 'Test Complete')
    
    
    
    