import requests
import json

'''
BOOK PREFIX VALUE 
 genesis - gen, exodus - ex, leviticus - lev, numbers - num, deuteronomy - deu, joshua - joashua,
 judges - judges, 1 sammuel - 1sam, 2 samuel - 2sam 

'''

def get_book_prefix(book):
  prefix =""
  if (book == "genesis"): prefix = "gen"
  elif (book == "exodus"): prefix = "ex"
  elif (book == "leviticus"): prefix = "lev"
  elif (book == "numbers"): prefix = "num"
  elif (book == "deuteronomy"): prefix = "deu"
  elif (book == "joshua"): prefix = "joshua"
  elif (book == "1 samuel"): prefix = "1sam"
  elif (book == "2 samuel"): prefix = "2sam"
  elif (book == "ruth"): prefix = "ruth"
  elif (book == "1 kings"): prefix ="1kings"
  elif (book == "2 kings"): prefix ="2kings"
  elif (book == "1 chronicles"): prefix ="1chronicles"
  elif (book == "2 chronicles"): prefix ="2chronicles"
  elif (book == "ezra"): prefix ="ezra"
  elif (book == "nehemiah"): prefix ="nehemiah" 
  elif (book == "esther"): prefix ="esther"
  elif (book == "job"): prefix ="job"
  elif (book == "psalm"): prefix ="ps"
  elif (book == "1 kings"): prefix ="1kings"
  else: 
    prefix = "wrong input for book"
  
  return prefix

def get_book(book):
  url = f"https://getbible.net/json?passage={book}&raw=true"
  response = requests.get(url)
  data = json.loads(response.text)
  chapters = data["book"]
  print(f"There are {len(chapters)} chapters. Choose a chapter between 1 - {len(chapters)}")

def get_passage(book, chapter):
  url = f"http://getbible.net/json?passage={book}{chapter}&raw=true"
  print((url))
  
  response = requests.get(url)
  jdata = json.loads(response.text)
  #print(response.status_code, response.headers)
  
  chapter = jdata["chapter"]
  
  for line in chapter.items():
    linenum = line[0]
    linedict = line[1]
    verse = linedict["verse"]
    print(linenum, verse)
 
def menu():
  print("\nBIBLE MENU OPTIONS")
  print("Press 1 - Search for a book")
  print("Press 2 - Search for a passage")
  choice = str(input("My Option: "))
  
  if (choice == "1"): 
    book = str(input("What book would you like me to open? (eg. Genesis): "))  
    prefix = get_book_prefix(book.lower()) 
    get_book(prefix)
    
    chapter = str(input("What chapter would you like me to open?: "))
    get_passage(prefix, chapter)

  elif (choice == "2"):
    book = str(input("Book (eg. Matthew): ")) 
    prefix = get_book_prefix(book.lower())
    get_book(prefix)
    
    chapter = str(input("What chapter do you want to look at?: "))
    get_passage(prefix, chapter)
  
  else:
    print("Invalid choice")

def terminate_loop():
  answer = str(input("Continue (Y/N)?: "))
  terminate = False
  if (answer == 'Y' or answer == 'y'):
    terminate = True
  elif (answer == 'N' or answer == 'n'):
    terminate = False
  
  return terminate
     
def main(): 
  
  #get_passage(get_book_prefix(book.lower()), chapter)
  loop = True
  try:
    while(loop):
      menu()
      loop = terminate_loop()
    print("Hope you enjoy the word. bless u!")
  except KeyError:
    print("Wrong spelling for inputs")
  except ValueError:
    print("Failed to decode json")

if __name__ == '__main__':
  main()
  
