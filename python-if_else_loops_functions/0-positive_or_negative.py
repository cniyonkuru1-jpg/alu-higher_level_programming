#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if type(number) != int:
    print(f"{number} is not a number")
elif number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
