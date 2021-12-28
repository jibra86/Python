import string

charToDel = string.whitespace + string.punctuation + string.digits

fhandle = input("Enter the name of the file: ")

try:
    fh = open(fhandle)
except:
    print("Invalid Input!!")
    quit()

letters = dict()

for line in fh:
    line = line.strip()
    for words in line:
        if words not in charToDel:
            letters[words] = letters.get(words, 0) + 1

lstOfWords = list()

for key, val in letters.items():
    lstOfWords.append( (val, key) )

# print(lstOfWords)
lstOfWords.sort(reverse=True)

for val, key in lstOfWords:
    print(key, val)
