#!/usr/bin/python3
# print ascii in reverse
# and alternate upper and lower case

for i in reversed(range(ord('a'), ord('z') + 1)):
    if i % 2 != 0:
        print("{}".format(chr(i - 32)), end="")
    else:
        print("{}".format(chr(i)), end="")
