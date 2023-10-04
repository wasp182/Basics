import timeit

menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ]

menu2 = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ]
menu3=menu2.copy()

# #Approach 1 : remove spam from list
for meal in menu:
    if "spam" not in meal:
        print(meal)
    else:
        top_index=len(meal)-1
        for index,item in enumerate(reversed(meal)):
            if item =="spam":
                del meal[top_index-index]
        print(meal)

my_code='''
for meal in menu:
    if "spam" not in meal:
        print(meal)
    else:
        top_index=len(meal)-1
        for index,item in enumerate(reversed(meal)):
            if item =="spam":
                del meal[top_index-index]
        print(meal)

'''

t1 = timeit.timeit(my_code,globals={'menu':menu},number=1)
print("approach 1 timing : {} ".format(t1))

#Approach 2: using temp list to print non spam meal
for meal in menu2:
    if "spam" not in meal:
        print(meal)
    else:
        temp_list=[]
        for item in meal:
            if item!="spam":
               temp_list.append(item)
        print(temp_list)

mycode2='''
for meal in menu2:
    if "spam" not in meal:
        print(meal)
    else:
        temp_list=[]
        for item in meal:
            if item!="spam":
               temp_list.append(item)
        print(temp_list)
'''

t2=timeit.timeit(mycode2,globals={'menu2':menu2},number=1)
print("approach 2 timing : {} ".format(t2))

#Approach 3: print items comma separated in single line
for meal in menu3:
    items=",".join((item for item in meal if item != "spam"))
    print(items.split(sep=','))

mycode3='''
for meal in menu3:
    items=",".join((item for item in meal if item != "spam"))
    print(items.split(sep=','))
'''
t3=timeit.timeit(mycode3,globals={'menu3':menu3},number=1)
print("approach 3 timing : {} ".format(t3))
