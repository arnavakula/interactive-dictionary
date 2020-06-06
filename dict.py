import json

data = json.load(open('data.json'))

def is_valid(word):
    return word in data 

def get_word():
    while True:
        word = str(input('Enter a word you would like to search up: '))
        word.lower()

        if not is_valid(word):
            print('That word is not found in the dictionary. Try again.')
        else:
            break

    return word

def print_def(word):
    defs = data[word]
    for d in defs:
        print(d)


print_def(get_word())


