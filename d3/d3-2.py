#!/usr/bin/env python3
import sys

filename = "input"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename, "r") as f:
    input = f.read()

not_symbols = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
schematic = input.split("\n")
for i in range(len(schematic)):
    schematic[i] = '.' + schematic[i] + '.'
border = ["." * len(schematic[0])]
schematic = border + schematic[:-1] + border


def get_gears(schematic):
    sum = 0
    for i in range(1, len(schematic)-1):
        for j in range(len(schematic[0])):
            char = schematic[i][j]
            if char != "*":
                continue

            adjacent_lines = schematic[i-1:i+2]
            adj_range = range(j-1, j+2)
            # Find adjacent numbers
            adj_numbers = []
            num_range = None
            for k in range(len(adjacent_lines)):
                for l in range(len(adjacent_lines[0])):
                    char = adjacent_lines[k][l]
                    if char in numbers:
                        if num_range is not None:
                            first = num_range.start
                            num_range = range(first, l+1)
                        else:
                            num_range = range(l, l+1)
                    else:
                        if num_range:
                            is_adj = any(n in adj_range for n in num_range)
                            first = num_range.start
                            last = num_range.stop
                            number = adjacent_lines[k][first:last]
                            if is_adj:
                                adj_numbers.append(int(number))
                        num_range = None

            if len(adj_numbers) == 2:
                print(adj_range)
                print(adj_numbers)
                print()
                ratio = adj_numbers[0] * adj_numbers[1]
                sum += ratio
    return sum
print(get_gears(schematic))
