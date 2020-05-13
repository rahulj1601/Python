import json
# JSON --> used to transfer data between server and application, can store data with this language

import difflib # used to complete comparisons between bits of data
from difflib import get_close_matches

data = json.load(open("data.json")) #loads the json data file with all of the word definitions

def translate(word):
    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]
    
    elif get_close_matches(word, data.keys()) != []: #checks to see if the word is close to any word in the json dictionary

        while True:
            wordQ = input("Do you mean %s? Y or N: " % get_close_matches(word, data.keys())[0])
            
            if wordQ == "Y":
                return data[get_close_matches(word, data.keys())[0]]

            elif wordQ == "N":
                return "Please double check the word you have entered."
            
    else:
        return "Please double check the word you have entered."

word = input("Enter word: ").lower()

output = translate(word)

if type(output) == list:
    for each in output:
        print(each)
else:
    print(output)
