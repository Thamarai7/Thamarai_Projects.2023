import tkinter
from tkinter import *

t = tkinter.Tk()
t.title("Miles to Kilometer Converter")
t.config(padx=20, pady=20)
miles_inp = Entry()
miles_inp.grid(column=1, row=0)
#
miles_lab = Label(text="Miles")
miles_lab.grid(column=2, row=0)
#
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
#
kilometer = Label(text="0")
kilometer.grid(column=1, row=1)

km_lable = Label(text="Km")
km_lable.grid(column=2, row=1)
def miles_to_km():
    mile = float(miles_inp.get())
    km = round(mile * 1.609)
    kilometer.config(text=f"{km} ")
Cal_button = Button(text="Calculate", command=miles_to_km)
Cal_button.grid(column=1,row=2)
t.mainloop()