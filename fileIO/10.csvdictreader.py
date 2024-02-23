# we trying change the name and home flip from one side to another but even after we will get this in name home format

import csv

students = []

with open ("students2.csv") as file:
   reader = csv.DictReader(file)
   for row in reader:
       students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key = lambda student: student["home"]):
    print(f"{student['name']} is from {student['home']}" )