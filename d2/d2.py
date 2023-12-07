#!/usr/bin/env python3

file = open("input", "r")
input = file.read()
file.close()
lines = input.splitlines()

bag = {
        "red": 12,
        "green": 13,
        "blue": 14,
      }
sum = 0
for id, game in enumerate(lines):
    sets = game.split(':')[1].split(';')
    possible = True
    for s in sets:
        s = s.strip()
        cubes = s.split(',')
        for c in cubes:
            c = c.strip().split()
            quantity = int(c[0])
            color = c[1]
            if quantity > bag[color]:
                possible = False
    if possible:
        sum += id + 1
print(sum)



