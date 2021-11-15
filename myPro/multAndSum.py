#!/usr/bin/env python3

def prodOrSum(num1, num2):
    prod = num1 * num2
    if prod <= 1000:
        return prod
    else:
        add = num1 + num2
        return add

print(prodOrSum(40, 30))
