import csv
import pandas as pd

# with open("weather_data.csv") as file:
#     data = [file.readlines()]
#     print(data)

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

# data = pd.read_csv("weather_data.csv")
# print(type(data["temp"]))
# print(type(data))
# print(data)
# print(data["temp"])
# print(data.to_dict())

# temp_list = data["temp"].to_list()

# average temp

# num = 0
# length = 0
# for i in temp_list:
#     num += i
#     length += 1
# print(num/length)
# same as
# print(data["temp"].mean())

# max of the column temp
# print(data["temp"].max())

# Data in Columns
# print(data["condition"])
# or:
# print(data.condition)

# Data in row
# print(data[data.day == "Monday"]) # gives the row where monday is he day
# print(data[data.temp == data["temp"].max()]) # gives the where the temp is max

# monday = data[data.day == "Monday"]
# print((9 / 5) * int(monday.temp.iloc[0]) + 32)  # will give us the temp and converts it to F

# Create a Data from scratch
# data_dict = {
#     "students": ["Shreyansh", "Anshu", "Prateek", "Siddu"],
#     "scores": [99, 100, 1, 0]
# }

# new_data = pd.DataFrame(data_dict)
# print(new_data)
#
# Making a csv file from this data
# new_data.to_csv("new_data.csv")

# Squirrel Challenge

data = pd.read_csv("Squirrel_Census.csv")
data_dict = {
    "Fur Color": [],
    "Count": []
}
for color in data["Primary Fur Color"].dropna().unique():
    data_dict["Fur Color"].append(color)
    data_dict["Count"].append(data[data["Primary Fur Color"] == color].count()["Primary Fur Color"])
df = pd.DataFrame(data_dict)
df.to_csv("primary_color_count.csv")
