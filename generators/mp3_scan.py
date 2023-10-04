import os
import fnmatch
import id3reader_p3 as id3reader


def find_music(root,extension):
    for path , dir , files in os.walk(root):
        for file in fnmatch.filter(files,"*.{}".format(extension)):
            # below will  print the absolute path
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path,file)

list_errors=[]
for f in find_music(r"C:\Users\swapn\Pictures\data0\Aayush\Coldplay1","mp3"):
    try:
        id3r = id3reader.Reader(f)
        print("{} : {} : {} {}".format(id3r.get_value('performer'),
                                       id3r.get_value('album'),
                                       id3r.get_value('track'),
                                       id3r.get_value('title')
                                       ))
    except :
        list_errors.append(f)

for error in list_errors:
    print(error)


