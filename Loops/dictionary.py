# students belongs to which club, normal code without dict

students = {
    "Hermoine": "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin",
}

print(students["Draco"])
print(students["Harry"])
print(students["Ron"])
print(students["Hermoine"])

# using for loop instead of general print statement

students = {
    "Hermoine": "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")