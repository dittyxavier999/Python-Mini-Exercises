students = [
        
    {"id": 1, "name": "Anu", "course": "Python"},
    {"id": 2, "name": "Rahul", "course": "Django"}
]


# CREATE
def create_student(student_id, name, course):
    student = {
        "id": student_id,
        "name": name,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")


# READ
def read_students():
    print("\nStudent List:")

    for student in students:
        print(student)


# UPDATE
def update_student(student_id, new_course):

    for student in students:
        if student["id"] == student_id:
            student["course"] = new_course
            print("Student updated successfully!")
            return

    print("Student not found!")


# DELETE
def delete_student(student_id):

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found!")


# Testing CRUD

read_students()

create_student(3, "Ditty", "Django")

read_students()

update_student(3, "Python Django")

read_students()

delete_student(2)

read_students()