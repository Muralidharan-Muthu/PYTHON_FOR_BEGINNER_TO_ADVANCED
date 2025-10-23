""" 
1. Introduction - It simply means that one class can inherit properties and methods from another class — just like a child inherits traits from their parents. 

2. super() Function 
super() is a built-in function that lets a child class access methods or attributes from its parent.

3. Types of Inheritance 

Type	                            Example	
Single Inheritance	          One parent → One child
Multilevel Inheritance	      Parent → Child → Grandchild	
Multiple Inheritance	      Child inherits from multiple parents	

4. Mini Project - Employee Management System
"""

# 1. super() function ----------------------------------------

class Parent:
    def __init__(self):
        print("Parent constructor called")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor called")

obj = Child()

# 2. Single Level Inheritance -----------------------------------

# Parent class
class Employee1:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: ₹{self.salary}")

# Child class (inherits from Employee)
class Manager1(Employee1):
    def __init__(self, name, salary, department):
        # call parent constructor
        super().__init__(name, salary)
        self.department = department

    def show_manager_info(self):
        self.show_details()
        print(f"Department: {self.department}")

# Create objects
emp1 = Employee1("Ravi", 40000)
mgr1 = Manager1("Priya", 80000, "Sales")

emp1.show_details()
print("------------------")
mgr1.show_manager_info()

# 3. Multilevel Inheritance --------------------------------------------

class SeniorManager1(Manager1):
    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        self.team_size = team_size

    def show_senior_info(self):
        self.show_manager_info()
        print(f"Team Size: {self.team_size}")

sm1 = SeniorManager1("Kiran", 120000, "Marketing", 10)
sm1.show_senior_info()

# 4. Multiple Inheritance -------------------------------------------

class Coder1:
    def code(self):
        print("Writing Python code...")

class Designer1:
    def design(self):
        print("Designing a new UI...")

class Developer1(Coder1, Designer1):
    def build(self):
        print("Building the project...")

dev1 = Developer1()
dev1.code()
dev1.design()
dev1.build()

# 5. Employee Management System - Hierarchical Inheritance ---------------------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Employee: {self.name}, Salary: ₹{self.salary}")

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def show_info(self):
        super().show_info()
        print(f"Programming Language: {self.language}")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def show_info(self):
        super().show_info()
        print(f"Manages a team of {self.team_size} members")

# Create objects
dev = Developer("Arun", 70000, "Python")
mgr = Manager("Divya", 90000, 8)

dev.show_info()
print("-----------------")
mgr.show_info()


# Thanks for the checkout . Plse give a star :)


