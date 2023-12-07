#!/usr/bin/env python3
import sys

input = (sys.argv[1].read().strip())
lines = input.split("\n")

total_winnigs = 0


def get_kind(hand):
    kinds = {}
    for card in hand:
        if card in kinds:
            kinds[card] += 1
        else:
            kinds[card] = 1
    # Full house
    if len(kinds) == 1:
        return 5

    if len(kinds) == 2:
        max_cards = max(kinds.values())

        # Four of a kind
        if max_cards == 4:
            return 4

        # Three of a kind
        elif max_cards == 3:
            return 3
