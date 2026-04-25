from tkinter import *
root = Tk()
root.title('Event Handler')
root.geometry('300x300')
def handler_event(event):
    print(event.char)
root.bind("<Key>", handler_event)
def handle_click(event):
    print('This is a message')
btnclickme = Button(root, text = 'Click me!', command = handle_click)
btnclickme.bind("<Button-1>", handle_click )
btnclickme.pack()
root.mainloop()