import json
from difflib import get_close_matches

data = json.load(open("076 data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        closem = get_close_matches(word, data.keys())[0]
        a = input("Did you mean " + closem +
                  ". Input Y for yes and N for no: ")
        a = a.lower()
        if a == "y":
            return data[closem]
        elif a == "n":
            return "Word not found in dictionary"
        else:
            return "Entry not understood"
    else:
        return "Word not found in dictionary"


quitt = False
while(not(quitt)):
    user_word = input("Enter word or Press 0 to quit: ")
    if user_word == "0":
        quitt = True
    else:
        output = (translate(user_word))
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)
