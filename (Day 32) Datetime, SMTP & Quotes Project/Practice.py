# import smtplib
#
# sender_email = "shreyanshvennamaneni8@gmail.com"
# password = "cvogbmaqrnbcrzfz"
#
# # This code has to be of the email address your sending from, this is for gmail account and it would be different for
# # other sending services
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # securing the connection
#     connection.starttls()
#     # loging in the account
#     connection.login(user=sender_email, password=password)
#     # the email your sending form and to the person you are sending
#     connection.sendmail(from_addr=sender_email,
#                         to_addrs="vennamenanianshu@gmail.com",
#                         msg="Subject:Is this working\n\nHi testing! With subject?")
#

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.year
day_of_week = now.weekday()
# computers start from 0 so 0 is monday 1 is tuesday and so on
print("day of the week:")
print(day_of_week)
print("type of year:")
print(type(year))
if year == now.year:
    print("Yo it 2024")

# Saving data of birth

birthday = dt.datetime(year=2010, month=5, day=13)
print(birthday)
