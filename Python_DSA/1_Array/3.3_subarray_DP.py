# Dynamic Programming  O(n)

def max_subarray(nums):
    if not  nums:
        return 0

    dp = [0] * len(nums)
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(nums[i],dp[i-1] + nums[i])

    return max(dp)

if __name__ == "__main__":
    arr = [10, -15, 12, -9, 6, -4, 3, 10, -8]

    sum_result = max_subarray(arr)
    if sum_result != -1:  # Kadane's algorithm doesn't return -1; this condition is unnecessary
        print("The sum of the maximum subarray using DP is:", sum_result)
    else:
        print("Sum is NOT Found!")