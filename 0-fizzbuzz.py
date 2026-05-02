#!/usr/bin/python3
import sys

output = []
for i in range(1, int(sys.argv[1]) + 1):
    if i % 15 == 0:
        output.append("FizzBuzz")
    elif i % 3 == 0:
        output.append("Fizz")
    elif i % 5 == 0:
        output.append("Buzz")
    else:
        output.append(str(i))
sys.stdout.write(" ".join(output))
