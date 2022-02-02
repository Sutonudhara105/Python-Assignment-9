'''Write a program to print random numbers infinitely. Raise the StopIteration exception after displaying 10 numbers to exit from the program'''

import random

print("Random numbers:")
for i in range(10):
    print(random.randint(1, 100))
raise StopIteration
