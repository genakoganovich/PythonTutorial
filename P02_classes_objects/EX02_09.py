class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f"Hi, it's {self.name}."

    @classmethod
    def create_anonymous(cls):
        return Person('Anonymous', 22)

class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title
