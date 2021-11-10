dictAddress = dict()
lst = list()

fhandle = input("Enter the name of the file: ")
try:
    fh = open(fhandle)
except:
    print("Invalid Input!!")
    quit()

for lines in fh:
    line = lines.rstrip()
    if line.startswith("From "):
        words = line.split()
        word = words[1]
        if word not in dictAddress:
            dictAddress[word] = 1
        else:
            dictAddress[word] += 1

for (key, val) in list(dictAddress.items()):
    lst.append((val, key))
    
lst.sort(reverse=True)

for count, email in lst[:1]:
    print(email, count)
