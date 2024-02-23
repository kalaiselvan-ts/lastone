# NameError: name 'x' is not defined

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not a number or integer")

print(f"x is {x}")