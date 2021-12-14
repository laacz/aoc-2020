#!/usr/bin/python
import sys

if len(sys.argv) != 3:
    print("Missing file and preamble length argument!")
    exit(1)

with open(sys.argv[1]) as f:
    numbers = [int(line.strip()) for line in f]

preamble_length = int(sys.argv[2])

result1 = 0
for pos in range(preamble_length + 1, len(numbers)):
    window = numbers[pos - preamble_length:pos]
    valid = any(a + b == numbers[pos] for a in window for b in window if a != b)
    if not valid and result1 == 0:
        print(f'Part 1: answer is {numbers[pos]} at position #{pos}')
        result1 = numbers[pos]
        break

result2 = 0
for pos in range(len(numbers)):
    for i in range(pos, len(numbers) - pos):
        window = numbers[pos:i]
        if sum(window) == result1:
            result2 = min(window) + max(window)
            print(f'Part 2: sum of {window} is {result1}, {min(window)} + {max(window)} = answer ({result2})')
            break
    if result2:
        break
