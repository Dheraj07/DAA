def bubbleSort(a):
    i=0
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
a=[5,4,3,2,1]
print(bubbleSort(a))