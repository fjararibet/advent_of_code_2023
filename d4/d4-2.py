#!/usr/bin/env python3
import sys

filename = "input"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename, "r") as f:
    input = f.read()

scratchcards = input.split("\n")[:-1]

card_quantity = [1] * (len(scratchcards) + 1)
card_quantity[0] = 0
for card in scratchcards:
    card = card.split(":")
    card_number = int(card[0].split()[1])
    print(f"{card_number=}")
    card = card[1].strip().split("|")
    winners = card[0].strip().split()
    numbers = card[1].strip().split()

    next_card = card_number + 1
    for n in numbers:
        if next_card >= len(card_quantity):
            continue

        if n in winners:
            card_quantity[next_card] += 1 * card_quantity[card_number]
            next_card += 1


print(sum(card_quantity))
