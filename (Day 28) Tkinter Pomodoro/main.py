from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = ""
timer = ""
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global checkmarks
    if timer != "":
        window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    global reps
    reps = 0
    checkmarks = ""
    checkmarks_label.config(text=checkmarks)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer_button():
    reset_timer()
    start_timer()

def start_timer():
    global reps
    reps += 1

    work_time = [1, 3, 5, 7]
    short_break = [2, 4, 6]

    if reps in work_time:
        timer_label.config(text="Timer", fg=GREEN)
        count_down(10)
    elif reps in short_break:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    elif reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global time_text
    global checkmarks
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks += "✔"
            checkmarks_label.config(text=checkmarks)
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
time_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text=" Start ", bg="white", highlightthickness=0, command=start_timer_button)
start_button.grid(column=0, row=2)

reset_button = Button(text=" Reset ", bg="white", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmarks_label = Label(fg=GREEN, font=(FONT_NAME, 10, "bold"), bg=YELLOW)
checkmarks_label.grid(column=1, row=3)

window.mainloop()
