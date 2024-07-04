# Arguments with default values
def my_function(a=1, b=2, c=3):  # if not changed when the function is called it is going to go with these values
    return a + b + c


print(my_function())  # we don't need to provide a value
print(my_function(a=0))  # we can also only change one value
print(my_function(a=0, b=1, c=2))  # or all

# *args: Many positional Arguments
print("*args: Many positional Arguments:")


def add(*args):
    print(args)  # this is going to be a tuple, and the position matters, because that is the order they are in
    num = 0
    for n in args:
        num += n
    print(num)


add(1, 2, 3, 4, 5, 6)

# **kwargs: Many Keyword Arguments
print(" **kwargs: Many Keyword Arguments: ")


def calculate(n, **kwargs):
    print(kwargs)  # this is going to be a dict and the key name is the keyword, and the value is the value assigned
    # when the function is called
    # for key, value in kwargs.items():  # can do this because it is a dict
    #     print(f"key of dict name: {key}")
    #     print(f"value of dict: {value}")
    # or this if we know the name of the keyword:
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]


calculate(1, add=5, multiply=0)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan", model="Rouge")
print(my_car.model)
# we can do this
