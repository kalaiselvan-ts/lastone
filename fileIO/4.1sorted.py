# to sort file wothin names file itself
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

# to sort the input as per decendign order we are using reverse = true

for name in sorted(names, reverse = True):
        print(f"hello, {name}")
