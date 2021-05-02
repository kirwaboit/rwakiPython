# In this example we instead use a JSON object that has already been created for us

import json

with open(r'C:\Users\Burudani\Documents\mainPythonFolder_v1\JSON\dictData2.json') as json_file:
    data = json.loads(json_file.read()) # this parses the JSON string

    print(data)
    print('data type is:-')
    print(type(data))