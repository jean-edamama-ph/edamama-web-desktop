class AUTO858:
    strEmailMsg = 'Email is required.'
    strFirstNameMsg = 'First Name is required.'
    strLastNameMsg = 'Last Name is required.'
    strPasswordMsg = 'Password is required.'
    strEmailInvalid = 'Email is not valid.'
    strPasswordInvalid = 'Password must be at least (6) characters with at least (1) number'
    strPrivacyPolicy = 'Please accept Privacy Policy and Terms of Use to continue'
    dictData = {
        'strFirstName': '',
        'strLastName': '',
        'strEmailAddress': 'test',
        'strPassword': 'test'}
    dictData2 = {
        'strFirstName': 'test',
        'strLastName': 'test',
        'strEmailAddress': 'test@edamama.ph',
        'strPassword': 'test123'}

class AUTO830:
    dictData = {
        'strFirstName': 'testFirstName',
        'strLastName': 'testLastName',
        'strEmailAddress': '',
        'strPassword': 'test123'}
    strMsg = 'Email is required.'

class AUTO831:
    dictData = {
        'strFirstName': '',
        'strLastName': 'testLastName',
        'strEmailAddress': 'testemail@edamama.ph',
        'strPassword': 'test123'}
    strMsg = 'First Name is required.'
    
class AUTO832:
    dictData = {
        'strFirstName': 'testFirstName',
        'strLastName': '',
        'strEmailAddress': 'testemail@edamama.ph',
        'strPassword': 'test123'}
    strMsg = 'Last Name is required.'
    
class AUTO833:
    dictData = {
        'strFirstName': 'testFirstName',
        'strLastName': 'testLastName',
        'strEmailAddress': 'testemail@edamama.ph',
        'strPassword': ''}
    strMsg = 'Password is required.'