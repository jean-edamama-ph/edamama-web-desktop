import pytest
import allure
import libraries.data.common as dCommon
import libraries.data.deploymentChecklist as dDepChkLst
import libraries.util.appCommon.appComm as uAppComm
import libraries.util.appCommon.email as uEmail
import libraries.util.appCommon.signUp as uSignUp
import libraries.util.common as uCommon
import libraries.util.profile.myOrders as uMyOrders
import libraries.util.appCommon.adminKpc as uAdminKpc
import libraries.util.shop as uShop


def test_Create_Test_User(page):
    arrEmailAddress = ['testkpcauto@gmail.com', 'testkpcmanual@gmail.com']
    dictNewAddress = {
                'strFName':'QA',
                'strLName': 'AUTOMATION',
                'strMobile': '9177654321',
                'strProvince': 'METRO MANILA',
                'strCity': 'NAVOTAS CITY',
                'selectBarangay': 'TANZA 1',
                'strZipCode': '2222',
                'strLotStreet': 'BLK 123',
                'strLandmark': 'ALING NENA STORE'
                } 
    
    intCnt = len(arrEmailAddress)
    for item in range(intCnt):
        uCommon.log(0, 'Step 1 - Go to https://www.kpc.edamamalabs.net/shop')
        uAppComm.ln.goToEdamamaURL(page)
        
        uCommon.log(0, 'Step 2 - Click Sign Up button')
        uSignUp.clickSignUp(page)
        uSignUp.validateSignUpPage(page)
        
        uCommon.log(0, 'Step 3 to 5 - Input Required fields >> Click policy checkbox >> Click Continue button')
        dCommon.signUp.dictData["strEmailAddress"] = arrEmailAddress[item]
        uSignUp.fillandContinueSignUpPage(page, dCommon.signUp.dictData)
        
        uCommon.log(0, 'Step 6 - In Email - verify Account in qa@edamama.ph mailbox. Click the link to verify the account')
        uSignUp.validateAndClickOKinAccountVerification(page)

        uCommon.log(0, 'Step 7 to 8 - Verify correct email was displayed >> Click completed my profile')
        uEmail.loginToGmail(page)
        uEmail.clickFirstConfirmEmail(page, dCommon.signUp.dictData)
        uEmail.clickYesThisIsMyEmail(page)
        window = uCommon.switchToWindow(page)
        uSignUp.validateEmailVerificationPageAndClickCompleteMyProfile(window)
        uSignUp.validateAddChildPage(window)
        
        uCommon.log(0, 'Step 9 to 10 - Input Required fields Child Name/Alias, Birthdate/Due Date, Gender >> Click Add Child')
        uSignUp.fillAndAddChild(window)
        uSignUp.validateAlmostDonePage(window)
        
        uCommon.log(0, 'Step 11 - Select attributes')
        uSignUp.clickNotAMama(window)
        
        uCommon.log(0, 'Step 12 - Click Submit')
        uSignUp.clickSubmit(window)
        
        uCommon.log(0, 'Step 13 - Click Continue button')
        uSignUp.validateThankYouAndClickContinue(window)
        print(f'user {arrEmailAddress[item]} is successfully created')
        uCommon.wait(page, 5)
        uAppComm.com.navigateToProfileMenu(window, 'my profile')
        uCommon.waitAndClickElem(window, '//span[text()=" My Address "]/..//button/span[text()=" ADD MORE "]')
        uMyOrders.di.na.fillOutNewAddress(window, dictNewAddress)
        uMyOrders.di.na.clickAddNewAddress(window)
        print(f'user {arrEmailAddress[item]} address added successfully')
        uAppComm.lo.logOutToEdamama(window)
        uCommon.closeWindow(window)
    uCommon.log(0, 'Test case completed')
    
def test_Add_New_Address(page):
    arrEmailAddress = ['testkpcauto@gmail.com', 'testkpcauto+1@gmail.com', 'testkpcauto+2@gmail.com', 'testkpcauto+3@gmail.com', 'testkpcauto+4@gmail.com', 'testkpcauto+5@gmail.com', 
                       'testkpcauto+6@gmail.com', 'testkpcauto+7@gmail.com', 'testkpcauto+8@gmail.com', 'testkpcauto+9@gmail.com', 'testkpcauto+10@gmail.com', ]
    dDepChkLst.AUTO666.dictNewAddress['strFName'] = 'DO NOT'
    dDepChkLst.AUTO666.dictNewAddress['strLName'] = 'DO DELETE'
    
    dictNewAddress = {
                'strFName':'QA',
                'strLName': 'AUTOMATION',
                'strMobile': '9177654321',
                'strProvince': 'METRO MANILA',
                'strCity': 'NAVOTAS CITY',
                'selectBarangay': 'TANZA 1',
                'strZipCode': '2222',
                'strLotStreet': 'BLK 123',
                'strLandmark': 'ALING NENA STORE'
                } 
    
    intCnt = len(arrEmailAddress)
    for item in range(intCnt):
        uAppComm.ln.loginToEdamama(page, arrEmailAddress[item], dCommon.user.strPassword1)
        uAppComm.com.navigateToProfileMenu(page, 'my profile')
        uCommon.waitAndClickElem(page, '//span[text()=" My Address "]/..//button/span[text()=" ADD MORE "]')
        uMyOrders.di.na.fillOutNewAddress(page, dictNewAddress)
        uMyOrders.di.na.clickAddNewAddress(page)
        print(f'user {arrEmailAddress[item]} address added successfully')
        uAppComm.lo.logOutToEdamama(page)
        
        
# Note: Update to your current time(Line 124)
def test_Create_Promo_Code(page):
    strPromoCode = 'EDAMAYA100'
    strCouponType = 'FLAT AMOUNT OFF'
    strCouponTags = 'Edamama Sponsored'
    strCouponDiscount = '100'

    # strPromoCode = 'BEAN300'
    # strCouponType = 'CREDIT BEANS'
    # strCouponTags = 'Edamama Sponsored'
    # strCouponDiscount = '300'
    
    # strPromoCode = 'CETAFLAT50'
    # strCouponType = 'FLAT AMOUNT OFF'
    # strCouponTags = 'Brand Sponsored'
    # strCouponDiscount = '50'
    
    # strPromoCode = 'EDAPERC10'
    # strCouponType = 'PERCENTAGE OFF'
    # strCouponTags = 'Edamama Sponsored'
    # strCouponDiscount = '10'
    
    arrTime = [8, 00, 'AM']
    strCouponDiscount = '10'
    strMaxDiscount = '50'
    intUses = '10000'
    uAppComm.ln.loginToAdminKPC(page)
    uCommon.wait(page, 1)
    uCommon.waitAndClickElem(page, '//h3[text()="Coupons/voucher"]')
    uAdminKpc.com.checkProgressBar(page)
    uCommon.waitAndClickElem(page, '//span[text()=" Add "]')
    uCommon.waitAndSetElem(page, '//input[@formcontrolname="couponCode"]', strPromoCode)
    uCommon.waitAndClickElem(page, '//mat-label[text()=" Coupon Type "]')
    uCommon.waitAndClickElemText(page, strCouponType)
    uCommon.waitAndClickElem(page, '//mat-label[text()=" Coupon Tags "]')
    uCommon.waitAndClickElemText(page, strCouponTags)
    uCommon.waitAndSetElem(page, '//input[@formcontrolname="discountValue"]', strCouponDiscount)
    if strPromoCode == 'EDAPERC10':
        uCommon.waitAndSetElem(page, '//input[@formcontrolname="maxDiscountValue"]', strMaxDiscount)
    uCommon.waitAndSetElem(page, '//input[@formcontrolname="couponRule"]', strPromoCode)
    uCommon.waitAndClickElem(page, '//span[text()="Website"]/..//input')
    uCommon.waitAndClickElem(page, '//span[text()="Mobile App"]/..//input')
    uCommon.waitAndClickElem(page, '//span[text()="Is Expiry Date Active "]')
    uCommon.waitAndClickElem(page, '//input[@placeholder="From Date"]/../..//button[@aria-label="Open calendar"]')
    uCommon.waitAndClickElem(page, '(//div[@class="mat-calendar-body-cell-content mat-focus-indicator"])[1]')
    for item in range(arrTime[0]):
        uCommon.waitAndClickElem(page, '(//button//mat-icon[text()="expand_less"])[1]')
    for item in range(arrTime[1]):
        uCommon.waitAndClickElem(page, '(//button//mat-icon[text()="expand_less"])[2]')
    if arrTime[2] == 'PM':
        uCommon.waitAndClickElem(page, '//span[text()=" AM "]')
    uCommon.waitAndClickElem(page, '//mat-icon[text()="done"]')
    uCommon.waitAndSetElem(page, '(//div[@class="ck-blurred ck ck-content ck-editor__editable ck-rounded-corners ck-editor__editable_inline"])[1]', strPromoCode)
    uCommon.waitAndSetElem(page, '(//div[@class="ck-blurred ck ck-content ck-editor__editable ck-rounded-corners ck-editor__editable_inline"])[1]', strPromoCode)
    uCommon.waitAndClickElem(page, '//input[@formcontrolname="uses"]')
    uCommon.waitAndSetElem(page, '//input[@formcontrolname="uses"]', intUses)
    uCommon.waitAndSetElem(page, '//input[@formcontrolname="usesPerCustomer"]', intUses)
    if strPromoCode == 'CETAFLAT50':
        uCommon.waitAndClickElem(page, '//mat-label[text()=" Brand "]')
        uCommon.waitAndSetElem(page, '//input[@placeholder="Search..."]', 'ceta')
        uCommon.wait(page, 1)
        uCommon.waitAndClickElem(page, '//input[@placeholder="Search..."]/../../..//span[text()="Cetaphil"]')
        uCommon.waitAndClickElem(page, '//input[@placeholder="Search..."]/../../..//span[text()="Cetaphil Baby"]')
    elif strPromoCode == 'EDAMAYA100':
        uCommon.waitAndClickElem(page, '//mat-label[text()=" Brand "]')
        uCommon.wait(page, 1)
        uCommon.waitAndClickElem(page, '//input[@placeholder="Search..."]/../../..//span[text()="All"]')
        uCommon.wait(page, 1)
        uCommon.waitAndClickElem(page, '//span[text()=" Add "]')
        uCommon.wait(page, 1)
        uCommon.waitAndClickElem(page, '//mat-label[text()=" Payment Method "]')
        uCommon.wait(page, 1)
        uCommon.waitAndClickElemText(page, 'Maya')
        uCommon.waitAndClickElem(page, '//span[text()=" Add "]')
    uCommon.waitAndClickElem(page, '//span[text()="Is Visible to Customers "]')
    uCommon.wait(page, 1)
    uCommon.waitAndClickElem(page, '//span[text()=" Add "]')
    uCommon.waitElemToBeVisible(page, '//span[text()="Coupon has been added successfully"]')
    uCommon.waitElemNotToBeVisible(page, '//span[text()="Coupon has been added successfully"]')
    
    
    # CLEAN UP DB TO DOs
    # Step1: Execute test_Create_Test_User in playwright_WEB
    # Step2: Mobile verification in mongoDB
    # Step3: Add Beans in AP
    # Step4: Execute the script below in BackEnd Monolith
    # npm run _cli/run createDummyCustomer -- --bundleId=kpc --count=50 --start=1 --email=testkpcauto@gmail.com - AUTOMATION testkpcauto+1@gmail.com/Edamama@123!
    # npm run _cli/run createDummyCustomer -- --bundleId=kpc --count=100 --start=1 --email=testkpcmanual@gmail.com - MANUAL testkpcmanual+1@gmail.com/Edamama@123!
    
    # Optional
    #  Step5: Sync "Plus Jumbo Pack Tape Diaper Large (42 pcs x 3 pack) - Subscription" in AP, also check if published. Check quantity.
    
    
    
""" Author: ccapistrano_20240108 | Execution Time: 6m 55s """
@pytest.mark.deploymentChecklist()
@allure.step('Verifying that the admin panel user can add a product')
def test_AUTO_635_Add_New_Product_in_Admin_Panel_Listing(page):
    uCommon.log(0, 'Step 1 to 3 - Go to admin panel website and login')
    uAppComm.ln.loginToAdminKPC(page)
    
    for item in range(10):
        uCommon.log(0, 'Step 4 to 5 - Click Products from the side navigation bar')
        uAdminKpc.pl.clickProductsThenSubMenu(page)
        
        uCommon.log(0, 'Step 6 - Click add button')
        uAdminKpc.pl.clickAdd(page)
        
        uCommon.log(0, 'Step 7 - Populate the following required fields with valid values')
        uAdminKpc.pl.bi.setProductName(page, f'AUTOMATION WEB {item}')
        uAdminKpc.pl.bi.selectCategory(page, dDepChkLst.AUTO635.dictData["strCategory"])
        uAdminKpc.pl.bi.selectBrand(page, dDepChkLst.AUTO635.dictData["strBrand"])
        uAdminKpc.pl.bi.selectVendor(page, dDepChkLst.AUTO635.dictData["strVendor"])
        uAdminKpc.pl.bi.selectBundleBuy(page, dDepChkLst.AUTO635.dictData["strBundleBuy"])
        uAdminKpc.pl.bi.selectAttributes(page, dDepChkLst.AUTO635.dictData["strAttributes"])
        uAdminKpc.pl.bi.setDescriptionAndSpecification(page, 'test description', 'test specification')

        uCommon.log(0, 'Step 8 - Click save and continue button')
        uAdminKpc.pl.bi.clickSaveAndContinue(page)
        
        uCommon.log(0, 'Step 9 to 13 - Select a color in Color dropdown field >> Click Add color button')
        uAdminKpc.pl.cv.addColor(page, dDepChkLst.AUTO635.dictData["strColor"], dDepChkLst.AUTO635.dictData["strPath"])

        uCommon.log(0, 'Step 14 to 18 - Select a pattern in Pattern dropdown field >> Click Add Add pattern button')
        
        uCommon.log(0, 'Step 19 - Populate the following fields in Variant')
        uAdminKpc.pl.cv.selectVariant(page, dDepChkLst.AUTO635.dictData["strVariant"])
        uAdminKpc.pl.cv.selectDisplayType(page, dDepChkLst.AUTO635.dictData["strDisplayType"])
        uAdminKpc.pl.cv.selectSelectTypeOptions(page, dDepChkLst.AUTO635.dictData["strTypeOptions"])
        
        uCommon.log(0, 'Step 20 - Click Add Variant button')
        uAdminKpc.pl.cv.clickAddVariant(page)
        
        uCommon.log(0, 'Step 21 - Populate the following fields in Filter')
        uAdminKpc.pl.cv.selectSelectFilters(page, dDepChkLst.AUTO635.dictData["strSelectFilters"]) # DEFECT ON AP - https://edamama.atlassian.net/browse/AUTO-728
        uAdminKpc.pl.cv.selectFiltersOptions(page, dDepChkLst.AUTO635.dictData["strFiltersOptions"])
        
        uCommon.log(0, 'Step 22 - Click Add Filters button')
        uAdminKpc.pl.cv.clickAddFilters(page)
        
        uCommon.log(0, 'Step 23 - Click Update and Continue button')
        uAdminKpc.pl.cv.clickUpdateAndContinue(page)
        
        uCommon.log(0, 'Step 24 - Click Published toggle button')
        uAdminKpc.pl.sp.setMRPpriceViaVariantname(page, dDepChkLst.AUTO635.dictData["strColor"], dDepChkLst.AUTO635.dictData["strPrice"])
        uAdminKpc.pl.sp.clickPublished(page)
        
        uCommon.log(0, 'Step 25 - Click Next button')
        uAdminKpc.pl.sp.clickUpdateAndContinue(page)
        
        uCommon.log(0, 'Step 26 - Click Save button')
        uAdminKpc.pl.at.clickSave(page)
        
        uCommon.log(0, 'Step 27 - Verify the recently added product')
        uAdminKpc.pl.searchProduct(page, f'AUTOMATION WEB {item}')
        uAdminKpc.pl.validatepublished(page, dDepChkLst.AUTO635.dictData["blnVisible"])
