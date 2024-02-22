import libraries.api.ap.data.headers as dHeaders
import libraries.api.ap.data.url as dUrl
import libraries.api.ap.data.payload as dPayload
import libraries.api.ap.util.common as uCommon

import libraries.data.common as dCommon

def getSubscriptionIDViaOrderID(strOrderID):
    """
    Method: GET
    API Endpoint: /getOrder
    Params strOrderID: Order ID
    Response Data: finalStatusa
    Author: ccapistrano_20230925
    """
    strResponse = uCommon.callGet(f'{dUrl.subscription.getOrder}{strOrderID}', dHeaders.withToken(dCommon.api.strAccessToken, False))
    uCommon.validateStatusCode(strResponse)
    instSubscriptionID = (strResponse.json()['data']['subscriptions'])[0]
    return instSubscriptionID


def getSubscriptionIDViaCustomerName(strCustomerName):
    """
    Method: GET
    API Endpoint: /getOrder
    Params strCustomerName: Customer Name
    Response Data: finalStatusa
    Author: ccapistrano_20230925
    """
    strCustomerName = strCustomerName.replace(' ', '%20')
    strResponse = uCommon.callGet(f'{dUrl.subscription.subscription(strCustomerName)}', dHeaders.withToken(dCommon.api.strAccessToken, False))
    if strResponse.json()['statusCode'] == 200 and strResponse.json()['data']['totalCount'] != 0:
        instSubscriptionID = strResponse.json()['data']['product'][0]['_id']
    else:
        instSubscriptionID = ''
    
    return instSubscriptionID


def cancelOrderViaSubscriptionID(strSubscriptionID):
    """
    Method: GET
    API Endpoint: /getOrder
    Params strOrderID: Order ID
    Response Data: finalStatusa
    Author: ccapistrano_20230925
    """
    strResponse = uCommon.callPut(dUrl.subscription.cancel, dHeaders.withToken(dCommon.api.strAccessToken, False), dPayload.subcription.cancel(strSubscriptionID))
    uCommon.validateStatusCode(strResponse)