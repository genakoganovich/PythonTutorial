class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)

print(john is jane)  # False
print(john == jane) # False
