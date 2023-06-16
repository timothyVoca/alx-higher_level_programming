#!/usr/bin/python3
import sys

if __name__ == "__main__":

    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 1:
        print("{} {}".format(num_arguments, "argument:"))
    elif num_arguments == 0:
        print("{} {}".format(num_arguments, "arguments."))
    else:
        print("{} {}".format(num_arguments, "arguments:"))

    for i, arg in enumerate(arguments, 1):
        print(f"{i}: {arg}")
