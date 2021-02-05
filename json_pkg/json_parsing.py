import json

courses = '{"name":"rasheed", "languages":["Python", "JavaScript"]}'

# loads method parse json string and it returns dictionary
dict_courses = json.loads(courses)
print(dict_courses) # {'name': 'rasheed', 'languages': ['Python', 'JavaScript']}

print(type(dict_courses)) # <class 'dict'>

print(dict_courses["languages"][0]) # Python

