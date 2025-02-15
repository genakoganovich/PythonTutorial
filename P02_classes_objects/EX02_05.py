class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, it's {self.name}."

print(Person.counter)

person = Person('John',25)
print(person.counter)
