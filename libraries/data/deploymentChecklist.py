import random
from datetime import datetime
strDateTimeToday = datetime.today().strftime("%Y%m%d%H%M%S")

# strItemName  = 'Baby Gentle Wash & Shampoo'
# strItemName  = 'Baby Gentle Wash & Shampoo Pump (400ml)' # EDA-24399
# strItemName  = 'Baby Gentle Wash & Shampoo (230ml)' # AAAA02741
#strItemName  = 'Baby Gentle Wash & Shampoo Automation Test Data' # AAAA02741
strItemName = 'Tala Tiles Magnetic Tiles Triangles Set (48-piece)'
# strItemName = 'Baby Advanced Protection Cream with Organic Calendula (85g)' # EDA-24367
# 'Baby Moisturizing Bath & Wash (230ML) - Buy 3 Get Free Baby Bar'
# 'Baby Advanced Protection Cream with Organic Calendula (85g)', 
# 'Baby Bath Set (with Free Baby Shampoo 200ml)',
strItemNameSNS = 'SNS Automation Product - PLEASE DO NOT UPDATE OR DELETE'
# strItemNameSNS = 'Baby Gentle Wash & Shampoo Pump (400ml x 2) - Subscription'
# strItemNameSNS = 'Plus Jumbo Pack Tape Diaper Large (42 pcs x 3 pack) - Subscription' # EDA-21717

class AUTO206:
    strCount = '1'
    strShopSection = 'fp'
    strItem = strItemName
    
class AUTO230:
    strFb = 'FB'
    strGmail = 'GM'

class AUTO215:
    strName = 'TEST AUTO'
    strPath = './libraries/data/uploadFile/FIND Test FS - newTemplate.csv'
    
class AUTO225:
    strUserName = 'testkpcmanual@gmail.com'
    strNewPassword = 'Edamama123!!'
    strOldPassword = 'Edamama123!'
    
class AUTO240: 
    strType1 = 'brand'
    strName1 = 'Chicco'
    
    strType2 = 'item'
    strName2 = 'Next2dreams'
    
class AUTO255:
    strCount = '1'
    
class AUTO235:
    strType1 = 'brand'
    strName1 = 'Chicco'
    strCategoryName = 'All Categories'
    strLvl3Name = 'Wipes'
    
class AUTO250:
    strTitle = 'ss'
    strCount = '1'
    
class AUTO260:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False
                }   

class AUTO265:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': 'beans',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False
                }    
    
class AUTO270:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDAPERC10',
                'strType': 'fp',
                'blnCoupon': True
                }    

class AUTO275:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': 'promo',
                'strPromoCode': 'BEAN300',
                'strType': 'fp',
                'blnCoupon': True
                }    
    
class AUTO280:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': 'promo',
                'strPromoCode': 'CETAFLAT50',
                'strType': 'fp',
                'blnCoupon': True
                }    

class AUTO285:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CREDIT CARD',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False
                } 

class AUTO290:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CREDIT CARD',
                'strBeansPromo': 'beans',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False
                }    

class AUTO295:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CREDIT CARD',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDAPERC10',
                'strType': 'fp',
                'blnCoupon': True
                }    
    
class AUTO300:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GCASH',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False
                } 
    
class AUTO305:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GCASH',
                'strBeansPromo': 'beans',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False
                }    
    
class AUTO310:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'BEAN300',
                'strType': 'fp',
                'blnCoupon': True
                }    
    
class AUTO315:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'CETAFLAT50',
                'strType': 'fp',
                'blnCoupon': True
                }    
    
class AUTO320:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GRAB PAY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False
                } 

class AUTO325:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GRAB PAY',
                'strBeansPromo': 'beans',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False
                }    
    
class AUTO330:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GRAB PAY',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDAPERC10',
                'strType': 'fp',
                'blnCoupon': True
                }    
    
class AUTO335:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'MAYA',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False
                } 
    
class AUTO384:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'MAYA',
                'strBeansPromo': 'beans',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False
                }    
    
class AUTO389:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'MAYA',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDAMAYA100',
                'strType': 'fp',
                'blnCoupon': True
                }    
    
class AUTO530:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False
                }   
    
class AUTO557:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False,
                'blnCancel': False
                }   

class AUTO562:
    dictData = {
                'strItemName': 'Baby Gentle Wash & Shampoo Automation Test Data - PLEASE DO NOT USE OR UPDATE',
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False,
                'skuCode': 'EDA-24399',
                #'skuCode': 'AAAA02741',
                'blnCancel': False
                }   
    
class AUTO567:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False,
                'blnCancel': True
                }   

class AUTO572:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False,
                'skuCode': 'EDA-30887',
                'blnCancel': True,
                }   

class AUTO617:
    strName = 'TEST RS AUTO'
    strPath = './libraries/data/uploadFile/FIND Test FS - newTemplate.csv'
    strType = 'RS'

class AUTO618:
    strName = 'TEST SNS AUTO'
    strPath = './libraries/data/uploadFile/FIND Test SNS.csv'
    strType = 'SNS'
    strSNS = 'Subscribe And Save'
    
class AUTO616:
    strName = 'TEST FS AUTO'
    strPath = './libraries/data/uploadFile/FIND Test FS - newTemplate.csv'
    
class AUTO412:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'ss',
                'blnCoupon': False
                }   
    
class AUTO417:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': 'beans',
                'strPromoCode': '',
                'strType': 'ss',
                'blnCoupon': False
                }    
    
class AUTO422:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDAPERC10',
                'strType': 'ss',
                'blnCoupon': True
                }    

class AUTO427:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': 'promo',
                'strPromoCode': 'BEAN300',
                'strType': 'ss',
                'blnCoupon': True
                }    
    
class AUTO432:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': 'promo',
                'strPromoCode': 'CETAFLAT50',
                'strType': 'ss',
                'blnCoupon': True
                }       
    
class AUTO437:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'CREDIT CARD',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'ss',
                'blnCoupon': False
                } 

class AUTO442:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'CREDIT CARD',
                'strBeansPromo': 'beans',
                'strPromoCode': '',
                'strType': 'ss',
                'blnCoupon': False
                }    

class AUTO447:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'CREDIT CARD',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDAPERC10',
                'strType': 'ss',
                'blnCoupon': True
                }    
    
class AUTO452:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'GCASH',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'ss',
                'blnCoupon': False
                } 
    
class AUTO457:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'GCASH',
                'strBeansPromo': 'beans',
                'strPromoCode': '',
                'strType': 'ss',
                'blnCoupon': False
                }    
    
class AUTO462:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'BEAN300',
                'strType': 'ss',
                'blnCoupon': True
                }    
    
class AUTO467:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'CETAFLAT50',
                'strType': 'ss',
                'blnCoupon': True
                }    
    
class AUTO472:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'GRAB PAY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'ss',
                'blnCoupon': False
                } 

class AUTO477:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'GRAB PAY',
                'strBeansPromo': 'beans',
                'strPromoCode': '',
                'strType': 'ss',
                'blnCoupon': False
                }    
    
class AUTO482:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'GRAB PAY',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDAPERC10',
                'strType': 'ss',
                'blnCoupon': True
                }    
    
class AUTO487:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'MAYA',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'ss',
                'blnCoupon': False
                } 
    
class AUTO492:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'MAYA',
                'strBeansPromo': 'beans',
                'strPromoCode': '',
                'strType': 'ss',
                'blnCoupon': False
                }    
    
class AUTO497:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'MAYA',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDAMAYA100',
                'strType': 'ss',
                'blnCoupon': True
                }    
    
class AUTO619:
    strRandom = str(random.randint(500, 800))
    strName = 'Easy Clean Bib'
    strPath = './libraries/data/uploadFile/Woven Green.png'
    dictData = {
                'strBrand': 'Kidsme',
                'strName': f'Easy Clean Bib test auto {strRandom}',
                'strPrice': strRandom,
                'strColor': 'Woven Green',
                }

class AUTO622:
    #strName = 'AUTO_UNPUBLISHED DO NOT UPDATE OR DELETE'
    strName = 'Squeaky Pet Toy Bundle'
    blnNotVisible = False
    
class AUTO620:
    #strName = 'AUTO_BLOCKED DO NOT UPDATE OR DELETE'
    strName = 'Pet tags (Single Sided) | e-Voucher'
    blnNotVisible = False
 
class AUTO635:
    strRandom = str(random.randint(100, 1000))
    dictData = {
                'strName': f'AUTOMATION NEW - {strRandom}',
                'strCategory': 'Food Storage',
                'strBrand': 'Little Dragon',
                'strVendor': 'Big Brute',
                'strBundleBuy': 'First Day School Products',
                'strAttributes': 'Active Mama',
                'strColor': 'Woven Green',
                'strPath': './libraries/data/uploadFile/Woven Green.png',
                'strVariant': 'Bamberry Baby',
                'strDisplayType': 'Radio',
                'strTypeOptions': '12M',
                'strSelectFilters': 'Age Group',
                'strFiltersOptions': '0M - 6M',
                'strPrice': strRandom,
                'blnVisible':  True
                }
    
class AUTO676:
    strPath = './libraries/data/uploadFile/order-cancellation.csv'
    strOrderCancellation = 'Order Cancellation'
    strMyOrders = 'my orders'
    strCancelledByAdmin = 'Cancelled by Admin'
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False
                }  
    
class AUTO671:
    strMyOrders = 'my orders'
    strShipped = 'Shipped'
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False
                }  
    
class AUTO666:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False
                } 
    
    dictNewAddress = {
                'strFName':'AUTO',
                'strLName': 'MATION',
                'strMobile': '9171234567',
                'strProvince': 'METRO MANILA',
                'strCity': 'MAKATI CITY',
                'selectBarangay': 'FORBES PARK',
                'strZipCode': '1111',
                'strLotStreet': 'LOT 143',
                'strLandmark': 'RED GATE'
                } 
    
class AUTO552:
    strGRurl = 'https://www.kpc.edamamalabs.net/profile/gift-lists/39047'
    strGiftNote = 'test gift note'
    
class AUTO701:
    blnCleanUp = True
    blnFirstGL = 'click'
    dictData = {
                'strOccassion': f'test occasion{strDateTimeToday}',
                'strAbout': 'test about',
                }
    
class AUTO706:
    blnFirstGL = 'click'
    blnCleanUp = True
    dictData = {
                'strOccassion': f'test occasion{strDateTimeToday}',
                'strAbout': 'test about',
                }

    
class AUTO711:
    blnFirstGL = 'click'
    blnCleanUp = True
    dictData = {
                'strOccassion': f'test occasion{strDateTimeToday}',
                'strAbout': 'test about',
                'strGiftNote': 'test gift note'
                }
    blnFirstAddProduct = False
    blnSignIn = True
    blnOwner = True
    
class AUTO716:
    strOwnerUserName = 'Qa20231031080254'
    blnFirstGL = 'click'
    blnTrue = True
    blnFalse = False
    blnCleanUp = blnTrue
    dictDataGift = {
                'strOccassion': f'test occasion{strDateTimeToday}',
                'strAbout': 'test about',
                'strGiftNote': 'test gift note'
                }
    blnFirstAddProduct = False
    blnSignIn = blnTrue
    blnOwner = blnTrue
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GCASH',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False
                } 
    
class AUTO547:
    strGRurl = 'https://www.kpc.edamamalabs.net/profile/gift-lists/39047'
    strGiftNote = 'test gift note'
    
class AUTO661:
    intCuratedIndex = 1
    strItemName = strItemName
    blnAdd = False
    
class AUTO721:
    strMySubscription = 'my subscription'
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'ss',
                'blnCoupon': False
                }   
    
class AUTO734:
    strMySubscription = 'my subscription'
    strUsername = 'testbuykpcfive'
    strNewProduct = 'Bar White (135g) Bundle of 3 - Subscription'
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'ss',
                'blnCoupon': False
                }  
    
class AUTO730:
    strMySubscription = 'my subscription'
    strUsername = 'testbuykpcfive'
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'ss',
                'blnCoupon': False
                }  

class AUTO542:
    strAll = 'all'
    strFeatured = 'featured articles'
    strStyle = 'style'
    strNurture = 'nurture'
    strPlayAndLearn = 'play and learn'
    intArticles = 2

class AUTO345:
    strShopSection = 'fp'