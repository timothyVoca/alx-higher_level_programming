#!/usr/bin/python3

# print a string in uppercase
# without calling str.upper() and str.isupper()

def uppercase(str):
    result = ""  # initialize and empty string to store the result
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            result += uppercase_char  # append the uppercase_char to result

        else:
            result += char  # add the other characters as is
    print("{}".format(result))
