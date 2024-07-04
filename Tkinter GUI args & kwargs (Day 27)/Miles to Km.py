from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize()
window.config(padx=10, pady=10)

def calculate_miles():
    km_result.config(text=str(float(entry.get()) * 1.609))

entry = Entry(width=10)
entry.insert(END, "0")
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10)

equal_to = Label(text="is equal to ")
equal_to.grid(column=0, row=1)
equal_to.config(padx=10, pady=10)

km_result = Label(text="0")
km_result.grid(column=1, row=1)
km_result.config(padx=10, pady=10)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=10)

button = Button(text="Calculate", command=calculate_miles)
button.grid(column=1, row=2)
button.config()

mainloop()
