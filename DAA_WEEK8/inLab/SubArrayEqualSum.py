def find_partition(arr):
    n = len(arr)
    total_sum = sum(arr)
    target = total_sum // 2

    dp = {0: []}
    for num in arr:
        new_dp = dp.copy()
        for s in dp.keys():
            new_sum = s + num
            if new_sum not in dp and new_sum <= target:
                new_dp[new_sum] = dp[s] + [num]
        dp = new_dp

    closest_sum = max(dp.keys())
    subset1 = dp[closest_sum]
    subset2 = arr.copy()

    for num in subset1:
        subset2.remove(num)

    return subset1, subset2

arr = [1, 5, 11, 5]
subset1, subset2 = find_partition(arr)
print("Subsets:", subset1, subset2)
