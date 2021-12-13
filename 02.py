#!/usr/bin/python
import sys
import re

if len(sys.argv) != 2:
    print("Missing file argument!")
    exit(1)

with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f]

result2 = result1 = 0
for line in lines:
    min_times, max_times, letter, password = re.findall(r'^(\d+)-(\d+) (.): (.+)$', line)[0]
    min_times = int(min_times)
    max_times = int(max_times)

    if min_times <= password.count(letter) <= max_times:
        result1 = result1 + 1
    if (password[min_times - 1] + password[max_times - 1]).count(letter) == 1:
        result2 = result2 + 1

print(f'Part 1: {result1}')
print(f'Part 2: {result2}')
