# matching name with city **used case
name = input("What's you name? ")

if name == "harry":
    print("Gryffindor")
elif name == "Hermoine":
    print("Gryffindor")
elif name == "Ron":
    print("Gryfindor")
elif name == "Draco":
    print ("slytherin")
else: 
    print("who?")

# reducing code weight
name = input("What's you name? ")

if name == "harry" or name == "hermoine" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print ("slytherin")
else: 
    print("who?")


# match syntax usage for this code
name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

#reducing code weight
name = input("What's your name? ")

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")