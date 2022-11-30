#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        r3 = i % 3
        r5 = i % 5
        if ((r3 == 0) and (r5 != 0)):
            print("Fizz", end=" ")
        elif ((r3 != 0) and (r5 == 0)):
            print("Buzz", end=" ")
        elif ((r3 == 0) and (r5 == 0)):
            print("FizzBuzz", end=" ")
        else:
            print(i, end=" ")
