import csv

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

header = ['album','artist','year']
filename="albums.txt"
with open(filename,'w',encoding='utf-8',newline="") as opstream:
    writer_obj = csv.DictWriter(opstream,fieldnames=header)
    writer_obj.writeheader()
    for item in albums:
        pairs = zip(header,item)
        # for thing in pairs:
        #     print(f' {thing}')
        album_dict = dict(pairs)
        writer_obj.writerow(album_dict)


