#!/usr/bin/env python3
import sys

input = open(sys.argv[1]).read().strip()
lines = input.split("\n")
times = [int(x) for x in lines[0].split(':')[1].strip().split()]
records = [int(x) for x in lines[1].split(':')[1].strip().split()]

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

margin = 1
for i in range (len(records)):
    beaten_records = get_records_beaten(times[i], records[i])
    # print(f"{beaten_records=}")
    margin *= beaten_records
print(margin)

    
