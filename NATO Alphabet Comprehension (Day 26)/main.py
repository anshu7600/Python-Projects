import pandas

student_dict = {
    "student": ["Ash", "Pikachu", "Doraemon"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    pass
    # Access key and value

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# final_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# user_input = input("What Phonetic code words do you want of: ")
# phonetic_code = [final_dict[letter.upper()] for letter in user_input]
# print(phonetic_code)

print([{row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}[letter.upper()] for letter in input("What Phonetic code words do you want of: ")])
