import json

# READ JSON FILE

with open("students.json", "r") as file:
    students = json.load(file)

print("Students:")
print(students)


# ADD NEW STUDENT

new_student = {
    "id": 3,
    "name": "Ditty",
    "course": "Python Django"
}

students.append(new_student)


# WRITE BACK TO JSON FILE

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Student added successfully!")