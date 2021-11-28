#!/usr/bin/env python3

####
## Print out how many times a person from a specific email address has made commits from the given file
####
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
