'''Write a program to read a number from the user and print its square. Generate KeyboardIntrrupt exception if Ctrl + C is pressed instead of a number'''

x = int(input("Enter a number: "))

try :
    print("Square of the number is: ", x**2)
except KeyboardInterrupt:
    print("\nCtrl + C pressed")
