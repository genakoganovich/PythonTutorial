class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    john = Person('John', 18)

    john.age = 19
    john.age = -1

    age = -1
    if age <= 0:
        raise ValueError('The age must be positive')
    else:
        john.age = age
