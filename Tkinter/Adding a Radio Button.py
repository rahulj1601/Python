# Adding a Radio Button

from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Complete Python Course")
window.geometry("400x200")

selected = IntVar()

rad1 = Radiobutton(window, text="First", value=7, variable=selected)
rad2 = Radiobutton(window, text="Second", value=2, variable=selected)
rad3 = Radiobutton(window, text="Third", value=3, variable=selected)
rad1.grid(column=0,row=0)
rad2.grid(column=1,row=0)
rad3.grid(column=2,row=0)

def clicked():
    print(selected.get())

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=0,row=1)

window.mainloop()
