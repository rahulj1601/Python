# Adding a Button

from tkinter import *
window = Tk()
window.title("Our First GUI")

lbl = Label(window, text="Hello")
lbl.grid(column = 0, row = 0)

btn = Button(window, text="Click Me!")
btn.grid(column=1,row=0)

window.mainloop()
