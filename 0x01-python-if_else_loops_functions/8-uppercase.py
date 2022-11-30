#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ((ord(i) <= 122) and (ord(i) >= 97)):
            print("{}".format(chr(int(ord(i)) - 32)), end="")
    print("")
