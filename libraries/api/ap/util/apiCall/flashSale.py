import libraries.api.ap.data.headers as dHeaders
import libraries.api.ap.data.url as dUrl

import libraries.api.ap.util.common as uCommon
import libraries.data.common as dCommon



def preUpload(strPayload):
    """
    Method: POST
    API Endpoint: /preUpload
    Params strOrderID: Array SKUs
    Response: None
    Author: ccapistrano_20231019
    """
    strResponse = uCommon.callPost(dUrl.flashSale.preUpload, dHeaders.withToken(dCommon.api.strAccessToken, False), strPayload)
    uCommon.validateStatusCode(strResponse)
    
def flashSale(strPayload):
    """
    Method: POST
    API Endpoint: /flash-sale
    Params strOrderID: Array SKUs
    Response: None
    Author: ccapistrano_20231019
    """
    strResponse = uCommon.callPost(dUrl.flashSale.flashSale, dHeaders.withToken(dCommon.api.strAccessToken, False), strPayload)
    uCommon.validateStatusCode(strResponse)

def getAllActiveUUID():
    """
    Method: GET
    API Endpoint: /product-discount/?page=1&limit=10&search
    Params: None
    Response strUUID: UUID
    Author: ccapistrano_20231023
    """
    strUUID = ''
    strResponse = uCommon.callGet(dUrl.flashSale.search, dHeaders.withToken(dCommon.api.strAccessToken, False))
    for item in range(19):
        if strResponse.json()['data']['list'][item]['status'] == 'active' or strResponse.json()['data']['list'][item]['status'] == 'pending':
            strUUID = f"{strUUID}, {strResponse.json()['data']['list'][item]['uuid']}"
    
    if strUUID != '':
        arrUUID = strUUID.split(', ')
        arrUUID.pop(0)
        return arrUUID
    return strUUID
    
     
def deleteFlashSale(strPayload):
    """
    Method: PUT
    API Endpoint: /flash-sale/cancel
    Params strUUID: UUID
    Response: None
    Author: ccapistrano_20231019
    """
    uCommon.callPut(dUrl.flashSale.cancel, dHeaders.withToken(dCommon.api.strAccessToken, False), strPayload)