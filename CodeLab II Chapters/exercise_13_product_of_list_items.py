def prodOfList(l):
    product = 1
    for i in l:
        product = product * i
    return product


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = prodOfList(li)
print(result)
