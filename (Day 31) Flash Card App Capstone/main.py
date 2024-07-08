from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
dict_data = data.to_dict(orient="records")
current_set = {}

def next_card_french():
    global current_set

    try:
        current_set = random.choice(dict_data)
    except IndexError:
        canvas.itemconfig(language_canvas, text="")
        canvas.itemconfig(current_card_side, image=front_card_image)
        canvas.itemconfig(word_canvas, text="You Learned all 100 words!", fill="black", font=("Arial", 40, "normal"))
        window.after(1000, exit)
    else:
        french_word = current_set['French']
        english_word = current_set['English']

        canvas.itemconfig(current_card_side, image=front_card_image)
        canvas.itemconfig(language_canvas, text="French", fill="black")

        canvas.itemconfig(word_canvas, text=f"{french_word}", fill="black")
        window.after(3000, flip_card, english_word)

def flip_card(english_word):
    canvas.itemconfig(current_card_side, image=back_card_image)
    canvas.itemconfig(language_canvas, text="English", fill="white")
    canvas.itemconfig(word_canvas, text=f"{english_word}", fill="white")

def remove_card():
    global dict_data
    dict_data.remove(current_set)
    new_data = pandas.DataFrame(dict_data)
    new_data.to_dict("list")
    new_data.to_csv("data/words_to_learn.csv")
    next_card_french()

window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=70, pady=50)
window.minsize(900, 776)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, bg=BACKGROUND_COLOR, command=lambda: remove_card(), relief=FLAT)
right_button.grid(column=0, row=1, pady=20)
wrong_button = Button(image=wrong_image, command=lambda: next_card_french(), bg=BACKGROUND_COLOR, relief=FLAT)
wrong_button.grid(column=1, row=1)

front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
current_card_side = canvas.create_image(400, 265, image=front_card_image)
canvas.grid(row=0, column=0, columnspan=2)
language_canvas = canvas.create_text(400, 125, text="French", font=("Arial", 35, "italic"))
word_canvas = canvas.create_text(400, 263, text="trouve", font=("Arial", 55, "bold"))

window.after(0, next_card_french)

window.mainloop()
