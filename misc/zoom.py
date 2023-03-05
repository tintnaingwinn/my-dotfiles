from pprint import pprint
import jwt
import requests
import json
from time import time

API_KEY = 'TpNU3zy0RKWGFFNpk47EAw'
API_SEC = 'g9opUKPthbeNPHVTAB4nsJvkX2Z8AXHJvyHk'

# your zoom live meeting id, it is optional though
meetingId = 83781439159

userId = 'Wkjaa_N1TdmAxueEh6va-A'

# create a function to generate a token using the pyjwt library
def generateToken():
    token = jwt.encode(
        # Create a payload of the token containing API Key & expiration time
        {'iss': API_KEY, 'exp': time() + 5000},
        # Secret used to generate token signature
        API_SEC,
        # Specify the hashing alg
        algorithm='HS256'
        # Convert token to utf-8
    )
    return token
    # send a request with headers including a token

#fetching zoom meeting info now of the user, i.e, YOU
def getUsers():
    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}

    r = requests.get('https://api.zoom.us/v2/users/', headers=headers)
    print("\n fetching zoom meeting info now of the user ... \n")
    print(r.text)

def createUsers():
    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}
    
    userdetails = {
        "action": "create",
        "user_info": {
            "email": "amigo.k8@gmail.com",
            "first_name": "TN",
            "last_name": "Win",
            "password": "if42!LfH@",
            "type": 1,
        }
    }

    r = requests.post(f'https://api.zoom.us/v2/users/', headers=headers, data=json.dumps(userdetails))
    print("\n Create new user ... \n")
    print(r.text)

#fetching zoom meeting participants of the live meeting

def getMeetingParticipants():
    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}
    r = requests.get(
        f'https://api.zoom.us/v2/metrics/meetings/{meetingId}/participants', headers=headers)
    print("\n fetching zoom meeting participants of the live meeting ... \n")

    # you need zoom premium subscription to get this detail, also it might not work as i haven't checked yet(coz i don't have zoom premium account)

    print(r.text)


# this is the json data that you need to fill as per your requirement to create zoom meeting, look up here for documentation
# https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingcreate


meetingdetails = {
   "topic":"ageekdev",
   "type":2,
   "start_time":"",
   "duration":100,
   "timezone":"Asia/Bangkok",
   "agenda":"",
   "recurrence":{
      "type":1,
      "repeat_interval":1
   },
   "settings":{
      "host_video":False,
      "participant_video":False,
      "join_before_host":False,
      "mute_upon_entry":False,
      "watermark":True,
      "allow_multiple_devices":True,
      "audio":"voip",
      "auto_recording": False,
      "join_before_host": True,
      "waiting_room": False,
      "breakout_room": {
        "enable":True,
      },
      # "alternative_hosts":"FL0_ksr6Tuyl99jTQzQF3Q",
      "screen_sharing":True,
      "disable_screen_sharing_for_host_meetings":False,
      "disable_screen_sharing_for_in_meeting_guests":False
   }
}

def createMeeting():
    headers = {
        'authorization': 'Bearer %s' % generateToken(),
        'content-type': 'application/json'
    }

    r = requests.post(
        f'https://api.zoom.us/v2/users/{userId}/meetings', headers=headers, data=json.dumps(meetingdetails))

    print("\n creating zoom meeting ... \n")
    obj = json.loads(r.text)
    print(json.dumps(obj, indent=4))

    i = r.json();
    print("\nJoin URL")
    print(i['join_url'])
    print("Meeting ID: " + str(i['id']))
    print("Password: " + str(i['password']))

# getUsers()
# createUsers()
# getMeetingParticipants()
createMeeting()

###################################
# hire me pls ;(
###################################