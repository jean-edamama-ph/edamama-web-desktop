from playwright.sync_api import sync_playwright, Page, expect
from selenium.common.exceptions import NoSuchElementException
import playwright as playwright
import libraries.data.common as dCommon
import time
import logging
import os
import csv
    
# def __init__(page: Page):
#     page = page

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def log(intStatus, strMsg):
    """ 
    Objective: Perform log info
    param intStatus: 0 | 1 | 2
    param strMsg: Message
    returns: None
    Author: ccapistrano_20230327
    """
    if intStatus == 1:
        strStatus = 'PASS:'
    elif intStatus == 0:
        strStatus = 'INFO:'
    elif intStatus == 2:
        assert 1 == 0, strMsg
    # logging.warning(msg=f'{strStatus} {strMsg}')
    logging.info(msg=f'{strStatus} {strMsg}')

def funcLog(func: callable):
    """ 
    Objective: Perform decorator
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    def wrapper(*args, **kwargs):
        log(0, 'function [{}] Started: '.format(func.__name__))
        results = func(*args, **kwargs)
        if len(args) > 2:
            log(0, f'element: {args[1]} - Parameter: {args[2]}')
        elif len(args) > 1:
            log(0, f'element: {args[1]}')
        log(0, 'function [{}] Completed: '.format(func.__name__))
        return results
    return wrapper

def ufuncLog(func: callable):
    """ 
    Objective: Perform log decorator
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    def wrapper(*args, **kwargs):
        log(0, 'uFunction [{}] Started: Parameter: {}'.format(func.__name__, args))
        results = func(*args, **kwargs)
        log(0, 'uFunction [{}] Completed: '.format(func.__name__))
        return results
    return wrapper

@funcLog
def goToURL(page: Page, url):
    """ 
    Objective: Perform navigate to url
    param url: URL
    returns: None
    Author: ccapistrano_20230327
    """
    page.goto(url)
    page.wait_for_load_state('load')
    log(1, f'User navigated to URL "{url}".')
    # page.set_viewport_size({"width": 1920, "height": 980})
    
@funcLog
def maximize(page: Page):
    """ 
    Objective: Perform maximize the browser
    param url: URL
    returns: None
    Author: ccapistrano_20230327
    """
    page.set_viewport_size({"width": 1920, "height": 980})
    
@funcLog
def getTitle(page: Page):
    """ 
    Objective: Perform get page title
    param: None
    returns strTitle: Page title
    Author: ccapistrano_20230327
    """
    strTitle = page.title()
    log(1, f'Window title is "{strTitle}".')
    return strTitle

@funcLog
def hoverElem(page: Page, elem):
    """ 
    Objective: Perform hover to element
    param elem: Element
    returns: None
    Author: ccapistrano_20230327
    """
    page.locator(elem).hover()
    # page.hover(elem, force=True) 
    log(1, f'User hovered to element "{elem}".')
    
@funcLog
def clickElem(page: Page, elem):
    """ 
    Objective: Perform click element
    param elem: Element
    returns: None
    Author: ccapistrano_20230327
    """
    page.locator(elem).click(force=True)
    log(1, f'User clicked element "{elem}".')

@funcLog 
def clickOptElem(page: Page, elem):
    """ 
    Objective: Perform click element optional
    param elem: Element
    returns: None
    Author: ccapistrano_20230327
    """
    if verifyVisible(page, elem) == True:
        clickElem(page, elem)  

@funcLog
def clickElemText(page: Page, strText, intIndex = 1):
    """ 
    Objective: Perform click element containing specific text
    param elem: Element
    param intIndex: Index
    returns: None
    Author: ccapistrano_20230327
    """
    page.locator(f'(//*[contains(text(),"{strText}")])[{intIndex}]').click(force=True)
    log(1, f'User clicked element "//*[contains(text(),"{strText}")]"')
         
@funcLog
def expectElemTextToBeVisible(page: Page, strText, strParent = '', intIndex = 1, intTime = dCommon.time.intDefTimeOut):
    """ 
    Objective: Perform click element containing specific text
    param elem: Element
    param intIndex: Index
    returns: None
    Author: ccapistrano_20230327
    """
    page.locator(f'({strParent}//*[contains(text(),"{strText}")])[{intIndex}]').wait_for(state='visible', timeout= intTime)
    log(1, f'User clicked element "//*[contains(text(),"{strText}")]"')
    
@funcLog
def expectElemTextNotToBeVisible(page: Page, strText, strParent = '', intIndex = 1, intTime = dCommon.time.intDefTimeOut):
    """ 
    Objective: Perform click element containing specific text
    param elem: Element
    param intIndex: Index
    returns: None
    Author: ccapistrano_20230327
    """
    page.locator(f'({strParent}//*[contains(text(),"{strText}")])[{intIndex}]').wait_for(state='hidden', timeout= intTime)
    log(1, f'User clicked element "//*[contains(text(),"{strText}")]"')
    
@funcLog
def waitAndClickElemText(page: Page, strText, strParent = '', intIndex = 1, intWaitTime = 1):
    """ 
    Objective: Perform click element containing specific text
    param elem: Element
    param intIndex: Index
    returns: None
    Author: ccapistrano_20230327
    """
    wait(page, intWaitTime)
    page.locator(f'({strParent}//*[contains(text(),"{strText}")])[{intIndex}]').click(force=True)
    log(1, f'User clicked element "//*[contains(text(),"{strText}")]"')
    
@funcLog  
def expectOptElemToBeVisible(page: Page, elem):
    """ 
    Objective: Expect element to be visible optional
    param elem: Element
    returns: None
    Author: ccapistrano_20230327
    """
    if verifyVisible(page, elem) == True:
        expectElemToBeVisible(page, elem)                                                                                                             

@funcLog
def hoverAndClickElem(page: Page, elem):
    """ 
    Objective: Perform hover and click element
    param elem: Element
    returns: None
    Author: ccapistrano_20230327
    """
    hoverElem(page, elem)
    wait(page, .5)
    clickElem(page, elem)

@funcLog
def waitAndClickElem(page: Page, elem):
    """ 
    Objective: Wait element to be visible then click
    param elem: Element
    returns: None
    Author: ccapistrano_20230327
    """
    waitElemToBeVisible(page, elem)
    clickElem(page, elem)
    page.wait_for_load_state('load')

def wait(page: Page, intWaitTime = .5):
    """ 
    Objective: Perform wait
    param intWaitTime: Number count
    returns: None
    Author: ccapistrano_20230327
    """
    page.wait_for_timeout(1000*intWaitTime)

def waitForLoadState(page: Page, strState = 'load'):
    """ 
    Objective: Perform wait for load state
    param strState: load | domcontentloaded' | 'networkidle
    returns: None
    Author: ccapistrano_20230327
    """
    page.wait_for_load_state(strState)

@funcLog
def expectElemToBeVisible(page: Page, elem, intTime = dCommon.time.intDefTimeOut):
    """ 
    Objective: Expect element to be visible
    param elem: Element
    param intTime: Number count
    returns: None
    Author: ccapistrano_20230327
    """
    page.locator(elem).wait_for(state='visible', timeout= intTime)
    log(1, f'element "{elem}" is visible')

@funcLog
def expectElemToBeExist(page: Page, elem, intTime = dCommon.time.intDefTimeOut):
    """ 
    Objective: Expect element to be exist
    param elem: Element
    param intTime: Number count
    returns: None
    Author: ccapistrano_20230327
    """
    page.wait_for_selector(elem, state='hidden', timeout = intTime) 
    log(1, f'element "{elem}" exist')
    
@funcLog
def waitElemToBeVisible(page: Page, elem, intTimeOut = dCommon.time.intDefTimeOut):
    """ 
    Objective: Wait element to be visible
    param elem: Element
    param intTime: Number count
    returns: None
    Author: ccapistrano_20230327
    """
    page.wait_for_selector(elem, state='visible', timeout = intTimeOut)
         
@funcLog
def verifyVisible(page: Page, elem):
    """ 
    Objective: Verify element if visible
    param elem: Element
    returns blnVisible: True | False
    Author: ccapistrano_20230327
    """
    blnVisible = page.locator(elem).is_visible()
    return blnVisible

@funcLog
def expectElemNotToBeVisible(page: Page, elem):
    """ 
    Objective: Expect element not to be visible
    param elem: Element
    returns: None
    Author: ccapistrano_20230327
    """
    blnVisible = verifyVisible(page, elem)
    assert blnVisible == False, f'Element {elem} is visible' 
    log(1, f'Element {elem} should NOT be visible')

@funcLog 
def waitElemNotToBeVisible(page: Page, elem, intWait = 10):
    """ 
    Objective: Wait element not to be visible
    param elem: Element
    param intTime: Number count
    returns: None
    Author: ccapistrano_20230327
    """
    for item in range(intWait):
        blnVisible = verifyVisible(page, elem)
        if blnVisible == True:
            wait(page, 1)
        else:
            assert blnVisible == False, f'Element {elem} should not be visible'  
            expectElemNotToBeVisible(page, elem)

@funcLog  
def setElem(page: Page, elem, strValue):
    """ 
    Objective: Set value to an element
    param elem: Element
    param strValue: Value
    returns: None
    Author: ccapistrano_20230327
    """
    page.locator(elem).fill(strValue)
    log(1, f'Value "{strValue}" is set to element "elem"')
    
@funcLog  
def waitAndSetElem(page: Page, elem, strValue):
    """ 
    Objective: Wait and Set value to an element
    param elem: Element
    param strValue: Value
    returns: None
    Author: ccapistrano_20230508
    """
    waitElemToBeVisible(page, elem)
    setElem(page, elem, strValue)
    log(1, f'Value "{strValue}" is set to element "elem"')

@funcLog  
def switchToFrame(page: Page, arrAttrib):
    """ 
    Objective: Set value to an element
    param elem: Element
    param strValue: Value
    returns: None
    Author: ccapistrano_20230327
    """
    arriFrame = arrAttrib.split('|')
    frame = page.frame_locator(arriFrame[0])
    arriFrame.pop(0)
    for strAttrib in arriFrame:
         frame = frame.frame_locator(strAttrib)
    return frame
    
@funcLog  
def getElemText(page: Page, elem):
    """ 
    Objective: Get element text
    param elem: Element
    returns strValue: Text
    Author: ccapistrano_20230327
    """
    strValue = page.locator(elem).text_content()
    log(1, f'Text in element "{elem}" is "{strValue}.')
    return strValue.strip()

@funcLog  
def waitAndGetElemText(page: Page, elem):
    """ 
    Objective: Wait element to be visible then Get element text
    param elem: Element
    returns strValue: Text
    Author: ccapistrano_20230720
    """
    waitElemToBeVisible(page, elem)
    strValue = page.locator(elem).text_content()
    log(1, f'Text in element "{elem}" is "{strValue}.')
    return strValue.strip()

@funcLog  
def getElemAttribute(page: Page, elem, strAttribute):
    """ 
    Objective: Get element attribute value
    param elem: Element
    param strAttribute: Element attribute
    returns strValue: Value
    Author: ccapistrano_20230327
    """
    strValue = page.get_attribute(elem, strAttribute)
    log(1, f'Value of attribute "{strAttribute}" in element "{elem}" is "{strValue}.')
    return strValue.strip()

@funcLog  
def getAttributeAndCheckIfContainsText(page: Page, elem, strAttribute, strToFind):
    """ 
    Objective: Get element attribute value and check if contains text
    param elem: Element
    param strAttribute: Element attribute
    param strToFind: Text
    returns: None
    Author: ccapistrano_20230327
    """
    strToFindIn = getElemAttribute(page, elem, strAttribute)
    assert strToFind in strToFindIn, f'Expected text {strToFind} is NOT visible in the Actual text {strToFindIn}'
    log(1, f'Expected text "{strToFind}" is visible in the Actual text "{strToFindIn}".')

@funcLog  
def getArrayCount(page: Page, elem):
    """ 
    Objective: Get count of elements
    param elem: Element
    returns: None
    Author: ccapistrano_20230327
    """
    wait(page, .5)
    intCount = len(page.query_selector_all(elem))
    log(1, f'Array count of element "{elem}" is "{intCount}".')
    return int(intCount)

@funcLog  
def validateElemText(page: Page, elem, strToCompare, blnExact = True):
    """ 
    Objective: Compare Element text to a specific text
    param elem: Element
    param strToCompare: Text to compare
    returns : None
    Author: ccapistrano_20230327
    """
    if blnExact == True:
        strToCompareIn = getElemText(page, elem)
        assert strToCompare == strToCompareIn, f'Expected text {strToCompare} is NOT equal to Actual text {strToCompareIn}'
        log(1, f'Expected text "{strToCompare}" is equal to Actual text "{strToCompareIn}".')
    else:
        strToFind = strToCompare
        strToFindIn = getElemText(page, elem)
        assert strToFind in strToFindIn, f'Expected text {strToFind} is NOT visible in the Actual text {strToFindIn}'
        log(1, f'Expected text "{strToFind}" is visible in the Actual text "{strToFindIn}".')

@funcLog  
def switchToWindow(page: Page):
    """ 
    Objective: Switch to new window
    param: None
    returns window: Active window
    Author: ccapistrano_20230327
    """
    for item in range(20):
        if len(page.context.pages) == 2:
            break
        wait(page, 1)
    
    waitForLoadState(page)  
    assert len(page.context.pages) == 2, 'No new window displayed'
    window = page.context.pages
    window = window[1]
    log(1, f'Active window is "{window}".')
    page.wait_for_load_state('load')                                    
    return window

@funcLog  
def backToWindow(page: Page):
    """ 
    Objective: Switch back to default window
    param: None
    returns page: Default window
    Author: ccapistrano_20230327
    """
    window = page.context.pages
    page = window[0].bring_to_front()
    log(1, f'Active window is "{page}".') 
    return page

@funcLog  
def closeWindow(page: Page, intIndex = 1):
    """ 
    Objective: Close active window and back to default window
    param: None
    returns page: Default window
    Author: ccapistrano_20230327
    """
    window = page.context.pages
    window[intIndex].close()
    log(1, f'Window "{window[intIndex]}" closed.') 
    return page

@funcLog  
def openNewWindow(page: Page):
    """ 
    Objective: Open new window
    param: None
    returns page: New window
    Author: ccapistrano_20230327
    """
    page = page.context.new_page()
    log(1, f'New window "{page}" opened and active.') 
    return page

@funcLog  
def closeWinAndOpenNewWin(page: Page):
    """ 
    Objective: Close default window and open new window
    param: None
    returns page: New window
    Author: ccapistrano_20230327
    """
    page = closeWindow(page)
    page = openNewWindow(page)
    return page

@funcLog  
def sendKeys(page: Page, strKeys):
    """ 
    Objective: Send key press
    param strKeys: text
    returns: None
    Author: ccapistrano_20230327
    """
    page.keyboard.press(strKeys)
    log(1, f'Value "{strKeys}" is set.')
    
@funcLog
def reloadPage(page: Page):
    """ 
    Objective: Reload current page
    param: None
    returns: None
    Author: ccapistrano_20230327
    """
    page.reload(wait_until='load') 
    
@funcLog
def uploadFile(page: Page, elem, strPath):
    """ 
    Objective: Perform upload file
    param elem: Element
    param strPath: File Path
    returns: None
    Author: ccapistrano_20230327
    """
    file_path = os.path.abspath(strPath)
    with page.expect_file_chooser() as fc_info:
        wait(page, 1)
        clickElem(page, elem)
    file_chooser = fc_info.value
    file_chooser.set_files(file_path)
    wait(page, 1)

@funcLog
def setAndSelectFromSmartDropDown(page: Page, elem, strText, strParent = '', intIndex = 1, intWaitTime = 1):
    """ 
    Objective: Set and select from smart drop down
    param: None
    returns: None
    Author: ccapistrano_20230508
    """  
    waitAndSetElem(page, elem, strText)
    waitAndClickElemText(page, strText, strParent, intIndex, intWaitTime)
    
@funcLog
def clickElemAndDeleteText(page: Page, elem):
    """ 
    Objective: Click Elem and delete all text
    param: None
    returns: None
    Author: ccapistrano_20230508
    """
    waitAndClickElem(page, elem)
    sendKeys(page, 'ControlLeft')
    sendKeys(page, 'A')
    sendKeys(page, 'Delete')
    
@funcLog
def createFile(strPath, data):
    """ 
    Objective: Click Elem and delete all text
    param: None
    returns: None
    Author: ccapistrano_20230508
    """    
    # Specify the file path and name
    filename = strPath #'./libraries/data/uploadFile/data.csv'

    # Data to write to the CSV file
    data = data

    # Open the file in write mode
    with open(filename, 'w', newline='') as file:
        # Create a csv.writer object
        writer = csv.writer(file)

        # Write the data to the CSV file
        for row in data:
            writer.writerow(row)
            
@ufuncLog 
def scrollToElem(page: Page, elem, intMaxScrollAttempts = 15):
    """ 
    Objective: Perform Scroll to the element
    param elem: Element
    returns: None
    Author: ccapistrano_20230530
    """
    scroll_attempts = 1
    while scroll_attempts < intMaxScrollAttempts:
        try:
            if verifyVisible(page, elem) == False:
                intheight = 1000 * scroll_attempts
                page.evaluate(f'window.scrollTo(0, {intheight})')
                scroll_attempts += 1
                wait(page, .5)
            else:
                break
        except NoSuchElementException:
            break
        
@funcLog
def waitAndValidateElemText(page: Page, elem, strToCompare, blnExact = True):
    """ 
    Objective: Wait element to be visible then validate elem texts
    param elem: Element
    param strToCompare: Text to compare
    param blnExact: True | False
    returns: None
    Author: cgrapa_20230608
    """
    waitElemToBeVisible(page, elem)
    validateElemText(page, elem, strToCompare, blnExact)
    
@funcLog
def verifyIfClickable(page: Page, elem):
    """ 
    Objective: Attempt to click an element only if it is clickable
    param elem: Element
    returns: None
    Author: rmakiling_20231014
    """
    blnClickable = page.locator(elem).is_enabled()
    return blnClickable

@funcLog
def verifyOptElem(page: Page, elem):
    """ 
    Objective: Verify Element Optional
    param elem: Element
    returns: None
    Author: rmakiling_20231016
    """
    for item in range(3):
        wait(page, 1)
        if verifyVisible(page, elem) == True:
            expectElemToBeVisible(page, elem)

@funcLog
def getURL(page: Page):
    """ 
    Objective: get URL value
    
    param: None
    returns: None
    Author: ccapistrano_20230615
    """
    strUrl = page.url
    return strUrl

@funcLog
def getElemTextAndCheckIfContainsText(page: Page, elem, strToFind):
    """ 
    Objective: Get element text value and check if contains text
    param elem: Element
    param strToFind: Text
    returns: None
    Author: jatregenio_20240203
    """
    strToFindIn = getElemText(page, elem)
    assert strToFind in strToFindIn, f'Expected text {strToFind} is NOT visible in the Actual text {strToFindIn}'
    log(1, f'Expected text "{strToFind}" is visible in the actual text "{strToFindIn}".' )
    
@funcLog  
def stringCompare(strToCompare, strToCompareIn, blnExact = True):
    """ 
    Objective: Compare Strings
    param strToCompare: String 1
    param strToCompareIn: String 2
    returns: None
    Author: ccapistrano_20231005
    """
    if blnExact == True:
        assert strToCompare == strToCompareIn, f'Actual: "{strToCompare}" is not equal to Expected: "{strToCompareIn}"'
    elif blnExact == False:
        assert strToCompare in strToCompareIn, f'Actual: "{strToCompare}" is not in Expected: "{strToCompareIn}"'

@funcLog  
def switchToSecondWindow(page: Page):
    """ 
    Objective: Switch back to second window
    param: None
    returns page: Second window
    Author: abernal_20240313
    """
    window = page.context.pages
    page = window[1].bring_to_front()
    log(1, f'Active window is "{page}".') 
    return page