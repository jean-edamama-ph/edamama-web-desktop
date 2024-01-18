import pytest
import allure

import libraries.data.common as dCommon
import libraries.data.deploymentChecklist as dDepChkLst

import libraries.util.appCommon.adminKpc as uAdminKpc
import libraries.util.appCommon.appComm as uAppComm
import libraries.util.appCommon.email as uEmail
import libraries.util.common as uCommon
import libraries.util.tcTest as uTcTest


""" Author: ccapistrano_20230404 Execution Time: 58s - 1m 22s """
@pytest.mark.RegPrep()
@pytest.mark.smokeTesting()
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify that user can purchase and pay using Cash On Delivery')
def test_AUTO_260_Test_Purchase_COD(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName1)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO260.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230412 Execution Time: 1m 5s - 1m 24s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify that user can purchase and pay using Cash On Delivery and available beans')
def test_AUTO_265_Test_Purchase_COD_plus_beans(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName2)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO265.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230412 Execution Time: 1m 15s - 1m 22s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify that user can purchase and pay using Cash On Delivery and applied coupon')
def test_AUTO_270_Test_Purchase_COD_plus_1_edamama_Coupon(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName3)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO270.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230413 Execution Time: 1m 5s - 1m 11s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verifying that user can purchase and pay using Cash On Delivery with applied BEANBACK COUPON')
def test_AUTO_275_Test_Purchase_COD_plus_BEANBACK_COUPON(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName4)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO275.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230413 Execution Time: 1m 9s - 1m 21s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify that user can purchase and pay using Cash On Delivery with applied brand and edamama coupon')
def test_AUTO_280_Test_Purchase_COD_plus_1_Brand_plus_1_Edamama_coupon(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName5)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO280.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230418 Execution Time: 1m 23s - 1m 31s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verifying that user can purchase and pay using CC')
def test_AUTO_285_Test_Purchase_CC(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName6)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO285.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230418 Execution Time: 1m 2s - 1m 10s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verifying that user can purchase and pay using CC + beans')
def test_AUTO_290_Test_Purchase_CC_plus_beans(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName7)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO290.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230418 Execution Time: 1m 27s - 1m 46s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verifying that user can purchase and pay using CC with applied Brand coupon')
def test_AUTO_295_Test_Purchase_CC_Brand_Coupon(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName8)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO295.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230414 Execution Time: 57s - 1m 34s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verifying that user can purchase and pay using GCASH')
def test_AUTO_300_Test_Purchase_GCASH(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName9)

    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO300.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230414 Execution Time: 49s - 1m 26s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify that the user should be able to checkout with using gcash and their available beans')
def test_AUTO_305_Test_Purchase_GCASH_plus_beans(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName10)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO305.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230414 Execution Time: 1m 14s - 1m 26s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify that the user should be able to checkout with using gcash and a beanback coupon')
def test_AUTO_310_Test_Purchase_GCASH_plus_BEANBACK_COUPON(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName1)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO310.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230414 Execution Time: 1m 11s - 1m 29s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify that the user should be able to checkout with using gcash and adding a brand coupon. Brand coupon should only be used for items from the brand')
def test_AUTO_315_Test_Purchase_GCASH_plus_Brand_coupon(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName2)

    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO315.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230419 Execution Time: 1m 9s - 1m 14s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify that the user should be able to checkout with using GrabPay')
def test_AUTO_320_Test_Purchase_GrabPay(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName3)

    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO320.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230419 Execution Time: 59s - 1m 12s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify that the user should be able to checkout with using GrabPay and their available beans')
def test_AUTO_325_Test_Purchase_GrabPay_plus_beans(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName4)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO325.dictData)
    uCommon.log(0, 'Test case completed')
    

""" Author: ccapistrano_20230419 Execution Time: 1m 27s - 1m 30s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify that the user should be able to checkout with using gcash and adding a coupon')
def test_AUTO_330_Test_Purchase_GrabPay_plus_coupon(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName5)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO330.dictData)
    uCommon.log(0, 'Test case completed')
    
    
""" Author: ccapistrano_20230420 Execution Time: 1m 33s - 1m 36s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify that the user should be able to checkout with using Maya')
def test_AUTO_335_Test_Purchase_Maya(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName6)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO335.dictData)
    uCommon.log(0, 'Test case completed')
    

""" Author: ccapistrano_20230420 Execution Time: 1m 12s - 1m 25s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify that the user should be able to checkout with using Maya and their available bean')
def test_AUTO_384_Test_Purchase_Maya_plus_beans(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName7)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO384.dictData)
    uCommon.log(0, 'Test case completed')


""" Author: ccapistrano_20230420 Execution Time: 1m 22s - 1m 39s """
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify if user should be able to checkout using Maya and with Maya Coupon')
def test_AUTO_389_Test_Purchase_Maya_plus_Maya_coupon(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName8)
    
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO389.dictData)
    uCommon.log(0, 'Test case completed')
    

""" Author: ccapistrano_20230327 Execution Time: 2m 2s """
@pytest.mark.RegPrep()
@pytest.mark.sanityTesting()
@pytest.mark.deploymentChecklist()
@allure.step('Verify if user can Subscribe to a product')
def test_AUTO_412_User_subscribe_to_a_product_COD(page):
    uCommon.log(0, 'Step 1 to 2 - Go to Edamama website/App >> Login your credentials')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName9)
    
    uCommon.log(0, '[Precondtion Started] - Cancel All Order By Username')
    uAdminKpc.sc.cancelOrdersByUserName(page)
    uCommon.log(0, '[Precondtion Completed] - All orders were successfully cancelled')
    
    uAppComm.ln.goToEdamamaURL(page)
    uTcTest.validateE2EMOP(page, dDepChkLst.AUTO412.dictData)
    uCommon.log(0, 'Test case completed')   