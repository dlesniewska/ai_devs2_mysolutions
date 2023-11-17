import json

class JsonReader:
    def read(self):
        singleJsonsList = []
        print("Started Reading JSON file which contains multiple JSON document")
        with open("sample.json") as f:
            braceCount = 0
            jsonStr = ''
            for jsonObj in f:

                if jsonObj != '[\n' and jsonObj !=']':
                    braceCount += jsonObj.count('{')
                    braceCount -= jsonObj.count('}')
                    if jsonObj.count('},'):
                        print('repairing')
                        jsonObj = '}'
                    jsonStr += jsonObj
                    print(jsonStr)
                    if (braceCount == 0):
                        singleJsonDict = json.loads(jsonStr)
                        singleJsonsList.append(singleJsonDict)
                        jsonStr = ''

        print("Printing each JSON Decoded Object")
        for entry in singleJsonsList:
            print(entry["title"], entry["url"], entry["info"], entry["date"])


if __name__ == '__main__':
    JsonReader().read()