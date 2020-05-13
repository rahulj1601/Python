# Adding a Checkbutton

from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Complete Python Course")
window.geometry("1000x500")

checkState = IntVar()
checkState.set(1)

check = Checkbutton(window, text="Choose", var=checkState)
check.grid(column=0, row=0)

window.mainloop()
