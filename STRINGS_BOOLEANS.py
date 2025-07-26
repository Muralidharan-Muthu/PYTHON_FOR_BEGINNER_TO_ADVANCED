# 1. What is a string? 

"In python, a string is simply text enclosed in quotes."

name = "Hello"
message = "Hello ,murali"
place = 'cuddalore'

# 2. String Operations

#Concatenation

add = name + message
print(add)

#Repetition

echo = name*4
print(echo)

#Length

print(len(name))

# 3. String Indexing & Slicing

#Indexing 

print(name[0])
print(name[1])
print(name[-1])
print(name[-2])

#Slicing

print(message[1:4])

# 4. String methods

print(name.upper())
print(name.capitalize())
print(name.lower())
print(name.count('l'))
print(message.replace("murali","lokesh"))

# 5. Escape Character

print("He is my \"friend\"")
print("I am going to \n america")
print("Hello \t everyone")

# 6. Booleans in Python

x = 10
y = 20

print(10 > 20)
print(x < y)
print(x == y)

# 7. Boolean Logic

age = 18
is_student = True

print(age >= 18 and is_student) # 1 & 1 => 1
print(age < 18 or is_student) # 0 | 1 => 1

# 8. Mini Project : String Analyzer Tool

def analyze_text(text):
    print("Original : ", text)
    print("Length : ",len(text))
    print("Uppercase : ", text.upper())
    print("Starts with Hi? : ", text.startswith("Hi"))
    print(" contains 'Python' ? :","Python" in text)

inp = input("Enter a sentence: ")
analyze_text(inp)


# Match 
# switch case

# thankyouuuu 
