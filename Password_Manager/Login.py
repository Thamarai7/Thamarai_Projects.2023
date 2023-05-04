from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ........................Password Generator................
def _password_():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# print(f"Your password is: {password}")


# ...........................Add Password....................
def save():
    web = website_entry.get()
    mail = mail_entry.get()
    password = pass_entry.get()
    user_id = {web: {
        "mail": mail, "pass": password
    }}
    if len(web) == 0 or len(mail) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="You have missed some fields empty!!")
    else:

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(user_id, data_file, indent=4)
        else:
            data.update(user_id)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            mail_entry.delete(0, END)
            pass_entry.delete(0, END)


# ..........................Show User Data........................
def _showdata_():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No files found")
    else:
        if website in data:
                mail = data[website]["mail"]
                password = data[website]["pass"]
                messagebox.showinfo(title="Info", message=f"mail:{mail}\npass:{password}\n")
        else:
                messagebox.showwarning(title="No data", messagebox=f"No details for {website} exist's")




# ..........................UI Setup........................

t = Tk()
t.title("Password Generator")
t.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)
email_label = Label(text="Email")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1)
mail_entry = Entry(width=35)
mail_entry.grid(column=1, row=2)
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

# Buttons
generate_pass = Button(text="Generate Password", command=_password_)
generate_pass.grid(column=2, row=3)
Add_button = Button(text="Add", width=30, command=save)
Add_button.grid(column=1, row=4)

search = Button(text="Search", width=7, command=_showdata_)
search.grid(column=2, row=1)

t.mainloop()
