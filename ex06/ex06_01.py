#!/usr/bin/env python3
####
## print out the floating values from the file that are of string type and then change them to float type
####
theString = "str = X-DSPAM-Confidence: 0.8475 "
theCol = theString.find(":")

num = theString[theCol +1:]

num = num.strip()

fnum = float(num)
print(fnum)
print(type(fnum))
