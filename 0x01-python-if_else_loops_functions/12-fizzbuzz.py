#!/usr/bin/python3
# print Fizz for multiples of 3
# print Buzz for multiples of 5
# print FizzBuzz for multiples of 3 & 5
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            print("{}".format("Fizz"), end=" ")
        elif i % 3 != 0 and i % 5 == 0:
            print("{}".format("Buzz"), end=" ")
        elif i % 3 == 0 and i % 5 == 0:
            print("{}".format("FizzBuzz"), end=" ")
        else:
            print("{} ".format(i), end=" ")
