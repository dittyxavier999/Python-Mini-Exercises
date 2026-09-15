class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


student1 = Student("Ditty", 31, "Python Django")
student2 = Student("Anish", 33, "AI/ML")

student1.display()
student2.display()