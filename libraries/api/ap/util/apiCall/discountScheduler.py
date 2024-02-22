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
    strResponse = uCommon.callPost(dUrl.scheduler.preUpload, dHeaders.withToken(dCommon.api.strAccessToken, False), strPayload)
    uCommon.validateStatusCode(strResponse)
    
def productDiscount(strPayload):
    """
    Method: POST
    API Endpoint: /preUpload
    Params strOrderID: Array SKUs
    Response: None
    Author: ccapistrano_20231019
    """
    strResponse = uCommon.callPost(dUrl.scheduler.productDiscount, dHeaders.withToken(dCommon.api.strAccessToken, False), strPayload)
    uCommon.validateStatusCode(strResponse)

def searchScheduler(strSchedulerName):
    """
    Method: GET
    API Endpoint: /product-discount/?page=1&limit=10&search
    Params: None
    Response strUUID: UUID
    Author: ccapistrano_20231019
    """
    strResponse = uCommon.callGet(f'{dUrl.scheduler.search}{strSchedulerName}', dHeaders.withToken(dCommon.api.strAccessToken, False))
    if strResponse.json()['data']['totalCount'] > 0 and strResponse.json()['data']['list'][0]['status'] != 'cancelled':
        strUUID = strResponse.json()['data']['list'][0]['uuid']
        return strUUID
     
def deleteScheduler(strPayload):
    """
    Method: PUT
    API Endpoint: /product-discount/cancel
    Params strUUID: UUID
    Response: None
    Author: ccapistrano_20231019
    """
    uCommon.callPut(dUrl.scheduler.cancel, dHeaders.withToken(dCommon.api.strAccessToken, False), strPayload)