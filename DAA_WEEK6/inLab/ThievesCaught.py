def max_thieves_caught(arr, k):
    police = []
    thieves = []

    for i in range(len(arr)):
        if arr[i] == 'P':
            police.append(i)
        else:
            thieves.append(i)

    i, j, count = 0, 0, 0

    while i < len(police) and j < len(thieves):
        if abs(police[i] - thieves[j]) <= k:
            count += 1
            i += 1
            j += 1
        elif police[i] < thieves[j]:
            i += 1
        else:
            j += 1

    return count

arr = ['P', 'T', 'T', 'P', 'T']
k = 1
print(max_thieves_caught(arr, k))
