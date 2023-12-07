#!/usr/bin/env python3
import sys

input = open(sys.argv[1]).read().strip()
lines = input.split("\n")

i = 0
while lines[i] != '':
    line = lines[i]
    _, rest = line.split(':')
    seeds_ranges = [int(x) for x in rest.strip().split()]
    j = 0
    seeds = []
    while j < len(seeds_ranges):
        start, length = seeds_ranges[j:j+2]
        seeds.append(range(start, start+length))
        j += 2
    i += 1

source = set(seeds)
destinations = set(seeds)
while i < len(lines):
    i += 1
    # print("\n", lines[i])
    i += 1
    source = destinations.copy()
    mappings = []
    while lines[i] != '':
        line = lines[i]
        dest_start, source_start, rnge = [int(x) for x in line.strip().split()]
        mappings.append((dest_start, source_start, rnge))

        dest_stop = dest_start + rnge
        source_stop = source_start + rnge
        i += 1
        if i >= len(lines):
            break
    print("source", source)
    print("destinations", destinations)
    for sc in source:
        to_check = [sc]
        j = 0
        while j < len(to_check):
            s = to_check[j]
            for mapping in mappings:
                dest_start, source_start, rnge = mapping
                dest_stop = dest_start + rnge
                source_stop = source_start + rnge

                diff_stop = s.stop - source_start
                diff_start = s.start - source_start
                mapped_start = s.start
                mapped_stop = s.stop

                # range inside source_range
                if s.start >= source_start and s.stop <= source_stop:
                    mapped_start = dest_start + diff_start
                    mapped_stop = dest_start + diff_stop

                # range outside source_range
                elif s.start < source_start and s.stop > source_stop:
                    mapped_start = dest_start
                    mapped_stop = dest_stop
                    unch_1 = range(s.start, source_start)
                    unch_2 = range(source_stop, s.stop)
                    to_check.append(unch_1)
                    to_check.append(unch_2)

                # range behind source range
                elif s.start < source_start and s.stop > source_start and s.stop <= source_stop:
                    mapped_start = dest_start
                    mapped_stop = dest_start + diff_stop
                    unch = range(s.start, source_start)
                    to_check.append(unch)

                # range in front of source range
                elif s.start >= source_start and s.stop > source_stop and s.start < source_stop:
                    mapped_start = dest_start + diff_start
                    mapped_stop = dest_start + diff_stop
                    unch = range(source_start, s.start)
                    to_check.append(unch)

                mapped_range = range(mapped_start, mapped_stop)
                print("mapped_range ", mapped_range)
                destinations.remove(s)
                print("removed ", s)
                destinations.add(mapped_range)

mins = [s.start for s in destinations]
print(min(mins))
