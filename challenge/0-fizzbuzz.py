#!/usr/bin/python3
"""FizzBuzz implementation"""

import sys


def build_value(num):
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return str(num)


def main():
    if len(sys.argv) != 2:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    limit = int(sys.argv[1])
    if limit < 1:
        return

    result = [build_value(i) for i in range(1, limit + 1)]
    print(" ".join(result))


if __name__ == "__main__":
    main()
