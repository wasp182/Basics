menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]
meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append('meal skipped')

print(meals)

# simple comprehension
meal_and = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
print(meal_and)

# conditional comprehension
# here the filtering happens through if else during the iteration
meals2 = [meal if "spam" not in meal else "meal skipped" for meal in menu ]
print(meals2)

# used below format to get to above comprehension
x =12
expression = "twelve" if x ==12 else "not twelve"
print(expression)

# conditionals
for meal in menu:
    print(meal,"contains chicken" if "chicken" in meal else "contains bacon" if "bacon" in meal else "contains eggs" )

print()

# get all possible items in a meal in given menu
items = set()
for meal in menu:
    for item in meal:
        items.add(item)
print(items)

# print first matching item in meal
for meals in menu:
    for item in items:
        if item in meals:
            print("{} contains {}".format(meals,item))
            break

for x in range(1,31):
    fizzbuzz = "fizzbuzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)