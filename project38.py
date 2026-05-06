'''Write a Python program to create a Tkinter window. Use the following
parameters for creating this window and add widgets to it -
1. Window size - width = 400, height=400
2. Set title - Age Calculator App
3. Try using labels and entry widgets side by side to make the application
look better. You can use different geometry managers of Tkinter.
4. Accepts these four inputs from the user - Name, date, month, and year.
5. Display a personalized message for every user, with their name and
present
ht age.'''
from tkinter import *
from datetime import date
root = Tk()
root.title('Age Calculator App')
root.geometry('400x400')
label = Label(root, text = 'Enter your name:')
entry = Entry(root)
label2 = Label(root, text = 'Enter the day:')
entry2 = Entry(root)
label3 = Label(root, text = 'Enter the month:')
entry3 = Entry(root)
label4 = Label(root, text = 'Enter your year:')
entry4  = Entry(root)


def calculate_age():
    name = entry.get()
    day = int(entry2.get())
    month = int(entry3.get())
    year = int(entry4.get())
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    label.config(print ('Hello', name, '!',  ' Your age is' ,age, 'years.'))
button = Button(root, text = 'Calculate Age', bg = '#d0efff', command = lambda: calculate_age())
button.pack(pady = 20)
label.pack(pady = 10)
entry.pack(pady = 10)
label2.pack(pady = 10)
entry2.pack(pady = 10)
label3.pack(pady = 10)
entry3.pack(pady = 10)
label4.pack(pady = 10)
entry4.pack(pady = 10)
root.mainloop()