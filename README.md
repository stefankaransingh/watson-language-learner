# Learn a language using IBM Watson
Learn a new word everyday using IBM Watson's Language Translator API

## Access Watson API's - Instructions:

1. You would first need to sign-up for a free IBM Cloud account [here](https://console.eu-gb.bluemix.net/registration/?target=%2Fdeveloper%2Fwatson%2Fdashboard).
2. Select the Watson Language Translator service and add the service from [here](https://console.bluemix.net/developer/watson/services).
3. Click on the name of the service you just created [here](https://console.bluemix.net/developer/watson/existing-services)
4. Click on "Service credentials" and add a new credential.
5. You can then view the credentials and copy the **username** and **password**.
6. Read the documentation for the IBM Watson Language Translator API [here](https://www.ibm.com/watson/developercloud/language-translator/api/v2/).


## Project Setup

1. First get your Username and Password to access IBM Watson's API following the instructions above.
2. Second create a file called local.py containing the following variables. Please Note that the variable names should be exactly the same as the following listed below.
   - USERNAME : "Your IBM Watson API access username."
   - PASSWORD : "Your IBM Watson API access password."
   - SENDER_EMAIL: "The sender's email, currently only Gmail accounts are supported."
   - SENDER_EMAIL_PASSWORD: "The sender's email account's password."
   - RECEIVER_EMAIL: "The receiver's email address."
3. Install the required packages using the command `pip install -r requirements.txt`
4. Currently the default language it translates from is English and the default langugae it translates to is Spanish. To change the language to translate to, you have to first change the value of the variable `LEARN_LANGUAGE` in the file `translate.py` to one of the following supported languages.
  - French
  - Arabic
  - Spanish
  - Portuguese
