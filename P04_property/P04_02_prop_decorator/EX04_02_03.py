class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

if __name__ == "__main__":
    john = Person('John', 25)
    print(john.age)
