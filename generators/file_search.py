import os
import fnmatch
# matching files that have some pattern to them

def find_albums(root,artist_name):
    for path, directories , files in os.walk(root):
        for artist in fnmatch.filter(directories,artist_name):
            subdir_artist = os.path.join(path,artist)
            for album_path , albums , _ in os.walk(subdir_artist):
                for album in albums:
                    yield os.path.join(album_path,album) , album


def find_song_list(root,album_name):
    for path, art_dir_list , alb_dir_list in os.walk(root):
        for albums in art_dir_list:
            if albums == album_name:
                print("found album")
                artist_name = os.path.split(path)[-1]
                song_list = os.listdir(os.path.join(path,album_name))
                yield artist_name, album_name, song_list


def create_db(root):
    for path , dir , file in os.walk(root):
        if file:
            album = os.path.split(path)
            artist = os.path.split(album[0])
            song_names =[]
            for songs in file:
                song_names.append(songs.strip(".emp3").split("- ")[1])
            row = [artist[1],album[1],song_names]
            print(row)

def find_songs(albums):
    for album in albums:
        for songs in os.listdir(album[0]):
            yield album[1],songs


album_list = find_albums("music","Aerosmith")

# for gen in album_list:
#     print(gen)

# create_db('music')

# songs_list = find_song_list("music","Permanent Vacation")
#nothing will be printed unless we call below line
# for songs in songs_list:
#     print(songs)

songLists  = find_songs(album_list)
for songs in songLists:
    print(songs)

