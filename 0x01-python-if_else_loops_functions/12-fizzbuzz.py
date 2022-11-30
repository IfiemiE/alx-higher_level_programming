#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        r3 = i % 3
        r5 = i % 5
        if ((r3 == 0) and (r5 != 0)):
            print("Fizz")
        elif ((r3 != 0) and (r5 == 0)):
            print("Buzz")
        elif ((r3 == 0) and (r5 == 0)):
            print("FizzBuzz")
        else:
            print(i)

        if (i != 100):
            print(" ")
