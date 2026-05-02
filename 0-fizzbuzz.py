#!/usr/bin/python3
import sys

n = int(sys.argv[1])
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        word = "FizzBuzz"
    elif i % 3 == 0:
        word = "Fizz"
    elif i % 5 == 0:
        word = "Buzz"
    else:
        word = str(i)
    if i == n:
        print(word, end="")
    else:
        print(word, end=" ")
print()
