# from tqdm import tqdm
# from libraries.util.response.productListing import errorLog
import requests, allure, sys

# import libraries.data.url as dUrl

intErrorCount = 0

def callGet(strUrl, strHeaders, strParams='', strAuth=''):
    """
    Objective: GET API request
    Params: strUrl | strHeaders | strParams | strAuth
    Returns: response
    Author: ccapistra_20230922
    """
    response = requests.get(strUrl, headers=strHeaders, params=strParams, auth=strAuth)
    return response

def callPost(strUrl, strHeaders, strPayload, strAuth='', strFile=''):
    """
    Objective: POST API request
    Params: strUrl | strHeaders | strParams | strAuth
    Returns: response
    Author: ccapistra_20230922
    """
    response = requests.post(strUrl, headers=strHeaders, json=strPayload, auth=strAuth, files=strFile)
    return response

def callPut(strUrl, strHeaders, strPayload, strAuth=''):
    """
    Objective: PUT API request
    Params: strUrl | strHeaders | strParams | strAuth
    Returns: response
    Author: ccapistra_20230925
    """
    response = requests.put(strUrl, headers=strHeaders, json=strPayload, auth=strAuth)
    return response

def getStatusCode(response):
    """
    Objective: Retrieve API status code
    Params: response
    Returns: response.status_code
    Author: ccapistra_20230922
    """
    return response.status_code

def validateStatusCode(strResponse):
    """
    Objective: POST API request and validate response code
    Params: strUrl | strHeaders | strPayload | strAuth
    Returns: response
    Author: ccapistra_20230922
    """
    assert strResponse.status_code == 200, f'Status code is {strResponse.status_code} | Message: {strResponse.json()["message"]}'

def getResponseData(response): 
    """
    Objective: Get API response data
    
    Params: response
    Returns: responseData
    Author: cgrapa_20230803
    """
    responseData = response.json()
    return responseData