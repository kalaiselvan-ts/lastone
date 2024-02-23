# using sort function for get_name for this function for names in file
students = []

with open ("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key = get_name, reverse = True):
    print(f"{student['name']} is in {student['house']}")

# using sort function for get_name for this function for house in file
students = []

with open ("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_house(student):
    return student["house"]

for student in sorted(students, key = get_house):
    print(f"{student['name']} is in {student['house']}")