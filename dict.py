import json
from difflib import *

data = json.load(open('data.json'))

def is_valid(word):
    return word in data 

def has_alternative(word):
  return len(get_close_matches(word, data.keys())) > 0

def autocorrect(word):
    lst = get_close_matches(word, data.keys())
    return lst[0]

def handle_autocorrect(word):
    pred = autocorrect(word)
    ans = input("Did you mean %s?(y/n)" %pred)
    return pred if(ans.lower() == 'y') else word


def get_word():
    while True:
        word = str(input('Enter a word you would like to search up: '))
        word = word.lower()
        first = word

        if is_valid(first):
            break
        elif not is_valid(first) and has_alternative(first):
            word = handle_autocorrect(first)
            
        if word == first or not has_alternative(first):
            print('That word is not found in the dictionary. Try again.\n')
        else: 
            break
       

    return word

def print_def(word):
    defs = data[word]
    for d in defs:
        print(d)

print_def(get_word())