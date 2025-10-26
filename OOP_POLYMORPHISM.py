"""
Python Polymorphism

1. Introduction to Polymorphism
-> The word "polymorphism" means "many forms", 
-> In programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

2. Function Polymorphism

3. Class Polymorphism

4. Inheritance Class Polymorphism

5. Mini Project - Fleet Dispatcher
"""

# 2. Function Polymorphism
# String example
x = "Hello World!"
print(len(x))   # 1

# Tuple example
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))  # 2

# Dictionary example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))  # 3

# 3. Class Polymorphism

class Car1:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat1:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane1:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car1("Ford", "Mustang")
boat1 = Boat1("Ibiza", "Touring 20")
plane1 = Plane1("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()

# 4. INHERITANCE + POLYMORPHISM

class Vehicle2:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car2(Vehicle2):
    pass

class Boat2(Vehicle2):
    def move(self):
        print("Sail!")

class Plane2(Vehicle2):
    def move(self):
        print("Fly!")

car2 = Car2("Ford", "Mustang")
boat2 = Boat2("Ibiza", "Touring 20")
plane2 = Plane2("Boeing", "747")

for x in (car2, boat2, plane2):
    print(x.brand, x.model)
    x.move()

# 5. Fleet Dispatcher

class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):
    def move(self):
        print("Car is driving 🚗")

class Bike(Vehicle):
    def move(self):
        print("Bike is racing 🏍️")

class Bus(Vehicle):
    def move(self):
        print("Bus is running 🚌")

# polymorphic function
def start_journey(vehicles):
    for v in vehicles:
        v.move()

# create list of vehicles
vehicles = [Car(), Bike(), Bus()]

# start the journey
start_journey(vehicles)





