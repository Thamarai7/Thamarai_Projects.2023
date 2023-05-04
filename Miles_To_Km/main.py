import tkinter
from tkinter import *

t = tkinter.Tk()
t.title("Hello")
t.minsize(width=500, height=400)
t.config(padx=100, pady=200)
my_label = tkinter.Label(text="New Text", font=("Arial", 24, "normal"))
# my_label.pack(side="top")
# my_label["text"] = "Hello
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50,pady=100)
# my_label.pack(side="bottom")
# # we can directly change any of the arguement from lable
# my_label.config(text="Bro")
def button():
    print("its clicked ")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="click me", command= button)
button.grid(column=1, row=1)
n_button = Button(text="Hello")
n_button.grid(column=2,row=2)
input = Entry(width=10)
# input.pack()
input.grid(column=2, row=1)
# input.get()





t.mainloop()