from tkinter import *
from datetime import date
root = Tk()
root.title('Tkinter window')
root.geometry('350x400')
lbl = Label(root, text = 'Hey There!', fg = 'black', bg = 'orange')
name_label = Label(root, text = 'What is your name?')
name_entry = Entry(root)
txt = Text(root, width = 20, height = 15)
def display():
    e1 = name_entry.get()
    grt = 'Hello ' + e1 + ' '
    global Message
    Message = "Welcome to the Application! \nToday's date is: "
    txt.insert(END, grt)
    txt.insert(END, Message)
    txt.insert(END, date.today())
    
btn = Button(root, text = 'Begin', command = display, bg = 'orange', fg = 'black')
lbl.pack()
name_label.pack()
name_entry.pack()
txt.pack()
btn.pack()
root.mainloop()