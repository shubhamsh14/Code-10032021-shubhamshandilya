# Program for handling the input and output file

import json

class JsonHandle():
    def __init__(self):
        pass

    def readFile(self, filName):
        with open(filName) as json_file:
            return json.load(json_file)

    def writeFile(self, data, fileName):
        with open(fileName,'w') as outFile:
            json.dump(data, outFile)
            outFile.close()
