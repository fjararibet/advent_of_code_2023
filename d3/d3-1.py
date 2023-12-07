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


def get_sum(schematic):
    sum = 0
    for i in range(1, len(schematic) - 1):
        number_pos = None
        for j in range(len(schematic[0])):
            char = schematic[i][j]
            if char in numbers:
                if number_pos:
                    number_pos[1] += 1
                else:
                    number_pos = [j, j]
            else:
                if number_pos:
                    adjacent_lines = schematic[i-1:i+2]
                    number = int(
                        schematic[i][number_pos[0]:number_pos[1] + 1])
                    if is_part_number(number_pos, adjacent_lines):
                        sum += number
                        print(f"{number}\n")
                    else:
                        # print(f"Not counted= {number}")
                        pass
                    number_pos = None
    return sum


def is_part_number(number_pos, adjacent_lines):
    check_range = (number_pos[0] - 1, number_pos[1] + 1)

    for i in range(len(adjacent_lines)):
        for j in range(check_range[0], check_range[1] + 1):
            char = adjacent_lines[i][j]
            if char not in not_symbols:
                print(f"sym={char}")
                return True

    return False


print(get_sum(schematic))
