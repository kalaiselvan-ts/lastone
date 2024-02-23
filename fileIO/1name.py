# general way for getting name
name = input ("What's your name?")
print(f"hello, {name}")

# another way to sort the names as per order
names = []

for _ in range(3):
    names.append(input("Whats's your name?"))

for name in sorted(names):
    print(f"hello, {name}") 