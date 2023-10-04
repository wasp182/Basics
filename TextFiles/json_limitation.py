import json

languages = [
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Modula-2', 1977),
    ('Perl', 1987),
]

filename='test2.json'
with open(filename,'w',encoding='utf-8') as data:
    json.dump(languages,data)

with open(filename,'r',encoding='utf-8') as data2:
    json_tuples=json.load(data2)

print(json_tuples)
# we only get list since json is open standard and tuples are not as common