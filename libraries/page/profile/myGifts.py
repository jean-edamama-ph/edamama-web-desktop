class com:
    """COMMON"""
    firstGiftList = '(//app-gift-list-card//img[contains(@src,"https://media-v4.")])[1] | (//app-my-gift-lists//img[contains(@src,"https://media-v4.")])[1]'
    addProductIconBtn = '//mat-icon[text()="add"]'
    ParentDIVElm = '//div[@class="eda-add-to-gift-list"]'
    addToGLIconBtn = f'{ParentDIVElm}//mat-icon[text()="add"]'
    registeredGiftsLbl = '//p[text()="Registered Gifts"]'
    moreIconBtn = f'{registeredGiftsLbl}/..//mat-icon[text()="more_horiz"]'
    removeFromGiftListBtn = '//button[text()=" Remove from Gift List "]'
    productAddedSuccessMsg = '//span[contains(text(),"Product added successfully !")]'
    enterEmailAddressLbl = '//p[text()="Enter Email Address"]'
    emailAddIconBtn = f'{enterEmailAddressLbl}/../..//button[@class="add-email-button"]'
    emailXIconBtn = '//mat-icon[text()="close"]'
    enterEmailAddressTxt = f'{enterEmailAddressLbl}/../..//input[@type="email"]'
    sendInvitesBtn = '//button[text()=" Send Invites "]'
    pleaseAddEmailErrorMsg = '//span[text()="Please add Email/s to invite!"]'
    giftListSharedSuccessMsg = '//span[text()="Gift List shared successfully!"]'
    productCounterLbl = '//p[@class="count"]'
    

    


class ml:
    """MY LIST"""
    howGiftRegistryWorksLbl = '//h2[text()="How Gift Registry Works"]'
    xIconBtn = '//mat-icon[text()="close"]'
    
    addIconBtn = '//img[@src="assets/images/plus.png"]'
    welcomeGiftListLbl = '//p[text()="Welcome to your Gift Lists!"]'
    editGiftListLbl = '//p[text() = "Edit Gift List"]'
    moreIconBtn = f'({welcomeGiftListLbl}/../../../..//mat-icon[text()="more_horiz"])[1]'
    allMeatBallsIconBtn = f'({welcomeGiftListLbl}/../../../..//mat-icon[text()="more_horiz"])'
    removeGiftListBtn = '//button[text()=" Remove Gift List "]'
    editGiftListBtn ='//button[text() = " Edit Gift List "]'
    buyGiftLbl = '//span[text()=" Buy Gift "]'
    buyGiftChk = f'{buyGiftLbl}/..//span[@class="mat-checkbox-background"]'
    AddNameMessageHereTxt = '//textarea[@placeholder="Add your name and a quick message here."]'
    buySelectedGiftsBtn = '//button[text()=" Buy Selected Gifts "]'
    archiveGiftListBtn = '//button[text()=" Archive Gift List "]'
    eventDateLbl = '//p[@class="date-text ng-star-inserted"]'
    archivedLbl = '//div[@class="date-wrapper"]/p[text()="Archived"]'
    unarchiveGiftListBtn = '//button[text()=" Unarchive Gift List "]'
    createGiftListBtn = '//button[text()= " Create a Gift List "]'
    
    def giftListTitlelbl (strTitle):
        return f'//p[@class="title"][text()="{strTitle}"]'
    def giftListDesclbl (strDesc):
        return f'//p[@class="description"][text()="{strDesc}"]'


    
        
    
class cr:
    """CREATE PAGE"""
    whatsTheOccasionLbl = '//label[text()="What\'s the occasion?"]'
    whatsTheOccasionTxt = f'{whatsTheOccasionLbl}/..//input'
    whenIsYourEventHappeningLbl = '//label[text()="When is your event happening?"]'
    calendarIcobnBtn = '//mat-icon[text()="edit_calendar"]'
    nextIconBtn = '//button[@class="change-month increase"]'
    seventhActiveDate = '(//li[not(contains(@class,"date disabled"))]/span[@class="text"])[7]'
    TwelfthActiveDate = '(//li[not(contains(@class,"date disabled"))]/span[@class="text"])[12]'
    confirmBtn = '//span[text()="Confirm"]'
    tellUsMoreAboutYourEventLbl = '//label[text()="Tell us more about your event..."]'
    tellUsMoreAboutYourEventTxt = f'{tellUsMoreAboutYourEventLbl}/..//textarea'
    createGiftListBtn = '//button/span[text()="Create Gift List"]'
    newGiftListCreatedLbl = '//h2[text()="New Gift List Created!"]'
    addressLbl = '//p[@class="address"]'
    cancelBtn = '//button[@class="cancel-gift-list-btn"]'
    plsCompleteFormLbl= '//span[text()="Please complete the Form!"]'
    addressPlusIconBtn = '//div[@class="icon ng-star-inserted"]'
    
    
    
    
    
    
class sh:
    """SHARED PAGE"""
    sharedWithMeBtn = '//li[text()=" Shared With Me "]'
    shareGiftListLbl = '//p[text()="Here are your shared Gift Lists!"]'
    
  
  
  
    
class ep:
    """EDIT PAGE"""
    photoCoverImg2Btn = '//img[contains(@src, "grv2-image-2.png")]'
    eventTitleTxt = '//div[@class = "event-title"]/input'
    eventDescriptionLbl = '//label[text()="Event Description"]'
    eventDescriptionTxt = f'{eventDescriptionLbl}/..//textarea'
    updateGiftListBtn = '//span[text()="Update Gift List"]'
    giftListUpdatedLbl = '//span[text()="Gift List Updated !"]'
    
    
    
 
    
class gl:
    """GIFT LIST PAGE"""
    def addedProdLbl (strItemName):
        return f'//p[text()="{strItemName}"]'
    