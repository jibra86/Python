word = input("Enter a string value: ")
size = len(word)

for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])
