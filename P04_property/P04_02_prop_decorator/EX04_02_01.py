class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    age = property(fget=get_age)

if __name__ == '__main__':
    john = Person('John', 25)
    print(john.age)
    print(john.get_age())