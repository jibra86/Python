#!/usr/bin/env python3

####
## Looking the count of input integer being enterred, the total of the integer that were input and the average
####

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
