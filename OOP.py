"""
1. OOP in Python - OOP lets you model real things as objects (data + behaviour) 

using classes — 
    helps organize code, 
    reuse it, 

2. Class & Object — basic example - car

3. Instance vs Class variables

4. Methods: instance, @staticmethod, @classmethod
"""

# Simple Car class
class Car:
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

#car1 = Car("Toyato","Carollo")
#print(car1.full_name())

#print(Car.km_to_miles(100))

car2 = Car.from_string("Hondo-Civic") # Car("Honda","Civic")
print(car2.full_name())


                   
