# whole point is about printing ash in three lines

# 1 basic step
print("#")
print("#")
print("#")

# 2 another way
for _ in range(3):
    print("#")

# 3rd way
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
       print("#")


main()

# 4th way
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")

main()

# 5th way
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()


# the whole point is to create a matrix of 3by3  
def main():
    print_square(3)

def print_square(size):

# for each row in square
    for i in range(size):
# for each brick in row
        for j in range (size):
# print brick
            print("#" , end="")
        print()

main()

# alternate way for this matrix
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)
    
def print_row(width):
    print("#" * width)

main()