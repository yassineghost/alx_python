#!/usr/bin/python3

num = 0
while num < 100:
    print("{:02d}".format(num), end=", " if num < 99 else "\n")
    num += 1