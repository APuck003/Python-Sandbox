#!/usr/bin/env python3
import json
from difflib import get_close_matches

data = json.load(open('/Users/Austin_MacBook/Desktop/Austin_Python_Projects/Interactive Dictionary/data.json'))

def word_return(word):
    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yes_no = input("Did you mean {} instead? Enter Y is yes or N if no. ".format(get_close_matches(word, data.keys())[0]))
        yes_no = yes_no.lower()
        if yes_no == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yes_no == "n":
            return "Your word does not exists. Check your spelling."
        else:
            return "I didn't understand your entry."
    else:
        return "You must enter a real word."

word = input("Enter word to define: ")

output = word_return(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
