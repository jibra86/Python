#!/usr/bin/env python3

# Write a program to prompt the user for hours and rate per hour
# using input to compute gross pay.

hours = input("Enter hours: ")
rate = input("Enter rate per hour: ")

# Use 35 hours and a rate of 2.75 per hour to test the program
# (the pay should be 96.25).

# You should use input to read a string and float() to convert the
# string to a number.

fhours = float(hours)
frate = float(rate)

pay = fhours * frate
print("Pay:", pay)
