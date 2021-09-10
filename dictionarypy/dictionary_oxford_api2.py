import requests
import json
import os

# Authentication parameters
app_id = os.environ["OXFORD_APP_ID"]
api_key = os.environ["OXFORD_API_KEY"]

endpoint = "entries"
language_code ="en-us"
word_id = input("Word: " )

# Get request to url. Once the response returns, convert the response to unicode txt and json.loads() can be used to parse a valid Json string and
# convert it to a Python dictionary
url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()

response = requests.get(url, headers={"app_id": app_id, "app_key": api_key})

json_data = json.loads(response.text) # returns a python dictionary object with (response.text -> returns a response in unicode)


# Get all definitions in array
results = json_data["results"]

i = 1
for result in results:
    lexical_entries = result["lexicalEntries"]
    for lexical_entry in lexical_entries:

'''
i = 1
for result in results_arr:
  lexical_entries = result['lexicalEntries']
 
  for lexical_entry in lexical_entries:
    part_of_speech = lexical_entry['lexicalCategory']['id']
    definition_senses = lexical_entry['entries'][0]['senses']
    print(f"\nPart of Speech: {part_of_speech}")
    
    for definition_sense in definition_senses:
      definition = definition_sense['definitions'][0]
      print(f"\nDefinition {i}: {definition}")
      i+=1
    
    print("---------------------------------------------------------------------------")

'''
