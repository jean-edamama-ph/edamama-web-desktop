import libraries.page.common.wms as pWms

import libraries.util.common as uCommon

@uCommon.ufuncLog  
def selectDPorWH(page, strDSorWH = 'dropship'):
    """ 
    Objective: Select eiter Dropship or Warehouse
    
    param: None
    returns: None
    Author: ccapistrano_20230605
    """
    uCommon.waitAndClickElem(page, pWms.dsORwhLst)
    if strDSorWH == 'dropship':
        uCommon.waitAndClickElem(page, pWms.dropShipOption)
    else:
        uCommon.waitAndClickElem(page, pWms.wareHouseOption)
    uCommon.wait(page, 1)
    
@uCommon.ufuncLog  
def hoverToOrders(page):
    """ 
    Objective: Hover to Orders on the Left panel
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    uCommon.waitElemToBeVisible(page, pWms.od.orderSectionBtn)
    uCommon.wait(page, 1)
    uCommon.hoverElem(page, pWms.od.orderSectionBtn)
    uCommon.waitElemToBeVisible(page, pWms.od.ordersTabBtn)

@uCommon.ufuncLog  
def clickOrders(page):
    """ 
    Objective: Click Orders
    
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    uCommon.hoverAndClickElem(page, pWms.od.ordersTabBtn)
    uCommon.wait(page, 5)

@uCommon.ufuncLog  
def clickfilter(frame):
    """ 
    Objective: Click Orders
    
    param frame: iframe
    param: None
    returns: None
    Author: ccapistrano_20230327
    Updated By: abernal_20230320
    """ 
    uCommon.clickElem(frame, pWms.od.od.filtersBtn)

@uCommon.ufuncLog  
def setFilter(frame, strOrderID):
    """ 
    Objective: Set filter
    
    param frame: iframe
    param strOrderID: Order ID
    returns: None
    Author: ccapistrano_20230327
    """ 
    if '#' in strOrderID:
        strOrderID = strOrderID.replace('#', '')
    uCommon.setElem(frame, pWms.od.od.filterTxt, strOrderID)

@uCommon.ufuncLog  
def clickApply(frame):
    """ 
    Objective: Click Apply
    
    param frame: iframe
    returns: None
    Author: ccapistrano_20230327
    """ 
    uCommon.clickElem(frame, pWms.od.od.applyIconBtn)
    
@uCommon.ufuncLog  
def expectNoDataDisplay(frame):
    """ 
    Objective: Expect No Data Display is visible
    
    param frame: iframe
    returns: None
    Author: ccapistrano_20230327
    """     
    uCommon.expectElemToBeVisible(frame, pWms.od.od.noDataDisplayLbl)

@uCommon.ufuncLog  
def clickCancelledHeader(frame):
    """ 
    Objective: Click Cancelled header
    
    param frame: iframe
    returns: None
    Author: ccapistrano_20230327
    """ 
    uCommon.clickElem(frame, pWms.od.od.cancelledHeaderLbl)

@uCommon.ufuncLog  
def validateStatus(frame, strOrderID, strValue):
    """ 
    Objective: Click Cancelled header
    
    param frame: iframe
    param strOrderID: Order ID
    param strValue: Value
    returns: None
    Author: ccapistrano_20230327
    """ 
    uCommon.validateElemText(frame, pWms.od.od.statusValueLbl(strOrderID), strValue)
    
@uCommon.ufuncLog   
def validateDetails(frame, dictData, dicDetails):
    """ 
    Objective: Validate wms details
    
    param frame: iframe
    param dictData: Dictionary data
    returns: None
    Author: ccapistrano_20230327
    """
    uCommon.validateElemText(frame, pWms.od.od.productDescLbl, dictData["skuCode"], False)
    uCommon.validateElemText(frame, pWms.od.od.priceInfoLbl, (dicDetails['strPriceInfo'].replace('₱', '')).replace(',', ''))
    uCommon.validateElemText(frame, pWms.od.od.totalUnitsLbl, dicDetails['strQuantity'])
    uCommon.validateElemText(frame, pWms.od.od.inProcessLbl, dicDetails['strStatus'])
    uCommon.clickElem(frame, pWms.od.od.rightCaretIconBtn)
    uCommon.validateElemText(frame, pWms.od.od.dd.productionDescLbl, dictData["skuCode"], False)
    arrTotalPrice = dicDetails['strPriceInfo'].split('.')
    strTotalPrice = (arrTotalPrice[0].replace('₱', '')).replace(',', '')
    uCommon.validateElemText(frame, pWms.od.od.dd.priceInfoLbl, strTotalPrice, False)
    
@uCommon.ufuncLog   
def switchToFrame(page):
    """ 
    Objective: Switching to iFrame
    
    param: None
    returns frame: iframe
    Author: ccapistrano_20230327
    """
    frame = uCommon.switchToFrame(page, pWms.od.od.ngframeFrame)
    return frame