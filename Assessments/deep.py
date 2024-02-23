# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
# Ask user the question. 'What is the Answer to the Great Question of Life, the Universe, and Everything?'
name = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").title().replace(" ", "")

if name == "42":
    print("Yes")
elif name == "Forty-Two":
    print("Yes")
elif name == "FortyTwo":
    print("Yes")
else:
    print("No")


# **** Submitted this code ****
# Ask user the question. 'What is the Answer to the Great Question of Life, the Universe, and Everything?'
name = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").title().replace(" ", "")

#using match conditional to simplify the code
match name:
    case "42" | "Forty-Two" | "FortyTwo":
        print("Yes")
    case _:
        print("No")