#!/usr/bin/python
import sys
import re

if len(sys.argv) != 2:
    print("Missing file argument!")
    exit(1)

with open(sys.argv[1]) as f:
    rules = [line.strip() for line in f]

bags = {}
for rule in rules:
    color, contains = re.match(r'^(.+) bags contain (.+)$', rule).groups()
    bags[color] = re.findall(r'(\d+) (.+?) bag', contains)


def bag_can_contain_color(bag, search):
    if bag == search:
        return True
    return any(bag_can_contain_color(col, search) for cnt, col in bags[bag])


result1 = 0
for bag in bags:
    if bag_can_contain_color(bag, 'shiny gold'):
        result1 += 1


def sum_bags(c):
    return 1 + sum(int(cnt) * sum_bags(col) for cnt, col in bags[c])


result2 = sum_bags('shiny gold')

print(f'Part 1: {result1 - 1}')
print(f'Part 2: {result2 - 1}')
