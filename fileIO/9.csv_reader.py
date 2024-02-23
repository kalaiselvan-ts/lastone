# to use csv reader in the file

import csv

students = []

with open ("students1.csv") as file:
   reader = csv.reader(file)
   for row in reader:
       students.append({"name": row[0], "home": row[1]})

for student in sorted(students, key = lambda student: student["home"]):
    print(f"{student['name']} is from {student['home']}" )

# row [1] and [2] are list notations and we can use in normal other ways

import csv

students = []

with open ("students1.csv") as file:
   reader = csv.reader(file)
   for name, home in reader:
       students.append({"name": name, "home": home})

for student in sorted(students, key = lambda student: student["home"]):
    print(f"{student['name']} is from {student['home']}" )