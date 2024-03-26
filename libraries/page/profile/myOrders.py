import libraries.page.common.common as pCommon
import libraries.util.common as uCommon

class com:
    """COMMON"""
    myOrdersLbl = '//div[text()="My Orders"]'
    searchIconImg = '//app-search-header//mat-icon[text()="search"]'
    searchBtn = '//button//span[contains(text(),"Search")]'
    searchTxt = '//input[@data-placeholder="Search Items by Name, Order Id"]'
    allLbl = '//span[text()="All"]'
    filterListBtn = '//mat-icon[text()="filter_list"]'
    
    def myOrdersDataLbl(strOrderID, strColName):
        return f'//td[contains(text(),"{strOrderID}")]/ancestor::div[1]//td[{pCommon.go.getColIndex(strOrderID, strColName)}]'
    
    def parentTDOrderDetails(strOrderID):
        return f'//td[contains(text(),"{strOrderID}")]/ancestor::app-order-card'
    
    def ItemPictureImg(strParentDetails):
        return f'({strParentDetails}//img[@class="image"])[1]'
    
    def expressDeliveryLbl(strParentDetails):
        return f'({strParentDetails}//b[text()="Express Delivery"])[1]'
    
    def expressDeliveryIconBtn(strParentDetails):
        return f'({strParentDetails}//b[text()="Express Delivery"]/../..//img)[1]'
    
    def itemBrandLbl(strParentDetails):
        return f'{strParentDetails}//p[@class="brand"]'
    
    def itemNameLbl(strParentDetails):
        return f'{strParentDetails}//a[@class="name"]'
    
    def itemQuantityLbl(strParentDetails):
        return f'{strParentDetails}//span[@class="qty-label"]'
    
    def itemQuantityCountLbl(strParentDetails):
        return f'{strParentDetails}//span[@class="qty-count"]'
    
    def itemPriceLbl(strParentDetails):
        return f'{strParentDetails}//p[@class="total-price"]'
    
    def reviewsLbl(strParentDetails):
        return f'{strParentDetails}//p[contains(text(),"Review/s")]'
    
    def cancelBtn(strParentDetails):
        return f'({strParentDetails}//button[contains(text(),"Cancel Order")])[1]'
    
    def needHelpBtn(strParentDetails):
        return f'({strParentDetails}//a[contains(text(),"Need Help?")])[1]'
    
    def statusLbl(strParentDetails):
        return f'({strParentDetails}//span[contains(text(),"Status")])[1]'
    
    def statusDescLbl(strParentDetails):
        return f'({strParentDetails}//span[contains(@class,"status-text")])[1]'
    
    def editDeliveryDetailsBtn(strParentDetails):
        return f'{strParentDetails}//button[contains(@class,"edit-delivery-address-btn")]//img'
    
    oneTimeDeliveryChangeMsg = '//span[text()="Order Delivery Information can only be changed once per order"]'
    
    def couponUsedLbl(strOrderID):
        return f'//td[contains(text(),"{strOrderID}")]//..//..//th[contains(text(),"Coupon/s Used")]'
    
    
    
class co:
    """CANCEL ORDER"""
    xBtn = '//span[@class="mat_close btn-close"]'
    cancelOrderLbl = '//h2[text()="Cancel Order"]'
    cancelOrderDescLbl = '//p[contains(text(),"To provide you with a better experience in the future, please indicate your reason why you want to cancel.")]'
    changeOfShipLbl = '//h3[text()="Change of shipping info"]'
    changeOfDeliveryLbl = '//span[contains(text(),"Change of delivery adddress")]'
    changeOfDeliveryRdb = f'{changeOfDeliveryLbl}/..//span[@class="mat-radio-container"]'
    changeOfContactLbl = '//span[contains(text(),"Change of contact number")]'
    changeOfContactRdb = f'{changeOfContactLbl}/..//span[@class="mat-radio-container"]'
    changeMyMindLbl = '//h3[text()="Changed my mind"]'
    iDontWantTheItemLbl = '//span[contains(text(),"I don\'t want the item anymore")]'
    iDontWantTheItemRdb = f'{iDontWantTheItemLbl}/..//span[@class="mat-radio-container"]'
    iDecidedForAltProductLbl = '//span[contains(text(),"I decided for alternative product")]'
    iDecidedForAltProductRdb = f'{iDecidedForAltProductLbl}/..//span[@class="mat-radio-container"]'
    foundBetterDealLbl = '//h3[text()="Found a better deal"]'
    iFoundACheaperLbl = '//span[contains(text(),"I found a cheaper item elsewhere")]'
    iFoundACheaperRdb = f'{iFoundACheaperLbl}/..//span[@class="mat-radio-container"]'
    iForgotToApplyVoucherLbl = '//span[contains(text(),"I forgot to apply a voucher code")]'
    iForgotToApplyVoucherRdb = f'{iForgotToApplyVoucherLbl}/..//span[@class="mat-radio-container"]'
    iFoundFromAnotherSellerLbl = '//span[contains(text(),"I found a cheaper item from another seller")]'
    iFoundFromAnotherSellerRdb = f'{iFoundFromAnotherSellerLbl}/..//span[@class="mat-radio-container"]'
    changePaymentMethodLbl = '//span[contains(text(),"Change payment method")]'
    changePaymentMethodRdb = f'{changePaymentMethodLbl}/..//span[@class="mat-radio-container"]'
    changeCombineOrderLbl = '//span[contains(text(),"Change/combine order")]'
    changeCombineOrderRdb = f'{changeCombineOrderLbl}/..//span[@class="mat-radio-container"]'
    deliveryTimeTooLongLbl = '//span[contains(text(),"Delivery time is too long")]'
    deliveryTimeTooLongRbd = f'{deliveryTimeTooLongLbl}/..//span[@class="mat-radio-container"]'
    sellerRequestToCancelLbl  = '//span[contains(text(),"Seller request to cancel")]'
    sellerRequestToCancelRbd = f'{sellerRequestToCancelLbl}/..//span[@class="mat-radio-container"]'
    duplicateOrderLbl = '//span[contains(text(),"Duplicate order")]'
    changeCombineOrderRdb = f'{duplicateOrderLbl}/..//span[@class="mat-radio-container"]'
    shippingCostTooHighLbl = '//span[contains(text(),"Shipping cost is too high")]'
    shippingCostTooHighRdb = f'{shippingCostTooHighLbl}/..//span[@class="mat-radio-container"]'
    OthersLbl = '//span[contains(text(),"Others")]'
    OthersRdb = f'{OthersLbl}/..//span[@class="mat-radio-container"]'
    writeMsgHereTxt = '//textarea[@placeholder="Write your message here..."]'
    characterLimitLbl = '//p[contains(text(),"100")][text()="character limit"]'
    toContinueCancellationLbl = '//p[contains(text(),"To continue with your cancellation, please tap the button below.")]'
    cancelOrderBtn = '//section[@class="order-cancellation-container"]//button[contains(text(),"Cancel Order")]'





class di:
    """DELIVER INFORMATION"""
    addNewAddressBtn = '//button[normalize-space(text())="Add New Address"]'
    parentDIVName = '//div[@class="full-name-wrapper"]'
    updateDeliveryInfoBtn = '//button[text()=" Update Delivery Information "]'
    
    confirmationAddressChangeLbl = '//h3[text()="Confirmation of Address Change"]'
    confirmBtn = '//button[text()="Confirm"]'
    orderUpdateDelAddSuccessMsg = '//span[text()="Order Update Delivery Address is Successful"]'

    
    class na:
        """NEW ADDRESS"""
        newAddressLbl = '//h2[text()="New Address"]'
        firstNameTxt = '//input[@formcontrolname="firstName"]'
        lastNameTxt = '//input[@formcontrolname="lastName"]'
        mobileNumberTxt = '//input[@formcontrolname="phoneNumber"]'
        parentDIVListBox = '//div[@role="listbox"]'
        provinceDistrictLbl = '//label[text()="Province/District"]'
        provinceDistrictDownIconBtn = f'{provinceDistrictLbl}/..//div[contains(@class,"mat-select-arrow")]/div'
        searchTxt = '//input[@data-placeholder="Search"]'
        cityLbl = '//label[text()="City"]'
        cityDownIconBtn = f'{cityLbl}/..//div[contains(@class,"mat-select-arrow")]/div'
        barangayVillageLbl = '//label[text()="Barangay/Village"]'
        barangayVillageDownIconBtn = f'{barangayVillageLbl}/..//div[contains(@class,"mat-select-arrow")]/div'
        zipCodeTxt = '//input[@formcontrolname="zipCode"]'
        lotUnitStreetTxt = '//input[@formcontrolname="landmark"]'
        landmarkTxt = '//textarea[@formcontrolname="buildingNumber"]'
        addNewAddressBtn = f'{newAddressLbl}/../../..//button[text()=" Add New Address "]'
        addressAddedSuccessMsg = '(//span[text()="Address added successfully."])[1]'