available_parts = ['a','b','c','d','e']
computer_part=[]
current_choice = "--"
valid_choice= [str(i) for i in range(0, len(available_parts)+1)]
print(valid_choice)
while current_choice != '0':
    if current_choice in valid_choice:
        index = int(current_choice)-1
        chosen_part=available_parts[index]
        if chosen_part in computer_part:
            print('removing current choice {}'.format(current_choice))
            computer_part.remove(chosen_part)
        else:
            print('adding current choice {}'.format(current_choice))
            computer_part.append(chosen_part)
        print(computer_part)
    else:
        print('please add options')
        for no,parts in enumerate(available_parts):
            print('{0} :{1}'.format(no +1,parts))
    current_choice = input()

print(computer_part)