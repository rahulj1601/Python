# Creating a Label

from tkinter import *
window = Tk()
window.title("Our First GUI")

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

window.mainloop()
