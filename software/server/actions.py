import json

def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as user_config:
        return json.load(user_config)

