#!/usr/bin/env python3

fname = input("Enter the name of the file: ")

try:
    fh = open(fname)
except:
    print("The file does\'nt exist.")
    quit()
reqDict = dict()

for line in fh:
    line = line.strip()
    if line.startswith("From "):
        word = line.split()
        dom = word[1]
        domain = dom.split('@')[1]
        reqDict[domain] = reqDict.get(domain, 0) + 1

print(reqDict)
