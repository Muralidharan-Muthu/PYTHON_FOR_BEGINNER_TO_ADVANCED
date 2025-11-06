"""
Python Inner Classes - An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.

1. Accessing Inner Class from the Outside

2. Accessing Outer Class from Inner Class

3. Multiple Inner Classes

4. Practical Example
"""

class Car: # Outer class
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self.engine = self.Engine()

  class Engine: # inner class
    def __init__(self):
      self.status = "Off"

    def start(self):
      self.status = "Running"
      print("Engine started")

    def stop(self):
      self.status = "Off"
      print("Engine stopped")

  def drive(self): 
    if self.engine.status == "Running":
      print(f"Driving the {self.brand} {self.model}")
    else:
      print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()