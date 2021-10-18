#!/usr/bin/env python3

inp_file = input("Enter the name of the file: ")
fhandle = open(inp_file, "r")

count = 0
tot = 0

for line in fhandle:
    line = line.rstrip()  # using the same variable name
    # print(line)
    if line.startswith("X-DSPAM-Confidence:"):
        # print(line)
        col = line.find(":")
        # print(col)
        num = line[col + 2:]
        fnum = float(num)
        tot = tot + fnum
        count = count + 1

print("Average", tot/count)
