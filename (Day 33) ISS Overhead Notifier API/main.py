import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 33.078716
MY_LONG = -96.808304
SENDER_EMAIL = "shreyanshvennamaneni8@gmail.com"
PASSWORD = "cvogbmaqrnbcrzfz"
receiver = "vennamenanianshu@gmail.com"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = data["iss_position"]["longitude"]
iss_longitude = data["iss_position"]["latitude"]

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "tzid": "America/Chicago",
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour


def is_night():
    if sunset <= time_now >= sunrise:
        return True


def is_iss_overhead():
    if 5 > MY_LAT - iss_latitude or MY_LAT - iss_latitude > -5 and \
            5 > MY_LONG - iss_longitude or MY_LONG - iss_longitude > -5:
        return True


while True:
    if is_night() and is_iss_overhead():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=SENDER_EMAIL,
                                to_addrs=receiver,
                                msg="Subject:ISS Alert\n\nLook up, the ISS is above you, or at least kinda close."
                                    "\nI guess, if this code is right.")
            print("One Email Sent")
        for i in range(60, 0, -1):
            print(f"Another Email will be sent after: {i} seconds")
            time.sleep(1)
