def maximum(lis):
    max_ele = float('-inf')
    for ele in lis:
        if ele > max_ele:
            max_ele = ele

    return max_ele

def minimum(lis):
    min_ele = float('inf')
    for ele in lis:
        if ele < min_ele:
            min_ele = ele

    return min_ele

ar = [34, 23, 65, 1, 34, 94, 45]

print(maximum(ar))
print(minimum(ar))