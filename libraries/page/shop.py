def moreBtn(parentElm):
    return  f'({parentElm}/..//a[normalize-space(text())="More"])[1]'
def arrowForwardIconBtn(parentElm):
    return  f'{parentElm}/..//mat-icon[normalize-space(text())="arrow_forward"]'
def heartIconBtn(parentElm):
    return  f'({parentElm}/../..//mat-icon[@data-mat-icon-name="heart_wishlist"])[1]'
def heartActiveIconBtn(parentElm):
    return  f'({parentElm}/../..//mat-icon[@data-mat-icon-name="heart_wishlist_clicked"])[1]'
def firstItemImg(parentElm):
    return f'({parentElm}/../..//div[@class="product-card-image"])[1]'
def firstItemBrandLbl(parentElm):
    return  f'({parentElm}/../../..//span[@class="brand"])[1]'
def firstItemNameLbl(parentElm):
    return  f'({parentElm}/../..//span[@class="itemname"])[1]'
def firstItemPriceLbl(parentElm):
    return  f'({parentElm}/../..//div[@class="rf-product-price price"]/p)[1]'
def nextSwiperBtn(parentElm):
    return  f'{parentElm}/..//a[normalize-space(text())="More"]'





class com:
    """COMMON"""
    def itemNameLbl(strItemName):
        return f'//span[@class="itemname"][contains(text(),"{strItemName}")]'
    def ItemPicImg(strItemName):
        return f'//span[@class="itemname"][contains(text(),"{strItemName}")]/../../../..//div[@class="product-card-image"]'
    def itemBrandNameLbl(strItemName):
        return f'//span[@class="itemname"][contains(text(),"{strItemName}")]/..//span[@class="brand"]'
    def itemPriceLbl(strItemName):
        return f'//span[@class="itemname"][contains(text(),"{strItemName}")]/../../..//div[@class="rf-product-price price"]/p'
    def itemOriginalPriceLbl(strItemName):
        return f'//span[contains(text(),"{strItemName}")]/../../..//p[contains(@class,"original")]'
    def itemDiscountedPriceLbl(strItemName):
        return f'//span[contains(text(),"{strItemName}")]/../../..//p[contains(@class,"discounted")]'
   
   
   
    
class tabs:
    """TABS"""
    bannerDescLbl = '//p[contains(@class,"message")][contains(text(),"NATIONWIDE DELIVERY")]'
    allCategoriesBtn = '//a[text()="All Categories"][@href="/shop/listing"]'
    diaperingBtn = '//li/a[contains(text(),"Diapering")]'
    fashionBtn = '//li/a[contains(text(),"Fashion")]'
    foodAndNutrition = '//li/a[contains(text(),"Food & Nutrition")]'
    nurseryBtn = '//li/a[contains(text(),"Nursery")]'
    feedingAndMealTimeBtn = '//li/a[contains(text(),"Feeding & Mealtime")]'
    mamaBtn = '//li/a[contains(text(),"Mama")]'
    babyGearBtn = '//li/a[contains(text(),"Baby Gear")]'
    homeAndLifeStyleBtn = '//li/a[contains(text()," Home & Living ")]'
    ToysAndLearningBtn = '//li/a[contains(text(),"Toys & Learning")]'
    furmamaBtn = '//li/a[contains(text(),"Furmama")]'
    bathAndBodyBtn = '//li/a[normalize-space(text())="Bath & Body"]'
    def categoryBtn(strCategory):
        return f'//li[contains(@class,"category-nav-item")]/a[text()="{strCategory}"]'
    def lvl3Category(strName):
        return f'//div[@class="all-cat-wrapper"]//a[contains(text(),"{strName}")]'
    
    
    class ac:
        """ALL CATEGORIES"""
        parentDIV = '//div[@class="all_cat_drop_down_wrapper"]'
        # shopAllBtn = '//a[@href="/shop/listing"][text()="SHOP ALL"]'
        diaperingBtn = f'{parentDIV}//a[@href="shop/listing/diapering"][text()="Diapering"]'
        wipesBtn = f'{parentDIV}//a[@href="shop/listing/diapering/wipes"][text()="Wipes"]'
        diapersBagBtn = f'{parentDIV}//a[@href="shop/listing/diapering/diaper-bags"][text()="Diaper Bags"]'
        changingMatTablesBtn = f'{parentDIV}//a[@href="shop/listing/diapering/changing-mats-and-tables"][text()="Changing Mats & Tables"]'
        disposableDiapersBtn = f'{parentDIV}//a[@href="shop/listing/diapering/disposable-diapers"][text()="Disposable Diapers"]'
        clothDiapersBtn = f'{parentDIV}//a[@href="shop/listing/diapering/cloth-diapers"][text()="Cloth Diapers"]'
        
        fashionBtn = f'{parentDIV}//a[@href="shop/listing/fashion"][text()="Fashion"]'
        sleepWearBtn = f'{parentDIV}//a[@href="shop/listing/fashion/sleepwear"][text()="Sleepwear"]'
        womensFashionBtn = f'{parentDIV}//a[@href="shop/listing/fashion/women-s-fashion"][text()="Women\'s Fashion"]'
        sweatShirtsJacketBtn = f'{parentDIV}//a[@href="shop/listing/fashion/sweatshirts-and-jacket"][text()="Sweatshirts & Jacket"]'
        socksTightsBtn = f'{parentDIV}//a[@href="shop/listing/fashion/socks-and-tights"][text()="Socks & Tights"]'
        innerWearBtn = f'{parentDIV}//a[@href="shop/listing/fashion/innerwear"][text()="Innerwear"]'
        onesieRomperBtn = f'{parentDIV}//a[@href="shop/listing/fashion/onesie-and-romper"][text()="Onesie and Romper"]'
        shortSkirtsBtn = f'{parentDIV}//a[@href="shop/listing/fashion/shorts-and-skirts"][text()="Shorts & Skirts"]'
        topBottomSetBtn = f'{parentDIV}//a[@href="shop/listing/fashion/top-and-bottom-sets"][text()="Top & Bottom Sets"]'
        mensFashionBtn = f'{parentDIV}//a[@href="shop/listing/fashion/men-s-fashion"][text()="Men\'s Fashion"]'
        topsTshirtBtn = f'{parentDIV}//a[@href="shop/listing/fashion/tops-and-t-shirts"][text()="Tops & T-Shirts"]'
        parentChildSetBtn = f'{parentDIV}//a[@href="shop/listing/fashion/parent-and-child-sets"][text()="Parent & Child Sets"]'
        dressJumpsuitBtn = f'{parentDIV}//a[@href="shop/listing/fashion/dresses-and-jumpsuits"][text()="Dresses & Jumpsuits"]'
        costumesBtn = f'{parentDIV}//a[@href="shop/listing/fashion/costumes"][text()="Costumes"]'
        swimWearBenchWearBtn = f'{parentDIV}//a[@href="shop/listing/fashion/swimwear-and-beachwear"][text()="Swimwear & Beachwear"]'
        footWearBtn = f'{parentDIV}//a[@href="shop/listing/fashion/footwear"][text()="Footwear"]'
        kidsAccessoriesBtn = f'{parentDIV}//a[@href="shop/listing/fashion/kid-s-accessories"][text()="Kid\'s Accessories"]'

        foodNutritionBtn = f'{parentDIV}//a[@href="shop/listing/food-and-nutrition"][text()="Food & Nutrition"]'
        formulaMilkBtn = f'{parentDIV}//a[@href="shop/listing/food-and-nutrition/formula-and-milk"][text()="Formula & Milk"]'
        foodSnacksBtn = f'{parentDIV}//a[@href="shop/listing/food-and-nutrition/food-and-snacks"][text()="Food & Snacks"]'
        beveragesBtn = f'{parentDIV}//a[@href="shop/listing/food-and-nutrition/beverages"][text()="Beverages"]'
        vitaminsSupplementsBtn = f'{parentDIV}//a[@href="shop/listing/food-and-nutrition/vitamins-and-supplements"][text()="Vitamins & Supplements"]'
        healthyAlternativesBtn = f'{parentDIV}//a[@href="shop/listing/food-and-nutrition/healthy-alternatives"][text()="Healthy Alternatives"]'
        
        nurseryBtn = f'{parentDIV}//a[@href="shop/listing/nursery"][text()="Nursery"]'
        furnitueDecorBtn = f'{parentDIV}//a[@href="shop/listing/nursery/furniture-and-decor"][text()="Furniture & Decor"]'
        childProofingBtn = f'{parentDIV}//a[@href="shop/listing/nursery/childproofing"][text()="Childproofing"]'
        babyMonitorsBtn = f'{parentDIV}//a[@href="shop/listing/nursery/baby-monitors"][text()="Baby Monitors"]'
        cribEssentialsBtn = f'{parentDIV}//a[@href="shop/listing/nursery/crib-essentials"][text()="Crib Essentials"]'
        beddingEssentialsBtn = f'{parentDIV}//a[@href="shop/listing/nursery/bedding-essentials"][text()="Bedding Essentials"]'
        bouncersRockersSwingsBtn = f'{parentDIV}//a[@href="shop/listing/nursery/bouncers-rockers-and-swings"][text()="Bouncers, Rockers & Swings"]'
        playpensBtn = f'{parentDIV}//a[@href="shop/listing/nursery/playpens"][text()="Playpens"]'
        
        feedingMealtimeBtn = f'{parentDIV}//a[@href="shop/listing/feeding-and-mealtime"][text()="Feeding & Mealtime"]'
        bottlesCupAccBtn = f'{parentDIV}//a[@href="shop/listing/feeding-and-mealtime/bottles-cups-and-accessories"][text()="Bottles, Cups & Accessories"]'
        mealTimeBtn = f'{parentDIV}//a[@href="shop/listing/feeding-and-mealtime/mealtime"][text()="Mealtime"]'
        highChairsBtn = f'{parentDIV}//a[@href="shop/listing/feeding-and-mealtime/high-chairs"][text()="High Chairs"]'
        foodContainerUtensilsBtn = f'{parentDIV}//a[@href="shop/listing/feeding-and-mealtime/food-containers-and-utensils"][text()="Food Containers & Utensils"]'
        lunchBagsContainersBtn = f'{parentDIV}//a[@href="shop/listing/feeding-and-mealtime/lunch-bags-and-containers"][text()="Lunch Bags & Containers"]'
        feedingMatsBtn = f'{parentDIV}//a[@href="shop/listing/feeding-and-mealtime/feeding-mats"   ][text()="Feeding Mats"]'
        feedingSetBtn = f'{parentDIV}//a[@href="shop/listing/feeding-and-mealtime/feeding-set"][text()="Feeding Set"]'
        
        mamaBtn = f'{parentDIV}//a[@href="shop/listing/mama"][text()="Mama"]'
        lifeStyleWellnessBtn = f'{parentDIV}//a[@href="shop/listing/mama/lifestyle-and-wellness"][text()="Lifestyle & Wellness"]'
        breastFeedingBtn = f'{parentDIV}//a[@href="shop/listing/mama/breastfeeding"  ][text()="Breastfeeding"]'
        reproductiveHealthBtn = f'{parentDIV}//a[@href="shop/listing/mama/reproductive-health"][text()="Reproductive Health"]'
        maternityBtn = f'{parentDIV}//a[@href="shop/listing/mama/maternity"][text()="Maternity"]'
        
        babyGearBtn = f'{parentDIV}//a[@href="shop/listing/baby-gear"][text()="Baby Gear"]'
        carriersBtn = f'{parentDIV}//a[@href="shop/listing/baby-gear/carriers"][text()="Carriers"]'
        gearAccessoriesBtn = f'{parentDIV}//a[@href="shop/listing/baby-gear/gear-accessories"][text()="Gear Accessories"]'
        StrollerBtn = f'{parentDIV}//a[@href="shop/listing/baby-gear/stroller"][text()="Stroller"]'
        carSeatBtn = f'{parentDIV}//a[@href="shop/listing/baby-gear/car-seat"][text()="Car Seat"]'
        walkersBtn = f'{parentDIV}//a[@href="shop/listing/baby-gear/walkers"][text()="Walkers"]'
        boosterSeatsBtn = f'{parentDIV}//a[@href="shop/listing/baby-gear/booster-seats"][text()="Booster Seats"]'
        carryCotBtn = f'{parentDIV}//a[@href="shop/listing/baby-gear/carrycot"][text()="Carrycot"]'
        luggageBtn = f'{parentDIV}//a[@href="shop/listing/baby-gear/luggage"][text()="Luggage"]'

        homeLifeStyleBtn = f'{parentDIV}//a[@href="shop/listing/home-and-living"][text()="Home & Living"]'
        homeDecorBtn = f'{parentDIV}//a[@href="shop/listing/home-and-living/home-decor"][text()="Home Decor"]'
        cleaningBtn = f'{parentDIV}//a[@href="shop/listing/home-and-living/cleaning"][text()="Cleaning"]'
        bedroomBtn = f'{parentDIV}//a[@href="shop/listing/home-and-living/bedroom"][text()="Bedroom"]'
        laundryBtn = f'{parentDIV}//a[@href="shop/listing/home-and-living/laundry"][text()="Laundry"]'
        appliancesElectornicsBtn = f'{parentDIV}//a[@href="shop/listing/home-and-living/appliances-and-electronics"][text()="Appliances & Electronics"]'
        kitchenDiningBtn = f'{parentDIV}//a[@href="shop/listing/home-and-living/kitchen-and-dining"][text()="Kitchen & Dining"]'
        outdoorGardenBtn = f'{parentDIV}//a[@href="shop/listing/home-and-living/outdoor-and-garden"][text()="Outdoor & Garden"]'
        homeOfficeBtn = f'{parentDIV}//a[@href="shop/listing/home-and-living/home-office"][text()="Home Office"]'
        sportsTravelBtn = f'{parentDIV}//a[@href="shop/listing/home-and-living/sports-and-travel"][text()="Sports & Travel"]'
        
        toysLearningBtn = f'{parentDIV}//a[@href="shop/listing/toys-and-learning"][text()="Toys & Learning"]'
        artsCraftsBtn = f'{parentDIV}//a[@href="shop/listing/toys-and-learning/arts-and-crafts"][text()="Arts & Crafts"]'
        toysBtn = f'{parentDIV}//a[@href="shop/listing/toys-and-learning/toys"][text()="Toys"]'
        booksBtn = f'{parentDIV}//a[@href="shop/listing/toys-and-learning/books"][text()="Books"]'
        outdoorBtn = f'{parentDIV}//a[@href="shop/listing/toys-and-learning/outdoor"][text()="Outdoor"]'
        homeSchoolingBtn = f'{parentDIV}//a[@href="shop/listing/toys-and-learning/homeschooling"][text()="Homeschooling"]'
        
        furmamaBtn = f'{parentDIV}//a[@href="shop/listing/furmama"][text()="Furmama"]'
        petFoodBtn = f'{parentDIV}//a[@href="shop/listing/furmama/pet-food"][text()="Pet Food"]'
        bathingGroomingBtn = f'{parentDIV}//a[@href="shop/listing/furmama/bathing-and-grooming"][text()="Bathing & Grooming"]'
        petAccessoriesBtn = f'{parentDIV}//a[@href="shop/listing/furmama/pet-accessories"][text()="Pet Accessories"]'
        petHealthCareBtn = f'{parentDIV}//a[@href="shop/listing/furmama/pet-healthcare"][text()="Pet Healthcare"]'
        cleaningPottyBtn = f'{parentDIV}//a[@href="shop/listing/furmama/cleaning-and-potty"][text()="Cleaning & Potty"]'
        bowlsFeedersBtn = f'{parentDIV}//a[@href="shop/listing/furmama/bowls-and-feeders"][text()="Bowls & Feeders"]'
        petToysBtn = f'{parentDIV}//a[@href="shop/listing/furmama/pet-toys"][text()="Pet Toys"]'


     
     
        
class hs:
    """HOME SLIDER"""
    homeSliderImg = '//div[@class="edamama-shop"]//*[@slidertype="home"]'
    sliderSectionImg = '//section[contains(@class,"segment")]'
    whyMamasEdamamaLbl = '//h2[normalize-space(text())="Why mamas"][text()=" edamama "]'
    authenticImg = '//img[@src="assets/images/why-shop/authentic.svg"]'
    authenticLbl = '//figcaption[text()="Authentic, safe and trusted brands only"]'
    expressDeliveryImg = '//img[@src="assets/images/why-shop/express.svg"]'
    expressDeliveryLbl = '//figcaption[text()="Express delivery - get your essentials in a jiffy!"]'
    curatedContentImg = '//img[@src="assets/images/why-shop/star.svg"]'
    curatedContentLbl = '//figcaption[text()="Curated content to inspire you as you shop"]'
    happinessGuaranteedImg = '//img[@src="assets/images/why-shop/girl.svg"]'
    happinessGuaranteedLbl = '//figcaption[text()="Happiness guaranteed with our mama-led team"]' 
    referralBannerImg = '//div[@class="credit-box-desktop pointer ng-star-inserted"]'
    referAFriendLbl = f'{referralBannerImg}//h2[contains(text()," Give ₱300, get ₱100 when you refer a friend ")]'
    referAFriendDescLbl = f'{referralBannerImg}//p[contains(text(),"Share your unique code with your friends and family!")]'
    referralCodeLbl = f'{referralBannerImg}//p[@class="info"]'
    
    allPaginatioBulletIconBtn = '//span[contains(@class,"swiper-pagination-bullet")]'
    def paginatioBulletBtn(intIndex):
        return f'(//div[contains(@class,"swiper-pagination")]/span)[{intIndex}]'
    allDataSwiperSlideImg = '//app-home-slider//div[@class="swiper-wrapper"]/div[contains(@class,"swiper-slide ng-star-inserted")]'
    def dataSwiperSlideImg(intIndex):
        return f'(//app-home-slider//div[@class="swiper-wrapper"]/div[contains(@class,"swiper-slide ng-star-inserted")])[{intIndex}]'
    def curatedTitleLbl(strTitle):
        return f'//section[@class="curated-products-wrapper"]//h3[@class="title -template"][contains(text(),"{strTitle}")]'
    def allCuratedTitleLbl(intIndex):
        return f'(//section[@class="curated-products-wrapper"]//h3[@class="title -template"])[{intIndex}]'
    

    


class fp:
    """FEATURED PRODUCTS"""
    featuredProductsLbl = '//h2[normalize-space(text())="Featured Products"]'
    moreBtn = moreBtn(featuredProductsLbl)
    arrowForwardIconBtn = arrowForwardIconBtn(featuredProductsLbl)
    heartIconBtn = heartIconBtn(featuredProductsLbl)
    heartActiveIconBtn = heartActiveIconBtn(featuredProductsLbl)
    firstItemImg = firstItemImg(featuredProductsLbl)
    firstItemBrandLbl = firstItemBrandLbl(featuredProductsLbl)
    firstItemNameLbl = firstItemNameLbl(featuredProductsLbl)
    firstItemPriceLbl = firstItemPriceLbl(featuredProductsLbl)
    nextSwiperBtn = nextSwiperBtn(featuredProductsLbl)
    
    firstItemDiscountedPriceLbl = f'({featuredProductsLbl}/../../..//div[@class="rf-product-price price"]/p[not(@class="col original -slashed ng-star-inserted")])[1]'





class an:
    """ANKO"""
    ankoLbl = '//h2[normalize-space(text())="Anko"]'
    moreBtn = moreBtn(ankoLbl)
    arrowForwardIconBtn = arrowForwardIconBtn(ankoLbl)
    heartIconBtn = heartIconBtn(ankoLbl)
    heartActiveIconBtn = heartActiveIconBtn(ankoLbl)
    firstItemImg = firstItemImg(ankoLbl)
    firstItemBrandLbl = firstItemBrandLbl(ankoLbl)
    firstItemNameLbl = firstItemNameLbl(ankoLbl)
    firstItemPriceLbl = firstItemPriceLbl(ankoLbl)
    nextSwiperBtn = nextSwiperBtn(ankoLbl)
   
   
   
   
    
class dc:
    """DISCOVER SECTION"""
    discoverLbl = '//h2[text()="Discover"]'
    tipsGuideLbl = f'{discoverLbl}/../..//p[text()="Tips, guides & stories for mamas, by mamas"]'
    moreBtn = f'({discoverLbl}/../..//span[normalize-space(text())="More"])[1]'
    arrowForwardIconBtn = f'{discoverLbl}/..//mat-icon[normalize-space(text())="arrow_forward"]'
    nurtureBtn = f'({discoverLbl}/../../..//span[text()="Nurture"])[1]' # Possible defect
    
    
    
    
    
class bn:
    """BEAN"""
    beanLbl = '//h2[normalize-space(text())="bean"]'
    moreBtn = moreBtn(beanLbl)
    arrowForwardIconBtn = arrowForwardIconBtn(beanLbl)
    heartIconBtn = heartIconBtn(beanLbl)
    heartActiveIconBtn = heartActiveIconBtn(beanLbl)
    firstItemImg = firstItemImg(beanLbl)
    firstItemBrandLbl = firstItemBrandLbl(beanLbl)
    firstItemNameLbl = firstItemNameLbl(beanLbl)
    firstItemPriceLbl = firstItemPriceLbl(beanLbl)
    nextSwiperBtn = nextSwiperBtn(beanLbl)
    
    
    
    
    
class ss:
    """SUBSCRIBE and SAVE"""
    subscribeAndSaveLbl = '//h2[normalize-space(text())="Subscribe and Save"]'
    moreBtn = moreBtn(subscribeAndSaveLbl)
    arrowForwardIconBtn = arrowForwardIconBtn(subscribeAndSaveLbl)
    heartIconBtn = heartIconBtn(subscribeAndSaveLbl)
    heartActiveIconBtn = heartActiveIconBtn(subscribeAndSaveLbl)
    firstItemImg = firstItemImg(subscribeAndSaveLbl)
    firstItemBrandLbl = firstItemBrandLbl(subscribeAndSaveLbl)
    firstItemNameLbl = firstItemNameLbl(subscribeAndSaveLbl)
    firstItemPriceLbl = firstItemPriceLbl(subscribeAndSaveLbl)
    nextSwiperBtn = nextSwiperBtn(subscribeAndSaveLbl)
    subscribeAndSaveBtn = f'({subscribeAndSaveLbl}/../../..//button/span[text()="Next"]/../../..//div[contains(text(),"Subscribe & Save")])[1]'
    giftRegistryImg = '//img[@alt="Gift Registry Banner"]' # located between subscribeAndSave and baby gear section
    eGiftImg = '//img[@alt="Edamama E-Gifts"]' # located between subscribeAndSave and baby gear section
    
    
    
    
    
class bg:
    """BABY GEAR"""
    babyGearLbl = '//h2[normalize-space(text())="Baby Gear"]'
    moreBtn = moreBtn(babyGearLbl)
    arrowForwardIconBtn = arrowForwardIconBtn(babyGearLbl)
    heartIconBtn = heartIconBtn(babyGearLbl)
    heartActiveIconBtn = heartActiveIconBtn(babyGearLbl)
    firstItemImg = firstItemImg(babyGearLbl)
    firstItemBrandLbl = firstItemBrandLbl(babyGearLbl)
    firstItemNameLbl = firstItemNameLbl(babyGearLbl)
    firstItemPriceLbl = firstItemPriceLbl(babyGearLbl)
    nextSwiperBtn = nextSwiperBtn(babyGearLbl)
    
    
    
    
    
    
class fm:
    """FORMULA AND MILK"""
    formulaMilkLbl = '//h2[normalize-space(text())="Formula & Milk"]'
    moreBtn = moreBtn(formulaMilkLbl)
    arrowForwardIconBtn = arrowForwardIconBtn(formulaMilkLbl)
    heartIconBtn = heartIconBtn(formulaMilkLbl)
    heartActiveIconBtn = heartActiveIconBtn(formulaMilkLbl)
    firstItemImg = firstItemImg(formulaMilkLbl)
    firstItemBrandLbl = firstItemBrandLbl(formulaMilkLbl)
    firstItemNameLbl = firstItemNameLbl(formulaMilkLbl)
    firstItemPriceLbl = firstItemPriceLbl(formulaMilkLbl)
    nextSwiperBtn = nextSwiperBtn(formulaMilkLbl)
    
    
    
    
    
    
class ty:
    """TOYS"""
    toysLbl = '//h2[contains(normalize-space(text()),"Toys")]'
    moreBtn = moreBtn(toysLbl)
    arrowForwardIconBtn = arrowForwardIconBtn(toysLbl)
    heartIconBtn = heartIconBtn(toysLbl)
    heartActiveIconBtn = heartActiveIconBtn(toysLbl)
    firstItemImg = firstItemImg(toysLbl)
    firstItemBrandLbl = firstItemBrandLbl(toysLbl)
    firstItemNameLbl = firstItemNameLbl(toysLbl)
    firstItemPriceLbl = firstItemPriceLbl(toysLbl)
    nextSwiperBtn = nextSwiperBtn(toysLbl)






class dl:
    """DOWNLOAD APP"""
    viberBannerImg = '//div[@class="banner-contact-container"]/a[@href="https://invite.viber.com/?g2=AQBDGz0A2R29%2BkxAIhFU2aMIseQGn5KgsEfZk0RE7aEfDbPtER1R9Fq1pdcadaUA"]'
    downloadTheEdamamaAppLbl = '//h3[text()="Download the edamama app now!"]'
    enjoyAFasterLbl = '//p[contains(text(),"Enjoy a faster, better shopping experience with edamama.")]'
    appStoreIconBtn = '//div[@class="row no-gutters"]//a[@href="https://apps.apple.com/app/edamama-mom-and-baby-shopping/id1545877212"]'
    googlePlayIconBtn = '//div[@class="row no-gutters"]//a[@href="https://play.google.com/store/apps/details?id=com.edamama.app"]'
    badgeMobileImg = '//img[starts-with(@src,"https://media-v4.edamama.ph/pre-fetch/https://www.")][contains(@src,".edamamalabs.net/assets/images/badge/huawei-badge.png")]'






class fs:
    """FLASH SALE"""
    flashSaleTitleLbl = '//h2[@class="flash-sale-title"]'
    firstItemImg = f'({flashSaleTitleLbl}/../../..//div[@class="product-card-image"])[1]'
    firstItemBrandLbl = f'({flashSaleTitleLbl}/../../..//span[@class="brand"])[1]'
    firstItemNameLbl = f'({flashSaleTitleLbl}/../../..//span[@class="itemname"])[1]'
    firstItemPriceLbl = f'({flashSaleTitleLbl}/../../..//div[@class="rf-product-price price"]/p)[1]'
    counterLbl = '//div[@class="flash-deal-countdown -homepage ng-star-inserted"]'
    
    
    
    
    
    
class rs:
    """RETAIL SALE"""
    def discountLbl(strProductName):
        return f'//h2[contains(text(),"")]/../..//span[@class="itemname"][contains(text(),"{strProductName}")]/../../../..//div[contains(@class,"-discount")]'
    
    
    
    
    
# ---------------------------------------------------- PRODUCT PAGE----------------------------------------------------
class pf:
    """PRODUCT FORM"""
    # ---------------------------------------------------- COMMON PRODUCT FORM ELEMENTS----------------------------------------------------
    homeLnk = '//a[@href="/shop"][contains(text(),"Home")]'
    heartIconBtn = '//button//mat-icon[normalize-space(text())="favorite_border"]'
    heartActiveIconBtn = '//button//mat-icon[normalize-space(text())="favorite"]'
    shareBtn = '//button//mat-icon[contains(text(),"share")]'
    itemSmallPicImg = '(//span[@class="visually-hidden"]/../img)[2]'
    itemLargePicImg = '(//span[@class="visually-hidden"]/../img)[1]'
    itemBrandLbl = '(//a[@class="brand ng-star-inserted"])[2]'
    itemNameLbl = '(//span[@class="name ng-star-inserted"])[2]'
    itemPriceLbl =  '//span[contains(@class,"original")]'
    itemDisPriceLbl =  '//span[contains(@class,"discounted")]'
    quantityLbl = '//label[text()="Quantity"] | //div[text()="Quantity"]'
    thisItemLbl = '//span[text()="This item qualifies for:"]'
    sevenDaysRefundableImg = '//img[@src="/assets/images/delivery-icons/refundable.svg"]'
    sevenDaysRefundableLbl = '//figcaption[contains(text(),"7-Day Returns")]'
    cashOnDeliverImg = '//img[@src="/assets/images/delivery-icons/cod.svg"]'
    cashOnDeliverLbl = '//figcaption[contains(text(),"Cash on Delivery")]'
    groupBuyImg = '//img[@src="/assets/images/delivery-icons/group.svg"]'
    groupBuyLbl = '//figcaption[contains(text(),"Group Buy")]'
    subscribeAndSaveImg = '//img[@src="/assets/images/delivery-icons/subscribe.svg"]'
    subscribeAndSaveLbl = '//figcaption[contains(text(),"Subscribe & Save")]'
    expressDeliveryImage = '//img[@src="/assets/images/delivery-icons/expected.svg"]'
    expressDeliveryLbl = '//strong[text()="Express Delivery"]'
    forOrdersBeforeLbl = '//figcaption[contains(text(),"for orders before 5PM")]'
    addtoBagBtn = '//button//span[contains(text(),"Add to Bag")]'
    
    itemDiscountedPriceLbl = '//div[@class="product_price"]/span[not(@class="discounted-price")]'
    colorLbl = '//div[@class="colors ng-star-inserted"]/div[normalize-space(text())="Color"]'
    colorOptionBtn = f'{colorLbl}/..//button'
    def colorBtn(strColor):
        return f'//legend[text()="Product Choices/Variants"]/..//span[normalize-space(text())="{strColor}"]'
    firstSizeBtn = '(//div[text()=" Size "]/..//button)[1]'
    outOfStockBtn = '//button//span[text()="Out Of Stock"]'
    discountLbl = '//span[contains(@class,"percentage")]'
    
    # ---------------------------------------------------- FEATURE PRODUCT ELEMENTS----------------------------------------------------
    quantityMinusIconBtn = '//button//mat-icon[text()="remove"]' # not in ss
    quantityOutputLbl = '//input[@id="inputQuantitySelector"]' # not in ss
    quantityPlusIconBtn = '//button//mat-icon[text()="add"]' # not in ss
    
    # ---------------------------------------------------- SUBSCRIBE AND SAVE ELEMENTS----------------------------------------------------
    giftBtn = '//mat-icon[@svgicon="edamama:pdp_add_to_gift_list"]'
    quantityCountLbl = f'{quantityLbl}/..//select[contains(@class,"select-dropdown")]'
    quantityDrp = f'{quantityCountLbl}/..//div[@class="select_arrow"]'
    subsAndSaveRdb = '//span[@class="mat-radio-inner-circle"]'
    subsAndSaveLbl = '//span[contains(text(),"Subscribe and save")]'
    purchaseTypeLbl = '//legend[contains(text(),"Purchase Type")]'
    days15Lbl = '//select[@id="sns-frequency"]'
    days15Drp = f'{days15Lbl}/..//select'
    priceLbl = '//span[@class="d-block"]'
    howdoSubsWorkLbl = '//span[text()="How do subscriptions work?"]'
    infoIconBtn = f'{howdoSubsWorkLbl}/..//mat-icon'
    
    def daysOptionLbl(strDayOption):
        return f'//option[contains(text(),"{strDayOption}")]'
    
    
    
    
    
    
class pd:
    """PRODUCT DESCRIPTION"""
    descriptionBtn = '//button/..//div[text()="Description"]'
    descriptionTitleLbl = f'{descriptionBtn}/../../../../../..//h2[@class="title"]'
    descriptionContentLbl = f'({descriptionBtn}/../../../../../..//p)[1]'






class ps:
    """PRODUCT SPECIFICATION"""
    productSpecificationBtn = '//button/..//div[text()="Product Specification"]'
    productSpecificationTitleLbl = f'{productSpecificationBtn}/../../../../../..//h2[@class="title"]'
    productSpecificationContentLbl = f'({productSpecificationBtn}/../../../../../..//p)[1]'






class rr:
    """RATINGS AND REVIEWS"""
    ratingsAndReviewLbl = '//h3[text()="Ratings & Reviews"]'
    
    
    
    
    
    
class rp:
    """RELATED PRODUCTS"""
    relatedProductsLbl = '//a[text()="Related Products"]'
    showMoreBtn = '//a[normalize-space(text())="Show me more products"]'






class sp:
    """SUBSCRIBE AND SAVE PROMPT"""
    subsAndSaveLbl = '//h2[text()="Subscribe & Save"]'
    subsAndSaveMsg = '//p[contains(text(),"You’re about to add a subscription into your cart,")][text()=" Please review and confirm to continue: "]'
    xBtn = '//mat-icon[@svgicon="edamama:close-small-green"]'
    itemSmallPicImg = '//img[@class="media"]'
    itemNameLbl = '(//div[contains(@class,"subscription-product-info")]/span)[1]'
    daysLbl = '(//div[contains(@class,"subscription-product-info")]/span)[2]'
    itemCountLbl = '(//div[contains(@class,"subscription-product-info")]/span)[3]'
    discountedPriceLbl = '//div[@class="price-info"]/span[contains(@class,"discounted")]'
    deliveryEveryMsg = '//p[starts-with(text()," Delivery every 15 days, save")][contains(text(),"on first order. Price varies and subject to change at anytime.")][text()=" for more information. "]'
    viewSubscriptionPolicyBtn = '//a[contains(text()," View subscription policy")]'
    howDoSubsWorkBtn = '//span[text()="How Do Subscriptions Work?"]'
    infoIconBtn = f'{howDoSubsWorkBtn}/..//mat-icon'
    confirmAddToCartBtn = '//button[contains(text(),"Confirm & Add to Cart")]'





# ---------------------------------------------------- LISTING PAGE ----------------------------------------------------
class sl:
    """SHOP LISTING"""
    categoriesLbl = '//h3[@class="title"][text()="Categories"]'
    lvl1CategoryLvl = '//li[@class="item"]//span[@class="text"]'
    productSpotLightLbl = '//h3[@class="title"][text()="Product Spotlight"]'
    allLbl = '//span[text()="All"]'
    allChk = f'{allLbl}/../..//label[@class="mat-checkbox-layout"]'
    featuredProductsLbl = '//span[text()="Featured Products"]'
    featuredProductsChk = f'{allLbl}/../..//label[@class="mat-checkbox-layout"]'
    subscribeAndSaveLbl = '//span[text()="Subscribe And Save"]'
    subscribeAndSaveChk = f'{allLbl}/../..//label[@class="mat-checkbox-layout"]'
    priceLbl = '//h3[@class="title"][text()="Price"]'
    priceDecreaseBtn = '(//mat-slider-visual-thumb)[1]'
    priceIncreaseBtn = '(//mat-slider-visual-thumb)[2]'
    minLbl = '//span[text()="min"]'
    minAmountLbl = f'{minLbl}/..//span[@class="value"]'
    maxLbl = '//span[text()="max"]'
    maxAmountLbl = f'{maxLbl}/..//span[@class="value"]'
    applyBtn = '//button/span[contains(text(),"Apply")]'
    discountLbl = '//h3[@class="title"][text()="Discount"]'
    allDiscountLbl = f'{discountLbl}/..//span[@class="mat-checkbox-label"]'
    allDiscountChk = f'{discountLbl}/..//span[@class="mat-checkbox-inner-container"]'
    colorLbl = '//h3[@class="title"][text()="Color"]'
    firstColorLbl = f'({colorLbl}/..//span[@class="mat-checkbox-label"])[1]'
    firstColorChk = f'({colorLbl}/..//span[@class="mat-checkbox-inner-container"])[1]'
    showMoreColorBtn = f'{colorLbl}/..//a[contains(text(),"+ Show More")]'
    ageGroupLbl = '//h3[@class="title"][text()="Age Group"]'
    firstAgeGroupLbl = f'({ageGroupLbl}/..//span[@class="mat-checkbox-label"])[1]'
    firstAgeGroupChk = f'({ageGroupLbl}/..//span[@class="mat-checkbox-inner-container"])[1]'
    showMoreAgeGroupBtn = f'{ageGroupLbl}/..//a[contains(text(),"+ Show More")]'
    genderLbl = '//h3[@class="title"][text()="Gender"]'
    firstGenderLbl = f'({genderLbl}/..//span[@class="mat-checkbox-label"])[1]'
    firstGenderChk = f'({genderLbl}/..//span[@class="mat-checkbox-inner-container"])[1]'
    brandLbl = '//h3[@class="title"][text()="Brand"]'
    firstBrandLbl = f'({brandLbl}/..//span[@class="mat-checkbox-label"])[1]'
    firstBrandChk = f'({brandLbl}/..//span[@class="mat-checkbox-inner-container"])[1]'
    showMoreBrandBtn = f'{brandLbl}/..//a[contains(text(),"+ Show More")]'
    
    sortByLbl = '//span[text()="Sort By"]'
    popularityBtn = '//button/span[contains(text(),"Popularity")]'
    popularityDbtn = f'{popularityBtn}/mat-icon'
    relevanceBtn = '//button/span[contains(text(),"Relevance")]'
    relevanceDbtn = f'{relevanceBtn}/mat-icon'
    firstHeartIconBtn = '(//mat-icon[@data-mat-icon-name="heart_wishlist"])[1]'
    showingOutOfLbl = '//p[contains(text(),"Showing")][contains(text(),"out of")][text()="product"]'
    allBrandName = '(//span[@class="brand"])[1]'
    def brandNameLbl(intIndex):
        return f'(//span[@class="brand"])[{intIndex}]'
    allItemNameLbl = '//span[@class="itemname"]'
    def itemNameLbl(intIndex):
        return f'(//span[@class="itemname"])[{intIndex}]'
    paginationLbl = '//div[@class="mat-paginator-container"]'
    
    discountPercentLbl = '//div[contains(@class,"-discount")]'
    priceOriginalLbl = '(//div[@class="rf-product-price price"]/p)[1]'
    priceDiscountedLbl = '(//div[@class="rf-product-price price"]/p)[2]'





class msg:
    """MESSAGE"""
    bagSuccessfullyMsg = '//span[text()="Product added to Bag Successfully!"]'
    youAreAlreadySubscribedLbl = '//span[text()="You are already subscribed to this product!"]'
    
    closeBtn = '//span[text()="Close"]'