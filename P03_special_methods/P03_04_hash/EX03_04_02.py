class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):  # Два объекта равны, если у них одинаковое имя
        return isinstance(other, Person) and self.name == other.name

    def __hash__(self):  # Хэш зависит от имени (два объекта с одинаковым именем = одинаковый хэш)
        return hash(self.name)

a = Person("Alice")
b = Person("Alice")
c = Person("Bob")

print(a == b)  # ✅ True (так как их имена равны)
print(hash(a), hash(b))  # ✅ Одинаковые хэши

people = {a, b, c}
print(len(people))  # ✅ 2 (Alice считается одной записью!)
