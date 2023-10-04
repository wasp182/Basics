import tkinter
import sqlite3

conn = sqlite3.connect("music.db")

class ScrollBox(tkinter.Listbox):
    def __init__(self,window,**kwargs):
        super().__init__(window,**kwargs)
        # define its scroll bar i.e. add a scrollbar
        self.scrollbar = tkinter.Scrollbar(window,orient=tkinter.VERTICAL,command=self.yview)
        # self.listBox = tkinter.Listbox()

    def grid(self,row,column,sticky='nsew',rowspan=1,columnspan=1,**kwargs):
        super().grid(row=row,column=column,sticky=sticky,rowspan=rowspan,columnspan=columnspan,**kwargs)
        self.scrollbar.grid(row=row,column=column,sticky='nse',rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set

class DataListBox(ScrollBox):
    def __init__(self,window,connection, table,field,sort_order=(),**kwargs):
        super(DataListBox, self).__init__(window,**kwargs)
        self.cursor = connection.cursor()
        self.field = field
        self.table = table
        self.linked_box = None
        self.linked_field = None
        self.bind('<<ListboxSelect>>',self.on_select)
# TODO
        self.sql_query = "select "+self.field+", _id from "+self.table
        if sort_order:
            self.sql_sort = " order by "+','.join(sort_order)
        else:
            self.sql_sort = " order by " + self.field
        print(self.sql_query+self.sql_sort)

    def linked(self,widget,linked_field):
        self.linked_box = widget
        widget.linked_field = linked_field

    def clear(self):
        self.delete(0,tkinter.END)

    def requery(self, link_value = None):
        # print(self.sql_query)
        if link_value and self.linked_field:
            sql = self.sql_query + " where " + self.linked_field + "  = ? "+ self.sql_sort
            print(sql)
            self.cursor.execute(sql,(link_value,))
        else:
            print(self.sql_query+ self.sql_sort)
            self.cursor.execute(self.sql_query+ self.sql_sort)
        self.clear()
        for values in self.cursor:
            self.insert(tkinter.END,values[0])
        if self.linked_box:
            self.clear()

    def on_select(self,event):
            if self.linked_box:
                # print(self is event.widget)
                ids = self.curselection()[0]
                values = self.get(ids),
                print(values)
                # artist id
                get_albums =[]
                # only id is needed hence we take fetchone][1]
                link_id = conn.execute(self.sql_query + " where "+ self.field +" = ? ",values).fetchone()[1]
                # print(link_id)
                self.requery(link_id)


# def get_songs(event2):
#     ids = event2.widget.curselection()[0]
#     album_name = event2.widget.get(ids)
#     print(album_name)
#     get_songs=[]
#     album_id = conn.execute("select albums._id from albums where albums.name = ?",(album_name,)).fetchone()
#     for rows in conn.execute("select songs.title from songs where songs.album = ?",album_id):
#         get_songs.append(rows[0])
#     songLV.set(tuple(get_songs))
#     songLV.set("Select album")
#     print(get_songs)
#


mainWindow = tkinter.Tk()
mainWindow.title("Title")
mainWindow.geometry("1024x768")

mainWindow.columnconfigure(0,weight=2)
mainWindow.columnconfigure(1,weight=2)
mainWindow.columnconfigure(2,weight=2)
mainWindow.columnconfigure(2,weight=1)

mainWindow.rowconfigure(0,weight=1)
mainWindow.rowconfigure(1,weight=5)
mainWindow.rowconfigure(2,weight=5)
mainWindow.rowconfigure(3,weight=1)


# ======labels========

tkinter.Label(mainWindow,text="Artists").grid(row=0,column=0)
tkinter.Label(mainWindow,text="Albums").grid(row=0,column=1)
tkinter.Label(mainWindow,text="Songs").grid(row=0,column=2)

#===artist listboxes====
artList = DataListBox(mainWindow,conn,"artists","name")
artList.grid(row=1,column=0,rowspan=2,sticky='nsew',padx=(30,0))
artList.config(border=2,relief='sunken')

# for rows in  conn.execute("select artists.name from artists order by artists.name"):
#     # rows is returned as a tuple
#     artList.insert(tkinter.END,rows[0])
artList.requery()


#===albumslist====
albumLV = tkinter.Variable(mainWindow)
albumLV.set("Select artist")
albumList = DataListBox(mainWindow,conn,"albums","name",sort_order=("name",))
#listvariable=albumLV
albumList.grid(row=1,column=1,sticky='nsew',padx=(30,0))
albumList.config(border=2,relief='sunken')
# for rows in  conn.execute("select albums.name from albums order by albums.name"):
#     # rows is returned as a tuple
#     albumList.insert(tkinter.END,rows[0])

artList.linked(albumList,"artist")


#=====songslist======
songLV = tkinter.Variable(mainWindow)
songLV.set("select album")

# this code will make the scroll box for us and align the scrollbar next to out box
songList = DataListBox(mainWindow,conn,"songs","title",sort_order=("track","title"))
# songList.requery()
albumList.linked(songList,"album")

#listvariable=songLV

songList.grid(row=1,column=2,sticky='nsew')
songList.config(border=2,relief='sunken')


# for rows in  conn.execute("select songs.title from songs order by songs.title"):
#     # rows is returned as a tuple
#     songList.insert(tkinter.END,rows[0])


#=======MainLoop=======
# test = range(1,100)
# albumLV.set(tuple(test))
mainWindow.mainloop()
print('closing connection')
conn.close()