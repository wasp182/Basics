import copy

lion_list=["scary",'cat like']
elephant_list=["big",'memory']
teddy_list=["soft"]

animals_list_dict= {
    "lion": lion_list,
    "elephant":elephant_list,
    "teddy":teddy_list,
}

animals={
    "lion": ["scary"],
    "elephant":["big"],
    "teddy":["soft"],
}
things_copy = animals_list_dict.copy()

print()
teddy_list.append("gift")
print(animals_list_dict["teddy"])
print(things_copy["teddy"])
print(teddy_list)

print()
things_copy["teddy"]=["reset"]
#immutable object added instead of list object hence only things will change
print(animals_list_dict["teddy"])
print(things_copy["teddy"])
print(teddy_list)

print()
animals_list_dict["teddy"].append("another one")
print(animals_list_dict["teddy"])
print(things_copy["teddy"])
print(teddy_list)

#deep copy - makes two separate copies
thing_deepcopy = copy.deepcopy(animals_list_dict)
animals_list_dict["teddy"].append("deep copy test")
print()
print(animals_list_dict["teddy"])
print(thing_deepcopy["teddy"])
print(teddy_list)

thing_deepcopy=copy.deepcopy(animals)
animals["teddy"].append("deep copy test 2")
print()
print(animals["teddy"])
print(thing_deepcopy["teddy"])
print(teddy_list)
