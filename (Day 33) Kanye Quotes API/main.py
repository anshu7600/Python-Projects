from tkinter import *
import requests

def get_quote():
    response = requests.get(url="https://icanhazdadjoke.com/slack")
    response.raise_for_status()
    text_data = response.json()["attachments"][0]["fallback"]
    canvas.itemconfig(quote_text, text=text_data)


window = Tk()
window.title("Dad Jokes Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)
get_quote()

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
