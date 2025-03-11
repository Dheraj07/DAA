def quick_sort(a):
    global count
    if len(a)<=1:
        return a
    else:
        pivot=a[len(a)//2]
        left=[x for x in a if x<pivot]
        middle=[x for x in a if x==pivot]
        right=[x for x in a if x>pivot]
        count+=len(a)-1
        return quick_sort(left)+middle+quick_sort(right)

count=0
a=[4,3,5,1,2]
# print(quick_sort(a))
print(count)