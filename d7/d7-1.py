#!/usr/bin/env python3
import sys

input = open(sys.argv[1]).read().strip()
lines = input.split("\n")

card_to_value = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9,
                 "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}


def get_winnings(lines):
    bids = {}
    hands_values = []
    for line in lines:
        hand, bid = line.split()
        bids[hand] = int(bid)
        value = get_value(hand)
        value.append(int(bid))
        hands_values.append(value)
    print(sorted(hands_values))

    total_winnings = 0
    rankings = sorted(hands_values)
    for rank, c in enumerate(rankings):
        bid  = c[-1]
        winnings = int(bid) * (rank + 1)
        total_winnings += winnings
        print(hand, bid)
    return total_winnings


def get_value(hand):
    kind = get_kind(hand)
    value = [kind]
    for card in hand:
        val = card_to_value[card]
        value.append(val)
    return value


def get_kind(hand):
    kinds = {}
    for card in hand:
        if card in kinds:
            kinds[card] += 1
        else:
            kinds[card] = 1
    max_cards = max(kinds.values())
    # Five of a kind
    if len(kinds) == 1:
        return 6

    if len(kinds) == 2:
        # Four of a kind
        if max_cards == 4:
            return 5

        # Full house
        elif max_cards == 3:
            return 4
    if len(kinds) == 3:
        # Three of a kind
        if max_cards == 3:
            return 3

        # Two pair
        if max_cards == 2:
            return 2

    if len(kinds) == 4:
        # One pair
        return 1
    if len(kinds) == 5:
        # High card
        return 0
    print(len(kinds))
    print('Error', hand, kinds)


answer = get_winnings(lines)
print(answer)
