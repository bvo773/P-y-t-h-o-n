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
  else: prefix = "wrong input for book"
  
  return prefix

def passage(book, chapter):
  url = f"http://getbible.net/json?passage={book}{chapter}&raw=true"
  print((url))
  
  response = requests.get(url)
  jdata = json.loads(response.text)
  #print(response.status_code, response.headers)
  #print(jdata)
  
  chapter = jdata["chapter"]
  
  
  for line in chapter.items():
    linenum = line[0]
    linedict = line[1]
    verse = linedict["verse"]
    print(linenum, verse)
 

def main():
  
  book = str(input("Book: ")) 
  chapter = str(input("Chapter: "))
  
  
  passage(get_book_prefix(book.lower()), chapter)
  

if __name__ == '__main__':
  main()

