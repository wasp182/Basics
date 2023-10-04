class Song:
    '''
    Attribute
    name(str): name of song
    artist (str): artist object respresenting the artist
    duration(int): The duration of song in seconds
    '''
    def __init__(self,name,artist : str,duration=0 ):
        self.name=name
        self.duration=duration
        self.artist = artist


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

    def __init__(self,name,year,artist: str):
        self.name= name
        self.year= year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist= artist
        self.tracks = []

    def add_song(self,song: str,position=0):
        check_track = find_object(song,self.tracks)
        if check_track is None:
            check_track = Song(song,self.artist)
            if position is None:
                self.tracks.append(check_track)
            else:
                self.tracks.insert(position,check_track)

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
        self.albums = []

    def addAlbum(self,album):
        """
        Add album object to albums list if not present in album list
        :param album: Album object
        :return:
        """
        self.albums.append(album)

    def add_song(self,album,year,song):
        '''
        Add songs to collection of albums , create new album if not already there
        :param album: album name for given artist
        :param year:
        :param song:
        :return:
        '''
        check_album = find_object(album,self.albums)
        if check_album is None:
            check_album = Album(album,year,self.name)
            self.addAlbum(check_album)
        check_album.add_song(song)


def find_object(field, object_list):
    for items in object_list:
        if items.name == field:
            return items
    return None

def load_data():
    artist_list = []
    with open('albums.txt') as albums:
        index=0
        for lines in albums:
            artist_field, album_field , year_field ,song_field = tuple(lines.strip("\n").split('\t'))
            year_field = int(year_field)
            # print(artist_field, album_field , year_field ,song_field)

            # initialise new_artist by checking if already present or not
            new_artist = find_object(artist_field,artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            # add new song to artist's album
            new_artist.add_song(album_field,year_field,song_field)
    return artist_list

def check_file(artist_list):
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.name}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == "__main__":
    artists = load_data()
    print(f"no of artist {len(artists)}")
    #check files
    check_file(artists)
