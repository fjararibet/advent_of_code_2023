#!/usr/bin/env python3
import sys

filename = "input"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename, "r") as f:
    input = f.read()

scratchcards = input.split("\n")[:-1]

sum = 0
for card in scratchcards:
    card = card.split(":")[1].strip()
    card = card.split("|")
    winners = card[0].strip().split()
    numbers = card[1].strip().split()

    matches = -1
    for n in numbers:
        if n in winners:
            matches += 1
    if matches < 0:
        continue
    points = 2**matches
    sum += points

print(sum)
