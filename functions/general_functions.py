# Why use functions?
# Principles: DRY (Don't Repeat Yourself)

def print_something(print_string):
    print(print_string)


def addition(int1, int2):
    return int1 + int2


def multi_args(*multiargs):
    print(type(multiargs))
    for arg in multiargs:
        print(arg)

multi_args(1, 22, 4, 55, 5, 6)


def greeting(name: str):
    print("Hello, my name is " + name)

greeting("Rubel")

print_something("Bob is sick today")
print(addition(5,3))

