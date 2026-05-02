#!/usr/bin/python3
import sys

res = []
for i in range(1, int(sys.argv[1]) + 1):
    if i % 3 == 0 and i % 5 == 0:
        res.append("FizzBuzz")
    elif i % 3 == 0:
        res.append("Fizz")
    elif i % 5 == 0:
        res.append("Buzz")
    else:
        res.append(str(i))
print(" ".join(res))
