import requests
import json
import os

''' Authentication parameters
app_id = os.environ["OXFORD_APP_ID"]
api_key = os.environ["OXFORD_API_KEY"]
'''
'''
endpoint = "entries"
language_code ="en-us"
word_id = input("Word: " )
'''

def getapp_id():
  return os.environ["OXFORD_APP_ID"]

def getapp_apikey():
  return os.environ["OXFORD_API_KEY"]

def find_root_word(word):
  endpoint = "lemmas"
  url = f"https://od-api.oxforddictionaries.com:443/api/v2/{endpoint}/en-us/{word.lower()}"
  response = requests.get(url, headers={"app_id": getapp_id(), "app_key": getapp_apikey()})
  
  #data = json.dumps(response.json()) # returns a string object json
  data = json.loads(response.text) # return a dictionary object json
  results = data["results"]

  #get the root word in lexical list
  result = results[0] #returns a dict
  lexical_entry = result["lexicalEntries"][0]
  root_word = lexical_entry["inflectionOf"][0]["text"]
  
  print(f"Word lemma: {root_word}\n")
  return root_word
 

def find_word_definition(word):
  # Get request to url. Once the response returns, convert the response to unicode txt and json.loads() can be used to parse a valid Json string and
  # convert it to a Python dictionary
  endpoint = "entries"
  root_word = find_root_word(word)
  url = f"https://od-api.oxforddictionaries.com/api/v2/{endpoint}/en-us/{root_word.lower()}"
  response = requests.get(url, headers={"app_id": getapp_id(), "app_key": getapp_apikey()})

  data = json.loads(response.text) # returns a python dictionary object with (response.text -> returns a response in unicode)

  # Get all definitions in array
  results = data["results"]
  result = results[0]
  
  #in result, go to lexicalentries->entrties->senses->definitions, examples,
  #print (results)
  lexicalentries = result["lexicalEntries"]
  for lexicalentry in lexicalentries:
    lexical_category = lexicalentry["lexicalCategory"]["id"]
    print("Part of speech: ", lexical_category)  
   #get the entries to get the definitions
    get_entries(lexicalentry)  


def get_entries(lexicalentry):
  entries = lexicalentry["entries"]
  try:
    definition = entries[0]["senses"][0]["definitions"][0]
    print("Definition: ",definition)
    example = entries[0]["senses"][0]["examples"][0]["text"]
    print("Example: ", example)
    print("=============================================================================")
  except KeyError: #no key found in json
    print("No example found")   
    print("=============================================================================")

def terminate_loop():
  answer = str(input("Look for another word (y/n)? "))
  terminate = False
  if(answer == 'n' or answer == 'N'):
    terminate = False
  elif(answer == 'y' or answer == 'Y'):
    terminate = True
  else:
    print("Sorry, didn't understand your choice, please try again")
    terminate = True

  return terminate
    
def menu():
  print("=============================================================================")
  print("Hello, im botdict, i can help u look up a word with its definitions and examples")
  word = input("\nWhat WORD should botdict look up?  ")
  find_word_definition(word)
  
def main():
  loop = True
  while (loop):
    try:
      menu()
      loop = terminate_loop()
    except KeyError:
      print("Failed to retrieve word. Please check your spelling")
    except ValueError:
      print("Failed to decode json")     

if __name__ == "__main__":
  main()
