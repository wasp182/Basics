from nested_data import albums
# when python imports anything from a file , it will run the entire code
print(albums)
separators='=='

while True:
    print('Please select album to play (invalid choice to exit)')
    for index,album in enumerate(albums):
        print("{0}: {1}".format(index+1,album[0]))
    selected=int(input())
    if selected in range(1,len(albums)+1):
        print('please choose song to play (invalid choice to exit) ')
        for index in range(len(albums[selected-1])):
            print('{0}: {1}'.format(index+1,albums[selected-1][3][index][1]))
        selected_song=int(input())
        if selected_song in range(1,len(albums[selected-1][3])+1):
            print('Playing song: {}'.format(albums[selected-1][3][selected_song-1][1]))
            print(separators*10)
            continue
        else:
            print('Invalid choice. Exiting')
            break
    else:
        print('Invalid choice.Exiting')
        break



