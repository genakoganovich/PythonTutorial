class Counter:
    def __init__(self, start=1):
        self.count = start

    def increase(self):
        self.count += 1

    def value(self):
        return self.count

    def __call__(self):
        self.increase()


counter = Counter()
counter()

print(callable(counter))  # True

