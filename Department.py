from enum import Enum

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"

class Person:
    def __init__(self, name, gender: Gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return f"{self.name} ({self.gender.value})"

class Employee(Person):
    def __init__(self, name, gender: Gender):
        super().__init__(name, gender)

class Department:
    def __init__(self, name, manager: Employee, employees: list[Employee]):
        self.name = name
        self.manager = manager
        self.employees = employees

    def __str__(self):
        return f"Department: {self.name}, Manager: {self.manager}, Employees: {[e.name for e in self.employees]}"

class Company:
    def __init__(self, name, departments: list[Department]):
        self.name = name
        self.departments = departments

    def count_employees(self):
        return sum(len(department.employees) for department in self.departments)

    def department_with_most_employees(self):
        max_department = max(self.departments, key=lambda d: len(d.employees))
        return max_department.name

    def __str__(self):
        return f"Company: {self.name}, Total Departments: {len(self.departments)}"

if __name__ == '__main__':
    emp1 = Employee("Alice", Gender.FEMALE)
    emp2 = Employee("Bob", Gender.MALE)
    emp3 = Employee("Charlie", Gender.MALE)

    manager1 = Employee("Diana", Gender.FEMALE)
    manager2 = Employee("Eve", Gender.FEMALE)

    dep1 = Department("IT", manager1, [emp1, emp2])
    dep2 = Department("HR", manager2, [emp3])

    company = Company("TechCorp", [dep1, dep2])

    # Ausgaben
    print(company)
    print(f"Total employees: {company.count_employees()}")
    print(f"Department with most employees: {company.department_with_most_employees()}")

    print(dep1)
    print(dep2)