import random
from datetime import datetime
strDateTimeToday = datetime.today().strftime("%Y%m%d%H%M%S")

# strItemName  = 'Baby Gentle Wash & Shampoo'
# strItemName  = 'Baby Gentle Wash & Shampoo Pump (400ml)' # EDA-24399
# strItemName  = 'Baby Gentle Wash & Shampoo (230ml)' # AAAA02741
#strItemName  = 'Baby Gentle Wash & Shampoo Automation Test Data' # AAAA02741
strItemName = 'Tala Tiles Magnetic Tiles Triangles Set (48-piece)'
strItemName2 = 'Baby Bath Emollient (150ml) - Auto Do Not Update or Delete'
strItemName3 = '16-Piece Brick Tile Set - Auto  Do Not Update or Delete'
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
                'blnCoupon': True,
                'strCouponTag': '',
                'strCouponType': '',
                'strVoucherDisc': '₱250.00'
                }    

class AUTO275:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': 'promo',
                'strPromoCode': 'BEAN300',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponType': 'CREDIT BEANS',
                'strVoucherDisc': '',
                'strCouponTag': ''
                }    
    
class AUTO280:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': 'promo',
                'strPromoCode': 'CETAFLAT50',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponTag': '',
                'strCouponType': '',
                'strVoucherDisc': '₱50.00'
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
                'blnCoupon': True,
                'strCouponTag': '',
                'strCouponType': '',
                'strVoucherDisc': '₱250.00'
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
                'blnCoupon': True,
                'strCouponType': 'CREDIT BEANS',
                'strVoucherDisc': '',
                'strCouponTag': ''
                }    
    
class AUTO315:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'CETAFLAT50',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponType': '',
                'strCouponTag': '',
                'strVoucherDisc': '₱50.00'
                }    
    
class AUTO320:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GRAB PAY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False,
                'strCouponType': '',
                'strCouponTag': ''
                } 

class AUTO325:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GRAB PAY',
                'strBeansPromo': 'beans',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False,
                'strCouponType': '',
                'strCouponTag': ''
                }    
    
class AUTO330:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GRAB PAY',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDAPERC10',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponType': '',
                'strCouponTag': 'Edamama Sponsored',
                'strVoucherDisc': '₱250.00'
                }    
    
class AUTO335:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'MAYA',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False,
                'strCouponType': '',
                'strCouponTag': ''
                } 
    
class AUTO384:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'MAYA',
                'strBeansPromo': 'beans',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False,
                'strCouponType': '',
                'strCouponTag': ''
                }    
    
class AUTO389:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'MAYA',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDAMAYA100',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponType': '',
                'strCouponTag': '',
                'strVoucherDisc': '₱100.00'
                }    
    
class AUTO530:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False,
                'strCouponType': '',
                'strCouponTag': '',
                'strOrderStatus': 'cancelledbyuser'
                }   
    
class AUTO557:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False,
                'blnCancel': False,
                'strCouponType': '',
                'strCouponTag': ''
                }   

class AUTO562:
    dictData = {
                'strItemName': 'Baby Gentle Wash & Shampoo Automation Test Data - PLEASE DO NOT USE OR UPDATE',
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False,
                #'skuCode': 'EDA-24399',
                'skuCode': 'AAAA02741',
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
                'blnCancel': True,
                'strCouponType': '',
                'strCouponTag': ''
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
                'blnCoupon': True,
                'strVoucherDisc': '₱50.00',
                'strCouponType': '',
                'strCouponTag': ''
                }    

class AUTO427:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': 'promo',
                'strPromoCode': 'BEAN300',
                'strType': 'ss',
                'blnCoupon': True,
                'strCouponType': 'CREDIT BEANS',
                'strVoucherDisc': '',
                'strCouponTag': ''
                }    
    
class AUTO432:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'CASH ON DELIVERY',
                'strBeansPromo': 'promo',
                'strPromoCode': 'CETAFLAT50',
                'strType': 'ss',
                'blnCoupon': True,
                'strVoucherDisc': '₱50.00',
                'strCouponType': '',
                'strCouponTag': ''
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
                'blnCoupon': True,
                'strVoucherDisc': '₱50.00',
                'strCouponType': ''
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
                'blnCoupon': True,
                'strCouponType': 'CREDIT BEANS',
                'strVoucherDisc': '',
                'strCouponTag': ''
                }    
    
class AUTO467:
    dictData = {
                'strItemName': strItemNameSNS,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'CETAFLAT50',
                'strType': 'ss',
                'blnCoupon': True,
                'strVoucherDisc': '₱50.00',
                'strCouponType': ''
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
                'blnCoupon': True,
                'strVoucherDisc': '₱50.00',
                'strCouponType': ''
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
                'blnCoupon': True,
                'strVoucherDisc': '₱100.00',
                'strCouponType': '',
                'strCouponTag': ''
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
                'strLandmark': 'RED GATE',
                'strFormattedProvince': 'Metro Manila',
                'strFormattedCity': 'Makati City',
                'selectFormattedBarangay': 'Forbes Park',
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
    strOwnerUserName = 'Qa20240708232439'
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
                'blnCoupon': False,
                'strCouponType': '',
                'strCouponTag': ''
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
    intArticles = 1

class AUTO345:
    strShopSection = 'fp'
    
class AUTO1948:
    dictData = {
                'strItemName': strItemName2,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDRIGCFAO',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponTag': 'Gift Card',
                'strVoucherDisc': '₱500.00',
                'strCouponType': ''
                }  

class AUTO1951:
    dictData = {
                'strItemName': strItemName3,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDRIBSCBTALA',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponTag': 'Brand Sponsored',
                'strCouponType': '',
                'strVoucherDisc': '₱500.00',
                'strCouponType': ''
                }  
    
class AUTO1954:
    dictData = {
                'strItemName': strItemName2,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDRIBSCBTALA',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponTag': 'Brand Sponsored',
                'strVoucherDisc': '',
                'strCouponType': ''
                }  
    
class AUTO1960:
    dictData = {
                'strItemName': strItemName2,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDRIESPO',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponTag': 'Edamama Sponsored',
                'strVoucherDisc': '₱250.00',
                'strCouponType': ''
                } 
    
class AUTO1969:
    dictData = {
                'strItemName': strItemName2,
                'strMOP': 'GRAB PAY',
                'strBeansPromo': 'promo',
                'strPromoCode': 'MOPPOGRABPAY',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponTag': 'Edamama Sponsored',
                'strVoucherDisc': '₱100.00',
                'strCouponType': ''
                }  
    
class AUTO1963:
    dictData = {
                'strItemName': strItemName2,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDRISHIPFRS',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponTag': 'Shipping',
                'strVoucherDisc': '',
                'strCouponType': ''
                } 
    
class AUTO1966:
    strMyProfile = 'my profile'
    dictDataAddress = {
        'strFirstName': 'New',
        'strLastName': 'Address',
        'strMobile': '9171234567',
        'strProvince': 'CAVITE',
        'strCity': 'SILANG',
        'strZipCode': '1234',
        'strBrgy': 'ACACIA',
        'strLotUnitStBldg': 'Test Street',
        'strLandmark': 'Random landmark'
    }
    dictData = {
                'strItemName': strItemName2,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'MARRIE430921',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponTag': 'Referral Code',
                'strVoucherDisc': '',
                'strCouponType': ''
    } 
    
class AUTO1972:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDRIGCFAO',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponTag': 'Gift Card',
                'strCouponType': '',
                'strVoucherDisc': '₱500.00'
                } 
    
class AUTO1975:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDRIBSCBTALA',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponTag': 'Brand Sponsored',
                'strCouponType': '',
                'strVoucherDisc':''
                } 
    
class AUTO1978:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDRIESPO',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponTag': 'Edamama Sponsored',
                'strCouponType': '',
                'strVoucherDisc': '₱250.00'
                } 
    
class AUTO1981:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'EDRISHIPFRS',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponTag': 'Shipping',
                'strCouponType': '',
                'strVoucherDisc': ''
                } 
    
class AUTO1984:
    strMyProfile = 'my profile'
    dictDataAddress = {
        'strFirstName': 'New',
        'strLastName': 'Address',
        'strMobile': '9171234567',
        'strProvince': 'CAVITE',
        'strCity': 'SILANG',
        'strZipCode': '1234',
        'strBrgy': 'ACACIA',
        'strLotUnitStBldg': 'Test Street',
        'strLandmark': 'Random landmark'
    }
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GCASH',
                'strBeansPromo': 'promo',
                'strPromoCode': 'MARRIE430921',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponTag': 'Referral Code',
                'strCouponType': '',
                'strVoucherDisc': '₱400.00'
    } 
    
class AUTO1987:
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GRAB PAY',
                'strBeansPromo': 'promo',
                'strPromoCode': 'MOPPOGRABPAY',
                'strType': 'fp',
                'blnCoupon': True,
                'strCouponTag': 'Edamama Sponsored',
                'strCouponType': '',
                'strVoucherDisc': '₱200.00'
                } 