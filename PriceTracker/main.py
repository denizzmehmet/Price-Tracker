from tkinter import *
from app import check_price
root = Tk()
root.title("Price Tracker")
root.geometry("500x250")

status = False
timeloop = 1000
def scanning():
    if status:
        print("Checking price...")
        url = urlEntry.get()
        target = float(targetEntry.get())
        check = check_price(url,target)
        if check:
            stopApp()
        root.after(timeloop,scanning())
def startApp():
    global status
    status = True
    exeButton.config(text="STOP",command=stopApp)
    scanning()
def stopApp():
    global status
    status = False
    exeButton.config(text="START",command=startApp)

global urlLabel
urlLabel = Label(root,text="TARGET URL")
urlLabel.pack(pady=10)

global urlEntry
urlEntry = Entry(root,width=40)
urlEntry.pack()

global targetLabel
targetLabel = Label(root,text="TARGET PRİCE")
targetLabel.pack(pady=10)

global targetEntry
targetEntry = Entry(root,width=40)
targetEntry.pack()

global exeButton
exeButton = Button(root,text="START",command=startApp,width=20,height=2)
exeButton.pack(pady=10)

root.mainloop()
