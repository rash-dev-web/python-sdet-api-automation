import json

with open("sample.json") as json_file:
    data = json.load(json_file)

menu_items = data["menu"]["popup"]["menuitem"]
for menu_item in menu_items:
    if menu_item["value"] == "New":
        on_click_value = menu_item["onclick"]
        assert on_click_value == "CreateNewDoc()"
