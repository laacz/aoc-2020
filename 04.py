#!/usr/bin/python
import sys
import re

if len(sys.argv) != 2:
    print("Missing file argument!")
    exit(1)

with open(sys.argv[1]) as f:
    passports = [passport.strip().replace('\n', ' ') for passport in f.read().split("\n\n")]

result2 = result1 = 0
for passport in passports:
    attributes = dict(re.findall(r'([a-z]{3}):([^ ]+)', passport))

    if len(attributes) == 8 or (len(attributes) == 7 and "cid" not in attributes):
        result1 += 1
        invalid = []

        if not 1920 <= int(attributes['byr']) <= 2002:
            invalid.append('byr')
        if not 2010 <= int(attributes['iyr']) <= 2020:
            invalid.append('iyr')
        if not 2020 <= int(attributes['eyr']) <= 2030:
            invalid.append('eyr')
        if attributes['hgt'][-2:] == 'cm' and not 150 <= int(attributes['hgt'][:-2]) <= 193:
            invalid.append('hgt')
        if attributes['hgt'][-2:] == 'in' and not 59 <= int(attributes['hgt'][:-2]) <= 76:
            invalid.append('hgt')
        if not attributes['hgt'][-2:] in ['in', 'cm']:
            invalid.append('hgt')
        if len(attributes['hcl']) != 7 or not all(digit in '0123456789abcdef' for digit in attributes['hcl'][1:]):
            invalid.append('hcl')
        if attributes['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            invalid.append('ecl')
        if len(attributes['pid']) != 9 or not all(digit in '0123456789' for digit in attributes['pid']):
            invalid.append('pid')

        if not len(invalid):
            result2 += 1

print(f'Part 1: {result1}')
print(f'Part 2: {result2}')
