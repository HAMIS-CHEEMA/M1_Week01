# Day one of python learning
print("Hello World")
# This is a comment
# This is a multi-line comment

# Variables and data types
name = "John"
age = 30
height = 5.9
is_student = True
# Print variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)
# Basic operations
sum = age + height
print("Sum of age and height:", sum)
difference = age - height
print("Difference of age and height:", difference)
product = age * height
print("Product of age and height:", product)
quotient = age / height
print("Quotient of age and height:", quotient)
# String concatenation
full_name = name + " Doe"
print("Full name:", full_name)
# String formatting
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)
# Lists
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)
# Accessing list elements
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Third fruit:", fruits[2])
# Adding an element to the list
fruits.append("orange")
print("Fruits after adding orange:", fruits)
# Removing an element from the list
fruits.remove("banana")
print("Fruits after removing banana:", fruits)
# Dictionaries
person = {
    "name": "John",
    "age": 30,
    "height": 5.9,
    "is_student": True
}
print("Person:", person)
# Accessing dictionary values
print("Name:", person["name"])
print("Age:", person["age"])
print("Height:", person["height"])
print("Is student:", person["is_student"])
# Adding a new key-value pair to the dictionary
person["city"] = "New York"
print("Person after adding city:", person)
# Removing a key-value pair from the dictionary
del person["is_student"]
print("Person after removing is_student:", person)
# Conditional statements
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")
# Loops
for i in range(5):
    print("Iteration:", i)
# While loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1