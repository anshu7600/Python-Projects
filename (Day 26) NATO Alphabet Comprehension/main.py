import pandas

# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# final_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# user_input = input("What Phonetic code words do you want of: ")
# phonetic_code = [final_dict[letter.upper()] for letter in user_input]
# print(phonetic_code)

# made for fun
# print([{row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}[letter.upper()] for letter in input("What Phonetic code words do you want of: ")])

# Updated in day 30, challenge

data = pandas.read_csv("nato_phonetic_alphabet.csv")
final_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    user_input = input("What Phonetic code words do you want of: ")
    try:
        phonetic_code = [final_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabets can be entered\n")
    else:
        print(phonetic_code)
        break
