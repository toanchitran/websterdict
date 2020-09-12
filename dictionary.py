import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys()))>0:
        suggested_w = get_close_matches(w, data.keys())
        i = 0
        while i < len(suggested_w):
            yn  = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[i]).upper()
            if yn == "Y":
                print(data[get_close_matches(w, data.keys())[i]])
                break
            elif yn == "N":
                i = i + 1
                if i == len(suggested_w):
                    return "The word does not exit. Please double check it"
                else:
                    continue
            else:
                print("We do not understand your entry. Please try again")
                i = 0
                continue
    else:
        return "The word does not exit. Please double check it"
word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
