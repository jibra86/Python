#!/usr/bin/env python3

fh = open("mbox-short.txt")
count = dict()

for line in fh:
    line = line.strip()
    if line.startswith("From "):
        lst = line.split()
        date = lst[2]
        # print(date)
        count[date] = count.get(date, 0) + 1

print(count)

