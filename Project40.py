'''Write a Python program to create a Tkinter window. Use the following
parameters for creating this window and add widgets to it -
1. Window size - width = 400, height=400
2. Set title - Interest Calculator App
3. Try using labels and entry widgets side by side to make the application
look better. Also, you can use different geometry managers of Tkinter.
4. Accepts these three inputs from the user - principle, time(in years), rate of
interest(%).
5. Display the value of simple interest and compound interest.'''
from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Interest Calculator App")
def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())

        simple_interest = (principal * time * rate) / 100
        compound_interest = principal * (1 + rate / 100) ** time - principal

        simple_interest_label.config(text=f"Simple Interest: {simple_interest:.2f}")
        compound_interest_label.config(text=f"Compound Interest: {compound_interest:.2f}")
    except ValueError:
        simple_interest_label.config(text="Invalid input. Please enter numeric values.")
        compound_interest_label.config(text="")
principal_label = Label(root, text="Principal:")
principal_label.grid(row=0, column=0, padx=10, pady=10)
principal_entry = Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=10)
time_label = Label(root, text="Time (years):")
time_label.grid(row=1, column=0, padx=10, pady=10)
time_entry = Entry(root)
time_entry.grid(row=1, column=1, padx=10, pady=10)
rate_label = Label(root, text="Rate of Interest (%):")
rate_label.grid(row=2, column=0, padx=10, pady=10)
rate_entry = Entry(root)
rate_entry.grid(row=2, column=1, padx=10, pady=10)
calculate_button = Button(root, text="Calculate", command=calculate_interest)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)
simple_interest_label = Label(root, text="")
simple_interest_label.grid(row=4, column=0, columnspan=2, pady=10)
compound_interest_label = Label(root, text="")
compound_interest_label.grid(row=5, column=0, columnspan=2, pady=10)
root.mainloop()
