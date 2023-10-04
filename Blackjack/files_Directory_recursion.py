import os

def list_directories(s):
    def dir_list(d):
        nonlocal tab_stop
        files=os.listdir(d)
        for f in files:
            current_path = os.path.join(d,f)
            if os.path.isdir(current_path):
                print("\t"*tab_stop + "Directory : " + f)
                tab_stop+=1
                dir_list(current_path)
                tab_stop-=1
            else:
                print("\t"*tab_stop + f)

    tab_stop=0
    if (os.path.exists(s)):
        print("directories of "+s)
        dir_list(s)
    else: print('Directory does not exist')



list_directories('.')

# listing = os.walk('.')
# for root , directory, files in listing:
#     print(root)
#     for dir in directory:
#         print(dir)
#     for file in files:
#         print(file)

