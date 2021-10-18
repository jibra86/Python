#!/usr/bin/env python3

fh = open("mbox-short.txt")
count = dict()
for line in fh:
    line = line.strip()
    # print(line)
    if line.startswith("From "):
        # print(line)
        lst = line.split()
        # print(lst)
        frm = lst[1]
        count[frm] = count.get(frm, 0) + 1

print(count)
