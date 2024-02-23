# trying get_int to be used 

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not a number or integer")
        else:
            break
    return x 

main()

# simplifying or decreasing the code length

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not a number or integer")

main()