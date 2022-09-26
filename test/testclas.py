class Employee():


    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary


emp = Employee('Alice', 100)

print(emp.name)
print(emp.get_salary())