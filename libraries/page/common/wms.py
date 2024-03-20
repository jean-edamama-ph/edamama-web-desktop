dsORwhLst = '//facilitymodule[@class="facility_module"]//a[@class="select2-choice"]'
dropShipOption = '//div[text()="Edamama Dropship"]'
wareHouseOption = '//div[text()="Edamama Warehouse"]'

class od:
    """ORDERS"""
    orderSectionBtn = '//section//a[@href="/orders"]'
    ordersTabBtn = f'{orderSectionBtn}/../../../..//tab//a[@href="/orders"]'
    
    class od:
        """ORDERS"""
        ngframeFrame = '//iframe[@id="ngframe"]'
        filtersBtn = '//span[contains(text(),"Filters")]'
        filterTxt = '//input[@placeholder="Enter Order # Contains"]'
        applyIconBtn  = '//ion-button[text()="Apply"]'
        noDataDisplayLbl = '//div[text()="No data to display"]/..'
        
        productDescLbl = '//div[@class="ion-text-left"]/span[contains(text(),"EDA")]'
        #productDescLbl = '//div[@class="ion-text-left"]/span[contains(text(),"AAAA")]'
        priceInfoLbl = '//div[@class="total-price-container"]/span'
        totalUnitsLbl = '(//div[contains(@class, "ion-text-left")]/span)[3]'
        inProcessLbl = '(//div[contains(@class, "ion-text-left")]/span)[4]'
        rightCaretIconBtn = '//div[@class="row-control-container"]//ion-icon[@role="img"]'
        
        cancelledHeaderLbl = '//li[contains(text(),"Cancelled")]' 
        def statusValueLbl(strOrderID):
            return f'(//a[text()="{strOrderID}"]/../../../../..//div[@class="ion-text-left"])[3]'
        
        class dd:
            """DROP DOWN""" # RIGHT CARET DROP DOWN
            productionDescLbl = '((//datatable-body//div[@class="datatable-row-center datatable-row-group"])[2]//datatable-body-cell/div)[2]'
            priceInfoLbl = '((//datatable-body//div[@class="datatable-row-center datatable-row-group"])[2]//datatable-body-cell/div)[9]'
        
    