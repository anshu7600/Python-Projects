from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Time 2.0")
window.config(background=YELLOW, padx=100, pady=50)
window.minsize(400, 350)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text=" Start ", bg="white", highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text=" Reset ", bg="white", highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmarks_label = Label(text="✔", fg=GREEN, font=(FONT_NAME, 10, "bold"), bg=YELLOW)
checkmarks_label.grid(column=1, row=3)

window.mainloop()
