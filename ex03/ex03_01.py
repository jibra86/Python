#!/usr/bin/env python3

# Write a program to prompt the user for
# hours and rate per hour using input to compute gross
# pay. Pay the hourly rate for the hours up to
# 40 and 1.5 times the hourly rate for all
# hours worked above 40 hours. Use 45 hours and a rate
# of 10.50 per hour to test the program
# (the pay should be 498.75).
# You should use input to read a string and float() to
# convert the string to a number.

hours = input("Enter hours: ")
rate = input("Enter rate per hour: ")

fhours = float(hours)
frate = float(rate)

if fhours > 40:
    reg = fhours * frate
    otp = (fhours - 40) * (frate * 0.5)
    pay = reg + otp
    print(pay)
elif fhours < 40:
    pay = fhours * frate
    print(pay)
