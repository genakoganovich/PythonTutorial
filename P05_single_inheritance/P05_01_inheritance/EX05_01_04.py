class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, it's {self.name}"


class Employee(Person):
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

class SalesEmployee(Employee):
    pass

if __name__ == '__main__':
    person = Person('Jane')
    print(type(person))

    employee = Employee('John', 'Python Developer')
    print(type(employee))

    print(isinstance(employee, Person))  # True
    print(isinstance(employee, Employee))  # True
    print(isinstance(person, Employee))  # False

    print(issubclass(Employee, Person))  # True

    print(issubclass(SalesEmployee, Employee))  # True
    print(issubclass(SalesEmployee, Person))  # True

    print(issubclass(Person, object))  # True

