"""
1. Python Encapsulation

-> Encapsulation is about protecting data inside a class.
-> It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
-> This prevents accidental changes to your data and hides the internal details of how your class works.

2. Why Use Encapsulation?

-> Data Protection: Prevents accidental modification of data
-> Validation: You can validate data before setting it
-> Flexibility: Internal implementation can change without affecting external code
-> Control: You have full control over how data is accessed and modified

3. Private Properties

4. Get Private Property Value

5. Set Private Property Value

"""

# Private Properties

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p = Person("Emil", 25)
print(p.name)
print(p.__age) # This will cause an error

# Get Private Property Value

class Person2:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p2 = Person2("Tobias", 25)
print(p2.get_age())

# Set Private Property Value
class Person1:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person1("Tobias", 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())