####
## Print out how many times the commits were made in a single date using tuples
####

theDictionary = dict()

fhandle = input("Enter the name of the file: ")

try:
    fh = open(fhandle)
except:
    print("Invalid Input!!")
    quit()

for line in fh:
    lines = line.strip()
    if lines.startswith("From "):
        words = lines.split()
        time = words[5]
        hour = time[0:2]
        theDictionary[hour] = theDictionary.get(hour, 0) + 1

# print(theDictionary)

for (key, val) in sorted(theDictionary.items()):
    print(key, val)
