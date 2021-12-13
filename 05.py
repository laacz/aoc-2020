#!/usr/bin/python
import sys

if len(sys.argv) != 2:
    print("Missing file argument!")
    exit(1)

with open(sys.argv[1]) as f:
    seats = [seat.strip() for seat in f]

result1 = result2 = 0
seat_ids = []

for seat in seats:
    rows = range(127)
    for i in range(7):
        if seat[i] == 'F':
            rows = rows[:int(len(rows) / 2)]
        else:
            rows = rows[int(len(rows) / 2) + 1:]
    row = rows.start

    cols = range(7)
    for i in range(3):
        if seat[7 + i] == 'L':
            cols = cols[:int(len(cols) / 2)]
        else:
            cols = cols[int(len(cols) / 2) + 1:]
    col = cols.start

    seat_ids.append(row * 8 + col)

result1 = max(seat_ids)
result2 = [seat for seat in range(8, 127 * 8) if seat not in seat_ids and seat-1 in seat_ids and seat+1 in seat_ids][0]

print(f'Part 1: {result1}')
print(f'Part 2: {result2}')
