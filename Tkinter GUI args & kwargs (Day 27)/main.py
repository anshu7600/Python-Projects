from tkinter import *

window = Tk()
window.title("GOmmy")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def button_clicked():
    my_label.config(text=input_enter.get())

# Label
my_label = Label(text="A little label", font=("Arial", 24, "bold"))
my_label.config(text="Config Change")
# my_label.place(x=150, y=115)
# my_label.pack(expand=True)
my_label.grid(column=0, row=0)

# Button
button = Button(text="GO! Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="Me so fresh", command=button_clicked)
new_button.grid(column=3, row=0)

# Entry
input_enter = Entry(width=20)
input_enter.insert(END, string="Some miles_label to start with")
# input_enter.pack()
input_enter.grid(column=4, row=3)

mainloop()