#!/usr/bin/python3
def uppercase(str):
    Upstr = ""
    for i in str:
        if ((ord(i) <= 122) and (ord(i) >= 97)):
            Upstr = Upstr + chr(int(ord(i)) - 32)
        else:
            Upstr = Upstr + i
    print("{}".format(Upstr))
