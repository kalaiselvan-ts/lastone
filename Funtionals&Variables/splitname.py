# Ask user for thier name
name = input("whats your name ").strip().title()

# split user's name into first and last name
first, second, third, fourth = name.split(" ")

# Say hello to user
print(f"hello, {third}")