from cs50 import get_string

students = []

for i in range(1):
    name = get_string("Name: ")
    dorm = get_string("Dorm: ")

    student = { "name": name, "dorm":dorm }

    students.append(student)

for student in students:
    print(f"Name: {student['name']} \t Dorm: {student['dorm']}")