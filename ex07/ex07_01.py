#!/usr/bin/env python3

####
## Read the content of file remove the extra spaces (new lines '\n') and print the output in uppercase
####
fhandle = open("mbox-short.txt", "r")

for word in fhandle:
    # print(word)
    # Now we need the remove \n
    word = word.rstrip()
    upper_word = word.upper()
    print(upper_word)
    # Now we see no new lines in the output
