# Day two of python learning
#           OPERATORS
#Arithmetic operators

a = int(input("enter 1st number "))
b = int(input("enter 2nd number "))
add = a + b
minus = a - b
mul = a * b
if b!=0:
    div = a / b
    modu_lus = a % b
    exponent = a ** b
    floor = a // b
    print("Sum = ",add)
    print("Difference = ",minus)
    print("Product = ",mul)
    print("Division = ",div)
    print("Remainder = ",modu_lus)
    print("a^b (power) = ",exponent)
    print("Floor division ",floor)
else:
    print("Can't divide by zero")

# logical operators

a = int(input("enter 1st num "))
b = int(input("enter 2nd num "))

print("a greater than b? ", a > b)
print(" a less than b? ", a<b)
print("Checking a and b are equal ? ", a==b)
print("Checking a and b are not equal ? ", a!=b)
print("a lesser or equal ? ", a<=b)
print("a Greater or equal ? ", a>=b)

# comparison operators

a = 10
b= 5
print(a>5 and b<10)
print(a>5 or b<10)
print(not(a>5 and b<10))

