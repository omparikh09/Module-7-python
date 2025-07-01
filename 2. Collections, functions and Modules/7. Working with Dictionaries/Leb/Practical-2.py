"""
Write a Python program to merge two lists into one dictionary using a loop.
"""

l1 = ['name', 'age', 'subject', 'marks']
l2 = ['Om', 22, 'Python', 88]

my_dict = {}

for i in range(len(l1)):
    my_dict[l1[i]] = l2[i]
    
print("My Dictionary :- ",my_dict)