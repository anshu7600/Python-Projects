import random
import pandas as pandas

# List comprehension
# remember
# [new_item for item in list]

numbers = [1, 2, 3]
new_list = []
for i in numbers:
    add_1 = i + 1
    new_list.append(add_1)
print(new_list)

# or

new_list = [i + 1 for i in numbers]
print(new_list)

# we can also do this to string

name = "Shreyansh"
new_string = [letter for letter in name]
# is going to result in ['S', 'h', 'r', 'e', 'y', 'a', 'n', 's', 'h']
# because it is going to append each of the letters  in the name
print(new_string)

# Challenge

# Need a list [2, 4, 6, 8] from range(1, 5)

new_list = [num * 2 for num in range(1, 5)]
print(new_list)
# Done

# Conditional List Comprehension
# remember
# [new_item for item in list if test]
# this will only add the new_item if the test is satisfied

# Challenge

names = ["Ash", "Tom", "Donkey", "Doraemon", "Pokemon", "Sam"]
# Only get the names which are 3 letters long
# use Conditional List Comprehension

new_list = [name for name in names if len(name) == 3]
print(new_list)
# Done

# Challenge
# Only get the names which are more than 3 letters long, and make them all caps
new_list = [name.upper() for name in names if len(name) > 3]
print(new_list)
# Done

# Dictionary Comprehension
# remember
# new_dict = {new_key: new_value for item in list}

# we can also create a new dict based of the values from an existing dict
# new_dict = {new_key: new_value for (key, value) in dict.items()}

# and we can also add a condition
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}

names = ["Ash", "Tom", "Donkey", "Doraemon", "Pikachu", "Sam"]
# generating random score for each name in a dict
students_score = {key: random.randint(0, 100) for key in names}
print(students_score)

# looping though dict

# looks through the scores and if the score is more than 60 then they passed
passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
print(passed_students)

# Iterating over a pandas DataFrame
student_dict = {
    "student": ["Ash", "Pikachu", "Doraemon", "Nobita", "Shinchan"],
    "score": [4, 99, 99, 0, 64]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Pandas in-built Loop
# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(index)  # will give the index of all the rows
    print(row)  # will print a row
    print(row.student)  # this is going to print out the student name in the row
