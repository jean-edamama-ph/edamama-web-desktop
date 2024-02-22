strUrl = 'https://api-v2.kpc.edamamalabs.net/api/v1/admin'

class login:
    login = f'{strUrl}/login'





class order:
    order = f'{strUrl}/orders?'
    getOrder = f'{strUrl}/getOrder/'
    updateDetails = f'{strUrl}/orders/update-details'
    processMassOrderCancel = f'{strUrl}/orders/processMassOrderCancellation'

    
    
    
    
    
class subscription:
    getOrder = f'{strUrl}/getOrder/'
    cancel = f'{strUrl}/subscriptions/cancel'
    def subscription(strCustomerName):
        return f'{strUrl}/products/subscriptions?status=active&page=1&limit=10&search={strCustomerName}&isExport=false'





class curated:
    curatedType = f'{strUrl}/curatedType'
    curatedTypeList = f'{curatedType}?page=1&limit=100&isHomePageShow=true'
    rank = f'{strUrl}/curatedType/rank'





class scheduler:
    preUpload = f'{strUrl}/product-discount/pre-upload'
    productDiscount = f'{strUrl}/product-discount/'
    search = f'{productDiscount}?page=1&limit=10&search='
    cancel = f'{productDiscount}cancel'





class flashSale:
    preUpload = f'{strUrl}/product-discount/pre-upload'
    flashSale = f'{strUrl}/flash-sale'
    search = f'{strUrl}/flash-sale?page=1&limit=20'
    cancel = f'{strUrl}/flash-sale/cancel'
    
    
    
    
    
class products:
    products = f'{strUrl}/products'
    getID = f'{products}?search='





class rewards:
    configurations = f'{strUrl}/credits/configurations'