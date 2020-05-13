# Adding a Tab Control Widget

from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Complete Python Course")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="First")

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Second")

tab_control.pack(expand=1, fill="both")

lbl1 = Label(tab1, text="Label 1")
lbl1.grid(column=0,row=0)
lbl2 = Label(tab2, text="Label 2")
lbl2.grid(column=0,row=0)

window.mainloop()
