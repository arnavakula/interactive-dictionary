import json
from difflib import *

data = json.load(open('data.json'))
done = False

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
        proper = word.title()
        word = word.lower()
        first = word
        
        if word =='\end' or is_valid(first):
            return word
        elif is_valid(proper):
            return proper
        elif not is_valid(first) and has_alternative(first):
            word = handle_autocorrect(first)
            
        if word == first or not has_alternative(first):
            print('That word is not found in the dictionary. Try again.\n')
        else: 
            break
       
    return word

def print_def(word):
    if word == '\end':
        print()
    else:
        defs = data[word]
        for d in defs:
            print(d)

def use_dict():
    while True:
        word = get_word()
        if word == '\end':
            break
        else:
            print_def(word)

use_dict()