# used to sort functions instead of using get_ function using here house 
students = []

with open ("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key = lambda student: student["house"]):
    print(f"{student['name']} is in {student['house']}" )
