#!/usr/bin/python
import sys
import re

if len(sys.argv) != 2:
    print("Missing file argument!")
    exit(1)

with open(sys.argv[1]) as f:
    code = [line.strip() for line in f]


def run(code):
    executed = []
    acc = pos = 0
    while True:
        if pos >= len(code):
            return pos, acc

        if pos in executed:
            return pos, acc

        executed.append(pos)
        operation, argument = code[pos].split(' ')
        if operation == 'acc':
            acc += int(argument)

        if operation == 'jmp':
            pos += int(argument)
        else:
            pos += 1


pos, result1 = run(code)

result2 = 0
for pos in range(len(code)):
    operation, argument = code[pos].split(' ')
    copy = code.copy()
    if operation == 'nop' or operation == 'jmp':
        copy[pos] = ('jmp' if operation == 'nop' else 'nop') + ' ' + argument
        pos, result2 = run(copy)
        if pos == len(code):
            break

print(f'Part 1: {result1}')
print(f'Part 2: {result2}')
