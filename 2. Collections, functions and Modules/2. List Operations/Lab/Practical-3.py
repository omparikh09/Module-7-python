"""
Write a Python program to remove elements from a list using pop() and remove().
"""

l1 = ['Python', 'C++', 'C', 'Java', 'Html', 'CSS', 'Javascripts']

# remove elements using pop() method 
l1.pop(5)
l1.pop(2)

print(f"List after using pop() method :- {l1}")

# remove elements using remove() method
l1.remove('Html')
l1.remove('Java')

print(f"List after using remove() method :- {l1}")