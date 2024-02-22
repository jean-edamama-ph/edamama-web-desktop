import libraries.api.ap.data.headers as dHeaders
import libraries.api.ap.data.url as dUrl

import libraries.api.ap.util.common as uCommon
import libraries.data.common as dCommon


def getProductID(strParam):
    """
    Method: GET
    API Endpoint: /products?search=
    Params strParam: Silicone%20Baby%20Bottle%20Twinpack%20(5oz)&page=1&limit=10
    Response Data: Product Details
    Author: ccapistrano_20231106
    """
    strResponse = uCommon.callGet(f'{dUrl.products.getID}{strParam}', dHeaders.withToken(dCommon.api.strAccessToken, False))
    uCommon.validateStatusCode(strResponse)
    intCount = strResponse.json()['data']['totalCount']
    if intCount > 0:
        strProductID = strResponse.json()['data']['product'][0]['_id']
        strStatus = strResponse.json()['data']['product'][0]['status']
        blnIsPublished = strResponse.json()['data']['product'][0]['isPublished']
        return {'intCount': intCount, 'strProductID': strProductID, 'strStatus': strStatus, 'blnIsPublished': blnIsPublished}
    else:
        return {'intCount': intCount}


def blockedUnBlocked(dictPayload):
    """
    Method: PUT
    API Endpoint: /products
    Params dictPayload: Payload
    Response: None
    Author: ccapistrano_20231106
    """
    strResponse = uCommon.callPut(dUrl.products.products, dHeaders.withToken(dCommon.api.strAccessToken, False), dictPayload)
    uCommon.validateStatusCode(strResponse)
    
def publishedUnPublished(dictPayload):
    """
    Method: PUT
    API Endpoint: /products
    Params dictPayload: Payload
    Response: None
    Author: ccapistrano_20231106
    """
    strResponse = uCommon.callPut(dUrl.products.products, dHeaders.withToken(dCommon.api.strAccessToken, False), dictPayload)
    uCommon.validateStatusCode(strResponse)
    
def updateProducts(dictPayload):
    """
    Method: PUT
    API Endpoint: /products
    Params dictPayload: Payload
    Response: None
    Author: ccapistrano_20231106
    """
    strResponse = uCommon.callPut(dUrl.products.products, dHeaders.withToken(dCommon.api.strAccessToken, False), dictPayload)
    uCommon.validateStatusCode(strResponse)
