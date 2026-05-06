'''Write a Python program to create a Tkinter window. Use the following
parameters for creating this window and add widgets to it -
1. Window size - width = 400, height=400
2. Set title - Password Strength Checker
3. If the password length is less than or equal to 5, the strength will be Weak.
If the password length is between 6 to 8, strength will be Medium. If the
length is greater than 8, then strength is Strong. If the length is greater
than 12, strength will be Very Strong. Display all these strengths in the
following colors respectively - (Red, Yellow, Light Green, Dark Green)'''
from tkinter import *  
root = Tk()
root.geometry("400x400")
root.title("Password Strength Checker")
entry = Entry(root)
strength_label = Label(root, text="Enter a password", fg="black")
strength_label.pack(pady=10)
def check_strength():
    password = entry.get()
    length = len(password)
    if length <= 5:
        strength_label.config(text="Weak", fg="red")
    elif 6 <= length <= 8:
        strength_label.config(text="Medium", fg="yellow")
    elif 9 <= length <= 12:
        strength_label.config(text="Strong", fg="light green")
    else:
        strength_label.config(text="Very Strong", fg="dark green")
entry.pack(pady=10)
check_button = Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=5)
root.mainloop()