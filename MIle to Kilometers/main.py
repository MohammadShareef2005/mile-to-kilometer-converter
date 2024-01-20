from tkinter import *


def to_km():
    mil = int(input.get())
    km = mil * 1.609
    km_l.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=100, width=300)
window.config(padx=20, pady=20)

input = Entry(width=10)
mil = input.get()
input.grid(column=1, row=0)

lable2 = Label(text="Mile")
lable2.grid(column=2, row=0)

lable1 = Label(text="is equal to")
lable1.grid(column=0, row=1)

lable3 = Label(text="Km")
lable3.grid(column=2, row=1)

km_l = Label(text="0")
km_l.grid(column=1, row=1)

button = Button(text='Calculate', command=to_km)
button.grid(column=1, row=3)
window.mainloop()
