#numbers={*" "}
# initialise set literal
# can be written as
# numbers ={*{}}

# numbers = set()
#
# while len(numbers)< 4:
#     next_value = int(input("enter number "))
#     numbers.add(next_value)
#
# print(numbers)

data = ['blue','red','green','red']
unique_data = sorted(set(data))
print(unique_data)

unique_data = list(dict.fromkeys(data))
print(unique_data)
print(dict.fromkeys(data))

