#!/usr/bin/env python3

file = open("input2", "r")
input = file.read()
file.close()
lines = input.splitlines()

sum = 0
for id, game in enumerate(lines):
    sets = game.split(':')[1].split(';')
    bag = {
            "red": 0,
            "green": 0,
            "blue": 0,
          }
    for s in sets:
        s = s.strip()
        cubes = s.split(',')
        for c in cubes:
            c = c.strip().split()
            quantity = int(c[0])
            color = c[1]
            if quantity > bag[color]:
                bag[color] = quantity
    sum += bag["red"] * bag["green"] * bag["blue"]

print(sum)



