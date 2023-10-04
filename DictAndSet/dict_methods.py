d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}
# value_list=[]
# index=0
## Initialise with constructor class
new1_dict= dict(foo=1,bar=2)
print(new1_dict)

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

for key,value in d.items():
    print(key+1,value)

new_dict = d.fromkeys(pantry_items)
print(new_dict)

list_keys=d.keys()
print(list_keys)

d2={7:"lucky seven",10:"tenner"}
d.update(d2)

for key,value in d.items():
    print(key,value)

d.update(enumerate(pantry_items))
print()
for key,value in d.items():
    print(key,value)

# d.values method
print(d.values())

v=d.values()
print('six' in d.values())

value_test = "spam"
for key,value in d.items():
    if value_test == value:
        print(f"{value} found with key {key}")
