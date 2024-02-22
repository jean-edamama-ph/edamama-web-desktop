import libraries.api.ap.data.headers as dHeaders
import libraries.api.ap.data.payload as dPayload
import libraries.api.ap.data.url as dUrl

import libraries.api.ap.util.common as uCommon
import libraries.data.common as dCommon

def postLogin():
    """
    Method: POST
    API Endpoint: /login
    Payload: email | password | latitude | longitude | guestToken
    Response Data: accessToken
    Author: ccapistrano_20230716 
    """
    strResponse = uCommon.callPost(dUrl.login.login, dHeaders.withToken('', False), dPayload.login.login(), dHeaders.auth)
    uCommon.validateStatusCode(strResponse)
    strAccessToken = strResponse.json()['data']['accessToken']
    dCommon.api.strAccessToken = strAccessToken
    
 