def add(a, b):
    return a + b


print(callable(add))  # True
print(callable(lambda x: x*x))  # True
