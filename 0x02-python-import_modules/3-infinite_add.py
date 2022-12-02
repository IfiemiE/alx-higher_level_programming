#!/usr/bin/python3
if __name__ == "__main__":
    import sys
num_arg = len(sys.argv) - 1
sum = 0
for i in range(1, num_arg + 1):
    sum = sum + int(sys.argv[i])
print("{}".format(sum))
