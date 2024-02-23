# creating a loop to get only integer as output
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not a number or integer")
    else:
        break

print(f"x is {x}")

# alternate ways for reprompting also to place break function in other way
while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not a number or integer")

print(f"x is {x}")