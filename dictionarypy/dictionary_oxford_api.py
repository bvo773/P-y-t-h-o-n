import json
import requests
import os

app_id = os.environ["OXFORD_APP_ID"]
app_apikey = os.environ["OXFORD_API_KEY"]

endpoint="entries"
language_code="en-us"
word_id=input('Word: ') 

#url = "https://od-api.oxforddictionaries.com/api/v2/{endpoint}/{language_code}/{word_id.lower()}".format(endpoint,language_code,word_id)

url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower() 


response = requests.get(url, headers= {"app_id": app_id, "app_key": app_apikey})
#data = response.json()
#print(type(data), data)

json_data = json.loads(response.text) #or data = response.json()
print(json_data)
#print(type(json_data), json_data)

#result_definition = json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]

#result_part_of_speech = json_data['results'][0]['lexicalEntries'][0]['lexicalCategory']['text']
#results = json_data['results'].[0]['lexicalEntries'].['entries'].[0]['senses'].[0]['definitions']
#print(json_data)

#print("\nDefinition: " + result_definition)
#print("\nPart of speech: " + result_part_of_speech +'\n')


