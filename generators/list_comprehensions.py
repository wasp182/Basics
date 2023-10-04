print(__file__)

nos = [1,2,3,4,5]
no = int(input("enter a no (for loop)"))
# no is same name as loop control variable that leads to mixing up in for loop
squares = []
for no in nos:
    squares.append(no**2)

index_pos = nos.index(no)
print(squares[index_pos])

print(squares)


# comprehensions
number = int(input("enter a no (for loop)"))
# despite the same name as loop control variable , list comprehension returns the correct value
# python 2 does leak the value of variable with same name as control var in loop
# in outer scope
squarecom = [number **2 for number in nos]
# here the
index_pos = nos.index(no)
print(squarecom[index_pos])

text = "what is going on"
upper_text = [chars.upper() for chars in text]
split_text = [chars.upper() for chars in text.split(" ")]
print(upper_text)
print(split_text)