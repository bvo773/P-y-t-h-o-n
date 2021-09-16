from spellchecker import SpellChecker
spell = SpellChecker()

word = str(input('Word: '))
print(spell.correction(word))
print(spell.candidates(word))
