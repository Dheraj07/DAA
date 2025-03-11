def count_occurrences(arr, left, right, element):
    count = 0
    for i in range(left, right + 1):
        if arr[i] == element:
            count += 1
    return count

def majority_element_rec(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2
    left_majority = majority_element_rec(arr, left, mid)
    right_majority = majority_element_rec(arr, mid + 1, right)

    if left_majority == right_majority:
        return left_majority

    left_count = count_occurrences(arr, left, right, left_majority)
    right_count = count_occurrences(arr, left, right, right_majority)

    return left_majority if left_count > right_count else right_majority

def majority_element(arr):
    n = len(arr)
    candidate = majority_element_rec(arr, 0, n - 1)

    if arr.count(candidate) > n // 2:
        return candidate
    return -1

arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print("Majority element:", majority_element(arr))  # Output: 4
