ar = [23, 12, 45, 12, 45, 12, 67, 90]

def bubblesort(li):
    Changed = False
    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            Changed = True
            li[i], li[i+1] = li[i+1], li[i]

    if Changed:
        bubblesort(li)

bubblesort(ar)
print(ar)