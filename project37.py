'''Write a Python program to create a Tkinter window. Use the following
parameters for creating this window and add widgets to it -
1. Window size - width = 400, height=300
2. Set title - Getting Started with Widgets
3. Add a label to describe the functionality of this application in brief
4. Add two labels for asking users to enter numbers in the respective text
box.
5. Add two Entry widgets below the last two mentioned labels to get the
numbers from the user.
6. Add a button that will calculate the product when it is clicked.
7. Add a Text Box to display the result.'''
from tkinter import *
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')
lbl = Label(root, text = 'This application will calculate the \nproduct of two numbers entered by the user.')
num1_label = Label(root, text = 'Enter first number:')
num2_label = Label(root, text = 'Enter second number:')
num1_entry = Entry(root)
num2_entry = Entry(root)
txt = Text(root, width = 20, height = 5)
def cp():
    n1 = num1_entry.get()
    n2 = num2_entry.get()
    product = float(n1) * float(n2)
    txt.insert(END, 'The product of ' + n1 + ' and ' + n2 + ' is: ' + str(product))
btn = Button(root, text = 'Calculate Product!', command = cp, bg = 'red', fg = 'white')
lbl.pack()
num1_label.pack()
num1_entry.pack()
num2_label.pack()
num2_entry.pack()
btn.pack()
txt.pack()
root.mainloop()
