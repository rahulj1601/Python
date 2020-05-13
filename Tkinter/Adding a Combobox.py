# Adding a Combobox

from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Complete Python Course")
window.geometry('500x200')

lbl1 = Label(window, text="Choose a number: ")
lbl1.grid(column=0, row=0)

combo = Combobox(window)
combo['values'] = (1,2,3,4,5)
combo.current(1)
combo.grid(column=1, row=0)

def clicked():
    opt = "You Chose: " + combo.get()
    lbl2 = Label(window, text=opt)
    lbl2.grid(column=0,row=1)

btn = Button(window, text="Done?", command=clicked)
btn.grid(column=2,row=0)

window.mainloop()

