#!/usr/bin/python
import sys
import operator
import functools

if len(sys.argv) != 2:
    print("Missing file argument!")
    exit(1)

with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f]

slopes = [
    [1, 1, 0],
    [3, 1, 0],
    [5, 1, 0],
    [7, 1, 0],
    [1, 2, 0],
]

for slope in slopes:
    x = y = trees = 0
    while y + slope[1] < len(lines):
        x += slope[0]
        y += slope[1]

        if lines[y][x % len(lines[y])] == '#':
            trees += 1

    slope[2] = trees

result1 = slopes[1][2]
result2 = functools.reduce(operator.mul, [x[2] for x in slopes], 1)

print(f'Part 1: {result1}')
print(f'Part 2: {result2}')
