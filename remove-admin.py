import requests
import json


#Collecting input to generate input URLs, then creating URLs
customer = raw_input("What customer is this for?:\n Example: alterra\n ")
environment = raw_input("What Environment is this for?:\n Type prod or stage\n ")
userListURL =  "https://ops.te2.io/rest/customer/"+customer+"/environment/"+environment+"/users"
userRolesURL = "https://ops.te2.io/rest/customer/"+customer+"/environment/"+environment+"/roles"
userUpdateURL = "https://ops.te2.io/rest/customer/"+customer+"/environment/"+environment+"/user"


#Searching for text file that is storing cookie header from EOS
print("Searching for eoscookie.txt")
#cookie = "_ga=GA1.2.900698836.1637098833; connect.sid=s%3AKHRLbpcA8Qvac7nPVxnBhtRiPlcJT3eU.WtljLVWKfCvdvcT%2BmCknxZHTYY1%2Bajuhz2Bt%2Be6pN30; _gid=GA1.2.1757648057.1638299111; mp_b4a6e096c5a8c1e6e0d8161b063ef928_mixpanel=%7B%22distinct_id%22%3A%20%22adrian.harris%40accesso.com%22%2C%22%24device_id%22%3A%20%2217d6cf61ca5c2e-0fd2a01854d829-1f396452-1aeaa0-17d6cf61ca61040%22%2C%22lastVisit%22%3A%20%222021-11-29T18%3A30%3A08Z%22%2C%22name%22%3A%20%22adrian.harris%40accesso.com%22%2C%22sessionId%22%3A%20%22XcvCfwJT87GXelIWAlWK7TVXQP_BATsf%22%2C%22%24user_id%22%3A%20%22adrian.harris%40accesso.com%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; mp_3e4e018fd73aee9bf0f84155bb19ca79_mixpanel=%7B%22distinct_id%22%3A%20%22adrian.harris%40accesso.com%22%2C%22%24device_id%22%3A%20%2217d76d331aa6f0-08a834fa46b60e-1f396452-1aeaa0-17d76d331abfc6%22%2C%22lastVisit%22%3A%20%222021-12-01T16%3A28%3A12Z%22%2C%22name%22%3A%20%22adrian.harris%40accesso.com%22%2C%22sessionId%22%3A%20%22dHaJg1FGV9tc5ZrEC79rwLUfHe5Tpf_K%22%2C%22%24user_id%22%3A%20%22adrian.harris%40accesso.com%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; mp_a09407ba50c261d87858ce0d1ca84941_mixpanel=%7B%22distinct_id%22%3A%20%22adrian.harris%40theexperienceengine.com%22%2C%22%24device_id%22%3A%20%2217d6cec5978543-00021351b98e6f-1f396452-1aeaa0-17d6cec5979f62%22%2C%22Last%20Site%20Visit%22%3A%20%222021-11-29T18%3A19%3A28Z%22%2C%22Role%22%3A%20%22editor%22%2C%22%24user_id%22%3A%20%22adrian.harris%40theexperienceengine.com%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D"
with open('eoscookie.txt','r') as file:
 cookie = file.read()


headers = {   "authority": "ops.te2.io","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"', 
  "accept": "application/json, text/plain, */*","sec-ch-ua-mobile": "?0",
  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
  "sec-ch-ua-platform": '"macOS"',
  "sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty",
  "referer": "https://ops.te2.io/","accept-language": "en-US,en;q=0.9",
  "cookie": cookie}


#Making API request and storing data into Python variable as JSON

#User List contain list of all Control Room Users
userListRequest = requests.get(userListURL, headers=headers)
userListData = userListRequest.json()

#Role data contains all current data about user roles
userRolesRequest = requests.get(userRolesURL, headers=headers)
userRoleData = userRolesRequest.json()


#Creating dictionary that stores Role ID as key and Role name as value for lookup.

userRoleDict = {}

for x in userRoleData:
  userRoleDict[x['id']] = x['name']
  print(userRoleDict[x['id']])

#Opening file for output




counter = 0
listOnlyAdmin = "List users with only admin access\n"

#Outer loop selects user from userlist and makes API call for specific user info
for x in userListData:
    
    if "accesso" in x["username"]:
        print("Found accesso employee " + x["username"])
        continue
    singleUserRequest = requests.get(userListURL+"/"+x['username'], headers=headers)
    singleUserData = singleUserRequest.json()
    if len(singleUserData['roles']) == 1 and singleUserData['roles'][0] == "admin" :
        listOnlyAdmin += x['username']+"\n"
        continue


#Inner loop preps individual user info to be added to csv file
    for y in singleUserData['roles']:
        if y == "admin":
            counter += 1
            
            singleUserData['roles'].remove(y)
            print(json.dumps(singleUserData))
            response = requests.post(userUpdateURL+"/"+x['username'], headers=headers,json = singleUserData)
            print(response.text)
            break
    print(counter)

print(listOnlyAdmin)

