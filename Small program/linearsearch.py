def linearsearch(li, target):
    for i in range(len(li)):
        if li[i] == target:
            return i
    return -1


ind = linearsearch([34, 7, 12, 90, 34], 30)
print(ind)