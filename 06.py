#!/usr/bin/python
import sys
import itertools

if len(sys.argv) != 2:
    print("Missing file argument!")
    exit(1)

with open(sys.argv[1]) as f:
    groups = [group.strip() for group in f.read().split('\n\n')]

result1 = result2 = 0
for group in groups:
    forms = [form.strip() for form in group.split('\n')]

    all_unique_answers = set(list(itertools.chain(*forms)))
    result1 += len(all_unique_answers)

    for answer in all_unique_answers:
        if all(answer in answers for answers in forms):
            result2 += 1

print(f'Part 1: {result1}')
print(f'Part 2: {result2}')
