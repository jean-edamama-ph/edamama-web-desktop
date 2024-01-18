import requests
import pytest
import json
import urllib.parse
from datetime import datetime

def pytestIntegration(strSuite):
    strUrl = 'https://api.zephyrscale.smartbear.com/v2/automations/executions/junit?projectKey=AUTO&autoCreateTestCases=true'

    strToken = Input your Zephyr Token
    dictHeaders = {'Authorization': f'Bearer {strToken}'}

    strFilePath = 'reports/output/junitxml_report.xml'
    # file_path = 'reports/backup/output/junitxml_report.xml'
    dictFiles = {'file': open(strFilePath, 'rb')}
    
    strDate = datetime.today().strftime("%m-%d-%Y")
    strTitle = f'{strDate} {strSuite} Test Execution - WEB'
    dictValue = {"name": f"{strTitle}"}
    dictFormData = {'testCycle': dictValue}
    
    response = requests.post(strUrl, json=json.dumps(dictFormData), files = dictFiles, headers = dictHeaders)
    print(response.json())
    print(strTitle)
    assert response.status_code == 200


@pytest.mark.checklist_web()
def test_Deployment_CheckList():    
    pytestIntegration('Deployment Checklist')
    
    
@pytest.mark.sanity_web()
def test_Sanity():
    pytestIntegration('Sanity')
    
    
@pytest.mark.smoke_web()
def test_Smoke():
    pytestIntegration('Smoke')
    
    
@pytest.mark.regression_web()
def test_Smoke():
    pytestIntegration('Regression')

