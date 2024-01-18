xBtn = '//button[@class="mat_close"]'
edamamaImg = '//img[@src="assets/images/edamamalogosquaregreen.png"]'





class com:
    """COMMON"""
    edamamaImg = edamamaImg
    loginBtn = '//div[text()="LOG IN"]'
    signUpBtn = '//div[text()="SIGN UP"]'
    creditsDescLbl = '//span[@class="credits"]'
    infoIconImg = '//mat-icon[text()="info"]'
    firstNameLbl = '//input[@data-placeholder="First Name"]/..//span[text()="First Name"]'
    emailAddressAsteriskLbl = '//input[@data-placeholder="First Name"]/..//span[text()="First Name"]/..//span[text()=" *"]'
    firstNameTxt = '//input[@data-placeholder="First Name"]'
    lastNameLbl = '//input[@data-placeholder="Last Name"]/..//span[text()="Last Name"]'
    lastAsteriskLbl = '//input[@data-placeholder="Last Name"]/..//span[text()="Last Name"]/..//span[text()=" *"]'
    lastNameTxt = '//input[@data-placeholder="Last Name"]'
    emailAddressLbl = '//input[@data-placeholder="Email Address"]/..//span[text()="Email Address"]'
    emailAddressAsteriskLbl = '//input[@data-placeholder="Email Address"]/..//span[text()="Email Address"]/..//span[text()=" *"]'
    emailAddressTxt = '//input[@data-placeholder="Email Address"]'
    passwordAddressLbl = '//input[@data-placeholder="Password"]/..//span[text()="Password"]'
    passwordAddressAsteriskLbl = '//input[@data-placeholder="Password"]/..//span[text()="Password"]/..//span[text()=" *"]'
    passwordAddressTxt = '//input[@data-placeholder="Password"]'
    visibilityOffIconBtn = '//mat-icon[contains(text(),"visibility_off")]'
    acceptChk = '//span[@class="mat-checkbox-frame"]/../..'
    acceptLbl = '//p[@class="text"]'
    privacyPolicyLnk = '//p/a[text()="Privacy Policy"][@href="/privacy-policy"]'
    termsOfUseLnk = '//p/a[normalize-space(text())="Terms of Use"][@href="/terms-of-use"]'
    continueBtn = '//button[text()="CONTINUE"]'
    continueWithFacebookBtn = '//button/span[contains(text(),"Continue with Facebook")]'
    facebookImg = '//img[@src="assets/images/socials/facebook.png"]'
    magSignInSaGoogleBtn = '//span[text()="Mag-sign up sa Google"][1]'





class av:
    """ACCOUNT VERIFICATION"""
    xBtn = xBtn
    accountVerificationLbl = '//h3[text()="Account Verification"]'
    aLinkHasBeenSentLbl = '//p[text()="A link has been sent to your registered email address."]'
    verifyYourEmailLbl = '//p[text()="Verify your email to complete your registration to get your bonus credits."]'
    okBtn = '//button/span[contains(text(),"OK")]'




  
class ev:
    """EMAIL VERIFICATION"""
    successIconImg = '//img[@src="success.jpg"]'
    xBtn = xBtn
    emailVerificationSuccessfullLbl = '//h2[text()="Email verification successful"]'
    userEmailLbl = '//p[@class="user-email"]'
    youHaveEarnedLbl = '//p[contains(text(),"You have earned")][text()=" by completing your signup! "]'
    fiveBeansLbl = '//span[text()="5 Beans"]'
    startShoppingBtn = '//button[contains(text(),"Start Shopping")]'
    getadditionalLbl = '//p[contains(text(),"Get additional")][text()=" by completing your profile "]'
    tenBeansLbl = '//span[text()="10 Beans"]'
    completeMyProfileBtn = '//a[contains(text(),"Complete My Profile")]'
    rightArrowBtn = f'{completeMyProfileBtn}/..//mat-icon[text()="chevron_right"]'





class ac:
    """ADD CHILD"""
    edamamaImg = edamamaImg
    childNameLbl = '//span[text()="Child name / Alias"]'
    childNameTxt = '//input[@data-placeholder="Child name / Alias"]'
    birthDateLbl = '//span[text()="Birthdate/Due Date"]'
    birthDateTxt = '//input[@data-placeholder="Birthdate/Due Date"]'
    calendarIconImg = '//button[@aria-label="Open calendar"]'
    genderLbl = '//div[text()="Gender*"]'
    boyLbl = '//span[contains(text(),"Boy")]'
    boyRdb = f'{boyLbl}/..//span[@class="mat-radio-outer-circle"]/../..'
    girlLbl = '//span[contains(text(),"Girl")]'
    girlRdb = f'{girlLbl}/..//span[@class="mat-radio-outer-circle"]/../..'
    ratherNotToSayLbl = '//span[contains(text(),"Rather not say")]'
    ratherNotToSayRdb = f'{ratherNotToSayLbl}/..//span[@class="mat-radio-outer-circle"]'
    addChildBtn = '//button/span[text()="Add Child"]'
    skipBtn = '//div[@class="form-btn"]//button/span[contains(text(),"Skip")]'
    nextBtn = '//div[@class="form-btn"]//button/span[contains(text(),"Next")]'
    
    def yearLbl(strYear):
        return f'//button/span[contains(text(),"{strYear}")]'
    def monthLbl(strMonth):
        return f'//button/span[contains(text(),"{strMonth}")]'
    def dateLbl(strDate):
        return f'//button/span[contains(text(),"{strDate}")]'
    childAddSuccessfullyMsg = '//*[text()="Child has been added successfully"]'





class ad:
    """ALMOST DONE"""
    edamamaImg = edamamaImg
    almostDoneLbl = '//h2[text()="Almost done!"]'
    pickAttributesDescLbl = '//p[contains(text(),"No two mamas are the same. Pick the attributes that best describe you,")]'
    rewardOnCompletingDescLbl = '//p[contains(text(),"5")][text()=" will be rewarded on completing this step. "]'
    beanIconImg = '//img[@src="assets/images/bean_solid.svg"]'
    activeMamaBtn = '//span[@class="attribute-image active_mama"]'
    activeMamaLbl = '//span[text()="Active Mama"]'
    careerMamaBtn = '//span[@class="attribute-image career_mama"]'
    careerMamaLbl = '//span[text()="Career Mama"]'
    craftyMamaBtn = '//span[@class="attribute-image crafty_mama"]'
    craftyMamaLbl = '//span[text()="Crafty Mama"]'
    dealQueenBtn = '//span[@class="attribute-image deal_queen"]'
    dealQueenLbl = '//span[text()="Deal Queen"]'
    expectingMamaBtn = '//span[@class="attribute-image expecting_mama"]'
    expectingMamaLbl = '//span[text()="Expecting Mama"]'
    fashionistaBtn = '//span[@class="attribute-image fashionista"]'
    fashionistaLbl = '//span[text()="Fashionista"]'
    firstTimeMamaBtn = '//span[@class="attribute-image first-time_mama"]'
    firstTimeMamaLbl = '//span[text()="First-time Mama"]'
    mamaChefBtn = '//span[@class="attribute-image mama_chef"]'
    mamaChefLbl = '//span[text()="Mama Chef"]'
    mamaTeacherBtn = '//span[@class="attribute-image mama_teacher"]'
    mamaTeacherLbl = '//span[text()="Mama Teacher"]'
    mamasteBtn = '//span[@class="attribute-image mamaste"]'
    mamasteLbl = '//span[text()="Mamaste"]'
    modernMamaBtn = '//span[@class="attribute-image modern_mama"]'
    modernMamaLbl = '//span[text()="Modern Mama"]'
    naturalMamaBtn = '//span[@class="attribute-image natural_mama"]'
    naturalMamaLbl = '//span[text()="Natural Mama"]'
    notAMamaBtn = '//span[@class="attribute-image not_a_mama"]'
    notAMamaLbl = '//span[text()="Not a Mama"]'
    partyPlannerBtn = '//span[@class="attribute-image party_planner"]'
    partyPlannerLbl = '//span[text()="Party Planner"]'
    stayAtHomeMamaBtn = '//span[@class="attribute-image stay-at-home_mama"]'
    stayAtHomeMamaLbl = '//span[text()="Stay-At-Home Mama"]'
    skipBtn = '//div[@class="form-btn ng-star-inserted"]//span[contains(text(),"Skip")]'
    nextBtn = '//div[@class="form-btn ng-star-inserted"]//span[contains(text(),"Back")]'
    
    submitBtn = '//button/span[contains(text(),"Submit")]'





class ty:
    """THANK YOU"""
    xBtn = xBtn
    thankYouLbl = '//h3[text()="Thank you for completing your profile!"]'
    thankYouDescLbl = '//p[text()="By completing your profile, you have been rewarded with points. Check My Profile>>My Credits to learn more about turning your beans into peso discounts at checkout!"]'
    continueBtn = '//button/span[contains(text(),"Continue")]'