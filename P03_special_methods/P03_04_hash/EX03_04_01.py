class Example:
    pass

a = Example()
b = Example()

print(hash(a))  # Например: 140391841277328 (ID в памяти)
print(hash(b))  # Например: 140391841278512 (другой ID)

print(id(a))
print(id(b))