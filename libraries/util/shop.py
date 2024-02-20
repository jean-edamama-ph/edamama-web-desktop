import libraries.page.shop as pShop
import libraries.page.common.common as pCommon
import libraries.util.common as uCommon
import datetime

class com:
    """COMMON"""
    @uCommon.ufuncLog  
    def clickShop(page):
        """ 
        Objective: Click Shop successfully
        
        param: None
        returns: None
        Author: ccapistrano_20230509
        """
        uCommon.waitAndClickElem(page, pCommon.header.shopBtn)
        uCommon.waitElemToBeVisible(page, pShop.hs.homeSliderImg)






class sp:
    """SHOP PAGE"""
    @uCommon.ufuncLog  
    def validateHomeSlider(page, blnLoggedIn = True):
        """ 
        Objective: Validate hoe slider section elements
        
        param blnLoggedIn: True or False
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['homeSliderImg','sliderSectionImg', 'whyMamasEdamamaLbl', 'authenticImg', 'authenticLbl', 'expressDeliveryImg',
                'expressDeliveryLbl', 'curatedContentImg', 'curatedContentLbl', 'happinessGuaranteedImg', 'happinessGuaranteedLbl']
        if blnLoggedIn == True:
            arrObj.extend(['referralBannerImg', 'referralCodeLbl'])
            for item in arrObj:
                uCommon.waitElemToBeVisible(page, pShop.hs.__dict__[item])
            uCommon.waitElemToBeVisible(page, pShop.hs.referAFriendLbl)
        else:
            arrObj1 = (['referralBannerImg', 'referralCodeLbl'])
            for item in arrObj:
                uCommon.waitElemToBeVisible(page, pShop.hs.__dict__[item])
            for item in arrObj1:
                uCommon.expectElemNotToBeVisible(page, pShop.hs.__dict__[item])
            uCommon.expectElemToBeExist(page, pShop.hs.referAFriendLbl)

    @uCommon.ufuncLog  
    def validateFeaturedProducts(page):
        """ 
        Objective: Validate feature section products elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['firstItemImg','firstItemBrandLbl', 'firstItemNameLbl', 'firstItemPriceLbl']
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pShop.fp.__dict__[item])

    @uCommon.ufuncLog  
    def validateAnko(page):
        """ 
        Objective: Validate Anko section elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['ankoLbl','moreBtn', 'arrowForwardIconBtn', 'heartIconBtn', 'firstItemImg',
                'firstItemBrandLbl', 'firstItemNameLbl', 'firstItemPriceLbl', 'nextSwiperBtn']
        uCommon.scrollToElem(page, pShop.an.ankoLbl)
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pShop.an.__dict__[item])

    @uCommon.ufuncLog         
    def validateDiscover(page):
        """ 
        Objective: Validate Discover section elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['discoverLbl','tipsGuideLbl', 'moreBtn', 'arrowForwardIconBtn', 'nurtureBtn']
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pShop.dc.__dict__[item])

    @uCommon.ufuncLog      
    def validateBean(page):
        """ 
        Objective: Validate Bean section elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['beanLbl','moreBtn', 'arrowForwardIconBtn', 'heartIconBtn', 'firstItemImg',
                'firstItemBrandLbl','firstItemNameLbl', 'firstItemPriceLbl', 'nextSwiperBtn']
        uCommon.scrollToElem(page, pShop.bn.beanLbl)
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pShop.bn.__dict__[item])

    @uCommon.ufuncLog   
    def validateSubscribeAndSave(page):
        """ 
        Objective: Validate Subscribe and Save section elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['subscribeAndSaveLbl','moreBtn', 'arrowForwardIconBtn', 'heartIconBtn', 'subscribeAndSaveBtn','firstItemImg',
                'firstItemBrandLbl', 'firstItemNameLbl', 'firstItemPriceLbl', 'nextSwiperBtn', 'giftRegistryImg', 'eGiftImg']
        uCommon.scrollToElem(page, pShop.ss.subscribeAndSaveLbl)
        for item in arrObj:
            if item == 'giftRegistryImg':
                uCommon.scrollToElem(page, pShop.ss.__dict__[item])
            uCommon.waitElemToBeVisible(page, pShop.ss.__dict__[item])

    @uCommon.ufuncLog  
    def validateBabyGear(page):
        """ 
        Objective: Validate Baby gear section elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['babyGearLbl','moreBtn', 'arrowForwardIconBtn', 'heartIconBtn', 'firstItemImg',
                'firstItemBrandLbl', 'firstItemNameLbl', 'firstItemPriceLbl', 'nextSwiperBtn']
        uCommon.scrollToElem(page, pShop.bg.babyGearLbl)
        for item in arrObj:
            uCommon.expectElemToBeVisible(page, pShop.bg.__dict__[item])

    @uCommon.ufuncLog  
    def validateFormulaAndMilk(page):
        """ 
        Objective: Validate Formula and Milk section elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['formulaMilkLbl','moreBtn', 'arrowForwardIconBtn', 'heartIconBtn', 'firstItemImg',
                'firstItemBrandLbl', 'firstItemNameLbl', 'firstItemPriceLbl', 'nextSwiperBtn']
        uCommon.scrollToElem(page, pShop.fm.formulaMilkLbl)
        for item in arrObj:
            uCommon.expectElemToBeVisible(page, pShop.fm.__dict__[item])   

    @uCommon.ufuncLog  
    def validateToys(page):
        """ 
        Objective: Validate Toys section elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['toysLbl','moreBtn', 'arrowForwardIconBtn', 'heartIconBtn', 'firstItemImg',
                'firstItemBrandLbl', 'firstItemNameLbl', 'firstItemPriceLbl', 'nextSwiperBtn']
        uCommon.scrollToElem(page, pShop.ty.toysLbl)
        for item in arrObj:
            uCommon.expectElemToBeVisible(page, pShop.ty.__dict__[item])   
        
    @uCommon.ufuncLog   
    def validateDownload(page):
        """ 
        Objective: Validate DOwnload section elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['viberBannerImg','downloadTheEdamamaAppLbl', 'enjoyAFasterLbl', 'appStoreIconBtn', 'googlePlayIconBtn', 'badgeMobileImg']
        uCommon.hoverElem(page, pShop.dl.viberBannerImg)
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pShop.dl.__dict__[item])   

    @uCommon.ufuncLog  
    def validateShopPage(page, blnLoggedIn = True):
        """ 
        Objective: Validate Shop page elements
        
        param blnLoggedIn: True or False
        returns: None
        Author: ccapistrano_20230327
        """
        if blnLoggedIn == True:
            sp.validateHomeSlider(page)
        else:
            sp.validateHomeSlider(page, blnLoggedIn)    
        sp.validateFeaturedProducts(page)
        sp.validateAnko(page)
        sp.validateDiscover(page)
        sp.validateBean(page)
        sp.validateSubscribeAndSave(page)
        sp.validateBabyGear(page)
        sp.validateFormulaAndMilk(page)
        sp.validateToys(page)
        sp.validateDownload(page)
            

    @uCommon.ufuncLog   
    def validateProductDescriptionAndSpecification(page):
        """ 
        Objective: Validate product description and specification section elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['descriptionBtn','descriptionTitleLbl', 'descriptionContentLbl']
        for item in arrObj:
            uCommon.expectElemToBeVisible(page, pShop.pd.__dict__[item])
        uCommon.waitAndClickElem(page, pShop.ps.productSpecificationBtn)
        arrObj = ['productSpecificationBtn','productSpecificationTitleLbl', 'productSpecificationContentLbl']
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pShop.ps.__dict__[item])

    @uCommon.ufuncLog  
    def validateCarouselBanner(page):
        """ 
        Objective: Validate carousel banner elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.clickElem(page, pShop.hs.whyMamasEdamamaLbl)
        intPaginationBullet = uCommon.getArrayCount(page, pShop.hs.allPaginatioBulletIconBtn)
        for item in range(intPaginationBullet):
            uCommon.waitAndClickElem(page, pShop.hs.paginatioBulletBtn(item+1))
            uCommon.getAttributeAndCheckIfContainsText(page, pShop.hs.paginatioBulletBtn(item+1), 'class', 'active')
            uCommon.getAttributeAndCheckIfContainsText(page, pShop.hs.dataSwiperSlideImg(item+1), 'class', 'active')

    @uCommon.ufuncLog       
    def validateFlashSale(page):
        """ 
        Objective: Validate Flash Sale section elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        
        for item in range(30):
            if uCommon.verifyVisible(page, pShop.fs.flashSaleTitleLbl) == True:
                arrObj = ['flashSaleTitleLbl','firstItemImg', 'firstItemBrandLbl', 'firstItemNameLbl', 'firstItemPriceLbl','counterLbl']
                for item in arrObj:
                    uCommon.waitElemToBeVisible(page, pShop.fs.__dict__[item])
            else:
                if item == 30:
                    uCommon.log(2, f'Flash Sale is not visible in the page')
                uCommon.reloadPage(page)
                uCommon.wait(page, 2)
        
    @uCommon.ufuncLog  
    def searchName(page, strName):
        """ 
        Objective: Perform search item or brand name
        
        param strName: Item or Brand Name
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.waitElemToBeVisible(page, pCommon.header.searchForYourFavTxt)
        uCommon.setElem(page, pCommon.header.searchForYourFavTxt, strName)
        uCommon.wait(page, 1)
        uCommon.sendKeys(page, 'Enter')
        uCommon.wait(page, 2)
        uCommon.clickOptElem(page, pCommon.header.xBtn)
        uCommon.wait(page, 1)
    
    @uCommon.ufuncLog  
    def searchAndValidateName(page, strType, strName):
        """ 
        Objective: Perform search item or brand name
        
        param strType: Item | Brand
        param strName: Item or Brand Name
        returns: None
        Author: ccapistrano_20230327
        Update: jatregenio_20240219
        """
        sp.searchName(page, strName)
        if uCommon.verifyVisible(page, pShop.sl.showingOutOfLbl) == False:
            sp.searchName(page, strName)
        if strType == 'brand':
            intBrandnameCnt = uCommon.getArrayCount(page, pShop.sl.allBrandName)
            for item in range(intBrandnameCnt):
                uCommon.validateElemText(page, pShop.sl.brandNameLbl(item+1), strName, )
        elif strType == 'item':
            intItemNameCnt = uCommon.getArrayCount(page, pShop.sl.allItemNameLbl)
            for item in range(intItemNameCnt):
                if item == 0:
                    uCommon.validateElemText(page, pShop.sl.itemNameLbl(item+1), strName) 
                else:
                    break

    
    @uCommon.ufuncLog  
    def searchAndWaitItem(page, strName, blnVisible = True, intMin = 20):
        """ 
        Objective: Search and wait for item to be visisible or not visible
        
        param strName: Item | Brand
        param blnVisible: True | False
        param intMin: minutes
        returns: None
        Author: ccapistrano_20230327
        """
        # get current time
        startTime = datetime.datetime.now()
        # set wait time to 15 minutes from now
        endTime = startTime + datetime.timedelta(minutes=intMin)
        for item in range(900):
            sp.searchName(page, strName)
            if blnVisible == True:
                if uCommon.verifyVisible(page, pShop.sl.showingOutOfLbl) == True:
                    break
                else:
                    if datetime.datetime.now() > endTime:
                        uCommon.log(2, f'REPLICATION ISSUE: Item "{strName}" still not visible after {intMin} mins')
            else:
                if uCommon.verifyVisible(page, pShop.sl.showingOutOfLbl) == False:
                    break
                else:
                    if datetime.datetime.now() > endTime:
                        uCommon.log(2, f'REPLICATION ISSUE: Item "{strName}" still visible after {intMin} mins') 
            uCommon.reloadPage(page)            
            
    @uCommon.ufuncLog  
    def validateSuccessfulMessageModal(page):
        """ 
        Objective: Validate successful message modal elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.waitElemToBeVisible(page, pShop.msg.bagSuccessfullyMsg)
        uCommon.waitElemToBeVisible(page, pShop.msg.closeBtn)
        uCommon.clickElem(page, pShop.msg.closeBtn)

    @uCommon.ufuncLog  
    def clickFPfirstItem(page):
        """ 
        Objective: Click Featured Product first item 
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.hoverAndClickElem(page, pShop.fp.firstItemImg)
        uCommon.waitElemToBeVisible(page, pShop.pf.itemLargePicImg)
    
    @uCommon.ufuncLog  
    def clickSSfirstItem(page):
        """ 
        Objective: Click Subscribe and Save first item 
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.wait(page, .5)
        uCommon.hoverAndClickElem(page, pShop.ss.firstItemImg)
        uCommon.waitElemToBeVisible(page, pShop.pf.itemLargePicImg)
        
    @uCommon.ufuncLog  
    def expectCuratedTitleNotVisible(page, strTitleName):
        """ 
        Objective: Expect Curated title not visible
        
        param strTitleName: title name
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.expectElemNotToBeVisible(page, pShop.hs.curatedTitleLbl(strTitleName))
        
    @uCommon.ufuncLog  
    def waitAndexpectCuratedTitleIsVisible(page, strTitleName):
        """ 
        Objective: Expect Curated title is visible
        
        param strTitleName: title name
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.waitElemToBeVisible(page, pShop.hs.curatedTitleLbl(strTitleName))

    @uCommon.ufuncLog  
    def validateCuratedTitleIsVisible(page, intIndex, strTitleName):
        """ 
        Objective: Expect Curated title is visible
        
        param intIndex: Index
        param strTitleName: title name
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.validateElemText(page, pShop.hs.allCuratedTitleLbl(intIndex), strTitleName)
    
    @uCommon.ufuncLog  
    def waitAndGetCuratedTitle(page, intIndex):
        """ 
        Objective: wait and get Curated title
        
        param intIndex: Index
        returns strTitle: Title
        Author: ccapistrano_20230517
        """
        strTitle = uCommon.getElemText(page, pShop.hs.allCuratedTitleLbl(intIndex))
        return strTitle
    
    @uCommon.ufuncLog  
    def waitAndClickCuratedTitle(page, intIndex):
        """ 
        Objective: wait and Click Curated title successfully
        
        param intIndex: Index
        returns: None
        Author: ccapistrano_20230517
        """
        strTitle = uCommon.waitAndClickElem(page, pShop.hs.allCuratedTitleLbl(intIndex))
    
    @uCommon.ufuncLog  
    def searchAndClickItem(page, strItemName):
        """ 
        Objective: Perform search item or brand name
        
        param strName: Item or Brand Name
        returns: None
        Author: ccapistrano_20230327
        """
        sp.searchName(page, strItemName)
        uCommon.waitAndClickElemText(page, strItemName)
        uCommon.waitElemToBeVisible(page, pShop.pf.itemBrandLbl)
    
    @uCommon.ufuncLog
    def setShopSection(page, strShopSection):
        """ 
        Objective: Set Shop section
            
        param strShopSection: Shop Section
        returns strSection: strSection
        Author: cgrapa_20230615
        """
        match strShopSection:
            case 'fp': strSection = pShop.fp
            case 'an': strSection = pShop.an
            case 'bn': strSection = pShop.bn
            case 'ss': strSection = pShop.ss
            case 'bg': strSection = pShop.bg
            case 'fm': strSection = pShop.fm
            case 'ty': strSection = pShop.ty
            case _: uCommon.log(2, f'Incorrect strShopSection. Kindly use any of the ff: "fp", "an", "bn", "ss", "bg", "fm" or "ty"')
        return strSection
    
    @uCommon.ufuncLog
    def getShopItemDetails(page, strShopSection):
        """ 
        Objective: Get item details
            
        param strShopSection: Shop Section
        returns dictData: strBrand, strName, strPrice
        Author: cgrapa_20230615
        """
        strSection = sp.setShopSection(page, strShopSection)
        strBrand = uCommon.getElemText(page, strSection.firstItemBrandLbl)
        strName = uCommon.getElemText(page, strSection.firstItemNameLbl)
        strPrice = uCommon.getElemText(page, strSection.firstItemPriceLbl)
        dictData = {'strBrand': strBrand, 'strName': strName, 'strPrice': strPrice}
        return dictData
    
    @uCommon.ufuncLog
    def addShopItemToWishlist(page, strShopSection):
        """ 
        Objective: Add Item to Wishlist
            
        param strShopSection: Shop section
        returns: None
        Author: cgrapa_20230615
        """
        strSection = sp.setShopSection(page, strShopSection)
        uCommon.waitAndClickElem(page, strSection.heartIconBtn)
        uCommon.expectElemToBeVisible(page, strSection.heartActiveIconBtn)
    
    @uCommon.ufuncLog
    def removeShopItemFromWishlist(page, strShopSection):
        """ 
        Objective: Remove item from Wishlist
            
        param strShopSection: Shop section
        returns: None
        Author: cgrapa_20230619
        """
        strSection = sp.setShopSection(page, strShopSection)
        uCommon.waitAndClickElem(page, strSection.heartIconBtn)
        uCommon.wait(page, 3)
        uCommon.waitAndClickElem(page, strSection.heartActiveIconBtn)





class pp:
    """PRODUCT PAGE"""
    @uCommon.ufuncLog  
    def validateProductForm(page, strTitle = 'fp'):
        """ 
        Objective: Validate product form elements
        
        param strTitle: fp | ss
        returns: None
        Author: ccapistrano_20230327
        """
        if strTitle == 'fp':
            arrObj = ['homeLnk','heartIconBtn', 'shareBtn', 'giftBtn', 'itemSmallPicImg', 'itemLargePicImg', 'itemBrandLbl', 'itemNameLbl', 'itemPriceLbl', 'thisItemLbl', 
                      'sevenDaysRefundableImg', 'sevenDaysRefundableLbl', 'cashOnDeliverImg', 'cashOnDeliverLbl', 'groupBuyImg',  'groupBuyLbl', 'subscribeAndSaveImg', 
                      'subscribeAndSaveLbl', 'expressDeliveryImage', 'expressDeliveryLbl', 'forOrdersBeforeLbl', 'addtoBagBtn']
            for item in arrObj:
                uCommon.waitElemToBeVisible(page, pShop.pf.__dict__[item])
                
            arrObj = ['quantityLbl', 'quantityMinusIconBtn', 'quantityOutputLbl', 'quantityPlusIconBtn']
            for item in arrObj:
                uCommon.expectOptElemToBeVisible(page, pShop.pf.__dict__[item])
        elif strTitle == 'ss':
            uCommon.waitAndClickElem(page, pShop.pf.days15Lbl)
            uCommon.expectElemToBeExist(page, pShop.pf.daysOptionLbl('15 DAYS'))
            uCommon.expectElemToBeExist(page, pShop.pf.daysOptionLbl('30 DAYS'))
            uCommon.expectElemToBeExist(page, pShop.pf.daysOptionLbl('45 DAYS'))
            uCommon.expectElemToBeExist(page, pShop.pf.daysOptionLbl('60 DAYS'))
            uCommon.expectElemToBeExist(page, pShop.pf.daysOptionLbl('90 DAYS'))
            uCommon.expectElemToBeExist(page, pShop.pf.daysOptionLbl('120 DAYS'))
            uCommon.getAttributeAndCheckIfContainsText(page, f'{pShop.pf.sevenDaysRefundableImg}/..', 'class', 'content -disabled ng-star-inserted')
            uCommon.getAttributeAndCheckIfContainsText(page, f'{pShop.pf.cashOnDeliverImg}/..', 'class', 'content ng-star-inserted')
            uCommon.getAttributeAndCheckIfContainsText(page, f'{pShop.pf.groupBuyImg}/..', 'class', 'content -disabled ng-star-inserted')
            uCommon.getAttributeAndCheckIfContainsText(page, f'{pShop.pf.subscribeAndSaveImg}/..', 'class', 'content ng-star-inserted')
            uCommon.getAttributeAndCheckIfContainsText(page, f'{pShop.pf.expressDeliveryImage}/..', 'class', 'content -disabled ng-star-inserted')
            
            arrObj = ['homeLnk','heartIconBtn', 'shareBtn', 'itemSmallPicImg', 'itemLargePicImg', 'itemBrandLbl', 'itemNameLbl', 'itemPriceLbl', 'quantityLbl', 'quantityCountLbl',
                'quantityDrp', 'subsAndSaveRdb', 'subsAndSaveLbl', 'purchaseTypeLbl', 'days15Lbl', 'days15Drp', 'priceLbl', 'howdoSubsWorkLbl', 'infoIconBtn', 'thisItemLbl', 
                'sevenDaysRefundableImg', 'sevenDaysRefundableLbl', 'cashOnDeliverImg', 'cashOnDeliverLbl', 'groupBuyImg', 'groupBuyLbl', 'subscribeAndSaveImg', 'subscribeAndSaveLbl', 
                'expressDeliveryImage', 'expressDeliveryLbl', 'forOrdersBeforeLbl', 'addtoBagBtn']
            for item in arrObj:
                uCommon.waitElemToBeVisible(page, pShop.pf.__dict__[item])
        
    @uCommon.ufuncLog  
    def validateDetails(page, dictDetails):
        """ 
        Objective: Validate Product page Brand, Name and Price
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.validateElemText(page, pShop.pf.itemBrandLbl, dictDetails['strBrand'])
        uCommon.validateElemText(page, pShop.pf.itemNameLbl, dictDetails['strName'], False)
        uCommon.validateElemText(page, pShop.pf.itemPriceLbl, dictDetails['strPrice'])

    @uCommon.ufuncLog  
    def clickAddToBag(page, blnSuccMsg = True):
        """ 
        Objective: Click Add to Bag
        
        param blnSuccMsg: True | False
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.wait(page, 1)
        uCommon.waitAndClickElem(page, pShop.pf.addtoBagBtn)
        if blnSuccMsg == True:
            sp.validateSuccessfulMessageModal(page)
        elif blnSuccMsg == 'opt':
            uCommon.wait(page, 2)
            if uCommon.verifyVisible(page, pShop.sp.confirmAddToCartBtn) == True:
                ss.clickConfirmAddToCart(page)
            else:
                sp.validateSuccessfulMessageModal(page)
    
    @uCommon.ufuncLog  
    def validateDiscountRate(page, dictDetails):
        """ 
        Objective: Validate Discount Rate and other details
        
        param dictDetails: dictDetails
        returns: None
        Author: ccapistrano_20230327
        """
        for item in range(60):
            if uCommon.verifyVisible(page, pShop.pf.discountLbl) == True:
                break
            uCommon.reloadPage(page)
            uCommon.wait(page, 5)
        uCommon.waitElemToBeVisible(page, pShop.pf.discountLbl)
        if '%' in dictDetails['strTotalDiscount']:
            uCommon.validateElemText(page, pShop.pf.discountLbl, dictDetails['strTotalDiscount'], False)
        uCommon.validateElemText(page, pShop.pf.itemPriceLbl, dictDetails['strPriceOriginal'].replace(' ', ''))
        uCommon.validateElemText(page, pShop.pf.itemDisPriceLbl, dictDetails['strPriceDiscounted'].replace(' ', ''))
    
    @uCommon.ufuncLog  
    def clickColorBtn(page, strColor):
        """ 
        Objective: Click Add to Bag
        
        param blnSuccMsg: True | False
        returns: None
        Author: ccapistrano_20230327
        """
        uCommon.waitAndClickElem(page, pShop.pf.colorBtn(strColor))
        uCommon.wait(page, 1)
        uCommon.getAttributeAndCheckIfContainsText(page, f'{pShop.pf.colorBtn(strColor)}/..', 'aria-pressed', 'true')
    
    @uCommon.ufuncLog
    def addItemToWishlist(page):
        """ 
        Objective: Add Item to Wishlist
            
        param: None
        returns: None
        Author: cgrapa_20230615
        """
        uCommon.waitAndClickElem(page, pShop.pf.heartIconBtn)
        uCommon.expectElemToBeVisible(page, pShop.pf.heartActiveIconBtn)
    
    @uCommon.ufuncLog
    def removeItemFromWishlist(page):
        """ 
        Objective: Remove item from Wishlist
            
        param: None
        returns: None
        Author: cgrapa_20230619
        """
        uCommon.waitAndClickElem(page, pShop.pf.heartIconBtn)
        uCommon.wait(page, 3)
        uCommon.waitAndClickElem(page, pShop.pf.heartActiveIconBtn)
    
    

    
    
        
class lp:
    """LISTING PAGE"""
    @uCommon.ufuncLog  
    def validateListingPage(page, blnSearch = False):
        """ 
        Objective: Validate listing page elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['categoriesLbl','lvl1CategoryLvl', 'productSpotLightLbl', 'allLbl', 'allChk','featuredProductsLbl', 'featuredProductsChk', 'subscribeAndSaveLbl', 'subscribeAndSaveChk', 
                'priceLbl', 'priceDecreaseBtn', 'priceIncreaseBtn', 'minLbl', 'minAmountLbl', 'maxLbl', 'maxAmountLbl', 'applyBtn', 'discountLbl', 'showMoreAgeGroupBtn', 'showMoreBrandBtn']
        for item in arrObj:
            uCommon.expectOptElemToBeVisible(page, pShop.sl.__dict__[item])
        arrObj = ['colorLbl', 'firstColorLbl', 'firstColorChk', 'showMoreColorBtn', 'ageGroupLbl', 'firstAgeGroupLbl', 'firstAgeGroupChk',  'genderLbl', 'firstGenderLbl', 
                'firstGenderChk', 'brandLbl', 'firstBrandLbl', 'firstBrandChk', 'sortByLbl', 'firstHeartIconBtn', 'paginationLbl']
        if blnSearch == False:
            arrObj.extend(['popularityBtn', 'popularityDbtn'])
        else:
            arrObj.extend(['relevanceBtn', 'relevanceDbtn'])
        for item in arrObj:
            uCommon.expectElemToBeVisible(page, pShop.sl.__dict__[item]) 
            
    @uCommon.ufuncLog  
    def validateDiscountRate(page, dictDetails):
        """ 
        Objective: Perform search item or brand name
        
        param dictDetails: Item or Brand Name
        returns: None
        Author: ccapistrano_20230327
        """
        for item in range(60):
            if uCommon.verifyVisible(page, pShop.sl.discountPercentLbl) == True:
                break
            uCommon.reloadPage(page)
            uCommon.wait(page, 5)
        uCommon.waitElemToBeVisible(page, pShop.sl.discountPercentLbl)
        if '%' in dictDetails['strTotalDiscount']:
            uCommon.validateElemText(page, pShop.sl.discountPercentLbl, dictDetails['strTotalDiscount'], False)
        uCommon.validateElemText(page, pShop.sl.priceOriginalLbl, dictDetails['strPriceOriginal'].replace(' ', ''))
        uCommon.validateElemText(page, pShop.sl.priceDiscountedLbl, dictDetails['strPriceDiscounted'].replace(' ', ''))
    
    @uCommon.ufuncLog
    def getItemDetails(page, strItemName):
        """ 
        Objective: Get item details
            
        param strItemName: Item Name
        returns dictData: strBrand, strName, strPrice
        Author: cgrapa_20230615
        """
        strBrand = uCommon.getElemText(page, pShop.com.itemBrandNameLbl(strItemName))
        strName = uCommon.getElemText(page, pShop.com.itemNameLbl(strItemName))
        strPrice = uCommon.getElemText(page, pShop.com.itemOriginalPriceLbl(strItemName))
        dictData = {'strBrand': strBrand, 'strName': strName, 'strPrice': strPrice}
        return dictData
    
    @uCommon.ufuncLog
    def getItemDetailsAndClick(page, strItemName):
        """ 
        Objective: Get item details and click item
            
        param: None
        returns dictDetails: strBrand, strName, strPrice
        Author: cgrapa_20230615
        """
        dictData = lp.getItemDetails(page, strItemName)
        uCommon.waitAndClickElem(page, pShop.com.itemNameLbl(dictData['strName']))
        uCommon.waitElemToBeVisible(page, pShop.pf.itemBrandLbl)
        return dictData





class ss:
    """SUBRCRIBE AND SAVE PROMPT PAGE"""
    @uCommon.ufuncLog  
    def validateSubsAndSavePrompt(page):
        """ 
        Objective: Validate subs and save prompt elements
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """
        arrObj = ['subsAndSaveLbl', 'subsAndSaveMsg', 'xBtn', 'itemSmallPicImg', 'itemNameLbl', 'daysLbl', 'itemCountLbl',
                    'discountedPriceLbl', 'deliveryEveryMsg', 'viewSubscriptionPolicyBtn', 'howDoSubsWorkBtn', 'infoIconBtn', 'confirmAddToCartBtn']
        uCommon.scrollToElem(page, pShop.sp.subsAndSaveLbl) 
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pShop.sp.__dict__[item]) 
    
    @uCommon.ufuncLog 
    def clickConfirmAddToCart(page):
        """ 
        Objective: Click Confirm Add To Cart
        
        param: None
        returns: None
        Author: ccapistrano_20230327
        """     
        uCommon.wait(page, 1)
        uCommon.waitAndClickElem(page, pShop.sp.confirmAddToCartBtn)
        uCommon.expectElemNotToBeVisible(page, pShop.msg.youAreAlreadySubscribedLbl)
        sp.validateSuccessfulMessageModal(page)
            