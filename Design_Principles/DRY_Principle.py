# DRY principle means avoiding code duplication by ensuring every piece of knowledge or logic exists 
# in one place. A simple example shows how repeating validation logic leads to bugs, while extracting 
# it once fixes issues everywhere.
# The DRY principle, short for "Don't Repeat Yourself," advocates reducing repetition of logic, data, 
# or knowledge in software by ensuring each piece has a single, authoritative representation.
#BAD EXAMPLE
# Repeated validation in two functions
# def process_user_age(age):
#     if age < 0 or age > 120:
#         raise ValueError("Invalid age")
#     print(f"User age: {age}")

# def process_employee_age(age):
#     if age < 18 or age > 65:  # Different logic!
#         raise ValueError("Invalid employee age")
#     print(f"Employee age: {age}")

# process_user_age(150)  # Raises error
# process_employee_age(150)  # No error! Bug.

def validate_age(age, min_age=0, max_age=120):
    if age < min_age or age > max_age:
        raise ValueError(f"Invalid age: {age}")
    return age

def process_user_age(age):
    process_age("User", validate_age(age))

def process_employee_age(age):
    process_age("Employee", validate_age(age, min_age=18, max_age=65))

def process_age(role, age):
    print(f"{role} age: {age}")

process_user_age(150)     # Raises error
process_employee_age(150)  # Raises error consistently

