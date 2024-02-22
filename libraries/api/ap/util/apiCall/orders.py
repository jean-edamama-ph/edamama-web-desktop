import libraries.api.ap.data.headers as dHeaders
import libraries.api.ap.data.url as dUrl

import libraries.api.ap.util.common as uCommon
import libraries.data.common as dCommon


def getOrderDetailsViaOrderID(strParam):
    """
    Method: GET
    API Endpoint: /orders
    Params strParam: page = 1 | limit = 10 | search = strOrderID
    Response Data: Order Details
    Author: ccapistrano_20230922
    """
    strResponse = uCommon.callGet(dUrl.order.order, dHeaders.withToken(dCommon.api.strAccessToken, False), strParam)
    uCommon.validateStatusCode(strResponse)
    strOrderID = strResponse.json()['data']['order'][0]['orderNumber']
    strCustomerName = strResponse.json()['data']['order'][0]['user']['name']
    strFirstName = strResponse.json()['data']['order'][0]['user']['firstName']
    strLastName = strResponse.json()['data']['order'][0]['user']['lastName']
    intQuantity = strResponse.json()['data']['order'][0]['orderItems'][0]['quantity']
    intPaymentMethod = strResponse.json()['data']['order'][0]['paymentMethod']
    intShippingAmount = strResponse.json()['data']['order'][0]['orderSummary']['shippingCharge']
    intTotalAmount = strResponse.json()['data']['order'][0]['orderSummary']['totalAmount']
    intFinalStatus = strResponse.json()['data']['order'][0]['finalStatus']
    return {'strOrderID': strOrderID, 'strCustomerName': strCustomerName, 'strFirstName': strFirstName, 'strLastName': strLastName, 'intQuantity': intQuantity,
            'intPaymentMethod': intPaymentMethod, 'intShippingAmount': intShippingAmount, 'intTotalAmount': intTotalAmount, 'intFinalStatus': intFinalStatus}
    
def getAddressDetailsViaOrderID(strOrderID):
    """
    Method: GET
    API Endpoint: /getOrder
    Params strOrderID: Order ID
    Response Data: Address Details
    Author: ccapistrano_20231017
    """
    strResponse = uCommon.callGet(f'{dUrl.order.getOrder}{strOrderID}', dHeaders.withToken(dCommon.api.strAccessToken, False))
    uCommon.validateStatusCode(strResponse)
    strID = strResponse.json()['data']['_id']
    strFullName = strResponse.json()['data']['deliveryAddress']['fullName']
    strRegion = strResponse.json()['data']['deliveryAddress']['region']['name']
    strCity = strResponse.json()['data']['deliveryAddress']['city']['name']
    strBarangay = strResponse.json()['data']['deliveryAddress']['barangay']['name']
    strLandmark = strResponse.json()['data']['deliveryAddress']['landmark']
    strBuildingNumber = strResponse.json()['data']['deliveryAddress']['buildingNumber']
    strZipCode = strResponse.json()['data']['deliveryAddress']['zipCode']
    return {'strID': strID, 'strFullName': strFullName, 'strRegion': strRegion, 'strCity': strCity, 'strBarangay': strBarangay,
            'strLandmark': strLandmark, 'strBuildingNumber': strBuildingNumber, 'strZipCode': strZipCode}

def updateDetails(dictPayload):
    """
    Method: PUT
    API Endpoint: /getOrder
    Params dictPayload: Payload
    Response: None
    Author: ccapistrano_20231027
    """
    strResponse = uCommon.callPut(dUrl.order.updateDetails, dHeaders.withToken(dCommon.api.strAccessToken, False), dictPayload)
    uCommon.validateStatusCode(strResponse)
    
# def massCancellation():
#     """
#     Method: GET
#     API Endpoint: /getOrder
#     Params strOrderID: Order ID
#     Response Data: Address Details
#     Author: ccapistrano_20231017
#     """
#     strFile = './libraries/data/uploadFile/order-cancellation.csv'
#     strFile = {"file": open(strFile, "rb")}
#     strFile = {"file": (strFile, open(strFile, "rb"))}
#     strFile = {'csv_file': (strFile, open(strFile, 'rb'))}
#     strResponse = uCommon.callPost(f'{dUrl.order.processMassOrderCancel}', dHeaders.withToken(dCommon.api.strAccessToken, False), '', strFile)
#     uCommon.validateStatusCode(strResponse)
#     strFullName = strResponse.json()['data']['deliveryAddress']['fullName']
#     strRegion = strResponse.json()['data']['deliveryAddress']['region']['name']
#     strCity = strResponse.json()['data']['deliveryAddress']['city']['name']
#     strBarangay = strResponse.json()['data']['deliveryAddress']['barangay']['name']
#     strLandmark = strResponse.json()['data']['deliveryAddress']['landmark']
#     strBuildingNumber = strResponse.json()['data']['deliveryAddress']['buildingNumber']
#     strZipCode = strResponse.json()['data']['deliveryAddress']['zipCode']
#     return {'strFullName': strFullName, 'strRegion': strRegion, 'strCity': strCity, 'strBarangay': strBarangay,
#             'strLandmark': strLandmark, 'strBuildingNumber': strBuildingNumber, 'strZipCode': strZipCode}