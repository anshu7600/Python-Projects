# FileNotFound
# with open("a_file") as file:
#     file.read()

# KeyError
# a_dict = {"key": "value"}
# value = a_dict["a_key_that's_not_there"]

# IndexError
# fruit_list = ["Orange", "apple"]
# fruit = fruit_list[2]

# TypeError
# text = "abc"
# print(text + 5)

# Catching Exceptions

# try:
#     something that might cause an exception
# except:
#     do this it there was an exception
# else:
#     do this if there were no exception
# finally:
#     do this no matter what happens


# try:
#     file = open("a_file")
#     fruit_list = ["Orange", "apple"]
#     fruit = fruit_list[1]
# except FileNotFoundError:
#     with open("a_file", mode="w") as file:
#         print("File was not found, so created.")
# except IndexError as error_message:  # can have multiple except, and we can save the error message we would have got:
#     print(f"{error_message}")
# else:  # will rin if the code didn't have any errors
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     # Raising own exceptions
#     raise KeyError("This is an error I made up, great right") # will crash the code even if there is no error

height = float(input("Height: "))
if height > 3:
    raise ValueError("Human height should not be over 3 meters")

weight = int(input("Weight: "))

bmi = weight / height ** 2












