age: int
# # we can declare a variable and assign a type and just leave it empty
# # and later when we want to assign it to something we can change the value
# # we can do it to all datatype
name: str
height: float
is_human: bool

# we can specify the data type of the output like this, this is called type hints
# also we can declare the datatype of a parameter
def police_check(age_of_person: int) -> bool:
    if age_of_person >= 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

# we defined the type so we by chance pass "ten" a string, it is going to give a warning
if police_check(12):
    print("you may pass")
else:
    print("pay a fine")
