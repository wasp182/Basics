from nested_data import albums
# when python imports anything from a file , it will run the entire code
print(albums)
separators='=='
SONGLIST_INDEX=3
SONGNAME_INDEX=1

while True:
    print('Please select album to play (invalid choice to exit)')
    for index,(name,artist,year,songs) in enumerate(albums):
        print("{0}: {1}".format(index+1,name))
    selected_album=int(input())
    if selected_album in range(1, len(albums) + 1):
        print('please choose song to play (invalid choice to exit) ')
        song_list=albums[selected_album - 1][SONGLIST_INDEX]
        for index,(songs) in enumerate(song_list):
            print('{0}: {1}'.format(index + 1, songs[SONGNAME_INDEX]))
        selected_song=int(input())
        if selected_song in range(1,len(song_list)+1):
            print('Playing song: {}'.format(song_list[selected_song - 1][SONGNAME_INDEX]))
        else:
            print('Invalid choice. Choose Again')
        print(separators*10)
    else:
        print('Invalid choice.Exiting')
        break



