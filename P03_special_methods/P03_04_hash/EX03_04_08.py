class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age

members = {
    Person('John', 22),
    Person('Jane', 22)
}

hash(Person('John', 22))