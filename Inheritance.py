class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")


class Developer(Person):

    def code(self):
        print("I am writing Python code")


developer = Developer("Ditty")

developer.introduce()
developer.code()