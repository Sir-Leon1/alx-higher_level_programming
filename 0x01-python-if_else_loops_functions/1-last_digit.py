#!/usr/bin/python3
import random

number = random.randint(-1000, 1000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
print(f"Last digit of {number} is {digit}", end=" ")
if digit > 5:
    print(f"and is greater than 5")
elif digit == 0:
    print("and is 0")
elif digit < 6 and not 0:
    print("and is less than 6 and not 0")
