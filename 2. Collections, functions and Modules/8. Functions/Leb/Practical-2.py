"""
Write a Python program to create a calculator using functions.
"""

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4):- ")
n1 = int(input("Enter a number 1 :- "))
n2 = int(input("Enter a number 2 :- "))

if choice == '1':
    print("Result:", add(n1, n2))
elif choice == '2':
    print("Result:", sub(n1, n2))
elif choice == '3':
    print("Result:", mul(n1, n2))
elif choice == '4':
    print("Result:", div(n1, n2))
else:
    print("Invalid choice! Please select a valid operation.")
