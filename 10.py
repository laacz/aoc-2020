#!/usr/bin/python
import sys
from collections import Counter

"""
Learned about Counter today. Neat.
"""

if len(sys.argv) != 2:
    print("Missing file argument!")
    exit(1)

with open(sys.argv[1]) as f:
    numbers = [int(line.strip()) for line in f]

numbers = sorted(numbers + [0, max(numbers) + 3])
differences = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]
result1 = Counter(differences)[1] * Counter(differences)[3]

print(f'Part 1: {Counter(differences)[1]} * {Counter(differences)[3]} = {result1}')

scores = {numbers[-1:][0]: 1}
# Going from end, since target is to make chain not break
for i in range(len(numbers) - 2, -1, -1):
    number = numbers[i]
    triplet = numbers[i + 1:i + 4]

    scores[number] = 0
    for num in triplet:
        if num - number <= 3:
            scores[number] += scores[num]

print(f'Part 2: {scores[0]}')
