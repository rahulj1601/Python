from tkinter import *

window = Tk()

def conversion():
    grams = float(e1_value.get()) * 1000
    ounces = float(e1_value.get()) * 35.274
    pounds = float(e1_value.get()) * 2.20462
    t1.delete("1.0",END) #delete from index 1 onwards (starts from index 1 in tkinter)
    t1.insert(END,grams)
    t2.delete("1.0",END)
    t2.insert(END,ounces)
    t3.delete("1.0",END)
    t3.insert(END,pounds)

e0=Label(window,text="Kg")
e0.grid(row=0,column=0)

e1_value=StringVar() #declare string variable
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

b1 = Button(window,text="Convert",command=conversion)
b1.grid(row=0,column=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=1,column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1,column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1,column=2)

window.mainloop()

