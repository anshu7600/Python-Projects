from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


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


def save_data():
    try:
        with open(mode="x", file="data"):
            pass
    except FileExistsError:
        pass

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(password) == 0 or len(email) == 0 or len(website) == 0:
        messagebox.showinfo(title="Empty", message="Please Don't leave any fields empty!")
    elif "@gmail.com" not in email:
        messagebox.showinfo(title="Email not Valid", message="Not a valid Email.\nPlease double check your email.")
    else:
        ok_info = messagebox.askokcancel(title="Confirmation", message=f"These are the details entered: \nWebsite: "
                                                                       f"{website}\nEmail: {email}\nPassword: "
                                                                       f"{password}\nDo you confirm the save?")

        if ok_info:
            with open(file="data", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        website_entry.focus()


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

website_entry = Entry(width=56, highlightthickness=1, highlightbackground="#DCDCDC", highlightcolor="#DCDCDC", bd=0,
                      bg="#FBFBFB")
website_entry.grid(column=1, row=1, columnspan=2, pady=2, padx=15)
website_entry.focus()
email_entry = Entry(width=56, highlightthickness=1, highlightbackground="#DCDCDC", highlightcolor="#DCDCDC", bd=0,
                    bg="#FBFBFB")
email_entry.insert(END, "vennamenanianshu@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, pady=2, padx=15)
password_entry = Entry(width=37, highlightthickness=1, highlightbackground="#DCDCDC", highlightcolor="#DCDCDC", bd=0,
                       bg="#FBFBFB")
password_entry.place(x=144, y=252)

generate_button = Button(text="Generate Password", bg="#FBFBFB", command=generate_password)
generate_button.place(x=374, y=249)
add_button = Button(text="Add", width=48, bg="#FBFBFB", command=save_data)
add_button.grid(column=1, row=4, columnspan=2, pady=12, padx=15)

window.mainloop()