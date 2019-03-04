import json

def getDetails_shelf():
    with open('shelfjson.txt', 'r+') as file:
        return json.load(file)
def getDteails_book():
    with open('bookjson.txt', 'r') as file:
        return json.load(file)
def setDetails_shelf(data):
    with open('shelfjson.txt', 'w') as file:
        json.dump(data, file, indent=4)
def setDetails_book(data):
    with open('bookjson.txt', 'w') as file:
        json.dump(data, file, indent=4)


