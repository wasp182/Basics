computer_parts = ['a',
                  'b',
                  'c',
                  'd'
                  ]
another_one = computer_parts
print(id(computer_parts))
print(id(another_one))

computer_parts += ['e']
print(computer_parts)
print(id(computer_parts))
print(id(another_one))

# all addresses wil be same for above ids

a=b=c=d=e=another_one
print("adding f")
b.append("f")
print(c)
print(d)
# multiple names for same list