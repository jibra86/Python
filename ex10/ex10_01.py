fhandle = input("Enter the name of the file: ")
no_messages = {}
lst = []
try:
    fh = open(fhandle)
except:
    print("Invalid Input!!")
    quit()

for line in fh:
    lines = line.strip()
    if lines.startswith("From "):
        words = line.split()
        word = words[1].split("@")
        person = words[1]
        # print(person)
        no_messages[person] = no_messages.get(person, 0) + 1
        # print(no_messages)

for (email, count) in no_messages.items():
            newTup = (email, count)
            lst.append(newTup)


