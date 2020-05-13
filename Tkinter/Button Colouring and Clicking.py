# Button Colouring and Clicking

from tkinter import *
window = Tk()
window.title("Our First GUI")

lbl = Label(window, text="Hello")
lbl.grid(column = 0, row = 0)

def clicked():
    lbl.configure(text="Button was clicked!")

btn = Button(window, text="Click Me!", bg="orange", fg="red", command=clicked)
btn.grid(column=1,row=0)

window.mainloop()
