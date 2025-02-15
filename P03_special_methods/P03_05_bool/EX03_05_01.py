class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    person = Person('John', 25)
    print(bool(person))