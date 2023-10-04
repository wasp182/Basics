import timeit

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
def spam_comp():
    meals = [meal for meal in menu if "spam" not in meal]
    return meals

def not_spam(meal_list):
    return "spam" not in meal_list

def spamless_filter():
    spamless_meal = list(filter(not_spam,menu))
    return spamless_meal

if __name__ =="__main__":
    # print(spam_comp())
    # print(spamless_filter())
    print(timeit.timeit(spam_comp,number=1000))
    print(timeit.timeit(spamless_filter,number=1000))
