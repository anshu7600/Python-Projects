import random
import smtplib
import datetime as dt

SENDER_EMAIL = "shreyanshvennamaneni8@gmail.com"
PASSWORD = "cvogbmaqrnbcrzfz"
receiver = "vennamenanianshu@gmail.com"

day_of_week = dt.datetime.now().weekday()

if day_of_week == 0:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quotes_for_today = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=receiver,
            msg=f"Subject:Read for Motivation\n\n{quotes_for_today}"
        )
