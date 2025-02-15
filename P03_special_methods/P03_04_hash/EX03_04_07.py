class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('John', 22)
p2 = Person('Jane', 22)

print(hash(p1))
print(hash(p2))

print(id(p1))
print(id(p2))
