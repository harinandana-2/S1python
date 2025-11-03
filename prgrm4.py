line = input("Enter a line of text: ")

words = line.split()

for word in words:
    count = words.count(word)
    print(word, ":", count)
