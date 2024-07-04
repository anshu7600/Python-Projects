with open("Input/Letters/starting_letter.txt") as start:
    starting_letter = start.read()
print(starting_letter)
with open("Input/Names/invited_names.txt") as names:
    for name in names:
        final_letter = starting_letter.replace("[name]", name.splitlines()[0])
        with open(f"Output/ReadyToSend/letter_to_{name.splitlines()[0]}", mode="w") as file:
            file.write(final_letter)
