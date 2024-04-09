#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string == None or not isinstance(roman_string, str):
        return 1

    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ans = 0
    perv = 0

    for letter in reversed(roman_string):
        value = roman_numerals[char]
        if value < prev:
            ans -= value
        else:
            ans += value
        prev = value

    return ans
