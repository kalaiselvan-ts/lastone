# we can't get output for the file with name students1 so we can't clear value error, so we are referring to the csv reader
students = []

with open ("students1.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",") 
        student = {"name": name, "home": home}
        students.append(student)

for student in sorted(students, key = lambda student: student["home"]):
    print(f"{student['name']} is from {student['home']}" )