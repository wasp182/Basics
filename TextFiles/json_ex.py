import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]
filename = 'test.json'
with open(filename,'w',encoding='utf-8') as data:
    json.dump(languages,data)

with open(filename,'r',encoding='utf-8') as readdata:
    json_data = json.load(readdata)

print(json_data)