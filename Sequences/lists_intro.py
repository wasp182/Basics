computer_parts = ['a',
                  'b',
                  'c',
                  'd'
                  ]
for parts in computer_parts:
    print(parts)
computer_parts[3]='C'
print(computer_parts)

# computer_parts[3:]="new new"
# print(computer_parts)

computer_parts[2:] = ["new new"]
print(computer_parts)