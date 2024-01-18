https://github.com/chris-brian-edamama-ph/edamamaWeb

1. Download and Install SourceTree(https://www.sourcetreeapp.com/)
    1a. Select Bitbucket Option >> Click Next
    1b. Click Skip >> Next
    1c. Fill Name and Email(Edamama)
    1d. Click "No" button

2. Download and Install Visual Studio Code(https://code.visualstudio.com/Download)
    2a. Open your workspace Folder 
    NOTE: Do not forget to tick "TRUST THE AUTHORS OF ALL FILES...." checkbox
    2b. Click "Yes, I trust the authors...." button
 
3. Download and Install Python(latest version - https://www.python.org/downloads/)
    # windows
    3a. When installing Python dont forget to tick "Add python.exe to Playwright" check box
    3b. Once successfully installed, Open CMD and enter:
        - python -V
        - where python
        - python
    3c. Check if added on the Environment variables(User variable) >> double click "Path" Variable
        - C:\Users\<userfolder> Tech\AppData\Local\Programs\Python\Python<version>\
        - C:\Users\<userfolder> Tech\AppData\Local\Programs\Python\Python<version>\Scripts\
        Note: Add manually if missing (Use "where python" to check correct folder path)
    3d. Add on Environment variable(User variable) >> Click "New..." button
        - PYTHONPATH = C:\Users\<userfolder>

    # mac      
    3a. Sownload and install Python
    3b. Once successfully installed, Open CMD and enter:
        - python -V
        - which python
    3c. Add on Environment variable(User variable) >> Click "New..." button
        - Open terminal
            - Enter 'touch .bash_profile'
            - Enter 'open .bash_profile'
                - Copy and paste in the .bash_profile terminal:
                    export PATH="/usr/local/bin:$PATH" 
                    export PATH="/Users/<userName>/edamamaWeb/vmWEB/bin/playwright:$PATH" (or you can type 'which playwright' to see the directory)
            - Enter 'source .bash_profile
     
4. Download and Add to PATH Allure(https://github.com/allure-framework/allure2/releases)
    4a. Extract downloaded folder in your C:\Program Files
    4b. Add on the Environment variables(System variable) >> double click "Path" Variable >> "New" button
        - C:\Program Files\allure-<version>\bin

5. How to create Python Virtual Machine
    Open terminal(Ctrl + `) and enter:
    # windows
    5.1. Create your VM path directory: 
        # windows
        - py -m venv <VMname> (py -m venv vmWEB)
    5.2. Activate you VM:
        # windows
        - .\vmWEB\Scripts\activate (If error encountered - Perform Issue Encountered 1)
        Note: To deactivate - deactivate
    5.3. Install requirements.txt
        5.3a. to Install, enter (vmWEB should be activated)
            - pip install -r requirements.txt
            - python.exe -m pip install --upgrade pip (if need to update)
            Note: To generate a new requirement.txt file - pip freeze > requirements.txt

    # mac
    5.1. Create your VM path directory: 
        - python3 -m venv vmWEB
    5.2. Activate you VM:
        - source vmWEB/bin/activate
        Note: To deactivate - deactivate
    5.3. Install requirements.txt
        5.3a. to Install, enter (vmWEB should be activated)
            - pip install -r requirements.txt
            - python.exe -m pip install --upgrade pip (if need to update)
            Note: To generate a new requirement.txt file - pip freeze > requirements.txt

(OPTIONAL)
6. Follow Python Playwright Installation Guide - https://playwright.dev/python/docs/intro
    6a. Open terminal(Ctrl + `) and enter:
        - pip install pytest-playwright
        - pip install --upgrade pip
        - playwright install
ç 
    6b. Python
        Python Extension Pack
        python snippets 
        




###########################################################################################################################################################
#                                                                   HOW TO EXECUTE TEST                                                                   #          
#       1. Click libraries\data\common.py >> use your desire ENV and OS                                                                                   #
#           env = 'kpc'                                                                                                                                   #
#           os = 'windows'                                                                                                                                #
#       2. Click pytest.ini >> uncomment your desire test suite                                                                                           # 
#           a. To run all tests under deploymentChecklist                                                                                                 #
#               addopts = -v -s --alluredir="allure-result" libraries\\tests\\deploymentChecklist --headed -n 5 --reruns 2 -m 'deploymentChecklist'       #
#           b. To run all tests under sanityTesting                                                                                                       #
#               addopts = -v -s --alluredir="allure-result" libraries\\tests\\deploymentChecklist --headed  -n 5 --reruns 2 -m 'sanityTesting'            #
#           c. To run all tests under smokeTesting                                                                                                        #
#               addopts = -v -s --alluredir="allure-result" libraries\\tests\\deploymentChecklist --headed -n 5 --reruns 2 -m 'smokeTesting'              #
#       3. In your terminal type "pytest" then press "Enter"                                                                                              #
#       4. To run a report >> In your terminal type "allure serve allure-result/" then press "Enter"                                                      #  
###########################################################################################################################################################



Issue Encountered:
1. When activating VM (File C:\Users\Edamama Tech\Desktop\playwright(POC)\vmtest\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on
this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.)
    - Step 1. Open the Windows PowerShell as an administrator by the above method.
    - Step 2. Then type the command "Get-ExecutionPolicy" and hit Enter.
    - Step 3. Then type the command "Set-ExecutionPolicy RemoteSigned" and hit Enter.
    - Step 4. Then type the command "Y" and hit Enter.
    
2. When using allure serve (The term 'allure' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the..)
    -restart Visual Studio Code or Restart Laptop

3. PR can not push error encountered: (SourceTree)
    git -c diff.mnemonicprefix=false -c core.quotepath=false --no-optional-locks push -v --tags origin Working:Working
    remote: Login failed due to incorrect login credentials or method.
    remote: If you are unsure of which login details or login method to use, visit:
    remote: https://support.atlassian.com/bitbucket-cloud/docs/log-into-or-connect-to-bitbucket-cloud/
    fatal: Authentication failed for 'https://bitbucket.org/<FOLDER>/<REPO>.git/'

    Solution:
    1. Create PERSONAL ACCESS TOKEN(PAT) in your GIT >> note your PERSONAL ACCESS TOKEN(PAT) -- https://github.com/settings/tokens
    2. delete "passwd" file  in your \\AppData\Local\Atlassian\SourceTree
    3. Open SourceTree >> push you code >> password prompt will appear >> paste your PERSONAL ACCESS TOKEN(PAT)



#####################################################################################################################################################################################
#                                                                   DATA SETUP AFTER CLEAN UP                                                                                       #          
#       1. Run test_Create_Test_User in libraries\tests\testDataCreation\test_createTestUser.py                                                                                     #
#           1a. Go to https://admin.kpc.edamamalabs.net/admin/users >> search for user "testkpcauto@gmail.com" and "testkpcmanual@gmail.com" >> add 1000000 beans                   #
#           1b. Mobile verification in MongoDB for users "testkpcauto@gmail.com" and "testkpcmanual@gmail.com"                                                                      #
#       2. Run test_Create_Promo_Code in libraries\tests\testDataCreation\test_createTestUser.py                                                                                    #
#           Using promoceode "EDAMAYA100", "BEAN300", "CETAFLAT50" and "EDAPERC10"                                                                                                  #
#       3. Run Backend Monolith                                                                                                                                                     #
#           3a. Open AWS VPN Client                                                                                                                                                 #
#           3b. Select AP Southeat 1 >> Click Connect                                                                                                                               #
#           3c. Open Backend Monolith in Visual Studio                                                                                                                              #
#           3d. npm run _cli/run createDummyCustomer -- --bundleId=kpc --count=10 --start=1 --email=testkpcauto@gmail.com - AUTOMATION testkpcauto+1@gmail.com/Edamama@123!         #
#           3e. npm run _cli/run createDummyCustomer -- --bundleId=kpc --count=100 --start=1 --email=testkpcmanual@gmail.com - MANUAL testkpcmanual+1@gmail.com/Edamama@123!        # 
#                                                                                                                                                                                   #
#           OR                                                                                                                                                                      #
#                                                                                                                                                                                    #
#           3d. npm run _cli/run createDummyCustomer -- --bundleId=kpc --count=40 --start=11 --email=testkpcauto@gmail.com - AUTOMATION testkpcauto+1@gmail.com/Edamama@123!         #
#           3e. npm run _cli/run createDummyCustomer -- --bundleId=kpc --count=40 --start=11 --email=testkpcmanual@gmail.com - MANUAL testkpcmanual+1@gmail.com/Edamama@123!        #                                                                                                                                          #  
#####################################################################################################################################################################################


npm run _cli/run createDummyCustomer -- --bundleId=kpc --count=40 --start=11 --email=testkpcmanual@gmail.com