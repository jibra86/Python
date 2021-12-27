fhandle = input("Enter the name of the file: ")

try:
    fh = open(fhandle)
except:
    print("Invalid Input!!")
    quit()

letters = dict()

for line in fh:
    line = line.rstrip()
    for word in line:
        letters[word] = letters.get(word, 0) + 1

# print(letters)

lst = list()


for val, key in letters.items():
    lst.append( (key, val) )

lst.sort(reverse=True)

for val, key in lst:
    print(key, val)
