# working with computer file system
import os

root = "music"
path_list = {}
for path , directories , files in os.walk(root,topdown=True):
    input("hi")
    print(path)
    print(directories)
    print(files)
    # for f in files:
    #     print("\t{}".format(f))
    # if directories:
    #     print('reached directory')
    #     print(directories)
    if files:
        print(path)
        # get directories i.e. album names
        first_split = os.path.split(path)
        print(first_split)
        # path_list['artist'] = first_split[1]

        # first split return tuple with last file split in lase column of tuple
        second_split = os.path.split(first_split[0])
        print(second_split)
        # path_list['albums'] = second_split[1]
        # path_list.append(second_split[1])
        for f in files:
            # print(f)
            songs_details = f.strip(".emp3").split("- ")
            print(songs_details)


print(path_list)


