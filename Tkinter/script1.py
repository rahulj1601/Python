from tkinter import * #can use button() instead of tkinter.button()

window = Tk()

def km_to_miles():
    miles = float(e1_value.get()) * 1.6
    t1.insert(END,miles)

b1 = Button(window,text="Execute",command=km_to_miles)
# b1.pack() --> just sticks the button on the screen
b1.grid(row=0,column=0)
#more control over the placement of the button with .grid()

e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value) #where you can enter a value
e1.grid(row=0,column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0,column=2)

window.mainloop()

