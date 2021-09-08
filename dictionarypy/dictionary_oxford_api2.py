import requests
import json
import os

# Authentication parameters
app_id = os.environ["OXFORD_APP_ID"]
api_key = os.environ["OXFORD_API_KEY"]

endpoint = "entries"
language_code ="en-us"
word_id = input("Word: " )

url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()

response = requests.get(url, headers={"app_id": app_id, "app_key": api_key})

json_data = json.loads(response.text) # returns a python dictionary object with (response.text -> returns a response in unicode)

definitions_arr = json_data["results"]
i = 1
for definition in definitions_arr:
    meaning = definition["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
    #print (type(meaning))
    print(f"\nDefinition {i}: {meaning}")
    i+=1
#print(json_data)
