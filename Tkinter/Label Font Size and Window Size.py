# Label Font Size and Window Size

from tkinter import *
window = Tk()
window.title("Our First GUI")

lbl = Label(window, text="Hello", font = ("Arial Bold", 50))
lbl.grid(column = 0, row = 0)

window.geometry('350x200')

window.mainloop()
