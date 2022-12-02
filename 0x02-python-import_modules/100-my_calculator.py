#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
num_arg = len(sys.argv) - 1
if num_arg != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
operator = sys.argv[2]
a = sys.argv[1]
b = sys.argv[3]
if operator == '+':
    print("{} + {} = {}".format(a, b, add(a, b)))
elif operator == '-':
    print("{} - {} = {}".format(a, b, sub(a, b)))
elif operator == '*':
    print("{} * {} = {}".format(a, b, mul(a, b)))
elif operator == '/':
    print("{} / {} = {}".format(a, b, div(a, b)))
else:
    print("Uknown operator. Available operators: +, -, *, and /")
    exit(0)
exit(0)
