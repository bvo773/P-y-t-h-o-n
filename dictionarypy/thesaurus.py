import nltk
from nltk.corpus import wordnet   #Import wordnet from the NLTK
syn = list()
ant = list()
word = str(input("Word: "))
for synset in wordnet.synsets(word):
   for lemma in synset.lemmas():
      syn.append(lemma.name())    #add the synonyms
      if lemma.antonyms():    #When antonyms are available, add them into the list
        ant.append(lemma.antonyms()[0].name())
print('Synonyms: ' + str(syn))
print('Antonyms: ' + str(ant))
