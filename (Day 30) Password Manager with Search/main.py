from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
import tkinter.ttk as tkstyle


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    new_password = "".join([password for password in password_list])
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)

def write_json(data_to_add):
    with open("data.json", "w") as data_file:
        json.dump(data_to_add, data_file, indent=4)

def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if len(password) == 0 or len(email) == 0 or len(website) == 0:
        messagebox.showinfo(title="Empty", message="Please Don't leave any fields empty!")

    elif "@gmail.com" not in email:
        messagebox.showinfo(title="Email not Valid", message="Not a valid Email.\nPlease double check your email.")

    else:
        ok_info = messagebox.askokcancel(title="Confirmation", message=f"These are the details entered: \nWebsite: "
                                                                       f"{website}\nEmail: {email}\nPassword: "
                                                                       f"{password}\nDo you confirm the save?")
        if ok_info:
            try:
                with open(file="data.json", mode="r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                write_json(new_data)
            except json.decoder.JSONDecodeError:
                write_json(new_data)
            else:
                write_json(data)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo(title="Saved", message="Data Saved!")
            website_entry.focus()

def get_data():
    website = website_entry.get()
    try:
        with open(file="data.json", mode="r") as data_file:
            data = json.load(data_file)[website]
            email = data['email']
            password = data['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}\n(Password Copied)")
            pyperclip.copy(data["password"])
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data!")
    except KeyError:
        messagebox.showerror(title="Error", message=f"No website record with the name: '{website}'")


window = Tk()
window.config(padx=40, pady=30, bg="#FBFBFB")
window.title("Password Manager 2.0")

logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="#FBFBFB", highlightthickness=0)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="#FBFBFB")
website_label.grid(column=0, row=1, padx=15)
email_label = Label(text="Email/Username:", bg="#FBFBFB")
email_label.grid(column=0, row=2, padx=15)
password_label = Label(text="Password:", padx=15, bg="#FBFBFB")
password_label.grid(column=0, row=3)

website_entry = Entry(width=37, highlightthickness=1, highlightbackground="#DCDCDC", highlightcolor="#DCDCDC", bd=0,
                      bg="#FBFBFB")
website_entry.place(x=144, y=200)
website_entry.focus()
email_entry = Entry(width=56, highlightthickness=1, highlightbackground="#DCDCDC", highlightcolor="#DCDCDC", bd=0,
                    bg="#FBFBFB")
email_entry.insert(END, "vennamenanianshu@gmail.com")
email_entry.place(x=144, y=224)
password_entry = Entry(width=37, highlightthickness=1, highlightbackground="#DCDCDC", highlightcolor="#DCDCDC", bd=0,
                       bg="#FBFBFB")
password_entry.place(x=144, y=248)

generate_button = tkstyle.Button(text="Generate Password", command=generate_password)
generate_button.place(x=374, y=247)
generate_button = tkstyle.Button(text="Search", command=get_data, width=17)
generate_button.place(x=374, y=197)
add_button = tkstyle.Button(text="Add", width=56, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, pady=12, padx=15)

window.mainloop()
