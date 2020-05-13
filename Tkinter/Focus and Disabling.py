# Focus and Disabling

from tkinter import *
window = Tk()
window.title("Our First GUI")

lbl = Label(window, text="Enter your name: ")
lbl.grid(column = 0, row = 0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus()

def clicked():
    msg = "Welcome " + txt.get()
    lbl.configure(text=msg)

btn = Button(window, text="Done?", bg="orange", fg="red", command=clicked)
btn.grid(column=2,row=0)

window.geometry('400x200')

window.mainloop()
