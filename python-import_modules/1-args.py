#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(num_args, 's' if num_args != 1 else ''))
        for i, arg in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(i, arg))