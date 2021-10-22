fhandle = open("mbox-short.txt")
dic = {}

for line in fhandle:
    line = line.strip()
    if line.startswith("From "):
        words = line.split()
        address = words[1]
        print(address)
        for key, val in address:
            
