import libraries.util.appCommon.adminKpc as uAdminKpc
import libraries.util.appCommon.appComm as uAppComm
import libraries.util.appCommon.email as uEmail
import libraries.util.appCommon.wms as uWms
import libraries.util.common as uCommon
import libraries.util.profile.myOrders as uMyOrders
import libraries.util.profile.myProfile as uMyProfile
import libraries.util.profile.mySubscription as uMySubscription
import libraries.util.checkOut as uCheckOut


# --------------- TEST TEMPLATE START ---------------#
""" End to end checkout via different mode of payment """
def validateE2EMOP(page, dictData, intStep = 3):
    uCommon.log(0, f'Step {intStep} - Select and click any product >> Click "Add to Bag" >> Click the bag icon')
    arrCartDetails = uCheckOut.checkOutItem(page, dictData["strItemName"], dictData["strType"])
    
    uCommon.log(0, f'Step {intStep + 1} - Select cash on delivery as payment method')
    uCheckOut.closeMobileVerificationModal(page)
    uCheckOut.selectModeOfPaymentAndBeansOrPromo(page, dictData, dictData["strMOP"], dictData["strBeansPromo"], dictData["strPromoCode"])
    
    uCommon.log(0, f'Step {intStep + 1} - Verify that the order id was displayed >> Take note of the order id >> Click "My Orders" page')
    arrCODetails = uCheckOut.validateCheckOutDetails(page, arrCartDetails)
    strOrderID =uCheckOut.clickPlaceOrderAndGetOrderID(page, dictData["strMOP"], dictData["strBeansPromo"])
    uCheckOut.clickMyOrders(page)
    
    uCommon.log(0, f'Step {intStep + 1} - Verify the details was correct')
    uMyOrders.validateMyOrderDetails(page, strOrderID, arrCartDetails, arrCODetails, dictData["blnCoupon"])
    
    if dictData["strType"] == 'ss':
        uAppComm.com.navigateToProfileMenu(page, 'my subscription')
        uMySubscription.com.validateDetails(page, arrCartDetails)
        
        uEmail.loginToGmail(page)
        uEmail.validateWeGotYourOrderEmail(page, strOrderID)
    uCommon.log(0, f'ORDER ID: {strOrderID}')
    return strOrderID

""" Check Checkout OIDs in Admin Panel > Orders Module """
def checkCheckoutOIDsInAdminPanel(page, dictData):
    uAppComm.com.navigateToProfileMenu(page, 'my profile')
    dictProfile = uMyProfile.com.getMyProfileDetails(page)
    strName = dictProfile['strName']

    uCommon.log(0, 'Step 2 - Select and click any product to purchase')
    strOrderID = validateE2EMOP(page, dictData, 2)

    if dictData["blnCancel"] == True:
        uCommon.log(0, 'Step 6 - Cancel Order')
        uMyOrders.cancelOrder(page, strOrderID)
    dicDetails = uMyOrders.getMyOrderDetails(page, strOrderID, dictData)

    uCommon.log(0, 'Step 7 - Copy the Order ID and navigate to the Order Module in the Admin Panel')
    uAppComm.ln.loginToAdminKPC(page)
    uAdminKpc.od.clickOrders(page)
    
    uCommon.log(0, 'Step 8 - Verify the result')  
    uAdminKpc.od.validateCustomerName(page, strOrderID, strName)
    uAdminKpc.od.validateDetails(page, strOrderID, dicDetails, dictData["blnCancel"])
    return strOrderID

""" Check Checkout OIDs in WMS """
def checkCheckoutOIDsInWMS(page, dictData):
    strOrderID = validateE2EMOP(page, dictData, 2)
    if dictData["blnCancel"] == True:
        uCommon.log(0, 'Step 6 - Search for the OID and click the cancel button')
        uMyOrders.cancelOrder(page, strOrderID)
    dicDetails = uMyOrders.getMyOrderDetails(page, strOrderID, dictData)

    uCommon.log(0, 'Step 7 - Copy the Order ID and navigate to the Order Module in WMS')
    uCommon.wait(page, 60) # wait 120 secs to sync order
    uAppComm.ln.loginToWMS(page)
    uWms.hoverToOrders(page)
    uWms.clickOrders(page)
    uWms.selectDPorWH(page, 'dropship')
    frame = uWms.switchToFrame(page)
    uCommon.wait(page, 10)
    uWms.clickfilter(frame, 'Order #')
    
    uCommon.log(0, 'Step 8 - Paste the OID in the Sale Order search field and enter. Verify the result')
    uWms.setFilter(frame, strOrderID)
    uCommon.wait(page, 2)
    uWms.clickApply(frame)
    uCommon.wait(page, 6)
    
    if dictData["blnCancel"] == True:
        uCommon.log(0, 'Step 9 - Verify the result for the Order Details')
        uWms.expectNoDataDisplay(frame)
        # uWms.clickCancelledHeader(frame)
        # uCommon.wait(page, 3)
        # uWms.clickfilter(frame, 'Order #')
        # uWms.setFilter(frame, strOrderID)
        # uCommon.wait(page, 1)
        # uWms.clickApply(frame)
        # uCommon.wait(page, 3)
        # uWms.validateStatus(frame, strOrderID, 'CANCELLED')
    else:
        uCommon.log(0, 'Step 9 - Expand the row')
        uCommon.clickElemText(frame, strOrderID, 2)
        uCommon.wait(page, 1)
        
        uCommon.log(0, 'Step 10 - Verify the result for the Order Details, Item Summary, Payment Summary, and Billing/Shipping Address')
        uWms.validateDetails(frame, dictData, dicDetails)
#--------------- TEST TEMPLATE END ---------------#