# using with function for read mode
    
with open("names.txt", "r") as file:
          lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())


# lowering the code weight
with open ("names.txt", "r") as file:
       for line in file:
              print("hello,", line.rstrip())


