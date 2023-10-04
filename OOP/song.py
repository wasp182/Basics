class Song:
    '''
    Attribute
    name(str): name of song
    artist (str): artist object respresenting the artist
    duration(int): The duration of song in seconds
    '''
    def __init__(self,name,artist,duration=0 ):
        self.name=name
        self.artist=artist
        self.duration=duration


# print(Song.__doc__)

# #alternate way to create docstring
# Song.__init__.__doc__ = '''
#                         args:
#                         title
#                         artist
#                         duration
# '''
# help(Song)
class Album:
    """
    Attributes:
        album_name (str)
        year(Int)
        artist (Str)
        tracks (List[Songs])

    Methods:
        addSong: Add new song to artist album
    """

    def __init__(self,name,year,artist):
        self.name= name
        self.year= year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist= artist

        self.track = []

    def addSong(self,song,position=0):
        """
        Adds song to track list
        :param song:
        :param position: position where the track is to be added to track list
        :return:None
        """
        if position is None:
            self.track.append(song)
        else:
            self.track.insert(position,song)
        # using insert method


class Artist:
    # storing circular references
    """
    Storing artist details.
    Attributes:
        name(str)
        albums (List[albums]): list of albums
    Methods:
        addAlbum: add albums to list of albums

    """
    def __init__(self,name):
        self.name = name
        self.albums=[]

    def addAlbum(self,album):
        """
        Add album object to albums list if not present in album list
        :param album: Album object
        :return:
        """
        self.albums.append(album)

def find_object(field, object_list):
    for items in object_list:
        if items==field:
            return items
    return None

def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open('albums.txt') as albums:
        index=0
        for lines in albums:
            artist_field, album_field , year_field ,song_field = tuple(lines.strip("\n").split('\t'))
            year_field = int(year_field)
            # print(artist_field, album_field , year_field ,song_field)

            if new_artist is None:
                # first artist
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
                print("first artist only")
            elif new_artist.name != artist_field:
                print("new artist encountered and object created")
                # retreive artist details and check if to add them to list
                new_artist = find_object(artist_field,artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field,year_field,new_artist)
                # adding albums to existing artist
                new_artist.addAlbum(new_album)
                print("creating and adding new album")
            elif new_album.name != album_field:
                # new album from the artist , check if already there
                new_album = find_object(album_field,new_artist.albums)
                # create a new album for the artist if not present
                if new_album is None:
                    new_album = Album(album_field,year_field,new_artist)
                    new_artist.addAlbum(new_album)
                print("old artist and new album")
                # now we have new album to create as above
        # here we have new_artist and new_album updated , now we add the song to it
            song = Song(song_field,new_artist)
            new_album.addSong(song)
    return artist_list

def check_file(artist_list):
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.track:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.name}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == "__main__":
    artists = load_data()
    print(f"no of artist {len(artists)}")
    #check files
    check_file(artists)
