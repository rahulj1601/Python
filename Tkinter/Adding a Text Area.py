# Adding a Text Area

from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("Complete Python Course")
window.geometry('400x200')

txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.grid(column=0, row=0)
txt.insert(INSERT, "Your text goes here")

def clicked():
    txt.delete(1.0,END)

btn = Button(window, text="Clear Text", command=clicked)
btn.grid(column=0, row=1)

window.mainloop()
