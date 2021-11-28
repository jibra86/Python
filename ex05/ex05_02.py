#!/usr/bin/env python3

####
## Finding the maximum and minim input by the user
####

maximum = None
minimum = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum = float(num)
    except:
        print("Invalid Input")
        continue
    if maximum is None and minimum is None:
        maximum = fnum
        minimum = fnum
    elif maximum < fnum:
        maximum = fnum
    elif minimum > fnum:
        minimum = fnum

print("Maximum:", maximum,"\n" + "Minimum:", minimum)
