import libraries.api.ap.data.headers as dHeaders
import libraries.api.ap.data.url as dUrl

import libraries.api.ap.util.common as uCommon
import libraries.data.common as dCommon

def getCreditsConfigurations():
    """
    Method: GET
    API Endpoint: /credits/configurations
    Params: None
    Response Data: rewardsPercentageCap
    Author: cgrapa_20240222
    """
    strResponse = uCommon.callGet(dUrl.rewards.configurations, dHeaders.withToken(dCommon.api.strAccessToken, False))
    uCommon.validateStatusCode(strResponse)
    responseData = uCommon.getResponseData(strResponse)
    intRewardsPercentageCap = (responseData["data"])["rewardsPercentageCap"]
    intRewardsAmountCap = (responseData["data"])["rewardsAmountCap"]
    dictCreditsConfigurations = {'intRewardsPercentageCap': intRewardsPercentageCap, 'intRewardsAmountCap': intRewardsAmountCap}
    return dictCreditsConfigurations