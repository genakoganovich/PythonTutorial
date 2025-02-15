import pprint

class Person:
    __slots__ = ("_age",)

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("Age must be positive")
        self._age = value

if __name__ == '__main__':
    person = Person(40)
    pprint.pprint(Person.__dict__)