#!/usr/local/opt/python/libexec/bin/python

import json

data = json.load(open("/Users/puneetjain/Downloads/data.json","r"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "Not a Word in the dictionary. Please double check it."

if __name__=="__main__":
    word = raw_input("Enter a word:")
    print(translate(word))

