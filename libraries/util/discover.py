import libraries.page.discover as pDiscover
import libraries.page.common.common as pCommon

import libraries.util.common as uCommon

class com:
    """COMMON"""
    @uCommon.ufuncLog 
    def navigateToDiscover(page):
        """ 
        Objective: Navigate to Discover page and validate Discover banner image
    
        param: None
        returns: None
        Author: cgrapa_20230518
        """
        uCommon.waitAndClickElem(page, pCommon.header.discoverBtn)
        uCommon.waitElemToBeVisible(page, pDiscover.al.discoverBannerImg)
            
    @uCommon.ufuncLog  
    def navigateToDiscoverCategories(page, strMenu):
        """ 
        Objective: Navigate to desired Discover category
   
        param strMenu: Menu
        returns: None
        Author: cgrapa_20230519
        """
        uCommon.wait(page, 1)
        if strMenu == 'all':
            uCommon.waitAndClickElem(page, pDiscover.com.allNavBtn)
            uCommon.waitElemToBeVisible(page, pDiscover.al.discoverBannerImg)
        elif strMenu == 'style':
            uCommon.waitAndClickElem(page, pDiscover.com.styleNavBtn)
            uCommon.waitElemToBeVisible (page, pDiscover.st.styleTitleLbl)
        elif strMenu == 'nurture':
            uCommon.waitAndClickElem(page, pDiscover.com.nurtureNavBtn)
            uCommon.waitElemToBeVisible (page, pDiscover.nu.nurtureTitleLbl)
        elif strMenu == 'play and learn':
            uCommon.waitAndClickElem(page, pDiscover.com.playAndLearnNavBtn)
            uCommon.waitElemToBeVisible (page, pDiscover.pl.playAndLearnTitleLbl)
        else:
            uCommon.log(2, f'Incorrect strMenu. Kindly use any of the ff: "all", "style", "nurture" or "play and learn"')
   
    @uCommon.ufuncLog
    def validateDiscoverNav(page):
        """ 
        Objective: Validate Discover navigation buttons
    
        param: None
        returns: None
        Author: cgrapa_20230518
        """
        arrObj = ['allNavBtn','styleNavBtn','nurtureNavBtn','playAndLearnNavBtn']
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pDiscover.com.__dict__[item])
   
    

   

class al:
    """ALL PAGE"""
    @uCommon.ufuncLog
    def validateDiscover(page):
        """ 
        Objective: Validate Discover page
    
        param: None
        returns: None
        Author: cgrapa_20230518
        """
        uCommon.waitForLoadState(page)
        com.validateDiscoverNav(page)
        arrObj = ['discoverBannerImg','featuredArticlesLbl','nurtureLbl','playAndLearnLbl','styleLbl','featuredArticleFirstImg','nurtureArticleFirstImg',
                  'playAndLearnArticleFirstImg','styleArticleFirstImg']
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pDiscover.al.__dict__[item])
        intDescLblCount = uCommon.getArrayCount(page, pDiscover.al.allArticlesDescPreviewLbl)
        assert intDescLblCount == 40, f'Discover page is expected to load 40 Articles - (Articles Loaded:{intDescLblCount})'





class st:
    """STYLE PAGE"""
    @uCommon.ufuncLog 
    def validateStyleCategory(page):
        """ 
        Objective: Validate Style category page and articles
    
        param: None
        returns: None
        Author: cgrapa_20230518
        """
        uCommon.waitForLoadState(page)
        ap.validateCategory(page)
        intTagCount = uCommon.getArrayCount(page, pDiscover.st.allStyleTagLbl)
        for index in range(intTagCount):
            uCommon.validateElemText(page, pDiscover.st.styleTagLbl(index+1), 'Style')





class nu:
    """NURTURE PAGE"""
    @uCommon.ufuncLog 
    def validateNurtureCategory(page):
        """ 
        Objective: Validate Nurture category page and articles
    
        param: None
        returns: None
        Author: cgrapa_20230518
        """
        uCommon.waitForLoadState(page)
        ap.validateCategory(page)
        intTagCount = uCommon.getArrayCount(page, pDiscover.nu.allNurtureTagLbl)
        for index in range(intTagCount):
            uCommon.validateElemText(page, pDiscover.nu.nurtureTagLbl(index+1), 'Nurture')





class pl:
    """PLAY AND LEARN PAGE"""
    @uCommon.ufuncLog 
    def validatePlayAndLearnCategory(page):
        """ 
        Objective: Validate Play & Learn category page and articles
        
        param: None
        returns: None
        Author: cgrapa_20230518
        """
        uCommon.waitForLoadState(page)
        ap.validateCategory(page)
        intTagCount = uCommon.getArrayCount(page, pDiscover.pl.allPlayAndLearnTagLbl)
        for index in range(intTagCount):
            uCommon.validateElemText(page, pDiscover.pl.playAndLearnTagLbl(index+1), 'Play & Learn')





class ap:
    """ARTICLE PREVIEWS"""
    @uCommon.ufuncLog 
    def validateCategory(page):
        """ 
        Objective: Validate Discover category preview articles
    
        param: None
        returns: None
        Author: cgrapa_20230518
        """
        uCommon.wait(page, 1)
        arrObj = ['articlePreviewImg','articlePreviewDateLbl','articlePreviewDescLbl']
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pDiscover.ap.__dict__[item])
        intArticleImgCount = uCommon.getArrayCount(page, pDiscover.ap.articlePreviewImg)
        intDescLblCount = uCommon.getArrayCount(page, pDiscover.ap.articlePreviewDescLbl)
        intDateLblCount = uCommon.getArrayCount(page, pDiscover.ap.articlePreviewDateLbl)
        assert intArticleImgCount == 25 and intDescLblCount == 25 and intDateLblCount == 25, f'Category Pages are expected to initially Load 25 Articles'





class ar:
    """ARTICLE PAGE"""
    @uCommon.ufuncLog 
    def validateArticle(page):
        """ 
        Objective: Validate article
    
        param: None
        returns: None
        Author: cgrapa_20230518
        """
        arrObj = ['articleBannerImg','articleCategoryLbl','articleAuthorLbl','articleTitleLbl']
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pDiscover.ar.__dict__[item])
            
    @uCommon.ufuncLog 
    def validateArticlesAndContents(page, strCategory, intArticles):
        """ 
        Objective: Validate article and its contents
        
        param strCategory: Category
        param intArticles: Number of Articles to check per Category
        returns: None
        Author: cgrapa_20230518
        """
        for index in range(intArticles):
            match strCategory:
                case 'featured articles':
                    uCommon.hoverAndClickElem(page, pDiscover.al.featuredArticleImg(index+1))
                case 'nurture':
                    uCommon.hoverAndClickElem(page, pDiscover.al.nurtureArticleImg(index+1))
                case 'play and learn':
                    uCommon.hoverAndClickElem(page, pDiscover.al.playAndLearnArticleImg(index+1))
                case 'style':
                    uCommon.hoverAndClickElem(page, pDiscover.al.styleArticleImg(index+1))
                case _:
                    uCommon.log(2, f'Incorrect strCategory. Kindly use any of the ff: "featured articles", "style", "nurture" or "play and learn"')
            ar.validateArticle(page)
            com.navigateToDiscoverCategories(page, 'all')