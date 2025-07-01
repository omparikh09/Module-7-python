"""
Write a Python program to create a list with elements of multiple data types (integers,
strings, floats, etc.).
"""

# Creating a list with mixed data types
mixed_list = [42, "hello", 3.14, True]


print("Mixed Data Type List:", mixed_list)

for item in mixed_list:
    print(f"Value: {item}, Type: {type(item)}")
