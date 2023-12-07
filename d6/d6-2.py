#!/usr/bin/env python3
import sys
from functools import reduce

input = open(sys.argv[1]).read().strip()
lines = input.split("\n")
times = [x for x in lines[0].split(':')[1].strip().split()]
time = int(reduce(lambda x, y: x + y, times))

records = [x for x in lines[1].split(':')[1].strip().split()]
record = int(reduce(lambda x, y: x + y, records))


def get_distance(hold_time, time):
    speed = hold_time
    distance = (time - hold_time) * speed
    return distance


def get_records_beaten(time, record):
    beaten_records = 0
    for i in range(time):
        distance = get_distance(i, time)
        if distance > record:
            beaten_records += 1

    return beaten_records


def fast_get_records_beaten(time, record):
    start = 0
    end = time
    for i in range(time):
        distance = get_distance(i, time)
        if distance > record:
            start = i
            print(start - 0)
            break
    return (time - start) - start + 1


# margin = get_records_beaten(time, record)
margin = fast_get_records_beaten(time, record)
print(margin)
