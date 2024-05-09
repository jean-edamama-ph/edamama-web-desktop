addBtn = '//mat-icon[text()="add"]'
dateTodayLbl = '//div[contains(@class,"today")]'
spotLightTgl = '//mat-slide-toggle[@formcontrolname="isOnSpotlight"]//span[@class="mat-slide-toggle-bar"]'
allIsFeaturedDdb = '//table//div[contains(@class,"mat-select-arrow-wrapper")]'
yesBtn = '//mat-option/span[text()="Yes"]'
noBtn = '//mat-option/span[text()="No"]'
progressBarElm = '(//div[@class="loader-overlay"][@hidden=""])[1]'
searchIconBtn = '//mat-icon[text()="search"]'


class lp:
    """LEFT PANEL"""
    productsLbl = '//h3[text()="Products"]/../../..'
    ordersLbl = '//h3[text()="Orders"]/../../..'
    flashSaleLbl = '//h3[text()="Flash Sale"]/../../..'
    discountsSchedulerLbl = '//h3[text()="Discounts Scheduler"]/../../..'
    curatedProductsLbl = '//h3[text()="Curated Products"]/../../..'
    subscriptionLbl = '//h3[text()="Subscription"]/../../..'
    customerLbl = '//h3[text()="Customers"]/../../..'
    rewardsLbl = '//h3[contains(text(),"Rewards")]'
    
    
    
    
    
class pl:
    """PRODUCTS LISTING"""
    addBtn = '//button/span[text()=" Add "]'
    listingLbl = '//h3[text()="Listing"]'
    listingIconBtn = '//img[@src="/assets/images/list.svg"]'
    searchTxt = '//input[@placeholder="Search By Product Name, Brand,Vendor, SKU"]'
    searchIconBtn = searchIconBtn
    editIconBtn = '//mat-icon[text()=" edit"]'
    deleteIconBtn = '//mat-icon[text()=" delete"]'
    blockUnblockIconBtn = '//mat-icon[contains(@class,"mat-tooltip-trigger")]' #'//mat-icon[text()=" block "]'
    tableRowElm = '//tbody[@role="rowgroup"]/tr'
    noRecordFoundLbl = '//span[text()="No Record Found"]'
    publishedIcon = '//tbody//mat-icon[text()="done"]'
    unpublishedIcon = '//tbody//mat-icon[text()="close"]'
    
    confirmationlbl = '//h1[text()="Confirmation"]'
    deleteMsg = '//p[text()="Do you want to delete this product? "]'
    blockMsg = '//p[text()="Do you want to block this product? "]'
    unblockMsg = '//p[text()="Do you want to unblock this product? "]'
    noBtn = '//span[text()=" No "]'
    yesBtn = '//span[text()=" Yes "]'
    deleteSuccessMsg = '//span[text()="Product has been deleted successfully"]'
    blockSuccessMsg = '//span[text()="Product has been blocked successfully"]'
    unblockSuccessMsg = '//span[text()="Product has been unblocked successfully"]'
    
    
    class bi:
        """BASIC INFORMATION"""
        productbasicInfoLbl = '//h2[text()="Product basic Information"]'
        productNameTxt = '//input[@formcontrolname="name"]'
        updateAndContinueBtn = '(//button//span[contains(text(),"Update & Continue")])[1]'
        productSuccessMsg = '//span[text()="Product has been updated successfully"]'
        nextBtn = f'{productbasicInfoLbl}/../../../..//span[text()=" Next "]'
        selectCategoryLbl = '//div/span[text()="Select by Category or Subcategory..."]'
        searchCategoryTxt = '//input[@placeholder="Search by Category or Subcategory..."]'
        selectBrandLbl = '//div/span[text()="Select Brand"]'
        searchTxt = '//input[@data-placeholder="Search..."]'
        selectVendorLbl = '//div/span[text()="Select Vendor"]'
        bundleByLbl = '//mat-label[text()="Bundle Buy"]/..//span[contains(@class,"mat-select-placeholder")]'
        selectBrandLbl = '//div/span[text()="Select Brand"]'
        attributesLbl = '//mat-label[text()="Select Attributes"]/..//span[contains(@class,"mat-select-placeholder")]'
        descriptionTxt = '//ckeditor[@formcontrolname="description"]//div[@role="textbox"]'
        specificationTxt = '//ckeditor[@formcontrolname="specifications"]//div[@role="textbox"]'
        saveAndContinueBtn = '//span[text()=" Save & Continue "]'
        addedSuccessMsg = '//span[text()="Product has been added successfully"]'
        
        
    class cv:
        """COLOR & VARIANTS"""
        colorSelectionLbl = '//h2[text()="Color Selection"]'
        colorLbl = '//mat-label[text()="Color"]'
        selectColorlbl = '//span[text()="Select Color"]'
        searchTxt = '//input[@placeholder="Search..."]'
        colorAddIconBtn = f'{colorLbl}/../../..//img[@class="add_icon"]'
        selectBtn = '//button/span[text()="Select"]'
        addColorBtn = '//button/span[text()="Add Color"]'
        updateAndContinueBtn = f'{colorSelectionLbl}/../../../..//button/span[contains(text(),"Update & Continue")]/..'
        productSuccessMsg = '//span[text()="Product has been updated successfully"]'
        def deleteIconBtn(strColor):
            return f'//img[contains(@src,"{strColor}")]/../../../..//img[@class="delete_item"]'
        yesBtn = '//h1[text()="Confirmation"]/..//span[text()=" Yes "]'
        colorOptRemoveMsg = '//span[text()="Color Option Removed Successfully!"]'
        nextBtn = f'{colorSelectionLbl}/../../../..//span[text()="Next"]' 
        
        variantProductOptLbl = '//h2[text()="Variant (Product Option)"]'
        selectVariantLbl = '//span[text()="Select Variant"]'
        searchTxt = '//input[@data-placeholder="Search..."]'
        selectTypeLbl = '//span[text()="Select Type"]'
        selectTypeOptionsLbl = f'({variantProductOptLbl}/../..//*[contains(@id,"mat-select-value")]/span)[3]'
        addVariantBtn = '//span[text()="Add Variant"]'
        variantSuccessMsg = '//span[text()="Variant Added Successfully!"]'
        
        filterCategoryOptLbl = '//h2[text()="Filter (Category Option)"]'
        selectFiltersLbl = '//span[text()="Select Filters"]'
        filtersOptionsLbl = f'({filterCategoryOptLbl}/../..//*[contains(@id,"mat-select-value")]/span)[2]'
        addFilterBtn = '//span[text()="Add Filters"]'
        filtersSuccessMsg = '//span[text()="Filter Added Successfully!"]'
  
    
    class sp:
        """STOCK & PRICE"""
        publishedLbl = '//span[text()="Published"]'
        publishedTgl = f'{publishedLbl}/..//span[@class="mat-slide-toggle-bar"]'
        def mrpPriceTxt(strColor):
            return f'//p[contains(text(),"{strColor}")]/../..//input[@formcontrolname="price"]'
        updateAndContinueBtn = f'{publishedLbl}/../../../..//button/span[contains(text(),"Update & Continue")]/..'
        productSuccessMsg = '//span[text()="Product has been updated successfully"]'
        
        
    class at:
        """ATTIRBUTES"""    
        logisticsAttributesLbl = '//legend[text()="Logistics Attributes"]'
        saveBtn = f'{logisticsAttributesLbl}/../..//button/span[contains(text(),"Save")]'
        productSuccessMsg = '//span[text()="Product has been updated successfully"]'
        
    
    
    
    
class ol:
    """ORDERS LISTING"""
    def orderIDValue(strorderID):
        return f'//span[contains(text(),"{strorderID}")]/../..//td[contains(@class,"orderNumber")]/span'

    def customerNameValue(strorderID):
        return f'//span[contains(text(),"{strorderID}")]/../..//td[contains(@class,"cdk-column-name")]/span'
    
    def quantityValue(strorderID):
        return f'//span[contains(text(),"{strorderID}")]/../..//td[contains(@class,"totalQuantity")]'
    
    def paymentMethodValue(strorderID):
        return f'//span[contains(text(),"{strorderID}")]/../..//td[contains(@class,"paymentMethod")]'
    
    def shipPriceValue(strorderID):
        return f'//span[contains(text(),"{strorderID}")]/../..//td[contains(@class,"shippingCharge")]'
    
    def totalPriceValue(strorderID):
        return f'//span[contains(text(),"{strorderID}")]/../..//td[contains(@class,"subTotal")]'
    
    def returnCancelValue(strorderID):
        return f'//span[contains(text(),"{strorderID}")]/../..//td[contains(@class,"finalStatus")]/span'
    
    massUploadBtn = '//button/span[text()=" Mass Upload "]'
    selectFileBtn = '//button/span[text()=" Select File "]'
    uploadOrderCancellationBtn = '//button/span[text()=" Upload Order Cancellation "]'
    massCancellationSuccessMsg = '//span[text()="Mass Cancellation of Orders is Successful"]'


    class od:
        """ORDER"""
        deliveryDetailslbl = '//h3[text()="Delivery Details"]'
        receiverLbl = f'{deliveryDetailslbl}/../..//span[contains(text(),"Receiver")]'
        receiverValueLbl = f'{receiverLbl}/..//span[2]'
        regionLbl = f'{deliveryDetailslbl}/../..//span[contains(text(),"Region")]'
        regionValueLbl = f'{regionLbl}/..//span[2]'
        cityLbl = f'{deliveryDetailslbl}/../..//span[contains(text(),"City")]'
        cityValueLbl = f'{cityLbl}/..//span[2]'
        barangayLbl = f'{deliveryDetailslbl}/../..//span[contains(text(),"Barangay")]'
        barangayValueLbl = f'{barangayLbl}/..//span[2]'
        streetLbl = f'{deliveryDetailslbl}/../..//span[contains(text(),"Street")]'
        streetValueLbl = f'{streetLbl}/..//span[2]'
        deliveryNotesLbl = f'{deliveryDetailslbl}/../..//span[contains(text(),"Delivery Notes")]'
        deliveryNotesValueLbl = f'{deliveryNotesLbl}/..//span[2]'
        zipCodeLbl = f'{deliveryDetailslbl}/../..//span[contains(text(),"Zip Code")]'
        zipCodeValueLbl = f'{zipCodeLbl}/..//span[2]'
        
        class pt:
            """PRODUCT TABLE"""
            productTableElm = '//table[@class="product_table"]'
            editIconBtn = f'{productTableElm}//img[@src="assets/images/pencil.svg"]/..'
            # Order Status
            selectStatusLbl = '//span[text()="Select Status"]'
            trackingUrlLbl = '//textarea[@placeholder="Order Tracking Url..."]'
            trackingNumberLbl= '//textarea[@placeholder="Order tracking Number.."]'
            courierLbl= '//textarea[@placeholder="Courier"]'
            updateBtn = '//button/span[text()="Update"]'
            statusUpdatedSuccessMsg = '//span[text()="Status Updated Successfully!"]'
            


class fs:
    """FLASH SALE"""
    addBtn = addBtn
    def deleteIconBtn(strName):
            return f'(//td[contains(text(),"{strName}")]/..//mat-icon[text()=" delete"])[1]'
    yesBtn = '//button/span[text()=" Yes "]'
    sucCanceledMsg = '//span[text()="Flash sale cancelled successfully !"]'
    sucFlashSaleMsg = '//span[text()="Flash Sale added successfully!"]'


    class ap:
        """ADD PAGE"""
        nameTxt = '//input[@formcontrolname="name"]'
        dateLbl = '//input[@data-placeholder="Date"]'
        calendarIconBtn = '//button[@aria-label="Open calendar"]'
        dateTodayLbl = dateTodayLbl
        timeDdb = '(//mat-select[@formcontrolname="timeInterval"]//div[contains(@class,"select-arrow")])[1]'
        timeActiveLbl = '//mat-option[contains(@class,"active")]'
        spotLightTgl = spotLightTgl
        uploadSkuBtn = '//button//span[text()=" Upload SKU\'s "]'
        allIsFeaturedDdb = allIsFeaturedDdb
        def isFeaturedDdb(intIndex):
            return f'(//table//div[contains(@class,"mat-select-arrow-wrapper")])[{intIndex}]/../..'
        yesBtn = yesBtn
        noBtn = noBtn
        addBtn = '//mat-dialog-container//button/span[text()=" Add "]'
        
    
    
    
    
class ds:
    """DISCOUNTS SCHEDULER"""
    addBtn = addBtn
    def deleteIconBtn(strName):
            return f'//td[contains(text(),"{strName}")]/..//mat-icon[text()=" delete"]'
    def editIconBtn(strName):
            return f'//td[contains(text(),"{strName}")]/..//mat-icon[text()=" edit"]'
    yesBtn = '//button/span[text()=" Yes "]'
    sucStatusUpdateMsg = '//span[text()="Status updated successfully !"]'
    sucSchedulerMsg = '//span[text()="Scheduler timed successfully !"]'
    
    
    class ap:
        """ADD PAGE"""
        schedulerNameTxt = '//input[@formcontrolname="name"]'
        selectDiscountTypeDdb = '(//mat-select[@formcontrolname="discountTypeSku"]//div[contains(@class,"select-arrow")])[1]'
        optionRSLbl = '//span[@class="mat-option-text"][text()="RS "]'
        optionSNSLbl = '//span[@class="mat-option-text"][text()="SNS "]'
        validFromCalIconBtn = '//input[@data-placeholder="Valid From"]/../..//button[@aria-label="Open calendar"]'
        validUntilCalIconBtn = '//input[@data-placeholder="Valid Until "]/../..//button[@aria-label="Open calendar"]'
        dateTodayLbl = dateTodayLbl
        addHoursIconBtn = '(//button//mat-icon[text()="expand_less"])[1]'
        addMinutesIconBtn = '(//button//mat-icon[text()="expand_less"])[2]'
        checkIconBtn = '//button//mat-icon[text()="done"]/../..'
        amPmBtn = '//td[@class="ngx-mat-timepicker-meridian ng-star-inserted"]//button/span[@class="mat-button-wrapper"]'
        spotLightTgl = spotLightTgl
        uploadBtn = '//button//label[text()=" Upload "]'
        allIsFeaturedDdb = allIsFeaturedDdb
        def isFeaturedDdb(intIndex):
            return f'(//table//div[contains(@class,"mat-select-arrow-wrapper")])[{intIndex}]/../..'
        yesBtn = yesBtn
        noBtn = noBtn
        firstProductNameYesLbl = '(//span[text()="Yes"]/ancestor::tr/td/span)[1]'
        firstTotalDcPerLbl = '(//span[text()="Yes"]/ancestor::tr/td/span)[5]'
        firstPriceOrigLbl = '(//span[@class="discounted"])[1]'
        firstPriceDiscountedLbl = '((//span[@class="discounted"])[1]/..//span)[2]'
        addBtn = '//mat-dialog-container//button/span[text()=" Add "]'
        
        
        
        
        
class cp:
    """CURATED PRODUCTS"""
    rankBtn = '//button//span[contains(text(),"Rank")]'
    updateBtn = '//span[text()="Update"]'
    allRankingTxt = '//table/tr/td/input'
    def rankingIndexTxt(intIndex):
            return f'(//table/tr/td/input)[{intIndex}]'
    rankingNameIndex1Lbl = '(//table/tr/td)[1]'
    rankingNameIndex3Lbl = '(//table/tr/td)[3]'
    rankingNameIndex5Lbl = '(//table/tr/td)[5]'
    rankingNameIndex7Lbl = '(//table/tr/td)[7]'
    sucRankUpdatedMsg = '//span[text()="Rank updated Successfully !"]'
    searchTitleTxt = '//input[@placeholder="Search By Title"]'
    searchItemTxt = '//input[@placeholder="Search By Product Name,Brand,Vendor Name"]'
    searchIconBtn = searchIconBtn
    productBtn = '//td/span[text()="Products"]'
    noRecordFoundLbl = '//span[text()="No Record Found"]'
    
    
    class pr:
        """PRODUCTS PAGE"""
        productsLbl = '//a[text()="Products"]'
        firstChk = '(//tr//span/input[@type="checkbox"]/..)[2]'
        addBtn = '//button/span[text()=" Add "]'
        confirmationLbl = '//h1[text()="Confirmation"]'
        yesBtn = '//button/span[text()=" Yes "]'
        productAddedSuccessMsg = '//span[text()="Products added Successfully !"]'
        
        associatedTabLbl = '//div[text()="Associated"]'
        removeBtn = '//button/span[text()=" Remove "]'
        productRemovedSuccessMsg = '//span[text()="Products removed Successfully !"]'
        
        
        
            
            
            
            
            
class sc:
    """SUBSCRIPTION"""
    searchTxt = '//input[@placeholder="Search By Email, S&S ID, S&S Number, Name"]'
    searchIconBtn = searchIconBtn
    editIconBtn = '//mat-icon[text()=" edit"]'
    firstEditIconBtn = '(//mat-icon[text()=" edit"])[1]'
    cancelBtn = '//span[text()="Cancel"]'





class cu:
    """CUSTOMERS"""
    customersLbl = '//a[text()="Customers"]'
    searchByTxt = '//input[@placeholder="Search By Users Name,Email,Connected To,UId"]'
    customerResultBtn = '//td[contains(@class, "firstName")]//a'
    searchIconBtn = searchIconBtn
    customerMobileNumberLbl = '//p[text()="Mobile Number"]/../h3'
    uploadCreditRewardBtn = '//label[contains(text()," Upload User Credits Or Rewards ")]'
    totalCreditLbl = '//p[contains(text(),"Total Credit")]'
    totalRewardLbl = '//p[contains(text(),"Total Reward")]'
    totalCreditEditBtn = '//span//p[contains(text(),"Total Credit")]//..//..//mat-icon'
    totalRewardEditBtn = '//span//p[contains(text(),"Total Reward")]//..//..//mat-icon'
    rewardEditLbl = '//input[@data-placeholder="Input reward amount..."]'
    editEnterBtn = '//mat-icon[text()="subdirectory_arrow_right"]'
    confirmationModalLbl = '//h1[contains(text(),"Confirmation")]'
    confirmationYesBtn = '//span[contains(text(),"Yes")]'
    creditEditLbl = '//input[@data-placeholder="Input credit amount..."]'
    totalCreditValueLbl = '//p[contains(text(),"Total Credit")]/../h3[@class="mat-line"]'
    totalRewardValueLbl = '//p[contains(text(),"Total Reward")]/../h3[@class="mat-line"]'
    confirmationDeductionModalLbl = '//p[contains(text(),"were not deducted")]'
    closeConfirmationDeductBtn = '//button//span[text()=" Close "]'
    cancelEditBtn = '//mat-icon[contains(text(),"cancel")]'
    uploadRewardsCreditsBtn = '//label[contains(text()," Upload User Credits Or Rewards ")]'
    uploadRewardsCreditsSuccessLbl = '//span[contains(text(), "Your upload was successful! All users and their Rewards/Credits balances have been updated.")]'
    creditsAlreadyCreditedLbl = '//p[contains(text(),"has already been credited")]'
    creditsAlreadyDeductedLbl = '//p[contains(text(),"has already been deducted")]'
    userDoesNotExistLbl = '//p[contains(text(),"does not exist")]'
    creditsRewardsMoreThanLbl = '//p[contains(text(),"were not deducted") and contains(text(),"reward(s) available")]'
    
    activityLogsLbl = '//h2[contains(text(),"Activity Logs")]'
    beanRewardsTabLbl = '//span[contains(text(),"Bean Rewards")]'
    beanCreditsTabLbl = '//span[contains(text(),"Bean Credits")]'
    balanceAddedLbl = '//div[contains(text(),"Balance Added")]'
    balanceSubtractedLbl = '//div[contains(text(),"Balance Subtracted")]'
    def balanceAddedCustomerLbl(strCustomer):
        return f'(//td[contains(text(),"{strCustomer}")])[1]'
    def balanceAddedRewardLbl(strCustomer):
        return f'{cu.balanceAddedCustomerLbl(strCustomer)}/../td[6]'
    def balanceAddedTimeLbl(strCustomer):
        return f'{cu.balanceAddedCustomerLbl(strCustomer)}/../td[3]'
    activityLogsRowsLbl = '//h2[contains(text(),"Activity Logs")]//..//table//tbody[@role="rowgroup"]//tr'
    

class rm:
    "REWARDS"
    beanRewardsLbl = '//a[contains(text(),"Bean Rewards")]'
    maxCapPercentLbl = '(//input[@data-placeholder="Enter 1 - 100 %"])[2]'
    maxCapPHPLbl = '//input[@data-placeholder="Enter PHP0.01 - PHP10,000"]'
    updateBtn = '//span[contains(text(),"Update")]'
    rewardsRatioUpdateLbl = '//span[contains(text(),"Rewards Ratio Updated Successfully!")]'
    positiveNumberPercentCapLbl = '//mat-error[contains(text()," Maximum Cap Percentage must be a positive whole number")]'
    valueGreaterThanPercentCapLbl = '//mat-error[contains(text()," Maximum Cap Percentage can\'t be greater than 100")]'
    upTo2DecimalPHPCapLbl = '//mat-error[contains(text(),"Maximum Cap Amount can contain only Valid upto 2 Decimal Numbers")]'
    valueGreaterThanPHPCapLbl = '//mat-error[contains(text(),"Maximum Cap Amount can\'t be greater than 10000")]'
    valueLbl = '//p[contains(text(),"1.0 Bean Reward is P1.00")]'
    calcPreviewLbl = '//p[contains(text(),"Calculation Preview")]'
    