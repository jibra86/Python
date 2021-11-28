#!/usr/bin/env python3

####
## Find out how many times the line starting with "From " are in the file
####
fhandle = input("Enter the name of the file: ")
fh = open(fhandle)

count = 0

for line in fh:
    line = line.strip()
    if line.startswith("From "):
        # print(line)
        lis = line.split()
        print(lis[1])
        count = count + 1

print("There were", count, "lines is the file with From as the first word")
