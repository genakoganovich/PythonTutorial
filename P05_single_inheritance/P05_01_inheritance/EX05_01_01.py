class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, it's {self.name}"


if __name__ == '__main__':
    person = Person("John")
    print(person.greet())
