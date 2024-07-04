from tkinter import *

window = Tk()
window.title("GOmmy")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="A little label", font=("Arial", 24, "bold"))
my_label.pack()
my_label.config(pady=10, padx=20)

# rename
my_label["miles_label"] = "New Text"
# or
my_label.config(text="Config Change")

# Button

def button_clicked():
    my_label.config(text=input_enter.get())
    #                      get current value from line 1 character 0 to end
    print(f"Text box info: {text_box.get('1.0', END)}")

button = Button(text="GO! Click me", command=button_clicked)
button.pack()

# Entry

input_enter = Entry(width=20)
input_enter.insert(END, string="Some miles_label to start with")
input_enter.pack()

# Text

text_box = Text(height=4, width=24)
text_box.insert(END, "This is a miles_label box")
# the cursor is going to start in this miles_label box
text_box.focus()
text_box.pack()

# Spin Box

spin_box = Spinbox(width=5, from_=0, to=24)
spin_box.pack()

# Scale

scale_box = Scale(from_=1, to=10)
scale_box.pack()

# CheckButton
# variable to hold on to checked state, 0 is off, 1 is on
def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()

checkbutton = Checkbutton(text="Switch on?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
checkbutton.pack()

# RadioButton
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
values = {"Option 1": "1",
          "Option 2": "2"}

for (text, value) in values.items():
    Radiobutton(text=text,
                value=value,
                variable=radio_state,
                command=radio_used).pack()

# List Box

def listbox_used(event):
    # gets the selected item from the list box
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=5)
items = ["Me", "You", "He"]
for item in items:
    listbox.insert(items.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
