import pytest
import allure

import libraries.util.appCommon.appComm as uAppComm
import libraries.util.common as uCommon
import libraries.util.shop as uShop
import libraries.data.regressionTestSuite.subscribeAndSave.sns as dSnS


""" Author: jatregenio_20240318 Execution Time: 15s - 17s """
@pytest.mark.regressionTestSuite()
@pytest.mark.subAndSaveTestSuite()
@allure.step('Verify that subscribe and save products should be displayed once user navigates to More in Homepage.')
def test_SNS_AUTO_1512_TC01_SHOP_FILTER_Display_List_of_SnS_Products_Subscribe_and_Save_Section_More(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - In Shop tab, browse the Homepage then search for "Subscribe and Save" section.Tap "More >"')
    uShop.sp.validateSubscribeAndSave(page)
    uShop.sp.clickSSMoreBtn(page)
    uCommon.log(0, 'Test Completed.')
    
""" Author: jatregenio_20240318 Execution Time: 15s - 17s """
@pytest.mark.regressionTestSuite()
@pytest.mark.subAndSaveTestSuite()
@allure.step('Verify that subscribe and save products should be displayed once user navigates to Right Arrow in Homepage')
def test_SNS_AUTO_1515_TC02_SHOP_FILTER_Display_List_of_SnS_Products_Subscribe_and_Save_Section_Right_Arrow(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - In Shop tab, browse the Homepage then search for "Subscribe and Save" section.Tap the "right arrow" (->) icon')
    uShop.sp.validateSubscribeAndSave(page)
    uShop.sp.clickSSArrowForward(page)
    uCommon.log(0, 'Test Completed.')
    
""" Author: jatregenio_20240318 Execution Time: 30s - 32s """
@pytest.mark.regressionTestSuite()
@pytest.mark.subAndSaveTestSuite()
@allure.step('Verify that subscribe and save products should be displayed once user search for a specific product.')
def test_SNS_AUTO_1521_TC04_SHOP_FILTER_Display_List_of_SnS_Products_Search_for_Specific_Product(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, 'Step 2 - Go to search textbox. Enter a specific subscribe and save product')
    uShop.sp.searchAndValidateName(page, dSnS.AUTO1521.strTypeItem, dSnS.AUTO1521.strName)
    
    uCommon.log(0, 'Step 3 - Verify that "Subscribe and Save" banner is displayed highlighted in purple.')
    uShop.sp.validateSnSBadge(page, dSnS.AUTO1521.strName)
    
    uCommon.log(0, 'Step 4 - Tap the product and verify if PDP is displayed.')
    uShop.sp.clickProdCard(page, dSnS.AUTO1521.dictdata)
    uCommon.log(0, 'Test Completed.')