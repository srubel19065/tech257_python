x = 1
a_int = int(input("Enter a number "))
b_int = int(input("Enter a number "))

while x < 101:
    #print(x)
    if x % (a_int) == 0 and x % (b_int) == 0:
        print("FizzBuzz")
    elif x % a_int == 0:
        print("Fizz")
    elif x % b_int == 0:
        print("Buzz")
    else:
        print(x)
    x += 1


