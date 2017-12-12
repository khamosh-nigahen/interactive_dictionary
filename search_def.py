#!/usr/local/opt/python/libexec/bin/python

import json
from difflib import get_close_matches

data = json.load(open("data.json","r"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(),cutoff=0.8)) > 0:
        yes_no = raw_input("Did you mean %s instead? Enter Y if Yes or N if No." % (get_close_matches(w, data.keys(),cutoff=0.8)[0]))
        if yes_no == "Y" or yes_no == "y":
            return data[get_close_matches(w, data.keys(),cutoff=0.8)[0]]
        elif yes_no == "N" or yes_no == "n":
            return "Word Doesnot Exits!!"
        else:
            return "We didn't understand your entry. :("
    else:
        return "Not a Word in the dictionary. Please double check it."

if __name__=="__main__":
    word = raw_input("Enter a word:")
    print(translate(word))

