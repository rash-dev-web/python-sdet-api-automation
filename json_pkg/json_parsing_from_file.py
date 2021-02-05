import json

with open("sample.json") as json_file:
    data = json.load(json_file)

print(data)  # json file data as dictionary
print(type(data))  # <class 'dict'>
