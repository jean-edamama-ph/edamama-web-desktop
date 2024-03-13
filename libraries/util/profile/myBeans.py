import libraries.page.profile.myBeans as pMyBeans
import libraries.page.common.adminKpc as pAdminKpc

import libraries.util.common as uCommon
import libraries.util.appCommon.appComm as uAppComm
import libraries.util.appCommon.adminKpc as uAdminKpc

class com:
    """COMMON"""
    @uCommon.ufuncLog   
    def verifyBeansRewardFromAddingChild(page):
        """ 
        Objective: To check if On Add Child was rewarded.
        param: None
        returns: None
        Author: abernal_20240229
        """  
        if uCommon.expectElemToBeVisible(page, pMyBeans.com.onAddChildLbl) == True:
            uCommon.expectElemToBeVisible(page, pMyBeans.com.onAddChildRewardLbl)
            uCommon.log(2, f'On Add Child activity is visible.') 
        
    @uCommon.ufuncLog   
    def verifyBeansRewardFromAddingAttribute(page):
        """ 
        Objective: To check if On Add Attribute was rewarded.
        param: None
        returns: None
        Author: abernal_20240229
        """  
        if uCommon.expectElemToBeVisible(page, pMyBeans.com.onAddAttributeLbl) == True:
            uCommon.expectElemToBeVisible(page, pMyBeans.com.onAddAttributeLbl)
            uCommon.log(2, f'On Add Attribute activity is visible.') 
        
    @uCommon.ufuncLog   
    def verifyBeansRewardFromProductPurchase(page):
        """ 
        Objective: To check if On Product Purchase was rewarded.
        param: None
        returns: None
        Author: abernal_20240229
        """  
        if uCommon.expectElemToBeVisible(page, pMyBeans.com.onProductPurchaseLbl) == True:
            uCommon.expectElemToBeVisible(page, pMyBeans.com.onProductPurchaseRewardLbl)
            uCommon.log(2, f'On Product Purchase activity is visible.') 
        
    @uCommon.ufuncLog   
    def verifyBeansRewardFromBeanbackVoucher(page):
        """ 
        Objective: To check if On Coupon Use was rewarded.
        param: None
        returns: None
        Author: abernal_20240301
        """  
        if uCommon.expectElemToBeVisible(page, pMyBeans.com.onCouponUseLbl) == True:
            uCommon.log(2, f'On Coupon Use activity is visible.') 
            
    @uCommon.ufuncLog   
    def verifyBeansRewardFromOnRegistration(page):
        """ 
        Objective: To check if On Registration was rewarded.
        param: None
        returns: None
        Author: abernal_20240311
        """  
        if uCommon.expectElemToBeVisible(page, pMyBeans.com.onRegistrationLbl) == True:
            uCommon.expectElemToBeVisible(page, pMyBeans.com.onRegistrationRewardLbl)
            uCommon.log(2, f'On Registration activity is visible.') 