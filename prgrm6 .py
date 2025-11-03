names = ["babu", "harinandana", "jasil", "Aman", "John"]

count = 0

for name in names:
    count += name.lower().count('a')

print("Total number of 'a's:", count)
