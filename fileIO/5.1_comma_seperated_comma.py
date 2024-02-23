# alternate way for this sorting
students = []

with open ("students.csv") as file:
    for line in file:
        name, house = line.strip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

# Alternate way by creating dictionary
students = []

with open ("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}") 