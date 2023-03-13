#!/usr/bin/python3
import random

number = random.randint(-1000, 1000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
<<<<<<< HEAD
print(f"Last digit of {number} is {digit}", end=" ")
if digit > 5:
    print(f"and is greater than 5")
=======
print("Last digit of {} is {}".format(number, digit), end=" ")
if digit > 5:
    print("and is greater than 5")
>>>>>>> 49f36a77b2d281a1c56da2da806b4ef055c1854d
elif digit == 0:
    print("and is 0")
elif digit < 6 and not 0:
    print("and is less than 6 and not 0")
