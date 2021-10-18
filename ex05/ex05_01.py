#!/usr/bin/env python3

count = 0
tot = 0

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum = float(num)
    except:
        print("Invalid Input")
        continue
    count = count + 1
    tot = tot + fnum

print(tot/count)
