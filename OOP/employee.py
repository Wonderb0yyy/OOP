class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

# Test polimorfizmu
if __name__ == "__main__":
    emp1 = Employee("Anna", 5000)
    mgr1 = Manager("Tomasz", 10000)
    dev1 = Developer("Krzysztof", 8000, "Python")

    employees = [emp1, mgr1, dev1]
    
    print("Premie pracowników:")
    for emp in employees:
        print(f"{emp.name} ({type(emp).__name__}): {emp.calculate_bonus()}")
