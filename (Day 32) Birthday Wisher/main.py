import smtplib
import pandas
import datetime as dt
import random

data = pandas.read_csv("birthdays.csv").to_dict(orient="records")

LETTERS_NAME = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
SENDER_EMAIL = "shreyanshvennamaneni8@gmail.com"
PASSWORD = "cvogbmaqrnbcrzfz"

current_month = dt.datetime.now().month
current_date = dt.datetime.now().day

for person in data:
    if current_date == person["day"] and current_month == person["month"]:
        name = person["name"]
        to_email = person["email"]

        if name == "Siddu":
            letter_path = "letter_templates/letter_4.txt"
        else:
            letter_path = f"letter_templates/{random.choice(LETTERS_NAME)}"

        with open(letter_path) as file:
            letter = str(file.read()).replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=to_email, msg=f"Subject:Happy Birthday\n\n{letter}")
