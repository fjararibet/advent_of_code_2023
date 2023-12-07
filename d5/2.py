#!/usr/bin/env python3
import sys

input = open(sys.argv[1]).read().strip()
lines = input.split("\n")

i = 0
while lines[i] != '':
    line = lines[i]
    _, rest = line.split(':')
    seeds_ranges = [int(x) for x in rest.strip().split()]
    seeds = []
    j = 0
    while j < len(seeds_ranges):
        seeds += list(range(seeds_ranges[j], seeds_ranges[j + 1] + seeds_ranges[j]))
        j += 2
    i += 1

source = seeds
destinations = seeds
while i < len(lines):
    print(i)
    i += 1
    # print("\n", lines[i])
    i += 1
    source = destinations.copy()
    mapppings = []
    while lines[i] != '':
        line = lines[i]
        dest_start, source_start, rnge = [int(x) for x in line.strip().split()]
        mapppings.append((dest_start, source_start, rnge))
        i += 1
        if i >= len(lines):
            break
    for idx, s in enumerate(source):
        if s in range(source_start, source_start + rnge):
            diff = s - source_start
            destinations[idx] = dest_start + diff
    # print(destinations)

print(min(destinations))
