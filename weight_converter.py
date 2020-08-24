from tkinter import *

window = Tk()


def kg_to_g():
    print(e1_value.get())
    grams = float(e1_value.get())*1000
    t1.insert(END, grams)

def kg_to_p():
    print(e1_value.get())
    pounds = float(e1_value.get())*2.20462
    t2.insert(END, pounds)


def kg_to_o():
    print(e1_value.get())
    ounces = float(e1_value.get())*35.274
    t3.insert(END, ounces)


e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

b1 = Button(window, text="Grams", command=kg_to_g)
b1.grid(row=1, column=0)

t1 = Text(window, height=1, width=20)
t1.grid(row=2, column=0)

b2 = Button(window, text="Pounds", command=kg_to_p)
b2.grid(row=1, column=1)

t2 = Text(window, height=1, width=20)
t2.grid(row=2, column=1)

b3 = Button(window, text="Ounces", command=kg_to_o)
b3.grid(row=1, column=2)

t3 = Text(window, height=1, width=20)
t3.grid(row=2, column=2)

window.mainloop()
