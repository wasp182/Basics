import os
import tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Screen Demo")
mainWindow.geometry("640x480")
mainWindow['padx']=15
label = tkinter.Label(mainWindow, text="Grid Demo")
label.grid(row=0, column=0, columnspan=3)

#scroll bar minimal weight
mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)
#

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')

for zone in os.listdir('C:/Windows/System32'):
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsew', rowspan=2)
# linking list scroll and lsit
fileList['yscrollcommand'] = listScroll.set

# options frame
option_frame = tkinter.LabelFrame(mainWindow, text="File details")
option_frame.grid(row=1, column=2, sticky='ne')

rbVal = tkinter.IntVar()
#sets default value to 3 for rbValue
rbVal.set(3)

radio1 = tkinter.Radiobutton(option_frame, text="Filename", value=1, variable=rbVal)
radio2 = tkinter.Radiobutton(option_frame, text="Path", value=2, variable=rbVal)
radio3 = tkinter.Radiobutton(option_frame, text="Timestamp", value=3, variable=rbVal)
radio1.grid(row=0,column=0,sticky='w')
radio2.grid(row=1,column=0,sticky='w')
radio3.grid(row=2,column=0,sticky='w')

# widget to display result
resultLabel = tkinter.Label(mainWindow,text="Result")
resultLabel.grid(row=2,column=2,sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2,column=2,sticky='sw')

#Frame for spoinner
timeFrame = tkinter.LabelFrame(mainWindow,text="Time")
timeFrame.grid(row=3,column=0,sticky='new')
#Time frames
hourSpinner = tkinter.Spinbox(timeFrame,width=2,values=tuple(range(0,24)))
minuteSpinner = tkinter.Spinbox(timeFrame,width=2,from_=0,to=59)
secondsSpinner = tkinter.Spinbox(timeFrame,width=2,from_=0,to=59)
hourSpinner.grid(row=0,column=0)
tkinter.Label(timeFrame,text=":").grid(row=0,column=1)
minuteSpinner.grid(row=0,column=2)
tkinter.Label(timeFrame,text=":").grid(row=0,column=3)
secondsSpinner.grid(row=0,column=4)
timeFrame['padx']=36

#dateframe
dateFrame= tkinter.LabelFrame(mainWindow,text="Dates")
dateFrame.grid(row=4,column=0,sticky='new')
#Date labels
dateLabel = tkinter.Label(dateFrame,text="Day")
monthLabel = tkinter.Label(dateFrame,text="Month")
yearLabel = tkinter.Label(dateFrame,text="year")
dateLabel.grid(row=0,column=0,sticky='w')
monthLabel.grid(row=0,column=1,sticky='w')
yearLabel.grid(row=0,column=2,sticky="w")
#Date Spinner
daySpinner = tkinter.Spinbox(dateFrame,width=5,values=tuple(range(1,32)))
monthSpinner = tkinter.Spinbox(dateFrame,width=5,values=("Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"))
yearSpinner = tkinter.Spinbox(dateFrame,width=5,values=tuple(range(1900,2100)))
daySpinner.grid(row=1,column=0)
monthSpinner.grid(row=1,column=1)
yearSpinner.grid(row=1,column=2)
dateFrame['padx']=36

#Ok button
button1 = tkinter.Button(mainWindow,text="OK")
button2 = tkinter.Button(mainWindow,text="Cancel",command=mainWindow.destroy)
# paranthessis is missing from destroy because there is no active call to button2 , it should only be called once pressed
button1.grid(row=4,column=3,sticky='e')
button2.grid(row=4,column=4,sticky='w')

mainWindow.mainloop()
