# Mini project : Multiplication Table generator

number = int(input("Enter a number: "))

print(f"\nMultiplication Table for {number}:\n")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
