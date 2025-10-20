"""
1. OOP in Python - OOP lets you model real things as objects (data + behaviour) 

using classes — 
    helps organize code, 
    reuse it, 

2. Class & Object — basic example - car

3. Instance vs Class variables

4. Methods: instance, @staticmethod, @classmethod
"""

# Class & Object — basic example - car

class Car1:                                
    def __init__(self, make, model, year):
        self.make = make                  
        self.model = model                
        self.year = year                  
        self.started = False             

    def start(self):                      
        self.started = True               
        return f"{self.make} {self.model} started."  

    def info(self):                       
        return f"{self.year} {self.make} {self.model}" 
    

# Instance vs Class variables

# create an object (instance)
my_car = Car1("Toyota", "Corolla", 2020)   
print(my_car.info())                      
print(my_car.start())                     

class Car2:
    wheels = 4                  # class variable (shared)
    def __init__(self, make):
        self.make = make        # instance variable (unique per car)

c1 = Car2("Honda")              # object 1
c2 = Car2("Ford")               # object 2
print(Car2.wheels)              # access class variable -> 4
print(c1.wheels, c2.wheels)    # both see 4
c1.wheels = 3                  # this creates an instance attribute on c1 only
print(c1.wheels, c2.wheels, Car2.wheels)  # 3, 4, 4

# Methods: instance, @staticmethod, @classmethod

# Simple Car class
class Car3:
    wheels = 4  # Class variable, shared by all cars

    # Constructor: called when we create a new Car
    def __init__(self, make, model):
        self.make = make  # Instance variable
        self.model = model  # Instance variable

    # Instance method: works with a specific car
    def full_name(self):
        return self.make + " " + self.model

    # Static method: works without needing a specific car
    @staticmethod
    def km_to_miles(km):
        return km * 0.62  # Convert km to miles

    # Class method: creates a Car from a string
    @classmethod
    def from_string(cls, car_str):
        make, model = car_str.split("-")  # Split string like "[Toyota,Corolla]"
        return cls(make, model)  # Create a new Car object
