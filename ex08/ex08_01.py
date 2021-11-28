#!/usr/bin/env python3
####
## Print out the content of the file in a list word by word and sort the output by using the sort function
####

fhandle = input("Enter the name of the file: ")
fh = open(fhandle)

lst = list()

for line in fh:
    lis = line.strip().split()
    # print(lis)
    for word in lis:
        if word in lst:
            continue
        else:
            lst.append(word)

lst.sort()
print(lst)

