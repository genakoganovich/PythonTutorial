class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):  # Мы изменили сравнение
        return isinstance(other, Person) and self.name == other.name

p1 = Person("Alice")
p2 = Person("Alice")

print(p1 == p2)  # ✅ True

print(hash(p1))  # ❌ TypeError: unhashable type: 'Person'
