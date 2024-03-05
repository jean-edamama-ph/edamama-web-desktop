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
        uCommon.waitElemToBeVisible(page, pMyBeans.com.onAddChildLbl)
        
    @uCommon.ufuncLog   
    def verifyBeansRewardFromAddingAttribute(page):
        """ 
        Objective: To check if On Add Attribute was rewarded.
        param: None
        returns: None
        Author: abernal_20240229
        """  
        uCommon.waitElemToBeVisible(page, pMyBeans.com.onAddAttributeLbl)
        
    @uCommon.ufuncLog   
    def verifyBeansRewardFromProductPurchase(page):
        """ 
        Objective: To check if On Product Purchase was rewarded.
        param: None
        returns: None
        Author: abernal_20240229
        """  
        uCommon.waitElemToBeVisible(page, pMyBeans.com.onProductPurchaseLbl)
        
    @uCommon.ufuncLog   
    def verifyBeansRewardFromBeanbackVoucher(page):
        """ 
        Objective: To check if On Coupon Use was rewarded.
        param: None
        returns: None
        Author: abernal_20240301
        """  
        uCommon.getElemText(page, pMyBeans.com.onCouponUseLbl)
        uCommon.waitElemToBeVisible(page, pMyBeans.com.onCouponUseLbl)