from collections import Counter

text = "this is a test this is only a test"
words = text.split()
word_counts = Counter(words)

print(word_counts)
