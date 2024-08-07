import libraries.page.profile.myProfile as pMyProfile
import libraries.page.profile.myBeans as pMyBeans
import libraries.page.common.adminKpc as pAdminKpc

import libraries.util.common as uCommon
import libraries.util.appCommon.appComm as uAppComm
import libraries.util.appCommon.adminKpc as uAdminKpc


class com:
    """COMMON"""
    @uCommon.ufuncLog   
    def getMyProfileDetails(page):
        """ 
        Objective: Get My Profile Name
        param: None
        returns dictData: Data
        Author: ccapistrano_20230327
        """  
        strName = uCommon.getElemText(page, pMyProfile.com.nameLbl)
        strEmail = uCommon.getElemText(page, pMyProfile.com.emailLbl)
        strMobileNumber = uCommon.getElemText(page, pMyProfile.com.mobileNumberLbl)
        dictData = {'strName': strName, 'strEmail': strEmail, 'strMobileNumber': strMobileNumber}
        return dictData
    
    @uCommon.ufuncLog 
    def getAddressDetails(page, strFullName):
        """ 
        Objective: Get address details
        param: Full Name
        returns updatedDictAddress
        Author: abernal_20231009
        """ 
        strUpdatedName = uCommon.getElemText(page, pMyProfile.com.addressContactNameLbl(strFullName))
        strUpdatedAddressDetails = uCommon.getElemText(page, pMyProfile.com.addressDetailsLbl(strFullName))
        strUpdatedSt = uCommon.getElemText(page, pMyProfile.com.addressStLbl(strFullName))
        strUpdatedZip = uCommon.getElemText(page, pMyProfile.com.addressZipLbl(strFullName))
        strUpdatedMobNum = uCommon.getElemText(page, pMyProfile.com.addressMobNumLbl(strFullName))
        updatedDictAddress = {'strUpdatedName': strUpdatedName, 'strUpdatedAddressDetails': strUpdatedAddressDetails, 'strUpdatedSt': strUpdatedSt, 
                                'strUpdatedZip': strUpdatedZip, 'strUpdatedMobNum': strUpdatedMobNum}
        return updatedDictAddress


    @uCommon.ufuncLog   
    def deleteAddress(page, strName):
        """ 
        Objective: Perform delete of the selected address
        param: None
        returns strName: Name to be delete
        Author: ccapistrano_20230512
        """ 
        inctCount = uCommon.getArrayCount(page, pMyProfile.com.allMenuIconBtn)
        for item in range(inctCount):
            if uCommon.verifyVisible(page, pMyProfile.com.defaultLbl(strName)) == True:
                    uCommon.waitAndClickElem(page, pMyProfile.com.secondMenuIconBtn(strName))
                    uCommon.wait(page, 1)
                    uCommon.waitAndClickElem(page, pMyProfile.com.addressEditBtn)
                    ea.untickSetAsDefault(page)
                    ea.clickUpdateAddress(page)
            if uCommon.verifyVisible(page, pMyProfile.com.secondMenuIconBtn(strName)) == True:
                uCommon.waitAndClickElem(page, pMyProfile.com.secondMenuIconBtn(strName))
                uCommon.wait(page, .5)
                uCommon.waitAndClickElem(page, pMyProfile.com.removeIconBtn)
                uCommon.waitAndClickElem(page, pMyProfile.com.yesBtn)
                uCommon.waitElemToBeVisible(page, pMyProfile.com.addressDeletedSuccessMsg)
                uCommon.waitElemNotToBeVisible(page, pMyProfile.com.addressDeletedSuccessMsg)
                uCommon.wait(page, 1)
            else:
                break

    @uCommon.ufuncLog
    def closeAddEditForm(page):
        """ 
        Objective: Close Add/Edit forms
        param: None
        returns: None
        Author: cgrapa_20230613
        """
        uCommon.waitAndClickElem(page, pMyProfile.com.xBtn)
        uCommon.waitElemNotToBeVisible(page, pMyProfile.com.xBtn)
        
    @uCommon.ufuncLog   
    def clickAddAChild(page):
        """ 
        Objective: Perform click Add a Child button.
        param: None
        returns: None
        Author: abernal_20231011
        """
        uCommon.waitAndClickElem(page, pMyProfile.com.addChildBtn)
        uCommon.waitElemToBeVisible(page, pMyProfile.ac.addChildLbl)
        
    @uCommon.ufuncLog   
    def clickChildKebabMenu(page, strName):
        """ 
        Objective: Perform click of kebab menu of a specific child
        param: Child Name
        returns: None
        Author: abernal_20231011
        """
        uCommon.waitAndClickElem(page, pMyProfile.com.childKebabBtn(strName))
        uCommon.waitElemToBeVisible(page, pMyProfile.com.editChildBtn)
        
    @uCommon.ufuncLog   
    def clickEditChild(page):
        """ 
        Objective: Perform click Edit button on child
        param: None
        returns: None
        Author: abernal_20231011
        """
        uCommon.wait(page, .5)
        uCommon.waitAndClickElem(page, pMyProfile.com.editChildBtn)
        uCommon.waitElemToBeVisible(page, pMyProfile.ec.editChildLbl) 
        
    @uCommon.ufuncLog   
    def verifyUpdatedChildDetails(page, strName):
        """ 
        Objective: Perform verification of child details
        param: Child Name
        returns: None
        Author: abernal_20231011
        """
        uCommon.waitElemToBeVisible(page, pMyProfile.com.childNameLbl(strName))
        uCommon.waitAndValidateElemText(page, pMyProfile.com.childNameLbl(strName), strName, False)
        
    @uCommon.ufuncLog   
    def clickDeleteChild(page, strName = ''):
        """ 
        Objective: Perform click Delete button on child
        param: Child Name
        returns: None
        Author: abernal_20231011
        """
        uCommon.waitElemToBeVisible(page, pMyProfile.com.deleteChildBtn)
        uCommon.wait(page, .5)
        uCommon.waitAndClickElem(page, pMyProfile.com.deleteChildBtn)
        if strName != '':
            uCommon.waitElemNotToBeVisible(page, pMyProfile.com.childNameLbl(strName))
        else:
            uCommon.wait(page, 2)

    @uCommon.ufuncLog
    def clickEditbtn(page):
        """ 
        Objective: To click edit button and wait for the edit modal to be visible
        param: None
        returns: None
        Author: rmakiling_20230928
        """
        uCommon.waitAndClickElem(page, pMyProfile.com.editBtn)
        uCommon.waitElemToBeVisible(page, pMyProfile.ep.editProfileLbl)

    @uCommon.ufuncLog
    def clickAddressAddMore(page):
        """ 
        Objective: Click 'Add More' button on My Address
        
        param: None
        returns: None
        Author: abernal_20231001
        """
        uCommon.waitAndClickElem(page, pMyProfile.com.addressAddMoreBtn)
        uCommon.waitElemNotToBeVisible(page, pMyProfile.com.addressAddMoreBtn)

    @uCommon.ufuncLog
    def verifyDefaultLabel(page, strName):
        """ 
        Objective: Verify the default label for address.
        
        param strName: Full Name
        returns: None
        Author: abernal_20231005
        """
        uCommon.validateElemText(page, pMyProfile.com.defaultLbl(strName), "Default")
    
    @uCommon.ufuncLog
    def checkAndDeleteChild(page, strChildName):
        """ 
        Objective: Check and delete existing child
        
        param strName: Full Name
        returns: None
        Author: abernal_20231016
        """
        if uCommon.verifyVisible(page, pMyProfile.com.childKebabBtn(strChildName)) == True:
            uCommon.waitAndClickElem(page, pMyProfile.com.childKebabBtn(strChildName))
            uCommon.waitElemToBeVisible(page, pMyProfile.com.deleteChildBtn)
            uCommon.wait(page, .5)
            uCommon.waitAndClickElem(page, pMyProfile.com.deleteChildBtn)
            uCommon.waitElemNotToBeVisible(page, pMyProfile.com.childNameLbl(strChildName))
            
    @uCommon.ufuncLog
    def deleteAllAddress(page, dictAddress=''):
        """ 
        Objective: Delete all existing address
        param dictAddress: dictionary for the existing address of the user acct.
        returns: None
        Author: jatregenio_20240113
        """
        strAddressCount = ''
        intCount = uCommon.getArrayCount(page, pMyProfile.com.allMenuIconBtn)
        if intCount > 0:
            for item in range(intCount):
                intAddressCount = intCount - item
                if intAddressCount == 1:
                    strAddressCount = ' '
                else:
                    strAddressCount = intAddressCount
                
                strFullName = uCommon.getElemText(page, pMyProfile.com.addressPanelHeaderFullName(strAddressCount))
                blnIsDefaultAddressSet = uCommon.verifyVisible(page, pMyProfile.com.defaultLbl(strFullName))
                if blnIsDefaultAddressSet == True:
                    ea.clickAddressEdit(page, strFullName)
                    ea.untickSetAsDefault(page)
                    ea.clickUpdateAddress(page, dictAddress["strMobile"])
                    com.deleteAddress(page, strFullName)
                else:
                    com.deleteAddress(page, strFullName)
        else:
            uCommon.log(0, 'No existing address to be deleted.')         
    
    @uCommon.ufuncLog
    def checkIfTheresSetDefaultAddress(page):
        """ 
        Objective: Check if there is an existing address that was set to default.
        param: None
        returns: True | False
        Author: jatregenio_202400202
        """
        blnIsDefaultAddressSet = uCommon.verifyVisible(pMyProfile.com.defaultAddressLbl)
        if blnIsDefaultAddressSet == True:
            return True
        else:
            return False      
        
    @uCommon.ufuncLog
    def verifyEmailAddress(page):
        """ 
        Objective: To check that email address exists on Profile page.
        param: None
        returns: None
        Author: abernal_20240227
        """
        strEmail = uCommon.getElemText(page, pMyProfile.com.emailLbl)
        uCommon.validateElemText(page, pMyProfile.com.emailLbl, strEmail)
        
    @uCommon.ufuncLog
    def clickMyBeansTab(page):
        """ 
        Objective: To click My Beans tab.
        param: None
        returns: None
        Author: abernal_20240229
        """
        uCommon.waitAndClickElem(page, pMyProfile.com.myBeansBtn)
        uCommon.waitElemToBeVisible(page, pMyBeans.com.beanRewardLbl)
    

    
class na:
    @uCommon.ufuncLog
    def addAddress(page, dictData):
        """ 
        Objective: Perform add new address
    
        param: dictData: {strFirstName, strLastName, strMobile, strProvince, strCity, strZipCode, strBrgy, strLotUnitStBldg, strLandmark}
        returns: None
        Author: abernal_20230511
        """ 
        
        if dictData["strFirstName"] != None:
            uCommon.setElem(page, pMyProfile.na.firstNameTxt, dictData["strFirstName"])
        if dictData["strLastName"] != None:
            uCommon.setElem(page, pMyProfile.na.lastNameTxt, dictData["strLastName"])
        if dictData["strMobile"] != None:
            uCommon.setElem(page, pMyProfile.na.mobileNumberTxt, dictData["strMobile"])
        if dictData["strProvince"] != None:
            na.selectProviceDistrict(page, dictData["strProvince"])
        if dictData["strCity"] != None:
            na.selectCity(page, dictData["strCity"])
        if dictData["strZipCode"] != None:
            uCommon.setElem(page, pMyProfile.na.zipCodeTxt, dictData["strZipCode"])
        if dictData["strBrgy"] != None:   
            na.selectBarangay(page, dictData["strBrgy"])
        if dictData["strLotUnitStBldg"] != None:
            uCommon.setElem(page, pMyProfile.na.lotUnitStreetTxt, dictData["strLotUnitStBldg"])
        uCommon.setElem(page, pMyProfile.na.landmarkTxt, dictData["strLandmark"])          

    @uCommon.ufuncLog 
    def selectProviceDistrict(page, strProvince):
        """ 
        Objective: Click, set and select Provice or District
        
        param strProvince: Provice | District
        returns: None
        Author: ccapistrano_20230511
        """  
        uCommon.wait(page, .5)
        uCommon.waitAndClickElem(page, pMyProfile.na.provinceDistrictDownIconBtn)
        uCommon.setAndSelectFromSmartDropDown(page, pMyProfile.na.searchTxt, strProvince, pMyProfile.na.parentDIVListBox)
        uCommon.wait(page, 1)
        
    @uCommon.ufuncLog 
    def selectCity(page, strCity):
        """ 
        Objective: Click, set and select City
        
        param strCity: City
        returns: None
        Author: ccapistrano_20230511
        """  
        uCommon.waitAndClickElem(page, pMyProfile.na.cityDownIconBtn)
        uCommon.setAndSelectFromSmartDropDown(page, pMyProfile.na.searchTxt, strCity, pMyProfile.na.parentDIVListBox)
        uCommon.wait(page, 1)
        
    @uCommon.ufuncLog 
    def selectBarangay(page, strBarangay):
        """ 
        Objective: Click, set and select Barangay or Village
        
        param strBarangay: Barangay | Village
        returns: None
        Author: ccapistrano_20230511
        """  
        uCommon.waitAndClickElem(page, pMyProfile.na.barangayVillageDownIconBtn)
        uCommon.setAndSelectFromSmartDropDown(page, pMyProfile.na.searchTxt, strBarangay, pMyProfile.na.parentDIVListBox)
        
    @uCommon.ufuncLog       
    def clickAddNewAddress(page):
        """ 
        Objective: Click Add New Address successful
        
        param: None
        returns: None
        Author: ccapistrano_20230511
        """
        uCommon.waitAndClickElem(page, pMyProfile.na.addNewAddressBtn)
        uCommon.waitElemToBeVisible(page, pMyProfile.na.addressAddedSuccessMsg)
        uCommon.waitElemNotToBeVisible(page, pMyProfile.na.addressAddedSuccessMsg)
        
    @uCommon.ufuncLog       
    def clickAndVerifyAddNewAddress(page, dictData):
        """ 
        Objective: Click Add New Address successful
    
        param: dictData: {strFirstName, strLastName, strMobile, strProvince, strCity, strZipCode, strBrgy, strLotUnitStBldg, strLandmark}
        returns: None
        Author: ccapistrano_20230511
        """
        uCommon.waitAndClickElem(page, pMyProfile.na.addNewAddressBtn)
        if dictData["strZipCode"] == None or dictData["strProvince"] == None or dictData["strMobile"] == None or dictData["strLotUnitStBldg"] == None or dictData["strFirstName"] == None or dictData["strLastName"] == None:
            na.verifyNewAddressMandatoryFields(page, dictData)
        else:
            uCommon.waitElemToBeVisible(page, pMyProfile.na.addressAddedSuccessMsg)
            uCommon.waitElemNotToBeVisible(page, pMyProfile.na.addressAddedSuccessMsg)
            
    @uCommon.ufuncLog       
    def verifyNewAddressMandatoryFields(page, dictData):
        """ 
        Objective: Verify Mandatory Fields on New Address.
    
        param: dictData: {strFirstName, strLastName, strMobile, strProvince, strCity, strZipCode, strBrgy, strLotUnitStBldg, strLandmark}
        returns: None
        Author: abernal_20240124
        """
        uCommon.waitAndClickElem(page, pMyProfile.na.addNewAddressBtn)
        if dictData["strZipCode"] == None:
            uCommon.waitElemToBeVisible(page, pMyProfile.na.zipCodeErrorMsg)
        if dictData["strProvince"] == None:
            uCommon.waitElemToBeVisible(page, pMyProfile.na.provinceErrorMsg)
            uCommon.waitElemToBeVisible(page, pMyProfile.na.cityErrorMsg)
            uCommon.waitElemToBeVisible(page, pMyProfile.na.brgyErrorMsg)
        if dictData["strMobile"] == None:
            uCommon.waitElemToBeVisible(page, pMyProfile.na.contactNumberErrorMsg)
        if dictData["strLotUnitStBldg"] == None:
            uCommon.waitElemToBeVisible(page, pMyProfile.na.streetAddressErrorMsg)
        if dictData["strFirstName"] == None:
            uCommon.waitElemToBeVisible(page, pMyProfile.na.addressFirstNameErrorMsg)
        if dictData["strLastName"] == None:
            uCommon.waitElemToBeVisible(page, pMyProfile.na.addressLastNameErrorMsg)

    @uCommon.ufuncLog       
    def tickSetAsDefault(page):
        """ 
        Objective: Tick the Set as Default checkbox.
        
        param: None
        returns: None
        Author: abernal_20231001
        """
        uCommon.waitAndClickElem(page, pMyProfile.na.setAsDefaultChk)
        uCommon.waitElemToBeVisible(page, pMyProfile.na.tickedDefaultChk)
    
    @uCommon.ufuncLog
    def addAddressAndSetAsDefault(page, dictData):
        """ 
        Objective: Adding new address and setting it as default address.
        
        param dictData: {strFirstName, strLastName, strMobile, strProvince, strCity, strZipCode, strBrgy, strLotUnitStBldg, strLandmark}
        returns: None
        Author: jatregenio_20240202
        """
        com.clickAddressAddMore(page)
        na.addAddress(page, dictData)
        na.tickSetAsDefault(page)
        na.clickAddNewAddress(page)
        
    @uCommon.ufuncLog
    def clickAddNewAddressAndSetDetails(page, dictData):
        """ 
        Objective: Click 'Add More' and add new address.
        
        param dictData: {strFirstName, strLastName, strMobile, strProvince, strCity, strZipCode, strBrgy, strLotUnitStBldg, strLandmark}
        returns: None
        Author: jatregenio_20240214
        """
        com.clickAddressAddMore(page)
        na.addAddress(page, dictData)
        na.clickAddNewAddress(page)

    
    
    

class ea:
    """EDIT ADDRESS"""
    @uCommon.ufuncLog   
    def clickAddressEdit(page, strName):
        """ 
        Objective: Perform click edit from the kebab menu of Address.
        param: Full Name: strName
        returns: None
        Author: abernal_20231003
        """ 
        uCommon.waitAndClickElem(page, pMyProfile.com.secondMenuIconBtn(strName))
        uCommon.wait(page, .5)
        uCommon.waitAndClickElem(page, pMyProfile.com.addressEditBtn)
        uCommon.waitElemToBeVisible(page, pMyProfile.ea.editAddressLbl)

    @uCommon.ufuncLog
    def editAddress(page, dictNewAddress):
        """ 
        Objective: Perform edit address
        param dictNewAddress: {strFirstName, strLastName, strMobile, strProvince, strCity, strZipCode, strBrgy, strLotUnitStBldg, strLandmark}
        returns strName: None
        Author: abernal_20231003
        """ 
        uCommon.setElem(page, pMyProfile.na.firstNameTxt, dictNewAddress["strFirstName"])
        uCommon.setElem(page, pMyProfile.na.lastNameTxt, dictNewAddress["strLastName"])
        uCommon.setElem(page, pMyProfile.na.mobileNumberTxt, dictNewAddress["strMobile"])
        na.selectProviceDistrict(page, dictNewAddress["strProvince"])
        na.selectCity(page, dictNewAddress["strCity"])
        uCommon.setElem(page, pMyProfile.na.zipCodeTxt, dictNewAddress["strZipCode"])
        na.selectBarangay(page, dictNewAddress["strBrgy"])
        uCommon.setElem(page, pMyProfile.na.lotUnitStreetTxt, dictNewAddress["strLotUnitStBldg"])
        uCommon.setElem(page, pMyProfile.na.landmarkTxt, dictNewAddress["strLandmark"])      

    @uCommon.ufuncLog       
    def clickUpdateAddress(page, strValue=''):
        """ 
        Objective: Click Update Address button.
        param strValue: Text value to be updated
        returns: None
        Author: abernal_20231003
        Updated By: jatregenio_20240201
        """
        uCommon.waitAndClickElem(page, pMyProfile.ea.updateAddressBtn)
        blnIsMobNumLengthErrMsgDisplayed = uCommon.verifyVisible(page, pMyProfile.ea.errorMobileNumLengthMsg)
        if blnIsMobNumLengthErrMsgDisplayed == True:
            ea.updateSpecificAddressField(page, pMyProfile.na.mobileNumberTxt, strValue)
            uCommon.waitAndClickElem(page, pMyProfile.ea.updateAddressBtn)

        uCommon.waitElemToBeVisible(page, pMyProfile.ea.addressEditedSuccessMsg)
        uCommon.waitElemNotToBeVisible(page, pMyProfile.ea.addressEditedSuccessMsg)  
            
    @uCommon.ufuncLog
    def updateSpecificAddressField(page, elemAddressField, elemValue):
        """ 
        Objective: Set a value to specified addres field.
        param elemAddressField: {First Name, Last Name, Mobile Number, Delivery Address(Province, City, Zip Code, Brgy, Lot, Landmarks)}
              elemValue: new value for the specified address field  
        returns: None
        Author: jatregenio_20210201
        """
        uCommon.clickElemAndDeleteText(page, elemAddressField)
        uCommon.setElem(page, elemAddressField, elemValue)
        

    @uCommon.ufuncLog       
    def verifyNewAddressDetails(page, dictNewAddress):
        """ 
        Objective: To verify if the address details were updated.
        
        param dictNewAddress: {strFirstName, strLastName, strMobile, strProvince, strCity, strZipCode, strBrgy, strLotUnitStBldg, strLandmark}
        returns: None
        Author: abernal_20231003
        """
        newAddressName = f'{dictNewAddress["strFirstName"]} {dictNewAddress["strLastName"]}'
        newAddressDetails = f'{dictNewAddress["strBrgy"]}, {dictNewAddress["strCity"]}, {dictNewAddress["strProvince"]}'
        uCommon.validateElemText(page, pMyProfile.com.addressContactNameLbl(newAddressName), newAddressName)
        uCommon.validateElemText(page, pMyProfile.com.addressDetailsLbl(newAddressName), newAddressDetails)
        uCommon.validateElemText(page, pMyProfile.com.addressStLbl(newAddressName), dictNewAddress["strLotUnitStBldg"], False)
        uCommon.validateElemText(page, pMyProfile.com.addressZipLbl(newAddressName), dictNewAddress["strZipCode"], False)
        uCommon.validateElemText(page, pMyProfile.com.addressMobNumLbl(newAddressName), dictNewAddress["strMobile"], False)

    @uCommon.ufuncLog
    def untickSetAsDefault(page):
        """ 
        Objective: Untick the Set as Default checkbox.
        
        param: None
        returns: None
        Author: jatregenio_20240212
        """
        uCommon.wait(page, 0.5)
        uCommon.waitAndClickElem(page, pMyProfile.na.setAsDefaultChk)
        uCommon.waitElemNotToBeVisible(page, pMyProfile.na.tickedDefaultChk)

    @uCommon.ufuncLog
    def clickEditAndUpdateAddressToDefault(page, strFullName, strValue = ''):
        """ 
        Objective: Tick the Set as Default checkbox.
        
        param: None
        returns: None
        Author: jatregenio_20240212
        """
        ea.clickAddressEdit(page, strFullName)
        na.tickSetAsDefault(page)
        ea.clickUpdateAddress(page, strValue)
        
    @uCommon.ufuncLog
    def clickEditAndUpdateAddressToNotDefault(page, strFullName, strValue = ''):
        """ 
        Objective: Untick the Set as Default checkbox.
        
        param: None
        returns: None
        Author: jatregenio_20240215
        """
        ea.clickAddressEdit(page, strFullName)
        ea.untickSetAsDefault(page)
        ea.clickUpdateAddress(page, strValue)





class ac:
    """ADD CHILD"""
    @uCommon.ufuncLog   
    def addChildDetails(page, dictData):
        """ 
        Objective: Perform adding details to child.
        param newChildData: Child Name, Child Year, Child Month, Child Day, Child Gender
        returns: None
        Author: abernal_20231011
        """ 
        if dictData["strChildName"] != None:
            uCommon.waitAndSetElem(page, pMyProfile.ac.childNameTxt, dictData["strChildName"])
        if dictData["strYear"] != None:
            uCommon.waitAndClickElem(page, pMyProfile.ac.childDateBtn)
            uCommon.waitAndClickElem(page, pMyProfile.ac.birthYearBtn(dictData["strYear"]))
            uCommon.waitAndClickElem(page, pMyProfile.ac.birthMonthBtn(dictData["strMonth"]))
            uCommon.waitAndClickElem(page, pMyProfile.ac.birthDayBtn(dictData["strDay"]))
        if dictData["strGender"] != None:
            uCommon.wait(page, 0.5)
            uCommon.waitAndClickElem(page, pMyProfile.ac.genderRdb(dictData["strGender"]))


    @uCommon.ufuncLog       
    def clickAndVerifyAddChild(page, dictData):
        """ 
        Objective: Click Add More + button.
    
        param: dictData: {strChildName, strMonth, strDay, strYear, strGender}
        returns: None
        Author: abernal_20240216
        """
        uCommon.wait(page, 0.5)
        if uCommon.verifyVisible(page, pMyProfile.ac.addMoreBtn) == True:
            uCommon.waitAndClickElem(page, pMyProfile.ac.addMoreBtn)
        elif uCommon.verifyVisible(page, pMyProfile.ac.addChildBtn) == True:
            uCommon.waitAndClickElem(page, pMyProfile.ac.addChildBtn)
        if dictData["strChildName"] == None or dictData["strMonth"] == None or dictData["strDay"] == None or dictData["strYear"] == None or dictData["strGender"] == None:
            ac.verifyChildMandatoryFields(page, dictData)
        else:
            uCommon.waitElemToBeVisible(page, pMyProfile.ac.addChildSuccessMsg)
            uCommon.waitElemNotToBeVisible(page, pMyProfile.ac.addChildSuccessMsg)
            
            
    @uCommon.ufuncLog       
    def verifyChildMandatoryFields(page, dictData):
        """ 
        Objective: Verify Mandatory Fields on New Address.
    
        param: dictData: {strChildName, strMonth, strDay, strYear, strGender}
        returns: None
        Author: abernal_20240216
        """
        if dictData["strChildName"] == None:
            uCommon.waitElemToBeVisible(page, pMyProfile.ac.childNameErrorMsg)
        if dictData["strYear"] == None:
            uCommon.waitElemToBeVisible(page, pMyProfile.ac.childBirthDateErrorMsg)
        if dictData["strGender"] == None:
            uCommon.waitElemToBeVisible(page, pMyProfile.ac.childGenderErrorMsg)
        
        
        
        
        
        
class ec:
    """EDIT CHILD"""
    @uCommon.ufuncLog   
    def editChildDetails(page, updatedChildData):
        """ 
        Objective: Perform edit child details.
        param: Child Name
        returns: None
        Author: abernal_20231011
        """ 
        uCommon.waitAndSetElem(page, pMyProfile.ac.childNameTxt, updatedChildData["strChildName"])
        uCommon.waitAndClickElem(page, pMyProfile.ac.childDateBtn)
        uCommon.waitAndClickElem(page, pMyProfile.ac.birthYearBtn(updatedChildData["strYear"]))
        uCommon.waitAndClickElem(page, pMyProfile.ac.birthMonthBtn(updatedChildData["strMonth"]))
        uCommon.waitAndClickElem(page, pMyProfile.ac.birthDayBtn(updatedChildData["strDay"]))
        uCommon.wait(page, .5)
        uCommon.waitAndClickElem(page, pMyProfile.ac.genderRdb(updatedChildData["strGender"]))
        uCommon.waitAndClickElem(page, pMyProfile.ec.updateBtn)
        uCommon.waitElemToBeVisible(page, pMyProfile.com.editChildSuccessMsg)
        uCommon.waitElemNotToBeVisible(page, pMyProfile.com.editChildSuccessMsg)
    
    
    
    
    
    
class mn:
    """MOBILE NUMBER"""
    @uCommon.ufuncLog
    def clickEditMobileNumber(page):
        """ 
        Objective: Click edit Mobile Number

        param: None
        returns: None
        Author: cgrapa_20230613
        """
        uCommon.waitAndClickElem(page, pMyProfile.com.mobileEditNumberBtn)
        uCommon.waitElemNotToBeVisible(page, pMyProfile.mv.mobileNumberVerificatonLbl)

    @uCommon.ufuncLog
    def validateMobileVerificationForm(page):
        """ 
        Objective: Validate Mobile Verification Form
        
        param: None
        returns: None
        Author: cgrapa_20230613
        """
        arrObj = ['mobileNumberVerificatonLbl', 'mobileNumberTxt', 'sendMeTheCodeBtn', 'contactSupportBtn']
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pMyProfile.mv.__dict__[item])

    @uCommon.ufuncLog
    def editNumberAndValidateForm(page):
        """ 
        Objective: Click edit Mobile Number and validate Mobile Verification form
        
        param: None
        returns: None
        Author: cgrapa_20230613
        """
        mn.clickEditMobileNumber(page)
        mn.validateMobileVerificationForm(page)

    @uCommon.ufuncLog
    def inputNumberAndSendCode(page, strMobileNumber):
        """ 
        Objective: Inpute Mobile Number and click Send Code
        
        param strMobileNumber: Mobile Number
        returns: None
        Author: cgrapa_20230613
        """
        uCommon.setElem(page, pMyProfile.mv.mobileNumberTxt, strMobileNumber)
        uCommon.waitAndClickElem(page, pMyProfile.mv.sendMeTheCodeBtn)

    @uCommon.ufuncLog
    def clickVerifyCode(page):
        """ 
        Objective: Click Verify Code in Mobile Verification form
        
        param: None
        returns: None
        Author: cgrapa_20230613
        """ 
        uCommon.waitAndClickElem(page, pMyProfile.mv.verifyCodeBtn)

    @uCommon.ufuncLog
    def validatePinForm(page):
        """ 
        Objective: validate Pin form and verify code
        
        param: None
        returns: None
        Author: cgrapa_20230613
        """ 
        arrObj = ['enterPinLbl', 'codeInputTxt', 'pinTimerLbl', 'verifyCodeBtn']
        for item in arrObj:
            uCommon.waitElemToBeVisible(page, pMyProfile.mv.__dict__[item])
    
    @uCommon.ufuncLog
    def validatePinFormAndClickVerifyCode(page):
        """ 
        Objective: Validate Pin form and click verify code
        
        param: None
        returns: None
        Author: cgrapa_20230613
        """ 
        mn.validatePinForm(page)
        mn.clickVerifyCode(page)

    @uCommon.ufuncLog
    def validateFailedMobileChange(page, dictData):
        """ 
        Objective: Validate Mobile Number update did not push through
        
        param dictData: {strName, strEmail, strMobileNumber}
        returns: None
        Author: cgrapa_20230613
        """
        uAppComm.ln.loginToAdminKPC(page)
        uAdminKpc.cu.clickCustomers(page)
        uAdminKpc.cu.searchCustomer(page, dictData['strEmail'])
        newWindow = uCommon.switchToWindow(page)
        uCommon.waitAndValidateElemText(newWindow, pAdminKpc.cu.customerMobileNumberLbl, dictData['strMobileNumber'].replace("+", ""))

    @uCommon.ufuncLog
    def clickCloseBtn(page):
        """ 
        Objective: To close the Mobile Verification modal
        
        returns: None
        Author: rmakiling_20240115
        """
        uCommon.clickElem(page,pMyProfile.mv.closeBtn)
        
    @uCommon.ufuncLog
    def verifyValidPhoneNumber(page):
        """ 
        Objective: To verify that phone number is valid.
        
        returns: None
        Author: abernal_20240227
        """
        uCommon.waitElemToBeVisible(page, pMyProfile.mv.invalidNumberErrorMsg)




class at:
    """MY ATTRIBUTES"""
    @uCommon.ufuncLog
    def clearAttributes(page):
        """ 
        Objective: Clear all Attributes
        
        param: None
        returns: None
        Author: cgrapa_20230613
        """
        uCommon.wait(page, .5)        
        uCommon.waitAndClickElem(page, pMyProfile.ma.myAttributesAddEditBtn)
        activeAttrCount = uCommon.getArrayCount(page, pMyProfile.ma.allActiveAttributesBtn)
        for item in range(activeAttrCount):
            uCommon.waitAndClickElem(page, pMyProfile.ma.firstActiveAttributesBtn)
        uCommon.waitAndClickElem(page, pMyProfile.ma.attributesFormSubmitBtn)


    @uCommon.ufuncLog
    def addAttributes(page, intAddAttributes):
        """ 
        Objective: Add Attributes
        
        param intAddAttributes: Number of Attributes to be added
        returns: None
        Author: cgrapa_20230613
        """
        uCommon.waitAndClickElem(page, pMyProfile.ma.myAttributesAddEditBtn)
        for item in range(intAddAttributes):
            uCommon.waitAndClickElem(page, pMyProfile.ma.firstAttributeItemBtn)
        uCommon.waitAndClickElem(page, pMyProfile.ma.attributesFormSubmitBtn)


    @uCommon.ufuncLog
    def validateAndAddAttributes(page, intAddAttributes):
        """ 
        Objective: Validate added attributes
        
        param intAddAttributes: Number of Attributes to be added
        returns: None
        Author: cgrapa_20230613
        """
        intAttributeCount = uCommon.getArrayCount(page, pMyProfile.ma.allMyAttributesLbl)
        if intAttributeCount > 0:
            at.clearAttributes(page)
            uCommon.wait(page, 2)
            at.addAttributes(page, intAddAttributes)
        else:
            at.addAttributes(page, intAddAttributes)
        intNewAttributeCount = uCommon.getArrayCount(page, pMyProfile.ma.allMyAttributesLbl)
        uCommon.wait(page, 2)
        assert intAddAttributes == intNewAttributeCount, f'Number of attributes on profile ({intNewAttributeCount}) does not match with the number set on data config ({intAddAttributes})'

    
    def updateAttributes(page, dictData=''):
        """ 
        Objective: Update Attributes
        param intEditAttributes: Number of Attributes to be edited
        returns: None
        Author: abernal_20231111
        Updated by: jatregenio_20240201
        """
        uCommon.waitAndClickElem(page, pMyProfile.ma.myAttributesAddEditBtn)
        activeAttrCount = uCommon.getArrayCount(page, pMyProfile.ma.allActiveAttributesBtn)
        if activeAttrCount <= 5:
            for item in range(activeAttrCount):
                uCommon.waitAndClickElem(page, pMyProfile.ma.firstActiveAttributesBtn)
            uCommon.waitAndClickElem(page, pMyProfile.ma.attributeBtn(dictData["editAttribute1"]))
            uCommon.waitAndClickElem(page, pMyProfile.ma.attributeBtn(dictData["editAttribute2"]))
            uCommon.waitAndClickElem(page, pMyProfile.ma.attributeBtn(dictData["editAttribute3"]))
            uCommon.waitAndClickElem(page, pMyProfile.ma.attributeBtn(dictData["editAttribute4"]))
            uCommon.waitAndClickElem(page, pMyProfile.ma.attributeBtn(dictData["editAttribute5"]))
            uCommon.verifyVisible(page, pMyProfile.ma.activeAttributeLbl(dictData["editAttribute1"]))
            uCommon.waitAndClickElem(page, pMyProfile.ma.attributesFormSubmitBtn)
        elif activeAttrCount == 5: 
            uCommon.waitAndClickElem(page, pMyProfile.ma.firstAttributeItemBtn)
            uCommon.waitElemToBeVisible(page, pMyProfile.ma.maxAttributesSelectedMsg)
            uCommon.waitElemNotToBeVisible(page, pMyProfile.ma.maxAttributesSelectedMsg)
            
        

            
        
             
    
        
        
        
class edp:
    """Edit Page"""
    @uCommon.ufuncLog
    def fillDetails(page, dictData):
        """ 
        Objective: To fill the First name and Last name field of Edit modal in my profile
        
        param dictData: Text
        returns: None
        Author: rmakiling_20230928
        """
        uCommon.setElem(page, pMyProfile.ep.FirstNameLbl, dictData['strFName'])
        uCommon.setElem(page, pMyProfile.ep.LastNameLbl, dictData['strLName'])
        uCommon.uploadFile

    @uCommon.ufuncLog
    def clickUpdate(page, blnError = False):
        """ 
        Objective: To click the update button, to verify if the success message is displayed, 
        and to verify that the edit modal is not visible.
        
        param None
        returns: None
        Author: rmakiling_20230928
        """
        uCommon.clickElem(page, pMyProfile.ep.updateBtn)
        if blnError == True:
            uCommon.waitElemToBeVisible(page, pMyProfile.ep.firstNameErrorMsg)
            uCommon.waitElemToBeVisible(page, pMyProfile.ep.lastNameErrorMsg)
        else:
            uCommon.waitElemNotToBeVisible(page, pMyProfile.ep.editProfileLbl)
            uCommon.verifyVisible(page, pMyProfile.ep.profileUpdatedSuccessfullyMsg)
    
    @uCommon.ufuncLog
    def verifyFullname(page, dictData):
        """ 
        Objective: To verify if the combination of the inputted value in First name 
        and Last name field is reflected to the FULL NAME section in My Profile page
        
        param dictData: Text
        returns: None
        Author: rmakiling_20230928
        """
        uCommon.validateElemText(page, pMyProfile.com.nameLbl, f'{dictData["strFName"]} {dictData["strLName"]}')

    @uCommon.ufuncLog
    def uploadPhoto(page, strPath):
        uCommon.uploadFile(page, pMyProfile.ep.uploadPhotoBtn, strPath)
        uCommon.waitAndClickElem(page, pMyProfile.ep.selectBtn)
        uCommon.waitElemNotToBeVisible(page, pMyProfile.ep.photoImg)

    @uCommon.ufuncLog
    def clickCloseBtn(page):
        """ 
        Objective: To Close the Edit Profile modal
        
        returns: None
        Author: rmakiling_20240115
        """
        uCommon.clickElem(page,pMyProfile.ep.closeBtn)
        
    @uCommon.ufuncLog
    def clickAndVerifyProfileDetails(page, dictData):
        """ 
        Objective: To click the update button, to verify if error message is displayed.
        
        param dictData: Text
        returns: None
        Author: abernal_20240219
        """
        uCommon.clickElem(page, pMyProfile.ep.updateBtn)
        if dictData["strFName"] == "":
            uCommon.waitElemToBeVisible(page, pMyProfile.ep.firstNameBlankErrorMsg)
        elif dictData["strLName"] == "":
            uCommon.waitElemToBeVisible(page, pMyProfile.ep.lastNameBlankErrorMsg)
        else:
            uCommon.waitElemNotToBeVisible(page, pMyProfile.ep.editProfileLbl)
            uCommon.verifyVisible(page, pMyProfile.ep.profileUpdatedSuccessfullyMsg)
            
    @uCommon.ufuncLog
    def clickEditAndVerifyProfileDetails(page, dictData):
        """ 
        Objective: To click the edit button, update profile details, and verify.
        
        param dictData: Text
        returns: None
        Author: abernal_20240219
        """
        
        com.clickEditbtn(page)
        edp.fillDetails(page, dictData)
        edp.clickAndVerifyProfileDetails(page, dictData)
        edp.clickCloseBtn(page)
    