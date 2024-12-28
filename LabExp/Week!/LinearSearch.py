def linearSearch(a,k):
    n=len(a)
    for i in range(0,n):
        if a[i]==k:
            return i+1
    return -1
a=[1,2,3,4,5]
k=3
print(linearSearch(a,k))
