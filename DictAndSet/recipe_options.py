recipes_tuple = {
    "Chicken and chips": [
        ("chicken", 100),
        ("potatoes", 3),
        ("salt", 1),
        ("malt vinegar", 5),
    ],
}

recipes_dict = {
    "Chicken and chips": {
        "chicken": 100,
        "potatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
    },
}

# my implementation
for recipe,ingredients in recipes_tuple.items():
    print('ingredients for {0} '.format(recipe))
    for ingredient,quantity in ingredients:
        print(f" quantity of {ingredient} is {quantity}")

for recipe,ingredients in recipes_dict.items():
    print(f"ingredients for {recipe}")
    for ingredient , quantity in ingredients.items():
        print(f" quantity of {ingredient} is {quantity}")






# using tuples
for recipe, ingredients in recipes_tuple.items():
    print(f"Ingredients for {recipe}")
    for ingredient, quantity in ingredients:  # ingredients is a tuple
        print(ingredient, quantity, sep=', ')

print()

# using a dictionary
for recipe, ingredients in recipes_dict.items():
    print(f"Ingredients for {recipe}")
    for ingredient, quantity in ingredients.items():  # ingredients is a dict
        print(ingredient, quantity, sep=', ')

