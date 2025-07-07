# Integers ( whole numbers)

a = 3456
b = -3456

# Floats( decimal numbers )
c = 3.14567
d = -4.567

# Complex number ( real + imaginary )

e = 4 + 5j

# Check the data type

print(type(a))
print(type(d))
print(type(e))

# Built-in functions for numbers in python

print(abs(-10))
print(abs(10))

print(pow(2,3)) # 8

print(round(3.14159))
print(round(3.14159,3))

print(min(1,2,3))
print(max(2,4,8))

# type conversion in python

x = 5.9
y = 10
z = "20"

print(int(x))
print(float(y))
print(type(int(z)))

# Mini project : Simple calculator

num1 = input("Enter first number: ") 
num2 = input("Enter second number: ")

# Convert string to float
num1 = float(num1) 
num2 = float(num2)

operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operation")



