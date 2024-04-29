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

class AUTO1639:
    strMyOrders = 'my orders'
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GRAB PAY',
                'strBeansPromo': '',
                'strPromoCode': '',
                'strType': 'fp',
                'blnCoupon': False
                } 

class AUTO1627:
    strMyOrders = 'my orders'
    dictData = {
                'strItemName': strItemName,
                'strMOP': 'GRAB PAY',
                'strBeansPromo': 'promo',
                'strPromoCode': 'BEAN300',
                'strType': 'fp',
                'blnCoupon': False,
                'strCouponTag': '',
                'strCouponType': 'CREDIT BEANS'
                } 