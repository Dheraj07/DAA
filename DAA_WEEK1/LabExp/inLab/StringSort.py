def StringSort(a):
    a=list(set(a))
    n=len(a)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if len(a[i]) > len(a[i + 1]):
                a[j],a[j+1]=a[j+1],a[j]
            elif len(a[i])==len(a[i+1]):
                if ord(a[j][0])>ord(a[j+1][0]):
                    a[j], a[j + 1] = a[j + 1], a[j]
    return a



a=["Mahesh","Suresh","Ramesh","Mahesh"]
print(StringSort(a))