# the try and except error will help you to handle if and ifnot of the function

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print(" x is not a number or integer")
