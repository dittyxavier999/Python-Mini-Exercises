class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


student1 = Student("Ditty", 31)

student1.display()