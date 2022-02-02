'''Write a program to generate a random number. Raise a user-defined exception if the number is below 0.5.'''

import random

num = random.random()

if num < 0.5:
    raise Exception('random number is less than 0.5')
else:
    print('random numbrt is:', num)
