# intially used file = open("names.txt", "w") and now changed to file = open("names.txt", "a") to change the output from rewriting to append, which is w to a.

name = input("What's your name?")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
