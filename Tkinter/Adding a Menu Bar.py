# Adding a Menu Bar

from tkinter import *
from tkinter import Menu

window = Tk()
window.title("Complete Python Course")

def clicked():
    print("clicked")

menu = Menu(window)

newItem = Menu(menu)
newItem.add_command(label="New", command=clicked)

newItem.add_separator()
newItem.add_command(label="Edit", command=clicked)

menu.add_cascade(label="File", menu=newItem)
window.config(menu=menu)

window.mainloop()
