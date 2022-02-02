'''Write a program to read two numbers from the user and perform basic mathematical operations (addition, multiplication, subtraction, division) by handling all possible exceptions.
'''

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

try :
    print("Addition: ", x + y)
    print("Subtraction: ", x - y)
    print("Multiplication: ", x * y)
    print("Division: ", x / y)
except ZeroDivisionError:
    print("Division by zero is not possible")
except ValueError:
    print("Invalid Input")
except Exception:
    print("Something went wrong")
finally:
    print("Program completed")
