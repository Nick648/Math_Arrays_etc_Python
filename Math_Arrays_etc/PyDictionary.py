from PyDictionary import PyDictionary

dictionary=PyDictionary("hotel","ambush","nonchalant","perceptive")
'There can be any number of words in the Instance'

print(dictionary.printMeanings())
'''This print the meanings of all the words'''
print(dictionary.getMeanings())
'''This will return meanings as dictionaries'''
print (dictionary.getSynonyms())

print (dictionary.translateTo("hi"))
'''This will translate all words to Hindi'''



from PyDictionary import PyDictionary

Dic = PyDictionary("super") # Enter word

synonym = Dic.synonyms()
antonym = Dic.antonyms()

Dic.prin_synonyms()
Dic.prin_antonyms()