#!/usr/bin/env python3

####
## Print out the person that had made the most commits from the file 'mbox-short.txt'
####

theDictionary = dict()
numMessages = 0
theMessenger = ""

fhandle = input("Enter the name of the file: ")

try:
    fh = open(fhandle)
except:
    print("The file does not exists")
    quit()

for line in fh:
    word = line.split()
    if len(word) < 2 or word[0] != "From":
        continue
    # print(word)

    if word[1] not in theDictionary:
        theDictionary[word[1]] = 1
    else:
        theDictionary[word[1]] += 1

# print(theDictionary)

for key in theDictionary:
    if theDictionary[key] > numMessages:
        numMessages = theDictionary[key]
        theMessenger = key

print(theMessenger, numMessages)
