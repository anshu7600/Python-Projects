# # file = open("a_simple_file")
# # content = file.read()
# # print(content)
# # file.close()
#
# # Deletes past things in the file when in mode w
# # with open("a_simple_file", mode="w") as file:
# #     file.write("NEW, NEW FRESH FRESH FRESH TEXT!")
#
# # adds to the file a stand for append
# with open("a_simple_file", mode="a") as file:
#     file.write("\nOLD crap ^")
#     file.write("\nNEW NEW FRESH FRESH FRESH TEXT!")
#
# # when we try to open a file in write mode and the file doesn't exist it makes it
# with open("make_me", mode="w") as file:
#     file.write("FRESH FRESH FILE")
#
# # reads the file
# with open("a_simple_file") as file:
#     content = file.read()
#     print(content)

# makes a file but fails if the file already exists
# with open("Yo_new_x", mode="x") as file:
#     pass

# absoulute
# with open("C:\\Users\\venki\\OneDrive\\Desktop\\a_simple_file") as file:
#     print(file.read())

# relative
# with open("../../OneDrive/Desktop/a_simple_file") as file:
#     print(file.read())
