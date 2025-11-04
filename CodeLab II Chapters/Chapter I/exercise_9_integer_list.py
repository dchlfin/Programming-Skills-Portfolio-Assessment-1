intlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Output the list using a for loop
for i in intlist:
    print(i)

# output the highest and lowest value
minmax = [min(intlist), max(intlist)]
lowest, highest = minmax
print(f"Highest: {highest}, Lowest: {lowest}")

# sort the list in ascending order
print(intlist[::-1])

# sort the list in descending order
print(intlist[0::])

# append two elements
addition = [11, 12]
for a in addition:
    intlist.append(a)

# print the list after appending
print(intlist)
