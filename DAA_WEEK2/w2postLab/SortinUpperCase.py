arr=["Hello","WORLD","abc","DEFGH","Testing"]

def count_uppercase(arr):
    count=0
    for a in arr:
        if a.isupper():
            count+=1
    return count
n=len(arr)
for i in range(0,n):
    for j in range(0,n-i-1):
        if count_uppercase(arr[j])>count_uppercase(arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

