from datetime import datetime
import libraries.data.deploymentChecklist as dDepChkLst
strDateTimeToday = dDepChkLst.strDateTimeToday


class AUTO1053:
    #strItemName = 'Baby Gentle Wash & Shampoo (230ml)'
    strItemName = 'Tala Tiles Magnetic Tiles Triangles Set (48-piece)'
    dictData = {
                'strOccassion': f'test occasion{strDateTimeToday}',
                'strAbout': 'test about',
                'strCount': '1'
                }
    
class AUTO1056:
    blnArchived = True
    blnClickable = False
    dictData = {
                'strOccassion': f'test occasion{strDateTimeToday}',
                'strAbout': 'test about',
                }
    
class AUTO1049:
    blnArchived = False
    blnClickable = True

class AUTO1059:
    dictData = {
                'strOccassion': f'test occasion{strDateTimeToday}',
                'strAbout': 'To test if user can create gift list',
                }
    
class AUTO1062:
    dictData = {
                'strOccassion': f'test occasion{strDateTimeToday}',
                'strAbout': 'To test if user can edit gift list',
                'strEditOccassion': f'Event Updated {strDateTimeToday}',
                'strEditAbout' : 'Updated the event description'
                }

class AUTO1065:
    dictData = {
                'strOccassion': f'test occasion{strDateTimeToday}',
                'strAbout': 'To test if user can remove item from gift list',
                'strCount': '1'
                }

class AUTO1068:
    dictData = {
                'strOccassion': f'AUTO-1068 test occasion{strDateTimeToday}',
                'strAbout': 'To test AUTO-1068, if user can create gift list',
                }

class AUTO1071:
    dictData = {
                'strOccassion': '',
                'strAbout': '',
                }

class AUTO1074:
    strMyProfile = 'my profile'
    dictData = {
        'strFirstName': 'QA',
        'strLastName': 'AUTOMATION',
        'strMobile': '9177654321',
        'strProvince': 'METRO MANILA',
        'strCity': 'NAVOTAS CITY',
        'strZipCode': '2222',
        'strBrgy': 'TANZA 1',
        'strLotUnitStBldg': 'BLK 123', 
        'strLandmark': 'ALING NENA STORE',
        
        'strOccassion': f'AUTO-1074 test occasion{strDateTimeToday}',
        'strAbout': 'To test AUTO-1074, if user can create gift list',
    }
    dictData2 = {
        'strFirstName': 'AUTO',
        'strLastName': 'MATION',
        'strMobile': '9171234567',
        'strProvince': 'METRO MANILA',
        'strCity': 'MAKATI CITY',
        'strZipCode': '1111',
        'strBrgy': 'FORBES PARK',
        'strLotUnitStBldg': 'LOT 143', 
        'strLandmark': 'RED GATE'
    }