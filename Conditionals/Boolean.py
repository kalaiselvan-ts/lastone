# even or odd defining modulo
def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


#adding def for boolean expression
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()
