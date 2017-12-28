import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def find(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        mod = input("Did u mean %s instead? If yes press Y or N for no: " % get_close_matches(word,data.keys())[0])
        if mod=="Y":
            word=get_close_matches(word,data.keys())[0]
            return find(word)
        else:
            return "Word doesn't exits, Please double check"
    else:
        return "Word doesn't exist, Please double check"

word = input("Enter word: ")

output = find(word)

if type(output)==list:
    for items in output:
        print(items)
else:
    print(output)
