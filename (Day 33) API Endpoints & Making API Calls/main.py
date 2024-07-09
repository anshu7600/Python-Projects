import requests
# API stands for
# Application Programming Interfaces

# An API is a set of commands, functions, protocols, and objects that programmers can use to create software or
# interact with an external system.

# we can make a request to the external system using there API and then if the request is valid it will give a response
# an API is all the things you can do to access the external server

# API Endpoint
# so if we want to get the data from a particular service we need to know the location that data is stored at.
# example if you want to get money out of a bank you first need to know where the bank is
# so if you want to get crypto data you might use api.coinbase.com

# API requests
# this is similar to going to a bank and getting some money out
# but there are rules for doing it like in this example: a bank person?
# and so here the bank person is kinda like the API the interface between you and the external server

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)

# Responses: HTTP Codes

# 404 means that thing your look for does exist
# if it is 1XX (one hundred) something it means Hold on this is not final
# 2XX means Here you go, done
# 3XX, go away, doesn't have permission
# 4XX, you screwed up
# 5XX, the server screwed up

# link to the HTTP Status Codes
# httpstatuses.com

# print(response.raise_for_status())
# will only give us the code

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)

print(iss_position)

# API Parameters
# A way to provide an input when requesting for data, so you get the specific data you want
