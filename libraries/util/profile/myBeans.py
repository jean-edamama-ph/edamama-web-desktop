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
        if uCommon.verifyVisible(page, pMyBeans.com.onAddChildLbl) == True:
            uCommon.expectElemToBeVisible(page, pMyBeans.com.onAddChildRewardLbl)
            uCommon.log(1, f'On Add Child activity is visible.') 
        elif uCommon.verifyVisible(page, pMyBeans.com.onAddChildLbl) == False:
            uCommon.expectElemNotToBeVisible(page, pMyBeans.com.onAddChildRewardLbl)
            uCommon.log(1, f'On Add Child activity is not visible.') 
        
    @uCommon.ufuncLog   
    def verifyBeansRewardFromAddingAttribute(page):
        """ 
        Objective: To check if On Add Attribute was rewarded.
        param: None
        returns: None
        Author: abernal_20240229
        """  
        if uCommon.verifyVisible(page, pMyBeans.com.onAddAttributeLbl) == True:
            uCommon.expectElemToBeVisible(page, pMyBeans.com.onAddAttributeRewardLbl)
            uCommon.log(1, f'On Add Attribute activity is visible.') 
        elif uCommon.verifyVisible(page, pMyBeans.com.onAddAttributeLbl) == False:
            uCommon.expectElemNotToBeVisible(page, pMyBeans.com.onAddAttributeRewardLbl)
            uCommon.log(1, f'On Add Attribute activity is not visible.') 
        
    @uCommon.ufuncLog   
    def verifyBeansRewardFromProductPurchase(page):
        """ 
        Objective: To check if On Product Purchase was rewarded.
        param: None
        returns: None
        Author: abernal_20240229
        """  
        if uCommon.verifyVisible(page, pMyBeans.com.onProductPurchaseLbl) == True:
            uCommon.expectElemToBeVisible(page, pMyBeans.com.onProductPurchaseRewardLbl)
            uCommon.log(1, f'On Product Purchase activity is visible.') 
        
    @uCommon.ufuncLog   
    def verifyBeansRewardFromBeanbackVoucher(page):
        """ 
        Objective: To check if On Coupon Use was rewarded.
        param: None
        returns: None
        Author: abernal_20240301
        """  
        if uCommon.verifyVisible(page, pMyBeans.com.onCouponUseLbl) == True:
            uCommon.log(1, f'On Coupon Use activity is visible.') 
            
    @uCommon.ufuncLog   
    def verifyBeansRewardFromOnRegistration(page):
        """ 
        Objective: To check if On Registration was rewarded.
        param: None
        returns: None
        Author: abernal_20240311
        """  
        if uCommon.verifyVisible(page, pMyBeans.com.onRegistrationLbl) == True:
            uCommon.expectElemToBeVisible(page, pMyBeans.com.onRegistrationRewardLbl)
            uCommon.log(1, f'On Registration activity is visible.') 
            
    @uCommon.ufuncLog   
    def verifyOnEdamamaRewards(page, value):
        """ 
        Objective: To verify On Edamama Rewards.
        param: None
        returns: None
        Author: abernal_20240311
        """  
        if uCommon.verifyVisible(page, pMyBeans.com.onEdamamaRewardsLbl) == True:
            elemValue = uCommon.getElemText(page, pMyBeans.com.onEdamamaRewardsValueLbl)
            if uCommon.waitAndValidateElemText(page, elemValue, value) == True:
                uCommon.log(1, f'On Edamama Rewards(+) activity is visible.') 
                
    @uCommon.ufuncLog   
    def verifyOnEdamamaCredits(page, value):
        """ 
        Objective: To verify On Edamama Credits.
        param: None
        returns: None
        Author: abernal_20240311
        """  
        if uCommon.verifyVisible(page, pMyBeans.com.onEdamamaCreditsLbl) == True:
            elemValue = uCommon.getElemText(page, pMyBeans.com.onEdamamaCreditsValueLbl)
            if uCommon.waitAndValidateElemText(page, elemValue, value) == True:
                uCommon.log(1, f'On Edamama Credits(+) activity is visible.') 