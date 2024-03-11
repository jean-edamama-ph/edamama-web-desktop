import pytest
import allure
import libraries.data.regressionTestSuite.profile.myProfile as dRegMyProfile
import libraries.data.regressionTestSuite.loginAndSignUp.signup as dRegSignUp
import libraries.data.regressionTestSuite.cart.checkout as dRegCheckout

import libraries.util.appCommon.adminKpc as uAdminKpc
import libraries.util.appCommon.appComm as uAppComm
import libraries.util.common as uCommon
import libraries.util.profile.myProfile as uMyProfile
import libraries.util.profile.myBeans as uMyBeans
import libraries.data.common as dCommon
import libraries.util.shop as uShop
import libraries.util.cart as uCart
import libraries.util.checkOut as uCheckOut
import libraries.util.appCommon.signUp as uSignUp
import libraries.util.appCommon.email as uEmail
import libraries.util.tcTest as uTcTest

""" Author: abernal_20240227 Execution Time: 50s - 54s"""
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that 5 bean rewards will be auto-credited to the user when adds a child attribute')
@allure.step('To verify that 5 bean rewards will be auto-credited to the user when adds mama attribute.')
#test_ACQ_AUTO_1630_Credited_Bean_Rewards_in_Bean_History_From_Adding_Attributes_Via_Profile
def test_ACQ_AUTO_1633_Credited_Bean_Rewards_in_Bean_History_From_Adding_a_Child_Via_Profile(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.goToEdamamaURL(page)
    
    uCommon.log(0, '[Pre-condition started]: Create new account without adding attributes and child.')
    uSignUp.clickSignUp(page)
    uSignUp.validateSignUpPage(page)
    arrData = uSignUp.fillandContinueSignUpPage(page, dRegSignUp.AUTO1621.dictData)
    uSignUp.validateAndClickOKinAccountVerification(page)
    uEmail.loginToGmail(page)
    uEmail.clickFirstConfirmEmail(page, arrData)
    uEmail.clickYesThisIsMyEmail(page)
    newWindow = uCommon.switchToWindow(page)
    uSignUp.validateEmailVerificationPageAndClickStartShopping(newWindow)
    uCommon.log(0, '[Pre-condition Completed]: Account created.')
    
    uCommon.log(0, 'Step 2 - Navigate to My Profile page')
    uAppComm.com.navigateToProfileMenu(newWindow, dRegMyProfile.AUTO1621.strMyProfile)
    
    uCommon.log(0, '[AUTO-1621 Started]: Add child via Profile.')
    uCommon.log(0, 'Step 3 - Scroll to My Children section and click Add Another Child button.')
    uMyProfile.com.clickAddAChild(newWindow)
    uMyProfile.ac.addChildDetails(newWindow, dRegMyProfile.AUTO1621.newChildData)
    uMyProfile.ac.clickAndVerifyAddChild(newWindow, dRegMyProfile.AUTO1621.newChildData)
    uCommon.log(0, '[AUTO-1621 Completed]: Added child via Profile.')
    
    uCommon.log(0, '[AUTO-1624 Started]: Add attributes via Profile.')
    uCommon.log(0, 'Step 4 - Scroll to My Attributes and click Add More. Select mama attributes and click Submit.')
    uMyProfile.at.validateAndAddAttributes(newWindow, dRegMyProfile.AUTO1624.intAddAttributes)
    uCommon.log(0, '[AUTO-1624 Completed]: Add attributes via Profile.')
    
    uCommon.log(0, 'Step 5 - Navigate to My Beans page and verify that 5 beans was rewarded to the user for adding a child and attributes.')
    uMyProfile.com.clickMyBeansTab(newWindow)
    uMyBeans.com.verifyBeansRewardFromAddingChild(newWindow)
    uMyBeans.com.verifyBeansRewardFromAddingAttribute(newWindow)
    uCommon.log(0, 'Test Completed')
    
    
""" Author: abernal_20240227 Execution Time: 1.17 - 1.36s  """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that 5 bean rewards will be auto-credited to the user when after purchase.')
def test_ACQ_AUTO_1639_Credited_Bean_Rewards_in_Bean_History_From_Product_Purchase(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName1)
    
    uCommon.log(0, 'Step 2 - Select a product and add to bag. Proceed to checkout. Select a MOP and click Place Order.')
    strOrderID = uTcTest.validateE2EMOP(page, dRegCheckout.AUTO1639.dictData)
    
    uCommon.log(0, 'Step 3 - Copy the Order ID and navigate to the Order Module in the Admin Panel. Change status to Delivered.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.od.clickOrders(page)
    uCommon.waitAndClickElemText(page, strOrderID)
    window = uCommon.switchToWindow(page)
    uAdminKpc.od.od.pt.clickEdit(window)
    uAdminKpc.od.od.pt.clickAndSelectOrderStatus(window, 'Delivered')
    uAdminKpc.od.od.pt.clickUpdate(window)
    uCommon.closeWindow(page)
    
    uCommon.log(0, 'Step 4 - Navigate back to edamama site.')
    uAppComm.ln.goToEdamamaURL(page)
    uAppComm.com.navigateToProfileMenu(page, dRegCheckout.AUTO1639.strMyOrders)
    
    uCommon.log(0, 'Step 5 - Navigate to My Beans page and verify that 5 beans was rewarded to the user for adding a child and attributes.')
    uMyProfile.com.clickMyBeansTab(page)
    uMyBeans.com.verifyBeansRewardFromProductPurchase(page)
    uCommon.log(0, 'Test Completed')
    
    
""" Author: abernal_20240301 Execution Time: 1.34 - 1.41s """
@pytest.mark.regressionTestSuite()
@pytest.mark.acquiTestSuite()
@allure.step('To verify that 5 bean rewards will be auto-credited to the user when using beanback voucher.')
def test_ACQ_AUTO_1627_Credited_Bean_Rewards_in_Bean_History_From_Beanback_Voucher(page):
    uCommon.log(0, 'Step 1 - Open edamama website')
    uAppComm.ln.loginToEdamama(page, dCommon.user.strUserName2)
    
    uCommon.log(0, 'Step 2 - Select a product and add to bag. Proceed to checkout. Select a MOP and click Place Order.')
    strOrderID = uTcTest.validateE2EMOP(page, dRegCheckout.AUTO1627.dictData)
    
    uCommon.log(0, 'Step 3 - Copy the Order ID and navigate to the Order Module in the Admin Panel. Change status to Delivered.')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.od.clickOrders(page)
    uCommon.waitAndClickElemText(page, strOrderID)
    window = uCommon.switchToWindow(page)
    uAdminKpc.od.od.pt.clickEdit(window)
    uAdminKpc.od.od.pt.clickAndSelectOrderStatus(window, 'Delivered')
    uAdminKpc.od.od.pt.clickUpdate(window)
    uCommon.closeWindow(page)
    
    uCommon.log(0, 'Step 4 - Navigate back to edamama site.')
    uAppComm.ln.goToEdamamaURL(page)
    uAppComm.com.navigateToProfileMenu(page, dRegCheckout.AUTO1627.strMyOrders)
    
    uCommon.log(0, 'Step 5 - Navigate to My Beans page and verify that 5 beans was rewarded to the user for adding a child and attributes.')
    uMyProfile.com.clickMyBeansTab(page)
    uMyBeans.com.verifyBeansRewardFromBeanbackVoucher(page)
    uCommon.log(0, 'Test Completed')