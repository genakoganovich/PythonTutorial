class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, it's {self.name}"

class Employee:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

    def greet(self):
        return f"Hi, it's {self.name}"

if __name__ == '__main__':
    employee = Employee("John", "worker")
    print(employee.greet())
    