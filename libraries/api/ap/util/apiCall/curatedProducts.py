import libraries.api.ap.data.headers as dHeaders
import libraries.api.ap.data.url as dUrl
import libraries.api.ap.data.payload as dPayload
import libraries.data.common as dCommon

import libraries.api.ap.util.common as uCommon


def getCuratedRanks():
    """
    Method: GET
    API Endpoint: /curatedType
    Params: None
    Response arrRanks: Array Curated ID and Title
    Author: ccapistrano_20230925
    """
    strResponse = uCommon.callGet(dUrl.curated.curatedTypeList, dHeaders.withToken(dCommon.api.strAccessToken, False))
    uCommon.validateStatusCode(strResponse)
    inctCount = strResponse.json()['data']['totalCount']
    arrRanks = []
    for item in range(inctCount):
        arrRanks.append(f'{strResponse.json()["data"]["curatedTypes"][item]["_id"]} | {strResponse.json()["data"]["curatedTypes"][item]["title"]}')
    return arrRanks


def rankCurated(arrRanks, strSort):
    """
    Method: PUT
    API Endpoint: /curatedType/rank
    Params strSort: Asc or Desc
    Response arrRanks: Array Curated ID and Title
    Author: ccapistrano_20230925
    """
    intCount = len(arrRanks)
    arrPayload = []
    if strSort == 'desc':
        arrRanks = arrRanks[::-1]
    
    for item in range(intCount):
        strRanks = arrRanks[item]
        strID = (strRanks.split(' | '))[0]
        arrPayload.append({"curatedTypeId":str(strID),"rank":item+1})
     
    strResponse = uCommon.callPut(dUrl.curated.rank, dHeaders.withToken(dCommon.api.strAccessToken, False), arrPayload)
    uCommon.validateStatusCode(strResponse)
    return arrRanks 

def getAllProductsInCuratedCollection(strCuratedId):
    """
    Method: GET
    API Endpoint: /curatedType/strCuratedId
    Params: None
    Response Data: Array Products
    Author: ccapistrano_20230925
    """
    strResponse = uCommon.callGet(f'{dUrl.curated.curatedType}/{strCuratedId}', dHeaders.withToken(dCommon.api.strAccessToken, False))
    uCommon.validateStatusCode(strResponse)
    arrProducts = strResponse.json()['data']['products']
    return arrProducts

def addRemoveItemInCuratedCollection(strCuratedId, arrProducts, strItemID, strAddRemove):
    """
    Method: PUT
    API Endpoint: /curatedType/strCuratedId
    Params: None
    Response Data: Array Products
    Author: ccapistrano_20230925
    """
    if strAddRemove == 'add':
        arrProducts.append({'_id': strItemID, 'rank': 1})
        for item in range(len(arrProducts)):
            arrProducts[item]['productId'] = arrProducts[item].pop('_id')
            arrProducts[item]['rank'] = arrProducts[item].pop('rank')
    elif strAddRemove == 'remove':
        arrProducts.remove({'productId': strItemID, 'rank': 1})
    
    dictPayload = {'products': arrProducts,'curatedTypeId': strCuratedId}
    strResponse = uCommon.callPut(dUrl.curated.curatedType, dHeaders.withToken(dCommon.api.strAccessToken, False), dictPayload)
    uCommon.validateStatusCode(strResponse)