class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name

    __hash__ = None  # Делаем объект unhashable

p1 = Person("Alice")
p2 = Person("Alice")

print(p1 == p2)  # ✅ True
print(hash(p1))  # ❌ TypeError (но теперь это ожидаемо)

