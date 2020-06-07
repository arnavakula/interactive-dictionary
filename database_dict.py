import mysql.connector
from difflib import *

con = mysql.connector.connect(
    username = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database')
cursor = con.cursor()

def is_valid(word):
    cursor.execute('SELECT * FROM Dictionary WHERE Expression = "%s"' %word)
    results = cursor.fetchall()
    return len(results) > 0

def autocorrect(word):
    cursor.execute('SELECT Expression FROM Dictionary')
    terms = [term[0] for term in cursor.fetchall()]
    pred = get_close_matches(word, terms, cutoff=0.8)[0]
    return pred

def has_alternative(word):
    cursor.execute('SELECT Expression FROM Dictionary')
    terms = [term[0] for term in cursor.fetchall()]
    return len(get_close_matches(word, terms, cutoff=0.8)) > 0

def is_alternative(word):
    yn = input("Did you mean %s?(y/n) " %autocorrect(word))
    return yn.lower() == 'y'

def get_valid_input():
    while True:
        word = input("What word do you need the definition for? ").lower()

        if word == '\end':
            return word
        elif normal(word) != False:
            return normal(word)
        elif has_alternative(word) and is_alternative(word):
            return autocorrect(word)
        elif has_alternative(word.upper()) and is_alternative(word.upper()):
            return word.upper()
        elif has_alternative(word.title()) and is_alternative(word.title()):
            return word.title()
        else:
            print("Sorry, this word does not exist in the dictionary. Try again \n")

   
    return "You have broken the system"

def normal(word):
    if is_valid(word):
        return word
    elif is_valid(word.title()):
        return word.title()
    elif is_valid(word.upper()):
        return word.upper()
    else: 
        return False

def alternative(word):
    if has_alternative(word.upper()):
        return is_alternative(word.upper())
    elif has_alternative(word.title()):
        return is_alternative(word.title())
    elif has_alternative(word):
        return is_alternative(word)
    else:
        return False
    
def print_defs(word):
    cursor.execute('SELECT * FROM Dictionary WHERE Expression = "%s"' %word)
    results = cursor.fetchall()
    for result in results:
        print(result[1])

def use_dict():
    while True:
        word = get_valid_input()
        if word == '\end':
            break
        else:
            print_defs(word)

use_dict()