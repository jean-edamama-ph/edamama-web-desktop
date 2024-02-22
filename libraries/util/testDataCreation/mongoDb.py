from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

import libraries.data.testDataCreation.testUser as dTestUser

def generateMongoDbConnectionString():
    strPemFilePath = dTestUser.md.strPemFilePath.replace('\\', '%5C').replace(':', '%3A').replace(' ', '+')
        
    strConnectionString = (
        f"mongodb+srv://{dTestUser.md.strConnectionStringScheme}"
        "?authMechanism=MONGODB-X509"
        f"&tlsCertificateKeyFile={strPemFilePath}"
        "&authSource=%24external"
    )
    return strConnectionString

def changeCustomerTypeToVerified(strEmail):
    strConnectionString = generateMongoDbConnectionString()
    searchCriteria = {"email": strEmail}
    editOperation = {"$set": {dTestUser.md.strTypeField: dTestUser.md.strType}}
    try:
        client = MongoClient(strConnectionString)
        db = client[dTestUser.md.strDatabaseName]
        collection = db['users']
        editResult = collection.update_one(searchCriteria, editOperation)
        assert editResult.matched_count > 0, f'Email: {strEmail}, was not found on DB'
    except ConnectionFailure as e:
        raise RuntimeError(f"Connection failed: {e}\nPLEASE MAKE SURE AWS VPN IS RUNNING AND CONNECTED")
    finally:
        client.close()

def updateMobileNumber(strEmail):
    strConnectionString = generateMongoDbConnectionString()
    searchCriteria = {"email": strEmail}
    addOperation = {"$set": {dTestUser.md.strMobileNumberField: dTestUser.md.strMobileNumber}}
    try:
        client = MongoClient(strConnectionString)
        db = client[dTestUser.md.strDatabaseName]
        collection = db['users']
        addResult = collection.update_one(searchCriteria, addOperation)
        assert addResult.matched_count > 0, f'Email: {strEmail}, was not found on DB'
    except ConnectionFailure as e:
        raise RuntimeError(f"Connection failed: {e}\nPLEASE MAKE SURE AWS VPN IS RUNNING AND CONNECTED")
    finally:
        client.close()

def addBeanRewads(strEmail):
    strConnectionString = generateMongoDbConnectionString()
    searchCriteria = {"email": strEmail}
    editOperation = {"$set": {dTestUser.md.strBeanRewardsField: dTestUser.md.strBeanRewards}}
    try:
        client = MongoClient(strConnectionString)
        db = client[dTestUser.md.strDatabaseName]
        collection = db['users']
        editResult = collection.update_one(searchCriteria, editOperation)
        assert editResult.matched_count > 0, f'Email: {strEmail}, was not found on DB'
    except ConnectionFailure as e:
        raise RuntimeError(f"Connection failed: {e}\nPLEASE MAKE SURE AWS VPN IS RUNNING AND CONNECTED")
    finally:
        client.close()

def setupCustomerDetails(strEmail):
    changeCustomerTypeToVerified(strEmail)
    updateMobileNumber(strEmail)
    addBeanRewads(strEmail)