class com:
    """COMMON"""
    nameLbl = '//h2[@class="name"]'
    emailLbl = '(//p[contains(@class,"user-email")])[2]'
    allMenuIconBtn = '//div[@class="row"]//div[@class="col-12 d-none d-md-block"]//mat-icon[text()="more_vert"]'
    def secondMenuIconBtn(strName):
        return f'(//div[@class="row"]//div[@class="col-12 d-none d-md-block"]//div[contains(text(),"{strName}")]/../..//mat-icon[text()="more_vert"])[1]' 
    removeIconBtn = '//mat-icon[text()="delete"]'
    yesBtn = '//span[text()=" Yes "]'
    addressDeletedSuccessMsg = '//span[text()="Address deleted successfully."]'
    mobileNumberLbl = '//div[@class="card-body"]//h4[@class="profile-mobile"]'
    mobileVerificationBtn = '//div[@class="profile-details"]//div[contains(@class,"verify-mobile")]'
    mobileEditNumberBtn = f'{mobileNumberLbl}/..//mat-icon[text()="edit"]'
    xBtn = '//mat-icon[text()="close"]'
    editBtn = '//div[@class="card-body"]/..//span[text() = " EDIT "]'
    def defaultLbl(strName):
        return f'//div[@class="row"]//div[@class="panel-header"][contains(text(),"{strName}")]/../..//span[text()=" Default "]'
    myAddressLbl = '//span[text()=" My Address "]'
    addressAddMoreBtn = f'{myAddressLbl}/..//span[text()=" ADD MORE "]'
    addressEditBtn = '//div[@role="menu"]/..//button[text()=" Edit "]'
    def addressContactNameLbl(strName):
        return f'//div[@class="row"]//div[@class="panel-header"][contains(text(),"{strName}")]'
    def addressDetailsLbl(strName): 
        return f'//div[@class="row"]//div[@class="panel-header"][contains(text(),"{strName}")]/../..//div[@class="adr"][1]'
    def addressStLbl(strName):
        return f'//div[@class="row"]//div[@class="panel-header"][contains(text(),"{strName}")]/../..//div[contains(text(),"Street")]'
    def addressZipLbl(strName):
        return f'//div[@class="row"]//div[@class="panel-header"][contains(text(),"{strName}")]/../..//div[contains(text(),"ZipCode")]'
    def addressMobNumLbl(strName):
        return f'//div[@class="row"]//div[@class="panel-header"][contains(text(),"{strName}")]/..//div[contains(text(),"Contact")]'
    childDetailsLbl = '//span[text()=" Child Details "]'
    addChildBtn = '//mat-icon[text()="add"]'
    addChildSuccessMsg = '//span[text()="Child has been added successfully"]'
    editChildSuccessMsg = '//span[text()="Child has been updated successfully"]'
    editChildBtn = '//div[@role="menu"]//button[text()="Edit"]'
    deleteChildBtn = '//div[@role="menu"]//button[text()="Delete"]'
    def childKebabBtn(strName):
        return f'//app-child-card[@class="ng-star-inserted"]/../..//h3[contains(text(),"{strName}")]/../..//mat-icon[text()="more_vert"]' 
    def childNameLbl(strName):
        return f'//h3[contains(text(),"{strName}")]/../../../../app-child-card[@class="ng-star-inserted"]'
    def addressDottedMenuIconBtn(strCount):
        return f'//div[@class="row"]//div[@class="col-12 d-none d-md-block"]/div[1]/div[contains(text(), "Address {strCount}")]/following-sibling::button'
    def addressPanelHeaderFullName(strCount):
        return f'//div[@class="row"]//div[@class="col-12 d-none d-md-block"]/div[1]/div[contains(text(), "Address {strCount}")]/../following-sibling::div/div[@class="panel-header"]'
    defaultAddressLbl = '//div[@class="row"]//div[@class="col-12 d-none d-md-block"]//span[contains(text(), "Default")]'
        




class mv:
    """MOBILE VERIFICATION FORM"""
    mobileNumberVerificatonLbl = '//p[@class="verify"]'
    mobileNumberTxt = '//input[@type="tel"]'
    sendMeTheCodeBtn = '//button//span[normalize-space(text())="Send Me The Code"]'
    contactSupportBtn = '//a[text()="Contact Support"]'
    enterPinLbl = '//p[text()="Enter the 6-Digit PIN"]'
    codeInputTxt = '//code-input[@class="inputer"]'
    pinTimerLbl = '//p[contains(@class,"timer")]'
    verifyCodeBtn = '//button//span[normalize-space(text())="Verify Code"]'
    closeBtn = '//mat-icon[text()="close"]'
    invalidPinErrorMsg = '//span[text()="PIN is required. Please input a PIN."]'





class ma:
    """MY ATTRIBUTES"""
    myAttributesLbl = '//span[text()="My Attributes"]'
    myAttributesAddEditBtn = '//div[@class="attribute-blk"]//button'
    allMyAttributesLbl = '//span[contains(@class,"attributes")]'
    allAttributesItemBtn = '//button[@class="attributes-btn ng-star-inserted"]'
    firstAttributeItemBtn = f'({allAttributesItemBtn})[1]'
    allActiveAttributesBtn = '//button[contains(@class,"attributes-btn active")]'
    firstActiveAttributesBtn = f'({allActiveAttributesBtn})[1]'
    attributesFormCloseBtn = '//button[@class="mat_close"]'
    attributesFormTitleLbl = '//h1[normalize-space(text())="Selected Attributes"]'
    attributesFormSubmitBtn = '//div[@class="attributes-list popup"]//span[normalize-space(text())="Submit"]'
    def attributeBtn(editAttribute):
        return f'//span[text()="{editAttribute}"]'
    def activeAttributeLbl(editAttribute):
        return f'//div[@class="attribute-blk"]//span[text()="{editAttribute}"]'
    maxAttributesSelectedMsg = '//span[text() = "Only 5 Attributes Can be selected!"]'

    
    
    

class ep:
    """Edit Profile"""
    editProfileLbl = '//h1[text()= "Edit Profile"]'
    updateBtn = '//span[text()= " Update "]'
    FirstNameLbl = '//mat-label [text() = "First Name"]'
    LastNameLbl = '//mat-label [text() = "Last Name"]'
    profileUpdatedSuccessfullyMsg = '//span[text()= "Profile Updated Successfully!"]'
    uploadPhotoBtn = '//span[text() = " Upload Photo "]'
    photoImg = f'{editProfileLbl}/..//img[@src="/assets/images/u_placeholder.svg"]' \
    f' | {editProfileLbl}/..//img[@src="https://media.kpc.edamamalabs.net/user/642397a6289a738f9b5a9133/profile-photo/profilepicture-default.jpg"]'
    selectBtn = '//button/span[text()=" Select "]'
    firstNameErrorMsg = '//mat-error[text()="Firstname can not be more than 40 characters long"]'
    lastNameErrorMsg = '//mat-error[text()="Lastname can not be more than 40 characters long"]'
    closeBtn = '//mat-icon[text()="close"]'


    
    
class na:
    """NEW ADDRESS"""
    newAddressLbl = '//h2[text()="New Address"]'
    firstNameTxt = '//input[@formcontrolname="firstName"]'
    lastNameTxt = '//input[@formcontrolname="lastName"]'
    mobileNumberTxt = '//input[@formcontrolname="phoneNumber"]'
    parentDIVListBox = '//div[@role="listbox"]'
    provinceDistrictLbl = '//label[text()="Province/District"]'
    provinceDistrictDownIconBtn = f'{provinceDistrictLbl}/..//div[contains(@class,"mat-select-arrow")]/div'
    searchTxt = '//input[@data-placeholder="Search"]'
    cityLbl = '//label[text()="City"]'
    cityDownIconBtn = f'{cityLbl}/..//div[contains(@class,"mat-select-arrow")]/div'
    barangayVillageLbl = '//label[text()="Barangay/Village"]'
    barangayVillageDownIconBtn = f'{barangayVillageLbl}/..//div[contains(@class,"mat-select-arrow")]/div'
    zipCodeTxt = '//input[@formcontrolname="zipCode"]'
    lotUnitStreetTxt = '//input[@formcontrolname="landmark"]'
    landmarkTxt = '//textarea[@formcontrolname="buildingNumber"]'
    addNewAddressBtn = f'{newAddressLbl}/../../..//button[text()=" Add New Address "]'
    addressAddedSuccessMsg = '//span[text()="Address added successfully."]'
    setAsDefaultChk = '//span[@class="mat-checkbox-inner-container"]'
    tickedDefaultChk = '//mat-checkbox[contains(@class, "mat-checkbox-checked")]'
    untickedDefaultChk = '//mat-checkbox[contains(@class, "mat-checkbox")]'

    
    
    

class ea:
    """EDIT ADDRESS"""
    editAddressLbl = '//h2[text()="Edit Address"]'
    updateAddressBtn = '//button[text()=" Update Address "]'
    addressEditedSuccessMsg = '//span[text()="Address updated successfully."]'
    errorMobileNumLengthMsg = '//mat-error[contains(text(), "Mobile Number length should be less than or equal to 10")]'

    


    
class ac:
    """ADD CHILD"""
    addChildLbl = '//h1[text()=" Add Child"]'
    childNameTxt = '//input[@data-placeholder="Child name / Alias"]'
    childDateBtn = '//button[@aria-label="Open calendar"]'
    def genderRdb(strGender):
        return f'//span[contains(text(),"{strGender}")]/../..//input[@class="mat-radio-input"]'
    def birthYearBtn(strYear):
        return f'//div[contains(text(),"{strYear}")]'
    def birthMonthBtn(strMonth):
        return f'//div[contains(text(),"{strMonth}")]'
    def birthDayBtn(strDay):
        return f'//button[contains(@class, "calendar")]//div[contains(text(),"{strDay}")]'
    addMoreBtn = '//span[text()="Add More +"]'




                
class ec:
    """EDIT CHILD"""
    editChildLbl = '//h1[text()=" Edit Child "]'
    updateBtn = '//span[text()=" Update "]'
    