import requests
import datetime

date = datetime.datetime.now().date()
hour_now = datetime.datetime.hour

MY_LAT = 33.078716
MY_LONG = -96.808304

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "date": date,
    "tzid": "America/Chicago",
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json",
                        params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise, ":Sunrise")
print(sunset, ":Sunset")
