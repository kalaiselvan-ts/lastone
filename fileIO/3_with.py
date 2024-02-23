# instead of using file.close() we are using with function

name = input("What's your name?")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# using with function for read mode
    
with open("names.txt, "r") as file:
          lines  = file.readlines()

for line in lines:
    print("hello,",line)
