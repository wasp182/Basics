animals={
    "lion": "scary",
    "elephant":"big",
    "teddy":"soft",
}

things = animals
animals["teddy"]="new soft"
print(things)

things=animals.copy()
# this makes shallow copy where underlying change is not reflected in new
# dictionary
# with immutble objects , shallow or deep copy is same
# only if objects in dictionary are mutable then shallow vs deep is relevant


animals["teddy"] = "old soft"
print(things)

# if values/object in dict are mutable eg- list

animals_list_dict= {
    "lion": ["scary"],
    "elephant":["big"],
    "teddy":["soft"],
}

things_shallow_copy = animals_list_dict.copy()
animals_list_dict["lion"].append("cat like")
print(animals_list_dict["lion"])
print(things_shallow_copy["lion"])

# this will return same as mutable objects i.e. list of characters of lion
# in dictionary are stored as one copy only
