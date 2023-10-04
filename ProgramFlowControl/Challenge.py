options = ['terminate','learn a','learn b','learn c','learn d']

print('choose bw below options \n')
for index,ops in enumerate(options):
    print(' {}. {}'.format(index,ops))

while True:
    choice=(input('enter choice number or press 0 to exit'))
    if choice==0:
        break
    elif choice in "12345":
        print('you chose {}'.format(choice))
    else:
        print('choose bw below options \n')
        for index,ops in enumerate(options):
            print('{}. {}'.format(index,ops))

