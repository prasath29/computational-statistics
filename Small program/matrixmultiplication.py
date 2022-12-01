## matrix multiplication
ar1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ar2 = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

# assumes all subarray are equal in length
def matmul(ar1, ar2):
    ## return -1 if not in the form a*n, n*b
    if len(ar1[0]) != len(ar2): return -1
    a, n, b = len(ar1), len(ar1[0]), len(ar2[0])

    ans = [[0]*b for _ in range(a)]

    for i in range(a):
        for j in range(b):
            ans[i][j] = sum([ar1[i][k]*ar2[k][j] for k in range(n)])
    
    return ans

ans_ar = matmul(ar1, ar2)
print(ans_ar)