"""
Write a Python program to add elements to a list using insert() and append().
"""

l1 = []

# add elements using append() method in list 
l1.append("Python")
l1.append("Java")

print(f"list after append() method :- {l1}")

# add elements using insert() method in list
l1.insert(1, "C")
l1.insert(0, "Html")

print(f"list after insert() method :- {l1} ")