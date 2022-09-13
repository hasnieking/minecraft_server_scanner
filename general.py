import json
import re

#read json file
def readJSON(filename):
    f = open(filename, "r")
    text = f.read()
    f.close()
    return json.loads(text)

#read text/sql file
def readText(filename):
    f = open(filename, "r")
    text = f.read()
    f.close()
    return text


def removeNonDec(string):
    nondec = re.sub(r'[^0-9]', '', string)
    return nondec