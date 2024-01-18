from datetime import datetime
strDateTimeToday = datetime.today().strftime("%Y%m%d%H%M%S")

############################CONTROLLER############################
env = 'kpc'         # kpc, gls
strOS = 'windows'   # windows, mac
##################################################################

class url:
    strBaseUrl = f'https://www.{env}.edamamalabs.net/'
    strUrlGmail = 'https://www.google.com/gmail/about/'
    strAdminUrl = f'https://admin.{env}.edamamalabs.net'
    strWMSUrl = 'https://auth2.unicommerce.com/'
class time:
    intDefTimeOut = 1000*30
    
class signUp:
    dictData = {
        'strFirstName': f'Qa{strDateTimeToday}',
        'strLastName': 'Testing',
        'strEmailAddress': f'qatesting{strDateTimeToday}@edamama.ph',
        'strPassword': 'Edamama@123!'}
    strChidlName = f'QaChild{strDateTimeToday}'
    
class user:
    strUserName = 'testkpcauto@gmail.com'
    strUserName1 = 'testkpcauto+1@gmail.com'
    strUserName2 = 'testkpcauto+2@gmail.com'
    strUserName3 = 'testkpcauto+3@gmail.com'
    strUserName4 = 'testkpcauto+4@gmail.com'
    strUserName5 = 'testkpcauto+5@gmail.com'
    strUserName6 = 'testkpcauto+6@gmail.com'
    strUserName7 = 'testkpcauto+7@gmail.com'
    strUserName8 = 'testkpcauto+8@gmail.com'
    strUserName9 = 'testkpcauto+9@gmail.com'
    strUserName10 = 'testkpcauto+10@gmail.com'
    strPassword1 = 'Edamama@123!'

    class email:
        strUserName = 'qa@edamama.ph'
        strPassword = 'Quality@QA'
        
    class adminKpc:
        strUserName = 'jean@edamama.ph'
        strPassword = 'Edamama@123!'
        
    class wms:
        strUserName = 'jean@edamama.ph'
        strPassword = 'Edamama@123!'
        
class card:
    strName = 'QA AUTOMATION'
    strNumber = '4000 0000 0000 1091'
    strDate  ='08/24'
    strCvv = '123'
    strPassword = '1234'