"""
Write a Python program to access values using dictionary keys.
"""

student_details = {
    "name": "Om",
    "age": 22,
    "course": "Python full-stack devloper",
    "location": "Ahmedabad",
}

# get student value using dictionary keys
for k in student_details:
    print(f"{student_details[k]}")