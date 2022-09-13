import json
import re

uuidlen = 36

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