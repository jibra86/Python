#!/usr/bin/env python3

score = input("Enter score: ")
fscore = float(score)

if fscore > 1.0:
    print("Input Should be less than 1.0.")
elif fscore >= 0.9:
    print("A")
elif fscore >= 0.8:
    print("B")
elif fscore >= 0.7:
    print("C")
elif fscore > 0.6:
    print("D")
elif fscore < 0.6:
    print("F")
elif fscore < 0.0:
    print("Input Should be greater than 0.0")
