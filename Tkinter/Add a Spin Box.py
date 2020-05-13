# Add a Spin Box

from tkinter import *
window = Tk()
window.title("Complete Python Course")
window.geometry('400x200')

var = IntVar()
var.set(55)

spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
spin.grid(column=0, row=0)

window.mainloop()
