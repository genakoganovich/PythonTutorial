class Counter:
    def __init__(self, start=1):
        self.count = start

    def increase(self):
        self.count += 1

    def value(self):
        return self.count

print(callable(Counter.increase))  # True