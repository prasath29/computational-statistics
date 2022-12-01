## make sure the lis is in ascending order
## lis is global variable
lis = [12, 15, 17, 20, 25, 30]

def binsearch(target, a=0, b=len(lis)):
    if a > b: return -1
    mid = (a+b)//2
    
    if target < lis[mid]:
        return binsearch(target, a, mid-1)

    elif lis[mid] < target:
        return binsearch(target, mid+1, b)

    else:
        return mid

print(binsearch(15))