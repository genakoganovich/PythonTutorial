import sys

class WithoutSlots:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class WithSlots:
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    p1 = WithoutSlots("Alice", 30)
    p2 = WithSlots("Alice", 30)

    print(sys.getsizeof(p1.__dict__))  # 296 байт
    print(sys.getsizeof(p1))           # 48 байт
    print(sys.getsizeof(p2))           # 48 байт
