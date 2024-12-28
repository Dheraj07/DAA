def median(a):
    i=0
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    if n%2==0:
        return (a[n//2]+a[n//2-1])/2
    else:
        return a[n//2]
a=[5,8,7,6]
print(median(a))