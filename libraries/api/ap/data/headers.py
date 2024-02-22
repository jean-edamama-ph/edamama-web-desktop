from requests.auth import HTTPBasicAuth

import libraries.api.ap.util.apiCall.login as apiLogin
# auth = HTTPBasicAuth('edamama', 'edamama@123')

auth = ('edamama', 'edamama@123')



def withToken(strToken = '', blnGuestToken = False):
    if strToken == '' and blnGuestToken == False:
        headers = {"Api-Key": "1234", "User-Agent":"edamama-load"}
    elif strToken != '' and blnGuestToken == True:
        headers = {"Guest-Token": f'{strToken}', "Api-Key": "1234", "User-Agent":"edamama-load"}
    else:
        headers = {"Authorization": f'Bearer {strToken}', "Api-Key": "1234", "User-Agent":"edamama-load"}
    return headers