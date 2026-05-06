'''Write a Python program to create a Tkinter window. Use the following
parameters for creating this window and add widgets to it -
1. Window size - width = 400, height=400
2. Set title - Length Converter App.'''
from tkinter import *
root = Tk()
root.title('Length Converter App')
root.geometry('400x400')
entlenth = Entry(root)
def Convert():
    value = float(entlenth.get())
    if value < 0:
        print('Please enter a valid number')
    print(value * 2.54)
btn = Button(root, text='Convert', command=Convert)
label = Label(root, text='Enter length in inches')
label.pack()
entlenth.pack()
btn.pack()
root.mainloop()
