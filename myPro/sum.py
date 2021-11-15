#!/usr/bin/env python3

prev_num = 0

for i in range(1, 11):
    print("The Previous Number =", prev_num, "\n" + "The Current Number =", i, "\n", "The Sum =", prev_num + i)
    prev_num = i
