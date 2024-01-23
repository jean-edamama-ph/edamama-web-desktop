class com:
    """COMMON"""
    allNavBtn = '//a/span[text()="All"]'
    styleNavBtn = '//a/span[text()="Style "]'
    nurtureNavBtn = '//a/span[text()="Nurture "]'
    playAndLearnNavBtn = '//a/span[text()="Play & Learn "]'





class al:
    """ALL PAGE"""
    discoverBannerImg = '//edamama-slider-carousel[@class="ng-star-inserted"]'
    allArticlesDescPreviewLbl = '//h3[@class="font-weight-bold text-dark title"]'
    featuredArticlesLbl = '//h2[text()="Featured Articles"]'
    featuredArticleFirstImg = f'({featuredArticlesLbl}/..//img)[1]'
    nurtureLbl = '//h2[text()="Nurture"]'
    nurtureArticleFirstImg = f'({nurtureLbl}/..//img)[1]'
    playAndLearnLbl = '//h2[text()="Play & Learn"]'
    playAndLearnArticleFirstImg = f'({playAndLearnLbl}/..//img)[1]'
    styleLbl = '//h2[text()="Style"]'
    styleArticleFirstImg = f'({styleLbl}/..//img)[1]'
    def featuredArticleImg(intIndex):
        return f'({al.featuredArticlesLbl}/..//img)[{intIndex}]'
    def nurtureArticleImg(intIndex):
        return f'({al.nurtureLbl}/..//img)[{intIndex}]'
    def playAndLearnArticleImg(intIndex):
        return f'({al.playAndLearnLbl}/..//img)[{intIndex}]'
    def styleArticleImg(intIndex):
        return f'({al.styleLbl}/..//img)[{intIndex}]'





class st:
    """STYLE PAGE"""
    styleTitleLbl = '//h2//b[text()="Style"]'
    allStyleTagLbl = '//p//b[text()="Style"]'
    def styleTagLbl(intIndex):
        return f'({st.allStyleTagLbl})[{intIndex}]'





class nu:
    """NURTURE PAGE"""
    nurtureTitleLbl = '//h2//b[text()="Nurture"]'
    allNurtureTagLbl = '//p//b[text()="Nurture"]'
    def nurtureTagLbl(intIndex):
        return f'({nu.allNurtureTagLbl})[{intIndex}]'





class pl:
    """PLAY & LEARN PAGE"""
    playAndLearnTitleLbl = '//h2//b[text()="Play & Learn"]'
    allPlayAndLearnTagLbl = '//p//b[text()="Play & Learn"]'
    def playAndLearnTagLbl(intIndex):
        return f'({pl.allPlayAndLearnTagLbl})[{intIndex}]'





class ap:
    """ARTICLE PREVIEW"""
    articlePreviewImg = '//article//img[@class="image"]'
    articlePreviewDescLbl = '//article//p[@class="preview"]'
    articlePreviewDateLbl = '//article//p[@class="date"]'




  
class ar:
    """ARTICLE PAGE"""
    articleBannerImg = '//div[@class="header-wrapper"]//img[@class="image ng-star-inserted"]'
    articleCategoryLbl = '//a[@class="type ng-star-inserted"]'
    articleTitleLbl = '//h1[@class="title"]'
    articleAuthorLbl = '//a[@class="author"]'
    articleRelatedLbl = '//h2[@class="title"]'