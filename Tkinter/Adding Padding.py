# Adding Padding

from tkinter import *

window = Tk()
window.title("Complete Python Course")
window.geometry('400x200')

lbl1 = Label(window, text="label1", padx=20, pady=20)
lbl1.grid(column=0,row=0)

lbl2 = Label(window, text="label2", padx=20, pady=20)
lbl2.grid(column=1,row=0)

window.mainloop()
