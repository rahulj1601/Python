# Creating a Message Box

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Complete Python Course")
window.geometry('400x200')

def clicked():
    result = messagebox.askretrycancel("Message Title", "Message Content")
    print(result)

btn = Button(window, text="Click here", command=clicked)
btn.grid(column=0, row=0)

window.mainloop()
