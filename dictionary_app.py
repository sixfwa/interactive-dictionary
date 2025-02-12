import json
from difflib import get_close_matches

data = json.load(open("data.json")) # Load the JSON file with the words and definitions

def translate(word):

    word = word.lower() # word is set to its' lowercase version
    
    # If the word is a key
    if word in data:
        return data[word]
    # Checks for Nouns
    elif word.title() in data:
        return data[word.title()]
    # Checks for acronyms 
    elif word.upper() in data:
        return data[word.upper()]
    # If the word is mispelt returns closest result
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist"
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist" 

word = input("Enter word: ")

output = translate(word)

# Checks if output is a list
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)