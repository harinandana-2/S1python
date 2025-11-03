
list1 = input("Enter first list (numbers separated by spaces): ").split()
list1 = [int(x) for x in list1]
list2 = input("Enter second list (numbers separated by spaces): ").split()
list2 = [int(x) for x in list2]
if len(list1) == len(list2):
    print("Both lists are of same length")
else:
    print("Lists are of different lengths")
if sum(list1) == sum(list2):
    print("Both lists have the same sum")
else:
    print("Lists have different sums")

common = []
for x in list1:
    if x in list2:
        common.append(x)

if len(common) > 0:
    print("Common values are:", common)
else:
    print("No common values")
