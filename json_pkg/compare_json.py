import json

with open("sample.json") as sample_json:
    sample_json_data = json.load(sample_json)

with open("menu_file.json") as menu_file_json:
    menu_file_json_data = json.load(menu_file_json)

assert sample_json_data == menu_file_json_data
