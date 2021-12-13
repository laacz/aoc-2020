#!/usr/bin/python
import sys

if len(sys.argv) != 2:
    print("Missing file argument!")
    exit(1)

with open(sys.argv[1]) as f:
    numbers = [int(line.strip()) for line in f]

result1 = False
result2 = False
for a in numbers:
    for b in numbers:
        if result1 is False and a + b == 2020:
            result1 = a * b
        for c in numbers:
            if result2 is False and a + b + c == 2020:
                result2 = a * b * c

print(f'Part 1: {result1}')
print(f'Part 2: {result2}')
