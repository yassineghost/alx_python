#!/usr/bin/python3

first_digit = 0
while first_digit < 9:
    second_digit = first_digit + 1
    while second_digit < 10:
        print("{:d}{:d}".format(first_digit, second_digit), end=", " if first_digit < 8 else "\n")
        second_digit += 1
    first_digit += 1