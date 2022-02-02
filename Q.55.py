'''Write a program to read the age of a person and raise exceptions if age is negative.'''

x = int(input("Enter your age: "))
if x < 0:
    raise ValueError("Age cannot be negative")
else:
    print("Age is valid")
