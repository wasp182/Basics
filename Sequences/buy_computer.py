computer_part=[]
current_choice = "--"

while current_choice != '0':
    if current_choice in '12345':
        print('adding current choice {}'.format(current_choice))
        if current_choice=='1':
            computer_part.append('a')
        elif current_choice=='2' :
            computer_part.append("b")
        elif current_choice=='3' :
            computer_part.append("c")
        elif current_choice=='4' :
            computer_part.append("d")
        elif current_choice=='5' :
            computer_part.append("e")
    else:
        print('please add options')
        print(' 1: add a')
        print(' 2: add b')
        print(' 3: add c')
        print(' 4: add d')
        print(' 5: add e')
        print(' 0 to exit')
    current_choice = input()

print(computer_part)